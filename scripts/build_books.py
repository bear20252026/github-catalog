# -*- coding: utf-8 -*-
"""从 catalog.json 生成 data/books.json —— 3D 图书馆与 README 的唯一数据源。

用法:
  python scripts/build_books.py            # 纯本地（用 catalog.json 里已有的数据）
  python scripts/build_books.py --live     # 额外用 gh api 刷新馆藏上游的 stars / pushed_at

数据驱动：catalog.json 新增条目，重跑本脚本即可自动多一本书。
"""
import json, os, sys, subprocess, datetime, concurrent.futures

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OWNER = "bear20252026"

# 分类 → 书脊色 / emoji / 展示名（3D 书架与 README 共用同一套配色）
CATS = {
    # 名下原创
    "置顶仓":               {"emoji": "🟨", "color": "#B99A2E", "kind": "pinned"},
    "游戏与互动娱乐":       {"emoji": "🟩", "color": "#4E7D5F", "kind": "original"},
    "Agent 桌面与 AI 客户端": {"emoji": "🟦", "color": "#46688C", "kind": "original"},
    "应用软件":             {"emoji": "🟧", "color": "#B06E45", "kind": "original"},
    "纯代码影片":           {"emoji": "🟥", "color": "#9E5250", "kind": "original"},
    "网页还原与镜像":       {"emoji": "🟪", "color": "#7B6099", "kind": "original"},
    "底层与逆向考古":       {"emoji": "🟫", "color": "#77603F", "kind": "original"},
    "分发与沙盒":           {"emoji": "⬛", "color": "#4E4B46", "kind": "original"},
    "空仓与占位":           {"emoji": "⚪", "color": "#A9A294", "kind": "original"},
    # 上游馆藏
    "AI 智能体与编码工具":  {"emoji": "🔹", "color": "#3F6284", "kind": "library"},
    "视觉艺术与网页特效":   {"emoji": "🟣", "color": "#96548A", "kind": "library"},
    "桌面与移动客户端":     {"emoji": "🟠", "color": "#B87A44", "kind": "library"},
    "开发工具与命令行":     {"emoji": "🟤", "color": "#6B6748", "kind": "library"},
    "AI 模型与机器学习":    {"emoji": "🟢", "color": "#2F7264", "kind": "library"},
    "学习资源与清单":       {"emoji": "🟡", "color": "#9C8227", "kind": "library"},
    "办公与创作套件":       {"emoji": "🫒", "color": "#66834A", "kind": "library"},
    "前端与 Web 框架":      {"emoji": "🔵", "color": "#4F8CA8", "kind": "library"},
    "后端与基础设施":       {"emoji": "◼️", "color": "#5A6470", "kind": "library"},
    "编程语言与通用库":     {"emoji": "⚪", "color": "#857667", "kind": "library"},
}

LIVE = "--live" in sys.argv

def gh(path):
    try:
        p = subprocess.run(["gh", "api", path], capture_output=True, text=True,
                           timeout=30, encoding="utf-8", errors="replace")
        return json.loads(p.stdout) if p.returncode == 0 else None
    except Exception:
        return None

def enrich(pairs):
    """pairs: list of full_name -> 并发拉 stars / pushed_at（失败则返回 None 字段）"""
    out = {}

    def work(fn):
        d = gh(f"repos/{fn}")
        if not d:
            return fn, None
        return fn, {"stars": d.get("stargazers_count", 0),
                    "pushed_at": (d.get("pushed_at") or "")[:10]}

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for fn, d in ex.map(work, pairs):
            out[fn] = d
    return out


def main():
    doc = json.load(open(os.path.join(ROOT, "catalog.json"), encoding="utf-8"))
    books = []
    now = datetime.date.today().isoformat()

    # 置顶
    p = doc["pinned"]
    books.append({
        "id": "pinned:github-catalog", "title": "github-catalog",
        "kind": "pinned", "category": "置顶仓", "subcategory": "",
        "lang": "", "stars": 0, "updated": doc.get("updated", now),
        "desc": p["what"], "url": p["url"],
    })

    # 名下仓库（原创 + 复刻）
    for o in doc["own_repos"]:
        if o["name"] == "github-catalog":
            continue
        books.append({
            "id": "own:" + o["name"], "title": o["name"],
            "kind": "original" if o["kind"] == "original" else "fork",
            "category": o["category"], "subcategory": o.get("subcategory", ""),
            "lang": o.get("language", ""), "stars": o.get("stars", 0),
            "updated": o.get("pushed_at", ""),
            "desc": o["what"], "url": o["url"],
        })

    # 上游馆藏
    lib = []
    for e in doc["catalog"]:
        if e.get("url", "").startswith(f"https://github.com/{OWNER}/"):
            continue  # 自己收藏自己的 5 件已在 own_repos 里
        lib.append({
            "id": "lib:" + e["full_name"], "title": e["full_name"].split("/")[-1],
            "kind": "library", "category": e["category"],
            "subcategory": e.get("subcategory", ""),
            "lang": e.get("language", ""), "stars": e.get("stars", 0),
            "updated": e.get("updated", ""),
            "desc": e.get("what", ""), "url": e["url"],
        })

    if LIVE:
        todo = [b["id"].split(":", 1)[1] for b in lib]
        got = enrich(todo)
        for b in lib:
            fn = b["id"].split(":", 1)[1]
            if got.get(fn):
                b["stars"] = got[fn]["stars"]
                b["updated"] = got[fn]["pushed_at"]
        # 名下仓库也顺带刷新
        own_pair = [b["id"].split(":", 1)[1] for b in books if b["kind"] in ("original", "fork")]
        g2 = enrich(own_pair)
        for b in books:
            if b["kind"] in ("original", "fork"):
                d = g2.get(b["id"].split(":", 1)[1])
                if d:
                    b["stars"], b["updated"] = d["stars"], d["pushed_at"]

    books.extend(lib)

    for b in books:
        c = CATS.get(b["category"])
        assert c, "category missing palette: " + b["category"]
        b["color"] = c["color"]
        b["emoji"] = c["emoji"]
        if not b["updated"]:
            b["updated"] = ""

    counts = {
        "total": len(books),
        "pinned": sum(1 for b in books if b["kind"] == "pinned"),
        "original": sum(1 for b in books if b["kind"] == "original"),
        "fork": sum(1 for b in books if b["kind"] == "fork"),
        "library": sum(1 for b in books if b["kind"] == "library"),
        "categories": len({b["category"] for b in books}),
    }
    assert counts["total"] == len(doc["own_repos"]) + len(lib), counts
    assert counts["pinned"] + counts["original"] + counts["fork"] == len(doc["own_repos"]), counts
    assert counts["library"] == len(lib), counts

    payload = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "owner": OWNER,
        "counts": counts,
        "palette": {k: {"emoji": v["emoji"], "color": v["color"], "kind": v["kind"]}
                    for k, v in CATS.items()},
        "books": books,
    }
    out = os.path.join(ROOT, "data", "books.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print("books:", counts, "->", out)


if __name__ == "__main__":
    main()
