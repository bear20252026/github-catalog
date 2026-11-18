# -*- coding: utf-8 -*-
"""从 catalog.json 重新生成现代卡片式 README.md（所有条目与链接保留，可重复生成）。

用法：python scripts/build_readme.py
"""
import json, os, re
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OWNER = "bear20252026"
PAGES = f"https://{OWNER}.github.io/github-catalog/"

doc = json.load(open(os.path.join(ROOT, "catalog.json"), encoding="utf-8"))
books = json.load(open(os.path.join(ROOT, "data", "books.json"), encoding="utf-8"))
PALETTE = books["palette"]

def esc(s):
    s = (s or "").replace("|", "，").replace("<", "‹").replace(">", "›").replace("`", "´")
    return re.sub(r"\s+", " ", s).strip()

def fmt_stars(n):
    n = n or 0
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)

def upd(u):
    return f" `{u}`" if u else ""

# ── 收集数据 ──────────────────────────────────────────────
own = doc["own_repos"]
originals = [o for o in own if o["kind"] == "original"]         # 78（含置顶）
forks = [o for o in own if o["kind"] == "fork"]                 # 142
lib = [e for e in doc["catalog"] if not e.get("url", "").startswith(f"https://github.com/{OWNER}/")]

cat_index = OrderedDict((k, []) for k in PALETTE)
for o in originals:
    cat_index[o["category"]].append(o)
lib_index = OrderedDict((k, []) for k in PALETTE)
for e in doc["catalog"]:
    lib_index[e["category"]].append(e)
fork_index = OrderedDict((k, []) for k in PALETTE)
for f in forks:
    fork_index[f["category"]].append(f)

# 特效专架：从馆藏 effects 字段派生
eff_index = OrderedDict()
for e in doc["catalog"]:
    for f in e.get("effects", []):
        eff_index.setdefault(f, []).append(e)
eff_index = OrderedDict(sorted(eff_index.items(), key=lambda kv: -len(kv[1])))

n_lib = len(doc["catalog"])
total_books = 1 + len(originals) - 1 + len(forks) + len(lib)   # 置顶 + 原创(除本仓) + 复刻 + 馆藏
assert total_books == 562, total_books

B = []  # README 行

# ── 头部 ──────────────────────────────────────────────────
B.append(f"""<a id="top"></a>

# 🏛️ bear20252026 的数字图书馆

**![仓库](https://img.shields.io/badge/名下仓库-220-1F3D2B) ![馆藏](https://img.shields.io/badge/上游馆藏-347-A8841C) ![藏书](https://img.shields.io/badge/藏书总数-562-2C5540) ![数据](https://img.shields.io/badge/数据驱动-catalog.json-C9A227)**

> 奶油白 · 暖木 · 墨绿与黄铜 —— 一座好逛的数字图书馆。
> 每一本「书」都是真实抓取过 README 与文件树后写的说明，不是算法标签。

### 🖼️ [点击进入 3D 数字图书馆 →]({PAGES})

在 3D 馆里你可以：**拖拽转视角** · **滚轮推近** · **顶部搜索框即时过滤** · **分类 chips 筛选** · **按名称/最近更新/星数排序** · **点击书脊看详情卡并跳转仓库** · 🌙 点台灯开夜读模式 · 🔔 点铜铃摇出一场书浪。
（GitHub README 不支持交互，搜索/筛选/排序都在上面的网页里；本页是完整静态目录。）

## 🧭 馆内导航

| 想看什么 | 去哪里 |
|---|---|
| 📌 置顶仓 · 本馆说明书 | [置顶仓](#pinned) |
| 🫖 原创仓库 · 78 本 | [原创书架](#originals) |
| 🍴 复刻仓库 · 142 本 | [复刻书架](#forks) |
| ⭐ 上游馆藏 · 347 本 | [馆藏书架](#library) |
| 🎨 动画与视觉特效专架 | [特效专架](#visual) |
| 🧱 数据与再生成脚本 | [数据与脚本](#meta) |

## 📖 这本目录怎么读

| 字段 | 含义 |
|---|---|
| **它是什么** | 逐仓读取 README 正文、章节标题与根目录文件后手写的一段话；无 README 的按描述与文件结构如实标注 |
| **书脊色 / emoji** | 分类配色，与 3D 图书馆书架一致（数据见 `data/books.json` 的 palette） |
| **📖 / ⭐ / 🍴** | 原仓库 / 收藏 / 复刻链接，全部保留可点 |
| **折叠书架** | 每架默认收起，点标题展开；列表很长，避免刷屏 |

---""")

# ── 置顶仓 ────────────────────────────────────────────────
B.append(f"""<a id="pinned"></a>

## 📌 置顶仓 · github-catalog

| | |
|---|---|
| **仓库** | 🟨 [**github-catalog**](https://github.com/{OWNER}/github-catalog)（本页所在仓） |
| **它是什么** | {esc(doc['pinned']['what'])} |
| **两份产物** | `README.md`（人读目录）＋ `catalog.json`（机读结构化数据） |
| **在线版** | [3D 数字图书馆]({PAGES}) |

[▲ 回到顶部](#top)

---""")

# ── 卡片表格渲染 ──────────────────────────────────────────
def card_own(o):
    return (f"| {PALETTE[o['category']]['emoji']} [**{o['name']}**]({o['url']})<br>"
            f"`{esc(o.get('subcategory','')) or esc(o['category'])}` · {o.get('language') or '—'}"
            f"{upd(o.get('pushed_at',''))} | {esc(o['what'])} |")

def card_lib(e):
    fork = f" · [🍴 复刻]({e['fork_url']})" if e.get("forked") else ""
    eff = " ".join(f"`{x}`" for x in e.get("effects", []))
    return (f"| {PALETTE[e['category']]['emoji']} [**{e['full_name'].split('/')[-1]}**]({e['url']}){fork}<br>"
            f"`{esc(e.get('subcategory',''))}` · {e.get('language') or '—'} · ⭐{fmt_stars(e.get('stars'))}"
            f"{(' · ' + eff) if eff else ''} | {esc(e.get('what',''))} |")

def table(header, rows):
    return "\n".join([header, "|---|---|"] + rows)

# ── 原创书架 ──────────────────────────────────────────────
B.append("""<a id="originals"></a>

## 🫖 原创书架 · 78 本

> 名下 78 个原创仓（含本馆），逐仓抓 README/文件树后手写说明；编号仓（agent-XX / chat-XX 等）如实标注「源码归档」。按书架分组，点开即读。
""")
ORIG_ORDER = ["置顶仓", "游戏与互动娱乐", "Agent 桌面与 AI 客户端", "应用软件", "纯代码影片",
              "网页还原与镜像", "底层与逆向考古", "分发与沙盒", "空仓与占位"]
for i, cat in enumerate(ORIG_ORDER):
    items = cat_index[cat]
    if not items:
        continue
    open_ = "open " if i == 0 else ""
    B.append(f"""### {PALETTE[cat]['emoji']} {cat} · {len(items)} 本

<details {open_}>

{table("| 书 | 它是什么 |", [card_own(o) for o in items])}

[▲ 回到顶部](#top)

</details>
""")

# ── 复刻书架 ──────────────────────────────────────────────
B.append("""<a id="forks"></a>

## 🍴 复刻书架 · 142 本

> 我名下的 142 个复刻仓，按馆藏书架分组；一句话说明沿用馆藏逐仓结论，完整版见下方[馆藏书架](#library)。
""")
for cat, items in fork_index.items():
    if not items:
        continue
    rows = [f"| [{f['name']}]({f['url']}) | [{f['fork_of']}]({f['fork_upstream_url']}) | {esc(f['what'])} |" for f in
            sorted(items, key=lambda x: x["name"].lower())]
    B.append(f"""### {PALETTE[cat]['emoji']} {cat} · {len(items)} 本

<details>

{table("| 我的仓库 | 复刻自 | 一句话说明 |", rows)}

[▲ 回到顶部](#top)

</details>
""")

# ── 馆藏书架 ──────────────────────────────────────────────
B.append(f"""<a id="library"></a>

## ⭐ 馆藏书架 · {n_lib} 本

> 收藏 / 复刻的上游项目，逐册登记（347 = 329 ⭐ + 142 🍴 − 124 重合）。
""")
for cat, items in lib_index.items():
    if not items:
        continue
    rows = [card_lib(e) for e in sorted(items, key=lambda x: -(x.get("stars") or 0))]
    B.append(f"""### {PALETTE[cat]['emoji']} {cat} · {len(items)} 本

<details>

{table("| 书（原仓库 / 复刻） | 它是什么 |", rows)}

[▲ 回到顶部](#top)

</details>
""")

# ── 特效专架 ──────────────────────────────────────────────
B.append("""<a id="visual"></a>

## 🎨 动画与视觉特效专架

> 馆藏里「某种动画 / 视觉效果的网页代码」，按具体效果重排；一件可出现在多个效果下（数据来自 catalog.json 的 effects 字段）。
""")
for eff, items in eff_index.items():
    rows = [f"| {PALETTE[e['category']]['emoji']} [**{e['full_name']}**]({e['url']})"
            f"{(' · [🍴](' + e['fork_url'] + ')') if e.get('forked') else ''} | {esc(e.get('what',''))} |" for e in items]
    B.append(f"""### ✨ {eff} · {len(items)} 件

<details>

{table("| 项目 | 它是什么 |", rows)}

[▲ 回到顶部](#top)

</details>
""")

# ── 数据与脚本 ────────────────────────────────────────────
B.append(f"""<a id="meta"></a>

## 🧱 数据与脚本

| 文件 | 作用 |
|---|---|
| `catalog.json` | 总数据源：`pinned` 置顶仓 + `own_repos` 名下 220 仓（分类与逐仓说明）+ `catalog` 馆藏 347 条（README 自述原文 / 章节 / 文件树 / 标签） |
| `data/books.json` | 由 catalog.json 派生的「书」视图（562 本，含书脊配色 palette），3D 图书馆与 README 共用 |
| `index.html` | 单文件 Three.js 3D 数字图书馆，零构建，可直接部署 GitHub Pages |
| `scripts/build_books.py` | `python scripts/build_books.py --live` → 重新生成 data/books.json（`--live` 会用 gh api 刷新 stars / 更新时间） |
| `scripts/build_readme.py` | `python scripts/build_readme.py` → 重新生成本 README |

**更新流程**：新收藏/新仓库后 → 重跑 `build_books.py`（书架自动多一本书）→ 重跑 `build_readme.py` → 提交推送即可。

---

*图书馆由 [catalog.json](catalog.json) 数据驱动生成；项目用途以各仓库自身说明为准。*))""".rstrip())

readme = "\n".join(B)
open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n").write(readme)

# 校验：每个名下仓库 / 馆藏条目的链接都在 README 中
missing = [o["name"] for o in own if f"]({o['name']})" not in readme and f"/{o['name']})" not in readme]
assert not missing, missing
missing_lib = [e["full_name"] for e in doc["catalog"] if f"]({e['full_name']})" not in readme and e['url'] not in readme]
assert not missing_lib, missing_lib[:10]
print("README bytes:", os.path.getsize(os.path.join(ROOT, "README.md")))
print("sections:", readme.count("<details"), "| OK")
