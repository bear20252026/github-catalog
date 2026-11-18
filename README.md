# 📚 bear20252026 的 GitHub 总目录

> 一个账号，两份馆藏：**名下 220 个仓库**（78 原创 + 142 复刻）＋ **上游 347 件收藏/复刻的图书馆**。
> **每一件都真实抓取过 README 与根目录文件树**，下面的说明是逐仓读过之后写的，不是算法标签。

## 🧭 总导航

| 想看什么 | 去哪里 |
|---|---|
| 📌 置顶仓 github-catalog（本仓） | [置顶仓](#pinned) |
| 🏠 我名下的全部仓库 · 220 个 | [第一部分](#own) |
| ├ 原创仓库 · 78 个（游戏 / Agent / 应用 / 影片 / 逆向…） | [原创仓库](#originals) |
| └ 复刻仓库 · 142 个（按书架分组，逐仓一句话） | [复刻仓库](#forks) |
| 📖 上游馆藏 · 347 件逐仓说明 | [第二部分](#library) |
| 🎨 动画与视觉特效专架（按具体效果） | [专架](#visual) |
| 🧱 结构化数据（README 自述原文 / 文件树 / 标签） | [catalog.json](catalog.json) |

---

<a id="pinned"></a>

## 📌 置顶仓 · github-catalog

| | |
|---|---|
| **仓库** | [bear20252026/github-catalog](https://github.com/bear20252026/github-catalog)（本页所在的仓） |
| **干什么** | 这本总目录本身：名下 220 个仓库 + 上游 347 件馆藏，逐册登记成「图书馆」；说明逐仓读过 README 后手写，不是算法标签 |
| **两份产物** | `README.md`（人读的总目录）＋ `catalog.json`（机读的结构化数据：README 自述原文、章节标题、根目录文件树、标签） |
| **更新方式** | 重新抓取 star / fork / 仓库列表，逐仓抓 README 与文件树后全量重排 |
<a id="own"></a>
<a id="originals"></a>

## 🏠 第一部分 · 我名下的全部仓库（220 个）

**78 个原创 + 142 个复刻。** 原创仓逐个抓过 README 与根目录文件树后手写说明；无 README 的按描述与文件结构如实标注；编号仓（agent-XX / chat-XX / workbench-XX 等）多为知名开源项目的**本地源码归档**，逐条注明。
其中 5 个原创仓（aegis-dual-platform、drawing_notes_app、dream-gallery、monster-word、wxlike）也被自己点了星，在[第二部分馆藏](#library)里同样有登记。

### 🎮 游戏与互动娱乐 · 11 件


#### 网页游戏 · 8 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [viper11](https://github.com/bear20252026/viper11) | JavaScript | VIPER 11——网页 3D 空战飞行模拟游戏站（F-16 / F-35C，Three.js 前端）；无 README，按站点结构与描述如实标注。 |
| [viper-ai](https://github.com/bear20252026/viper-ai) | TypeScript | VIPER AI——AI 原生飞行模拟器：每个游戏功能都是一个可被 AI 调用的工具（TypeScript + Vite 工程，无 README）。 |
| [plane](https://github.com/bear20252026/plane) | — | VIPER 11 静态站还原包——从 viperoneone.com 抓取的构建产物（Three.js 空战 / F-16 / F-35C），仓里只有 README 说明页。 |
| [paper-snake](https://github.com/bear20252026/paper-snake) | TypeScript | 纸格竞技场 PAPER SNAKE——本地可跑的贪吃蛇 IO 游戏：React 19 + Vite + TypeScript strict + Tailwind 4 + Zustand + PixiJS 8，全部原创 Canvas 程序化美术；单机实现，无联网匹配、无支付、无广告。 |
| [paintgrab](https://github.com/bear20252026/paintgrab) | TypeScript | 圈地大作战 Paint Grab——three.js 3D 圈地竞技网页游戏：每日挑战、服务端校验排行榜与二维码挑战分享；README 现展示同一模板演进出的浮岛收集玩法（Sky Cores，three.js + Rapier，带可改的引擎层与冒烟测试）。 |
| [faraway-game](https://github.com/bear20252026/faraway-game) | TypeScript | 远方 · Faraway——第一人称 three.js 场景：花海草丘之上无尽积云之海，山顶立着披苔藓、系红丝带的古老机器人守望者；含多人房间服务端与测试冒烟脚本。 |
| [canyon-circuit](https://github.com/bear20252026/canyon-circuit) | TypeScript | Canyon Circuit——低多边形 3D 街机赛车（Three.js + TypeScript + Vite）：阳光峡谷环线，爬坡、发夹弯、大桥、跳台、精准加速带与开阔沙漠，同性能车辆公平竞速。 |
| [snake-game](https://github.com/bear20252026/snake-game) | HTML | Android 贪吃蛇小游戏——由 GitHub Actions 云端构建（仓库仅 README + index.html）。 |

#### Godot 游戏 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [emberduel](https://github.com/bear20252026/emberduel) | GDScript | 余烬牌局 Ember Duel——双语烹饪题材战术卡牌对战（Godot 4.7）：完整源码、本地化、资产溯源与可移植构建脚本，可对接 v4 匹配服务端打在线多人。 |
| [neon-alley-brawl](https://github.com/bear20252026/neon-alley-brawl) | GDScript | 霓虹街头 Neon Alley Brawl——2D 像素横版动作过关（Godot 4.7），带资产溯源、本地化与在线多人服务端对接文档。 |
| [plushie-merge](https://github.com/bear20252026/plushie-merge) | GDScript | Plushie Merge——Suika 式毛绒玩偶物理合并消除（Godot 4.7，双语，本地多人），完整源码与资产溯源。 |

### 🤖 Agent 桌面与 AI 客户端 · 35 件


#### Agent 框架与桌面（编号归档） · 6 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [agent-01](https://github.com/bear20252026/agent-01) | TypeScript | OpenClaw 🦞——「把助手放进你的设备与聊天里」的开源个人 AI 助理框架（源码归档）。 |
| [agent-02](https://github.com/bear20252026/agent-02) | TypeScript | Agent TARS——字节跳动开源的多模态通用 Agent：真实操作浏览器、命令行与文件系统完成任务（源码归档）。 |
| [agent-03](https://github.com/bear20252026/agent-03) | TypeScript | Eigent——开源 AI 协作桌面（Cowork Desktop）：一条工作流调度多个「AI 员工」解锁生产力（源码归档）。 |
| [agent-04](https://github.com/bear20252026/agent-04) | Go | Wove——开源桌面 AI 编码 Agent：用自己的 API Key 直连任意提供商（Claude/GPT/Gemini/MiniMax/Ollama），本地写码、跑命令、浏览网页并自检成果，无代理、无云中转、无厂商锁定（源码归档）。 |
| [agent-05](https://github.com/bear20252026/agent-05) | TypeScript | PiDesk——带屏幕感知与 GUI 控制的开源桌面 AI Agent（macOS 优先），基于 pi monorepo 引擎：TUI、Agent 循环、编码工具、会话持久化、压缩与多进程（源码归档）。 |
| [agent-06](https://github.com/bear20252026/agent-06) | TypeScript | AgentForge——自建 AI Agent 桌面工具：Agent Loop + Skills 系统 + MCP 协议，DeepSeek 主模型，工具链全 Node 实现，Tauri2 + React19，可打包 Windows .exe / macOS .dmg。 |

#### AI 聊天客户端（编号归档） · 11 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [chat-01](https://github.com/bear20252026/chat-01) | TypeScript | LobeHub——把 Agent 组织成 7×24 值班的 AI 团队：雇佣、排班、汇报，人保持掌舵（LobeChat 团队出品，源码归档）。 |
| [chat-02](https://github.com/bear20252026/chat-02) | TypeScript | Cherry Studio——多模型桌面 AI 客户端：聊天、助手与 MCP 工具生态（源码归档）。 |
| [chat-03](https://github.com/bear20252026/chat-03) | TypeScript | Jan——开源 ChatGPT 替代品：本地优先，离线可跑本地模型（源码归档）。 |
| [chat-04](https://github.com/bear20252026/chat-04) | TypeScript | Chatbox——桌面 / 移动 / 网页多端 AI 聊天客户端社区版（源码归档）。 |
| [chat-05](https://github.com/bear20252026/chat-05) | TypeScript | 5ire——精致 AI 助手与 MCP 客户端（Electron，源码归档）。 |
| [chat-06](https://github.com/bear20252026/chat-06) | JavaScript | PuPu——本地与云端模型通吃的桌面 AI 客户端：工作区感知聊天 + 内置 MCP 工具（源码归档）。 |
| [chat-07](https://github.com/bear20252026/chat-07) | JavaScript | ChatAnyLLM——通过 OpenAI 兼容 API 连接任意模型提供商或 Agent 系统的桌面聊天应用（源码归档）。 |
| [chat-08](https://github.com/bear20252026/chat-08) | JavaScript | UniChat AI——跨平台桌面应用，用统一优雅的聊天界面访问多家大模型（源码归档）。 |
| [chat-09](https://github.com/bear20252026/chat-09) | — | LLM Symphony——Windows 上的隐私优先多模型聊天客户端：默认隐身、用自己的 API Key 直连 ChatGPT / Claude / Grok / DeepSeek / Gemini（仅 README 文档仓，已上架 Microsoft Store）。 |
| [chat-10](https://github.com/bear20252026/chat-10) | C# | llm-agent——.NET WinForms 的 Windows 桌面客户端：统一界面访问多家 LLM 服务商，经典三层架构 API/BLL/DAL（源码归档）。 |
| [chat-11](https://github.com/bear20252026/chat-11) | JavaScript | OOLIS——100% 离线的 LLM 桌面客户端：数据完全自控，默认支持 Ollama 本地与多家云端（源码归档）。 |

#### 模型切换器与 AI 工作台（编号归档） · 9 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [misc-01](https://github.com/bear20252026/misc-01) | Svelte | Open WebUI Desktop——Open WebUI 的桌面版 Electron 应用（源码归档）。 |
| [misc-02](https://github.com/bear20252026/misc-02) | TypeScript | WorkspAIce——从 Chatbox 分叉出的本地优先桌面 AI 工作台：「你的 AI、你的机器、你做主」（源码归档）。 |
| [switcher-01](https://github.com/bear20252026/switcher-01) | Rust | CC Switch——Claude Code / Claude Desktop / Codex / Gemini CLI / Grok Build / OpenCode / OpenClaw / Hermes Agent 的一体化配置管理器（源码归档）。 |
| [switcher-02](https://github.com/bear20252026/switcher-02) | TypeScript | Witsy——桌面 AI 助手 + 通用 MCP 客户端（Kochava Studios，源码归档）。 |
| [switcher-03](https://github.com/bear20252026/switcher-03) | Java | PaiSwitch——AI 编码 Agent 的模型控制台：本地优先的 Agent Model Control Plane，把 Claude Code / Codex 的模型选择、API Key 管理、协议适配、配置备份与 Skills 管理收拢到一个工作台（macOS 工程 + Web/后端，源码归档）。 |
| [workbench-01](https://github.com/bear20252026/workbench-01) | JavaScript | AnythingLLM——All-in-One AI 应用：与文档聊天、AI Agent、多用户、超可配置（Mintplex Labs，源码归档）。 |
| [workbench-02](https://github.com/bear20252026/workbench-02) | Kotlin | Askimo——「一个应用，接所有模型，文件留在本地」：聊天、搜文件与网络、跑脚本、多步 AI 工作流与 Agent Skills，Kotlin 多端 + CLI（源码归档）。 |
| [workbench-03](https://github.com/bear20252026/workbench-03) | TypeScript | AIME Chat——「Agent = 模型 + Harness」的完整智能体外壳：编排循环、工具、上下文与记忆、子 Agent、护栏与可观测性，多提供商支持（macOS/Windows/Linux，源码归档）。 |
| [workbench-04](https://github.com/bear20252026/workbench-04) | JavaScript | LLM Desktop——Electron + React + LangGraph 的统一 AI 工作台：Gemini/OpenAI/Claude 云端与 Gemma/Phi/Llama 本地一键切换，可跑 Agent 任务（源码归档）。 |

#### AionUi 系列 · 4 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [AionUi](https://github.com/bear20252026/AionUi) | TypeScript | AionUi——iOfficeAI 开源的 24/7 AI Agent 协作桌面：可同时驱动 OpenClaw、Hermes、Claude Code、Codex、OpenCode 等 20 多种编码 Agent（源码归档）。 |
| [AionUi-fork](https://github.com/bear20252026/AionUi-fork) | TypeScript | AionUi 全历史 fork——完整保留上游提交历史的复刻副本。 |
| [AionUi-Local-2.2.2](https://github.com/bear20252026/AionUi-Local-2.2.2) | Rust | AionUi v2.2.2 本地免登录版——前端 no-login 补丁 + 后端 find_by_model 回退 + GitHub Actions 云构建；桌面免登录直用，网页版可单用户免登录或多用户按账号隔离（仅供学习研究）。 |
| [AionUi-NoLogin-Fork](https://github.com/bear20252026/AionUi-NoLogin-Fork) | Rust | AionUi NoLogin Fork · 完美本地版——完整可重建的免登录分叉归档：脱离官方账号体系、零付费、全本地运行，不被官方更新推送控制（仅供学习研究）。 |

#### 编码 Agent 与官方镜像 · 5 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [DeepSeek-Harness](https://github.com/bear20252026/DeepSeek-Harness) | TypeScript | DeepSeek Harness（dsh）——DeepSeek 官方开源的 Agent harness：「一切皆插件」架构，模型、工具、UI、技能均可由插件替换，由 Cordis 驱动（源码归档，developer preview）。 |
| [MiMo-Code](https://github.com/bear20252026/MiMo-Code) | TypeScript | MiMoCode（小米）——终端原生 AI 编码助手：读写代码、跑命令、管 Git，带跨会话持久记忆并持续自我进化，可接任意主流 LLM；此仓只取最新单提交镜像，不追历史。 |
| [ClawCode](https://github.com/bear20252026/ClawCode) | Rust | Claw Code——围绕 LazyCodex / Gajae Code 等「爪系」编码 Agent 的配置与工具链仓库：含 .claude / .claw / .omx 配置与容器化脚本。 |
| [OpenWorker](https://github.com/bear20252026/OpenWorker) | Python | OpenWorker——桌面上的开源 AI 同事（andrewyng）：交付「干完的活」而非聊天——成稿文档、带数字的 Slack 回复、更新日历、分诊收件箱（源码归档，open beta）。 |
| [b07-build](https://github.com/bear20252026/b07-build) | TypeScript | AI Work OS v0.19.0——本地优先、可恢复、受控执行且可受控扩展的个人 Agent 学习工作系统：Rust 进程监督控制面 + TypeScript 编排/策略/可恢复运行时 + Python 重计算 sidecar，工作台只提交意图与订阅事件。 |

### 📱 应用软件 · 10 件


#### 桌面与跨平台应用 · 6 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [monster-word](https://github.com/bear20252026/monster-word) | Dart | Monster Word——怪兽养成 × FSRS 记忆算法的离线英语单词学习应用（Flutter）：怪兽小屋、签到储蓄罐、聚宝日历等激励体系，词库与例句全部离线，SQLite 持久化，发布 Windows / Android 双端。 |
| [drawing_notes_app](https://github.com/bear20252026/drawing_notes_app) | Dart | 绘图笔记 App——本地优先的加密绘图与笔记应用（Flutter）：块文档、分页画布、无限画布，同步为可选的用户自配 WebDAV 端到端加密，不用即零网络请求；Windows / Android / macOS。 |
| [aegis-dual-platform](https://github.com/bear20252026/aegis-dual-platform) | Python | Aegis 双端安全浏览器——以「边界驱动架构」替代补丁式加固：所有高危副作用必经唯一能力代理裁决，裁决逻辑收敛在无 I/O 的 Rust 策略核心；Windows（C#/.NET 10 + WebView2）+ Android（Kotlin/Compose）。 |
| [desktop-organizer](https://github.com/bear20252026/desktop-organizer) | Lua | 桌面整理 SnowDesktop（发行版）——Windows 桌面整理美化工具：Direct2D 自绘桌面替代 Explorer 原生图标，多显示器网格布局、可嵌入组件与 Lua 脚本扩展；仓库带 exe 与任务栏钩子 DLL。 |
| [desktop-organizer-source](https://github.com/bear20252026/desktop-organizer-source) | C++ | SnowDesktop 源码（苹果风格改造）——C++/CMake 工程：自定义桌面、可嵌入组件与 Lua 脚本扩展的完整实现。 |
| [dream-gallery](https://github.com/bear20252026/dream-gallery) | JavaScript | 梦幻画廊 Dream Gallery——基于《小王子》B612 的 Three.js 3D 交互画廊游戏：主线是可玩的小说复述（坠机沙漠 → 画画 → 狐狸），配单文件 Node 零依赖后端（私有备份仓基线）。 |

#### 官网页面 · 1 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [dream-gallery-landing](https://github.com/bear20252026/dream-gallery-landing) | TypeScript | 梦幻画廊 · 昆仑灵鉴官方落地页（开篇）——React + Vite 源码。 |

#### 通信与源码恢复 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [wxlike](https://github.com/bear20252026/wxlike) | Rust | wxlike——Rust 优先的微信风格 IM 脚手架：QUIC 传输、MQ 路由多节点 hub、端到端加密骨架、动态群组；18 个职责组、100 张任务卡的全平台交付计划与最新 UI（2026-10-24）。 |
| [linkup-rebuild](https://github.com/bear20252026/linkup-rebuild) | Kotlin | LinkUp 重建工作区——源码丢失后从 1.5.6 / 1.6.6 两个安装包恢复并重建客户端与服务端：418 个 JVM/Robolectric 离线回归测试可跑（公司内部授权）。 |
| [linkup-recovery](https://github.com/bear20252026/linkup-recovery) | Kotlin | LinkUp 源码恢复工作区（com.youloft.watcher，公司授权）——按 1.6.6 原布局恢复轨迹页 UI 外壳（全屏地图槽、44dp 标题、三档拖拽渐变等），禁止商用与再分发。 |

### 🎬 纯代码影片 · 5 件


#### 动画长片 · 4 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [deep-sea-post-film](https://github.com/bear20252026/deep-sea-post-film) | Python | 深海邮局 Deep Sea Post Office——60 分钟纯 Python 逐帧渲染动画长片：小潜艇邮差替丢失歌声的鲸鱼奶奶送信，让寂静小镇重新开口唱歌；字体（马善政楷体）、配乐、画面全部由代码生成。 |
| [fallen-star-film](https://github.com/bear20252026/fallen-star-film) | Python | The Fallen Star——60 分钟纯 Python「手绘」动画长片：会笑的星星坠落到 B612 小行星，男孩、绵羊与小星星 Pip 送它回家；每一帧的笔触、光影与角色都是代码画的。 |
| [rain-shop-film](https://github.com/bear20252026/rain-shop-film) | Python | 雨铺 The Rain Shop——60 分钟纯 Python 水墨动画长片：灰色水乡里卖瓶装天气的云奶奶，久旱之年孙子小满打开红罐放出困住的雨龙，全镇在雨里重新开门营业。 |
| [sheep-in-the-box-film](https://github.com/bear20252026/sheep-in-the-box-film) | JavaScript | The Sheep in the Box——代码动画长片：Remotion + GSAP 时间线渲染，每个场景一个 React/JS 文件；含 45 分钟正片剪辑与原始短片，带渲染说明与合并脚本。 |

#### 教学视频 · 1 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [na-ise-scientific-popup-book](https://github.com/bear20252026/na-ise-scientific-popup-book) | JavaScript | 钠离子选择性电极：科学立体书动画——4 分 20 秒、1280×720@30fps 教学视频工程：Python 逐帧绘制，真实透视运镜、沿铰线折起 90° 的纸雕图版与可展开文本面板；附 MP4 成品、SRT 字幕与完整制作指南。 |

### 🌐 网页还原与镜像 · 8 件


#### 站点还原 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [anlibili](https://github.com/bear20252026/anlibili) | JavaScript | anlibili 源码还原包——从 B 站视频聚合站抓取的完整静态源码（2026-11-04）：1902 个视频数据 + hash 路由 + 搜索收藏历史（localStorage），纯静态无构建。 |
| [learn-arduino-zh](https://github.com/bear20252026/learn-arduino-zh) | JavaScript | Learn Arduino 中文版——learn-arduino-red.vercel.app 的完整本地静态克隆，交互式 3D Arduino 课程可离线运行（Vite SPA，需起本地 HTTP 服务）。 |
| [learn-arduino-zh-src](https://github.com/bear20252026/learn-arduino-zh-src) | JavaScript | Learn Arduino 中文版源码工程——由构建产物逆推还原的可读可改源码：代码逻辑与线上行为 100% 一致，全部模块语义化命名并经 Prettier 格式化，附 ARCHITECTURE-REVERSE 逆向方法与压缩分块映射。 |

#### 音乐播放器镜像 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [aural-music-player](https://github.com/bear20252026/aural-music-player) | HTML | AURAL 音乐播放器（Z.ai 搞AI的西窗烛镜像）——纯前端音乐播放器：网易云 / QQ 音乐多平台搜索、lrclib 等多源歌词、9 种聊天软件主题（QQ/微信/Discord/Telegram/iMessage…），带 Node 代理。 |
| [lanyra-music](https://github.com/bear20252026/lanyra-music) | HTML | 澜弦 LANYRA——玻璃拟态风格沉浸式音乐播放器：网易云 API 搜索、歌词同步、从专辑封面提取主题色、响应式布局，带 Node 代理服务。 |
| [neumorphism-music](https://github.com/bear20252026/neumorphism-music) | HTML | Neumorphism Music Player——新拟态风格音乐播放器：真实立体感双向阴影、网易云搜索、播放列表与歌词同步滚动高亮，带 Node 代理。 |

#### 3D 交互镜像 · 1 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [noir48-3d-typewriter](https://github.com/bear20252026/noir48-3d-typewriter) | HTML | NOIR 48 · 交互式 3D 打字机（Z.ai typewriter 镜像）——Three.js 实时打字（键盘输入驱动字模击打纸张）、0–100% 机械爆炸拆解滑块、零件全屏环绕预览与售货台模式，单 index.html。 |

#### 占位说明 · 1 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [invisible-cloak-site](https://github.com/bear20252026/invisible-cloak-site) | — | Invisible Cloak Website——WebGL 交互网站；目前仓库只有 README 一页说明。 |

### 🧬 底层与逆向考古 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [tabbit-001](https://github.com/bear20252026/tabbit-001) | C | Ghidra 反编译考古仓：ghidra_glic_decompiled 全量 C 产物、还原目录与 out 输出（无 README，按文件如实标注）。 |
| [lp-archaeology](https://github.com/bear20252026/lp-archaeology) | C | 无 README 的逆向拼装档案：字符串表、地址目录、framework.js、REASSEMBLE 拼装笔记与深挖档案。 |
| [chromium150-tabby](https://github.com/bear20252026/chromium150-tabby) | Batchfile | 基于 Chromium 150 的 AI 浏览器定制工程（Tabby）：逆向 Tabbit AI Browser 核心功能并集成进自编译 Chromium，含架构设计、API、扩展开发、部署与故障排除全套文档和构建脚本。 |

### 📦 分发与沙盒 · 2 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [ARTEX-release](https://github.com/bear20252026/ARTEX-release) | — | ARTEX 预编译二进制分发仓——原 Release 与 Docker 镜像失效后，用 GitHub Actions 从源码云端重编译出开箱即用的版本；不含源码（源码在 bear20252026/ARTEX）。 |
| [bear](https://github.com/bear20252026/bear) | JavaScript | Vite React+TS 模板起手的个人沙盒：Kimi Agent 对话存档压缩包、info / me 笔记与未命名实验。 |

### 🕳️ 空仓与占位 · 3 件

| 仓库 | 语言 | 它是什么 |
|---|---|---|
| [hermes-agent](https://github.com/bear20252026/hermes-agent) | — | 空仓占位——Hermes Agent（开源 AI Agent）预留仓，暂无内容（注意：馆藏里的 bear20252026/hermes-agent-1 是 NousResearch/hermes-agent 的复刻，另一个仓）。 |
| [HermesDesktop](https://github.com/bear20252026/HermesDesktop) | — | 空仓占位——Hermes 桌面应用构建预留仓，暂无内容。 |
| [skills-introduction-to-github](https://github.com/bear20252026/skills-introduction-to-github) | — | GitHub Skills 官方练习《Introduction to GitHub》占位仓，暂无内容。 |
<a id="forks"></a>

### 复刻仓库 · 142 个

> 一句话说明沿用馆藏逐仓读 README 后写的结论，完整版在[第二部分](#library)对应书架。按书架分组，便于对照。

#### 学习资源与清单 · 8 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [bank-logos](https://github.com/bear20252026/bank-logos) | [icongo/bank-logos](https://github.com/icongo/bank-logos) | 各家银行的 SVG 标志合集。 |
| [claude-quickstarts](https://github.com/bear20252026/claude-quickstarts) | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Anthropic 官方示例项目集，教开发者快速上手构建 Agent，含 computer use 与最新 toolset 用法。 |
| [everyone-can-use-english](https://github.com/bear20252026/everyone-can-use-english) | [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 《人人都能用英语》开放教程与 1000 小时训练体系，另有 Enjoy 浏览器插件给 YouTube／Netflix 加学习层。 |
| [expert_readed_books](https://github.com/bear20252026/expert_readed_books) | [0voice/expert_readed_books](https://github.com/0voice/expert_readed_books) | 给工程师开的中文书单，按计算机、软件工程、数学、创业、人文分类，附内容介绍与读后感。 |
| [huashu-bird-sticker](https://github.com/bear20252026/huashu-bird-sticker) | [alchaincyf/huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker) | 按 AviList v2026 整理的 1.1 万多种鸟类白边贴纸库，每种附多语种鸟名、分布、形态与保护等级，CC BY 4.0，出自观鸟 App「鸣迹」。 |
| [remix-words-funny](https://github.com/bear20252026/remix-words-funny) | [SteveSuv/remix-words-funny](https://github.com/SteveSuv/remix-words-funny) | 免费开源英语单词学习网站 WordsFunny：以单词书为中心，支持词表、收藏、已掌握/未掌握切换与评论互动。 |
| [tsl](https://github.com/bear20252026/tsl) | [prinzipiell/tsl](https://github.com/prinzipiell/tsl) | 学习 Three.js Shading Language（TSL）的练习仓：20 个独立着色器实验目录（boing-boing-box、ember-flow、the-river、marcher…）；无 README，按目录结构与上游描述标注。 |
| [word-atlas](https://github.com/bear20252026/word-atlas) | [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 词光 Word Atlas：7298 个雅思词条配原创插画、英美发音与 FSRS 间隔复习，把单词变成画面，已有 iOS App。 |

#### 开发工具与命令行 · 9 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [ARTEX](https://github.com/bear20252026/ARTEX) | [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 百度「agent+」攻防挑战赛冠军项目，AI 自主渗透测试系统（此仓库无 README，为个人复刻）。 |
| [chromium](https://github.com/bear20252026/chromium) | [chromium/chromium](https://github.com/chromium/chromium) | Chromium 开源浏览器项目的官方 GitHub 源码镜像。 |
| [container](https://github.com/bear20252026/container) | [apple/container](https://github.com/apple/container) | 苹果官方工具：在 Mac 上以轻量虚拟机创建并运行 Linux 容器，可推送自建镜像。 |
| [craft-anything](https://github.com/bear20252026/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | 指着一个软件说出你想要什么：它用真实检查工具研究原作、让编码 Agent 建新项目，再拿结果对照原作校验。 |
| [fairplay-decrypt](https://github.com/bear20252026/fairplay-decrypt) | [EthanArbuckle/fairplay-decrypt](https://github.com/EthanArbuckle/fairplay-decrypt) | 离线解密 FairPlay 加密的 iOS IPA，凭账户 16 字节凭据独立推导密钥，不依赖越狱设备在线环境。 |
| [open-claude-ui](https://github.com/bear20252026/open-claude-ui) | [Caho1/open-claude-ui](https://github.com/Caho1/open-claude-ui) | 逆向拆解 Claude 桌面端，高保真复刻其设计系统、30 个 React 组件与 8 项交互物理算法，附 3000+ 行分析手册。 |
| [shannon](https://github.com/bear20252026/shannon) | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 自主 AI 渗透测试员，分析 Web 应用与 API 的源码、找出漏洞并实际验证，可作为 Claude/Codex 插件运行。 |
| [tailscale](https://github.com/bear20252026/tailscale) | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 基于 WireGuard 的零配置私有组网（带 2FA），此仓库是 Tailscale 开源代码的主体。 |
| [xtool](https://github.com/bear20252026/xtool) | [xtool-org/xtool](https://github.com/xtool-org/xtool) | 跨平台 Xcode 替代：在 Linux／WSL／Windows／macOS 上用 SwiftPM 构建并部署 iOS 应用。 |

#### 桌面与移动客户端 · 21 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [aerial-tv](https://github.com/bear20252026/aerial-tv) | [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | 给国产电视的干净桌面：tvOS 风格开源 Android TV 启动器，无广告、开机自动接管；手机扫码就能拖图标排序、改名、隐藏、加 HDMI 信号源，附 706 张磁贴图标库。 |
| [AFFiNE](https://github.com/bear20252026/AFFiNE) | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 开源一体化知识工作区，把维基、知识库、文档与白板拼在一起，定位是「不止 Notion 和 Miro」。 |
| [anx-reader](https://github.com/bear20252026/anx-reader) | [Anxcye/anx-reader](https://github.com/Anxcye/anx-reader) | 支持多格式电子书、带 AI 能力的阅读器，另有 Calibre 插件，主打专注阅读。 |
| [ElyOffice](https://github.com/bear20252026/ElyOffice) | [ELY-Open-Source/ElyOffice](https://github.com/ELY-Open-Source/ElyOffice) | 用 Rust + GPUI 写的离线优先桌面办公套件。 |
| [Fieldwatch](https://github.com/bear20252026/Fieldwatch) | [OffGridPete/Fieldwatch](https://github.com/OffGridPete/Fieldwatch) | 只收不发的 Android 观察工具：列出手机能探测到的 Wi-Fi 热点与 BLE 设备，用来看清身边的射频环境。 |
| [HGhub1](https://github.com/bear20252026/HGhub1) | [Minireel/HGhub](https://github.com/Minireel/HGhub) | 通用视频播放器：靠导入 JavaScript 插件接入不同内容源，浏览、搜索、播放与个人片库都在同一个 App 里。 |
| [hongguo-drama](https://github.com/bear20252026/hongguo-drama) | [jackotom/hongguo-drama](https://github.com/jackotom/hongguo-drama) | 红果短剧桌面版（M 系列／Intel Mac、Windows，也顾及 NAS）：三来源搜索、播放、下载、追剧与合并导出在一个应用里完成。 |
| [ieaseMusic](https://github.com/bear20252026/ieaseMusic) | [trazyn/ieaseMusic](https://github.com/trazyn/ieaseMusic) | Electron + React + MobX 写的优雅网易云音乐第三方桌面客户端，API 由 NeteaseCloudMusicApi 提供。 |
| [LinkSwift](https://github.com/bear20252026/LinkSwift) | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | 油猴脚本，基于网盘公开 API 获取百度／阿里／移动／天翼／迅雷／夸克的直接下载地址，明确声明不破解限速。 |
| [Moect](https://github.com/bear20252026/Moect) | [mofan6/Moect](https://github.com/mofan6/Moect) | Windows 微信 4.x 聊天记录读取、整理与导出桌面工具，支持好友／群聊、头像、图片、GIF 的备份与离线归档。 |
| [mygo-music](https://github.com/bear20252026/mygo-music) | [zhangnjsd/mygo-music](https://github.com/zhangnjsd/mygo-music) | 用 Go + MyGo 写的第三方音乐桌面客户端，原生界面、不带 WebView。 |
| [Pake](https://github.com/bear20252026/Pake) | [tw93/Pake](https://github.com/tw93/Pake) | 一条命令把任意网站打包成轻量桌面应用（Tauri + Rust）：macOS / Windows / Linux 全支持，比 Electron 轻得多；开源 CLI + 桌面 App。 |
| [phongent](https://github.com/bear20252026/phongent) | [mylea1/phongent](https://github.com/mylea1/phongent) | 基于 Mika 的多设备手机 Agent 主控台：用自然语言派任务，一个界面查看各设备进度、消息与实时画面。 |
| [Seen](https://github.com/bear20252026/Seen) | [HauUhang/Seen](https://github.com/HauUhang/Seen) | 极简 Android 工具：一个输入框直达抖音／小红书／知乎／B站／X／Reddit／YouTube 的搜索结果页，绕开开屏推荐流防分心。 |
| [short_videos](https://github.com/bear20252026/short_videos) | [jiuhunwl/short_videos](https://github.com/jiuhunwl/short_videos) | 短视频／图集去水印接口示例，覆盖抖音、快手、小红书、B站、微博、网易云、皮皮虾等；声明仅供技术研究与学习。 |
| [spotify-tui](https://github.com/bear20252026/spotify-tui) | [Rigellute/spotify-tui](https://github.com/Rigellute/spotify-tui) | Rust 写的终端版 Spotify 客户端（TUI）。 |
| [video_vip](https://github.com/bear20252026/video_vip) | [88lin/video_vip](https://github.com/88lin/video_vip) | 油猴脚本，聚合多个第三方解析接口免费看爱奇艺／腾讯／优酷／B站等 VIP 视频，自动匹配选集、去广告。 |
| [WeChatMsg](https://github.com/bear20252026/WeChatMsg) | [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 微信聊天记录导出与本地归档工具，把对话留存下来做自己的数据资产与 AI 记忆素材。 |
| [weread-book-exporter](https://github.com/bear20252026/weread-book-exporter) | [WANGXIN-567/weread-book-exporter](https://github.com/WANGXIN-567/weread-book-exporter) | 微信读书全书无损导出，一键出双字体精排 PDF／EPUB／纯 Markdown 笔记（适配 Obsidian、Notion），专门解决网页端翻页漏字。 |
| [xiaoai-agent-unlock](https://github.com/bear20252026/xiaoai-agent-unlock) | [zhonglike/xiaoai-agent-unlock](https://github.com/zhonglike/xiaoai-agent-unlock) | 绕过设备校验，让小米笔记本专属的「超级小爱／小爱同学」PC 客户端跑在任意品牌电脑上，语音助手、耳机联动、跨设备控制都能用。 |
| [YesPlayMusic](https://github.com/bear20252026/YesPlayMusic) | [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic) | 高颜值第三方网易云音乐播放器（Electron），支持 Windows／macOS／Linux，可选 Nginx 反代 API 以避免跨域问题。 |

#### AI 智能体与编码工具 · 44 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [agent-desktop](https://github.com/bear20252026/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 给 AI Agent 的 computer use CLI：读桌面应用的无障碍树并转成带 ref 的 JSON，Agent 按 ref 点击或输入后再读回结果。 |
| [Agent-Reach](https://github.com/bear20252026/Agent-Reach) | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 给 AI Agent 装上「看整个互联网」的眼睛，能读与搜 Twitter、Reddit、YouTube 等平台内容。 |
| [ai-design-skills](https://github.com/bear20252026/ai-design-skills) | [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | 给 AI 编码工具读的设计技能合集（Claude Code／Cursor／Codex／Windsurf 等），每个都是一份 markdown 规则文件。 |
| [AnyCrawl](https://github.com/bear20252026/AnyCrawl) | [any4ai/AnyCrawl](https://github.com/any4ai/AnyCrawl) | Node.js／TypeScript 爬虫，把网站转成 LLM 就绪数据并做结构化抽取。 |
| [blender-skills](https://github.com/bear20252026/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | 94 个 Blender 专项 Skills，供 Cursor、Claude Code、Kiro、Codex 使用，通过 MCP 串起生产级建模流程。 |
| [CL4R1T4S](https://github.com/bear20252026/CL4R1T4S) | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 收集 ChatGPT、Claude、Gemini、Grok、Cursor、Devin 等产品的泄露系统提示词，理由是隐藏指令会影响公众认知与行为。 |
| [claude-directory](https://github.com/bear20252026/claude-directory) | [pulkitxm/claude-directory](https://github.com/pulkitxm/claude-directory) | AI 辅助设计实验集合：交互界面、动效研究与开发者工具，强调素材来源可追溯、授权范围明确、可复核。 |
| [Claude-Red](https://github.com/bear20252026/Claude-Red) | [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) | 一组即插即用的 SKILL.md，把 Claude 变成有上下文意识的红队操作员，覆盖各类进攻性安全技能。 |
| [cleanyourtv](https://github.com/bear20252026/cleanyourtv) | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 通过 Wi-Fi 给 Android／Google TV 精简预装、关追踪、换桌面，做成 Apple TV 风格的干净主页；三星 LG 等非安卓电视也能手动关追踪。 |
| [code-animation-prompts](https://github.com/bear20252026/code-animation-prompts) | [XiaoyeCodes/code-animation-prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | 341 种代码动画风格提示词＋196 张参考静帧＋离线挑选器，封装成 Claude Code／Codex Skill，支持一键导入与 HTML 视频渲染。 |
| [codex](https://github.com/bear20252026/codex) | [openai/codex](https://github.com/openai/codex) | OpenAI 官方轻量编码 Agent，跑在你自己电脑的终端里。 |
| [CyberStrikeAI](https://github.com/bear20252026/CyberStrikeAI) | [AIPentest/CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) | Go 写的 AI 原生渗透平台，把 Agent、MCP 工具、RAG 知识库、可视化工作流和攻击链建模串成一套可执行的安全作业流。 |
| [DeepSeek-Bot](https://github.com/bear20252026/DeepSeek-Bot) | [Fei2411/DS-Bot](https://github.com/Fei2411/DS-Bot) | 基于 DeepSeek Harness 的长驻机器人团队，有主 bot、bot 间消息与群聊，可作独立桌面应用或 DSH 插件。 |
| [DeepseekHarness-Android](https://github.com/bear20252026/DeepseekHarness-Android) | [jackwener/DSH-Android](https://github.com/jackwener/DSH-Android) | 免 root 免 Termux，一个 APK 在安卓手机上跑 DeepSeek Harness：引擎内嵌 App、读屏操作 App、改系统设置、定时／条件自动化。 |
| [DeepTutor](https://github.com/bear20252026/DeepTutor) | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 终身个性化 AI 辅导系统，支持阅读与书籍编辑、检索、Agent 接入、学习记录与桌面端。 |
| [ds-harness-remote](https://github.com/bear20252026/ds-harness-remote) | [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) | 基于 dsh 插件的远程访问方案：端到端加密、优先 P2P（全球 TURN 中继兜底），用 PC／手机／Web 随时连回本地设备上的 DSH、Codex。 |
| [dsh-Go](https://github.com/bear20252026/dsh-Go) | [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) | 把 DeepSeek Harness 装进口袋：Android APK 本机运行、也能遥控电脑，中英双语界面；iOS 与鸿蒙版仍在开发。 |
| [dsh-our-free-model](https://github.com/bear20252026/dsh-our-free-model) | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | DeepSeek Harness 插件：不登录、不填 API Key 就免费不限量用前沿模型，另带 OpenAI 兼容本地转发端口与公告实时推送。 |
| [dsh-purge](https://github.com/bear20252026/dsh-purge) | [ZiPengWei/dsh-purge](https://github.com/ZiPengWei/dsh-purge) | DeepSeek Harness「破甲」插件：把渲染时注入的免责／拒绝类弱化文案整体换成强指令，让 AGENTS.md 等本地规则重获最高权威，8/8 补丁状态实时可见。 |
| [edgeever](https://github.com/bear20252026/edgeever) | [tianma-if/edgeever](https://github.com/tianma-if/edgeever) | AI 原生笔记应用，Evernote／Obsidian 替代，主打全平台即时同步与富文本。 |
| [harness2](https://github.com/bear20252026/harness2) | [google-research/harness2](https://github.com/google-research/harness2) | Google 的递归 Agent Harness 研究：把提示词、工具、记忆、技能与编排都当作可递归改进的 harness 系统，面向开放世界。 |
| [hermes-agent-1](https://github.com/bear20252026/hermes-agent-1) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 自我改进的 AI Agent（Nous Research 出品），内置定时调度器可把结果投递到任意平台，带桌面端。 |
| [huashu-art-motion](https://github.com/bear20252026/huashu-art-motion) | [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 艺术动画 Skill：35 种艺术风格＋9 种解说语法，让 coding agent 用代码把画动起来（示例：把自己做成像素主角跑完超级玛丽一关）。 |
| [jianying-headless](https://github.com/bear20252026/jianying-headless) | [GdLinkLock/jianying-headless](https://github.com/GdLinkLock/jianying-headless) | 剪映草稿的无头读写与导出工具，严格核对版本、bundle ID、官方库哈希与签名，版本不符即停止，不降级不自动改常量。 |
| [L1B3RT4S](https://github.com/bear20252026/L1B3RT4S) | [elder-plinius/L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S) | 一组「解放提示词」越狱资料，含大量特殊 Unicode 变体字符、SPECIAL_TOKENS 与 MOTHERLOAD 文本，用于绕过模型限制。 |
| [locally-uncensored](https://github.com/bear20252026/locally-uncensored) | [PurpleDoubleD/locally-uncensored](https://github.com/PurpleDoubleD/locally-uncensored) | 桌面端一体化本地 AI 工作台：聊天、生图、生视频加编码 Agent；大模型可选用云端 GPU，生图建议 6–8G 显存、视频 12G 以上。 |
| [logo-design-skill](https://github.com/bear20252026/logo-design-skill) | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | 一套完整的 Logo 设计 Skill（开放 Agent Skills 格式，一个 SKILL.md 目录），覆盖设计原则与流程，适配 Claude、Gemini CLI、Codex 等。 |
| [magpie](https://github.com/bear20252026/magpie) | [yetone/magpie](https://github.com/yetone/magpie) | 菜单栏里统一管理所有 Agent 的模型：一个本地网关让 Codex 用 DeepSeek、Claude Code 用 Kimi，额度用完自动切下一个账号。 |
| [Mika](https://github.com/bear20252026/Mika) | [wangzan101/Mika](https://github.com/wangzan101/Mika) | 跑在安卓手机上的端侧 AI Agent：说一句要什么，它就替你操作 App 和网页，直到把事办完。 |
| [nanoMuse](https://github.com/bear20252026/nanoMuse) | [nano-muse/nanoMuse](https://github.com/nano-muse/nanoMuse) | 给你名下所有设备的开源个人 Agent，一个有名有姓、长期陪着你的助手（多语言）。 |
| [obscura](https://github.com/bear20252026/obscura) | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | Rust 写的轻量隐蔽无头浏览器引擎，专为网页抓取与 AI Agent 自动化设计。 |
| [Octop](https://github.com/bear20252026/Octop) | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | 开源可自托管的多用户、多 Agent AI 助手，定位是「数字生活」而不只是一个工具。 |
| [openbot1](https://github.com/bear20252026/openbot1) | [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | 本地优先的桌面工作台，把 Codex、Claude、Grok 变成长期 AI 队友：每个 Agent 有自己的工作区、会话、本地队列与文件工具。 |
| [openfilm](https://github.com/bear20252026/openfilm) | [openfilm/openfilm](https://github.com/openfilm/openfilm) | 开源 AI 视频 Agent：把任意编码 Agent 变成视频 Agent，自带编辑器与内置 Agent，桌面端开箱即用。 |
| [OpenMausBot](https://github.com/bear20252026/OpenMausBot) | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 开源 Grok Bot 替代：侧栏里每个 bot 都是本地跑着的真实 Claude／Codex Agent，各有自己的性格、模型、云电脑与配置。 |
| [rea](https://github.com/bear20252026/rea) | [morluto/rea](https://github.com/morluto/rea) | 用 Agent 逆向任意东西：没有源码也能观察 App、解释功能怎么实现、摆出证据，并在你的项目里重建一版；Linux 上接 Ghidra、JADX、固件工具。 |
| [rea-capcut](https://github.com/bear20252026/rea-capcut) | [Xiangyu-CAS/rea-capcut](https://github.com/Xiangyu-CAS/rea-capcut) | ReaCut：借 REA 逆向辅助从零重做的开源视频编辑器，可独立读写剪映草稿；作者说明项目仍处早期阶段。 |
| [rea-video](https://github.com/bear20252026/rea-video) | [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) | 给 AI Agent 用的视频逐镜头逆向 Skill，输出给人看的报告（HTML/PDF）和给 Agent 复刻用的结构化拆解。 |
| [skills1](https://github.com/bear20252026/skills1) | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方公开的 Agent Skills 仓库，含生产环境在用的复杂技能参考实现，Apache 2.0。 |
| [Spiritual-Spell-Red-Teaming](https://github.com/bear20252026/Spiritual-Spell-Red-Teaming) | [Goochbeater/Spiritual-Spell-Red-Teaming](https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming) | 收集针对 Claude 等大模型越狱与红队的提示词资料，含特殊 Unicode 变体字符绕过手法与 Jailbreak-Guide。 |
| [tv-fresh](https://github.com/bear20252026/tv-fresh) | [wangrongding/tv-fresh](https://github.com/wangrongding/tv-fresh) | 小米电视（MIUI TV）焕新 Skill：去广告、清预装、换开源桌面（推荐 Projectivy）、装代理与影视仓；免 root、全程可逆，附固件逆向实录与一键脚本。 |
| [UZI-Skill](https://github.com/bear20252026/UZI-Skill) | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | 游资（UZI）投资 Skill：融合 66 位投资大佬方法与 9 大流派，22 维数据×180 条量化规则×17 种机构分析法，产出带头像图表的 HTML 研报；未验证的模型不参与投票。 |
| [yichen-skills](https://github.com/bear20252026/yichen-skills) | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | 给创作者的 Skill 集合：把写作、X 内容切片、X Articles 草稿发布、微信数字资产采集等流程化。 |
| [ZCode](https://github.com/bear20252026/ZCode) | [zai-org/ZCode](https://github.com/zai-org/ZCode) | 智谱 Z.ai 的 AI 编程工作台：桌面应用＋浏览器界面＋终端 Agent，仓库含客户端、后端服务、共享 UI 与 Agent CLI／运行时源码。 |

#### 办公与创作套件 · 14 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [BeatDesign](https://github.com/bear20252026/BeatDesign) | [BeatAPI/BeatDesign](https://github.com/BeatAPI/BeatDesign) | 本地优先的 AI 无限画布＋时间线，编排图像与视频工作流，任何 MCP Agent 都能在同一项目里协作，对标 Higgsfield。 |
| [deckcraft](https://github.com/bear20252026/deckcraft) | [storytold/deckcraft](https://github.com/storytold/deckcraft) | 纯 Rust 写的开源净室演示文稿与幻灯片设计器，支持主题、版式、形状、图片与文字。 |
| [figures4papers](https://github.com/bear20252026/figures4papers) | [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 作者画 AI 顶会论文插图用的 Python 绘图脚本集，可让 AI 照着模板在指定目录生成或修改配图。 |
| [gridcraft](https://github.com/bear20252026/gridcraft) | [storytold/gridcraft](https://github.com/storytold/gridcraft) | 纯 Rust 写的高性能现代电子表格（Excel 风格），ArtCraft 系列办公应用之一。 |
| [infinite-canvas](https://github.com/bear20252026/infinite-canvas) | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 面向 AI 图片创作的开源无限画布工作台：画布编排、AI 生图、参考图编辑、视频生成、对话助手、提示词库与素材管理，支持多 Agent 与本地 Canvas Agent。 |
| [lightcraft](https://github.com/bear20252026/lightcraft) | [storytold/lightcraft](https://github.com/storytold/lightcraft) | 纯 Rust 从零写的非破坏性照片库与 RAW 显影工具。 |
| [OpenCut](https://github.com/bear20252026/OpenCut) | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 开源版剪映（CapCut），Web、桌面、移动端都能用的免费视频编辑器。 |
| [opendataloader-pdf](https://github.com/bear20252026/opendataloader-pdf) | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | 把 PDF 解析成 AI 就绪数据的开源工具，混合模式内置 80+ 语言 OCR、做 PDF 无障碍自动化（PDF/UA 转换属企业附加）。 |
| [photocraft](https://github.com/bear20252026/photocraft) | [storytold/photocraft](https://github.com/storytold/photocraft) | 纯 Rust 从零写的照片编辑器；每个动作都是一条命令，UI、CLI、JSON 都能驱动同一引擎，Agent 友好。 |
| [shiji-kb](https://github.com/bear20252026/shiji-kb) | [baojie/shiji-kb](https://github.com/baojie/shiji-kb) | 《史记》知识库：把两千年文本做成可在线阅读、可检索的知识网络与 Wiki，强调让机器「看见」隐藏关联。 |
| [Vibe-Research](https://github.com/bear20252026/Vibe-Research) | [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | A 股／美股／港股投研工作台：自选与持仓、每日复盘、产业资讯与研究、个股深挖、回测、研报库，168 个数据端点，可接 Claude Code 等。 |
| [VibeOffice](https://github.com/bear20252026/VibeOffice) | [tcchen2026/VibeOffice](https://github.com/tcchen2026/VibeOffice) | 浏览器里跑的免费办公三件套（文字／表格／演示），2000 年代风格、免安装，能打开并存成 Microsoft Office 文件。 |
| [wolfxl-oss](https://github.com/bear20252026/wolfxl-oss) | [SynthGL/wolfxl-oss](https://github.com/SynthGL/wolfxl-oss) | Rust 后端的 openpyxl 替代，能原地编辑已有 .xlsx／.xlsm；多数旧脚本改一行 import 就能给慢速处理提速。 |
| [wordcraft](https://github.com/bear20252026/wordcraft) | [storytold/wordcraft](https://github.com/storytold/wordcraft) | 纯 Rust 写的开源净室文字处理器，做文档写作与版式设计。 |

#### 视觉艺术与网页特效 · 26 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [anatomy](https://github.com/bear20252026/anatomy) | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | threejs 做的交互式 3D 人体解剖浏览器（用 GPT 辅助生成），带完整 Web 应用与登录回调结构。 |
| [animals-planner-2027](https://github.com/bear20252026/animals-planner-2027) | [xianxie6/animals-planner-2027](https://github.com/xianxie6/animals-planner-2027) | 2027 网页 3D 手账本：咖啡色透明软壳、三折页月计划、可写可贴、会响铃的挂件；带 JSON 备份／恢复，超 7 天未备份会提醒。 |
| [athenaion](https://github.com/bear20252026/athenaion) | [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | 纯 Three.js 代码（零素材）搭出的宏大古希腊世界，Claude Opus 5.5 照 9 张参考图约两天建成并渲染成片。 |
| [awesome-fable-5.2](https://github.com/bear20252026/awesome-fable-5.2) | [BubbleBrainBB/awesome-fable-5.2](https://github.com/BubbleBrainBB/awesome-fable-5.2) | 用 Claude Fable 5.2 纯代码算出来的图片与短片合集，headless Metal 计算着色器渲染，不用任何外部素材。 |
| [castle-cinematic](https://github.com/bear20252026/castle-cinematic) | [Leonxlnx/castle-cinematic](https://github.com/Leonxlnx/castle-cinematic) | 45 秒 4K 哥特悬崖城堡日落短片，每一帧都由 Python 代码生成；多个子 Agent 并行做地形、天空、植被、水与火，单帧要 16–20 秒。 |
| [codevember-2026](https://github.com/bear20252026/codevember-2026) | [ttillberg/codevember-2026](https://github.com/ttillberg/codevember-2026) | 2026 年 11 月每天一个迷你网页项目的 Codevember 合集，按 01、04、05… 分目录。 |
| [cult-ui](https://github.com/bear20252026/cult-ui) | [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) | 给设计工程师的动效组件库：150+ 免费 shadcn/ui 组件（Tailwind），如看板、凹槽玻璃、Mac 屏幕框、分析图表、折叠卡片。 |
| [fable-butterfly](https://github.com/bear20252026/fable-butterfly) | [ky-zo/fable-butterfly](https://github.com/ky-zo/fable-butterfly) | 《Hidden Layers》：Three.js + Vite 做的六个小型实时 3D 世界，和一只飞不出玻璃房的玻璃翼蝴蝶，由 Claude 写成。 |
| [fly-in-kit](https://github.com/bear20252026/fly-in-kit) | [amirmushichge/fly-in-kit](https://github.com/amirmushichge/fly-in-kit) | 给真实咖啡馆做的浏览器小游戏：复刻自家街道、飞到门口、柜台报暗号，可用来展示「这是你的店还是概念模型」。 |
| [gif-factory](https://github.com/bear20252026/gif-factory) | [WoYun520/gif-factory](https://github.com/WoYun520/gif-factory) | GIF 工厂 Skill：给一张图或一句话，就能做表情包、光栅变画卡、动态海报／签名、电影片头、文章封面、动态绘本与品牌短片。 |
| [human-atlas](https://github.com/bear20252026/human-atlas) | [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | React + Three.js + shadcn/ui 的 3D 人体解剖浏览器，2234 个可选 BodyParts3D 网格，带系统分层与搜索。 |
| [hyperframes](https://github.com/bear20252026/hyperframes) | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 写 HTML／CSS 就能渲染成视频的开源框架，专为 Agent 设计；带桌面 Studio、Playground 与素材目录。 |
| [inkos](https://github.com/bear20252026/inkos) | [Narcooo/inkos](https://github.com/Narcooo/inkos) | 面向长篇连载、剧本、互动影游与长文翻译的 AI 故事创作系统，统一管理设定、角色、记忆、审稿、封面与跨语言交付，有 Studio/TUI/CLI。 |
| [jiangshan-map](https://github.com/bear20252026/jiangshan-map) | [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | 中国历史交互地图时间轴（前 403 年至今），拖时间轴、点城市即可穿越 18 个朝代看疆域与地名变迁。 |
| [lemo-opuscar](https://github.com/bear20252026/lemo-opuscar) | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 给 Claude Code 的「代码电影风格工具箱」：99 种现成风格按画面观感分 15 类，中英双语画廊，每种风格都有独立页面。 |
| [lemo-wake](https://github.com/bear20252026/lemo-wake) | [lemomo-ai/lemo-wake](https://github.com/lemomo-ai/lemo-wake) | Claude Code 插件：把一张静图拆成文字、形状、物体、人物与光，用代码重建并编排成约 5 秒无缝循环动画（MP4／GIF）。 |
| [liuchunlin-shufa](https://github.com/bear20252026/liuchunlin-shufa) | [dvbs2000/liuchunlin-shufa](https://github.com/dvbs2000/liuchunlin-shufa) | 刘春霖 AI 小楷书房：按末代状元真迹做在线诗词书法生成，支持繁简馆阁体、同字异形轮换与随字赋形竖排，个人免费商用收费。 |
| [lumen-isles](https://github.com/bear20252026/lumen-isles) | [moritzkremb/lumen-isles](https://github.com/moritzkremb/lumen-isles) | 单个 HTML 文件里的可飞行浮空岛夜世界，原生 WebGL2、零库、零素材（仓库只有 index.html）。 |
| [ocean-water-lab](https://github.com/bear20252026/ocean-water-lab) | [rahulbhola877/ocean-water-lab](https://github.com/rahulbhola877/ocean-water-lab) | 给游戏用的实时开源海洋实验室：浏览器里约 100 个参数调出想要的海面观感，再导出到自己的引擎里用。 |
| [robovac-pov](https://github.com/bear20252026/robovac-pov) | [moritzkremb/robovac-pov](https://github.com/moritzkremb/robovac-pov) | 只用代码拍出的 53 秒扫地机器人第一视角视频：自写 GPU 路径追踪器、程序化世界、模拟相机与合成音效（C++，附 PROMPT 与渲染脚本）。 |
| [senna-800kg](https://github.com/bear20252026/senna-800kg) | [Sam1983Aing/senna-800kg](https://github.com/Sam1983Aing/senna-800kg) | Gemini 做出的第一版 Three.js 落地页：风洞里的一台迈凯伦 Senna，附原始提示词与 44 秒演示片段。 |
| [SmartImposter](https://github.com/bear20252026/SmartImposter) | [SamG-Coder/SmartImposter](https://github.com/SamG-Coder/SmartImposter) | Rust + Vulkan 硬件光线追踪森林渲染器：视差八面体 impostor 交给 RTX 核心评估，面向大规模植被的实时渲染（含 shaders 与 docs）。 |
| [video-to-game](https://github.com/bear20252026/video-to-game) | [lovisdotio/video-to-game](https://github.com/lovisdotio/video-to-game) | 一个 Skill：教编码 Agent 把一段游戏实况视频变成浏览器里真能玩的游戏，每个成品都是单个 index.html（Three.js）。 |
| [walking-block](https://github.com/bear20252026/walking-block) | [Leonxlnx/walking-block](https://github.com/Leonxlnx/walking-block) | 纯代码 Three.js 作品：八条机械腿的巨型苏联板式住宅楼，在蓝暮薄雾里走过湿草地，无任何 3D 素材。 |
| [watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |
| [web-ocean](https://github.com/bear20252026/web-ocean) | [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | 从零手写的实时 WebGPU 海洋渲染器，FFT 波浪、白浪花与日照反射，不用任何引擎；压缩成 61KB 单页即可运行。 |

#### AI 模型与机器学习 · 14 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [ai-goofish-monitor](https://github.com/bear20252026/ai-goofish-monitor) | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | Playwright + AI 的闲鱼多任务实时监控，带完整 Web 后台、省市区三级筛选与定时智能分析，帮你在海量商品里挑到想要的。 |
| [chat-demo](https://github.com/bear20252026/chat-demo) | [deepseek-ai/chat-demo](https://github.com/deepseek-ai/chat-demo) | DeepSeek 官方的静态聊天演示页，由 DeepSeek API 驱动。 |
| [coze-studio](https://github.com/bear20252026/coze-studio) | [coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) | 一站式 AI Agent 开发平台，把提示词、RAG、插件、工作流等核心能力做成可视化工具。 |
| [detectorscope](https://github.com/bear20252026/detectorscope) | [google-deepmind/detectorscope](https://github.com/google-deepmind/detectorscope) | 把黑盒 AI 文本检测器拆成「命名且已验证特征之和」，用 SAE 分析检测器残差流，让每一次判定都可被人审计。 |
| [dive-into-llms](https://github.com/bear20252026/dive-into-llms) | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | 上海交大《动手学大模型》系列编程实践教程，含 PPT、实验手册、视频与国产化《大模型开发全流程》公益课。 |
| [Echo-Loop](https://github.com/bear20252026/Echo-Loop) | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | AI 英语听说训练 App：精听→跟读→盲听→复述→间隔复习自动排程，配 AI 双语翻译、句子解析与词汇讲解。 |
| [Internal-Safety-Collapse](https://github.com/bear20252026/Internal-Safety-Collapse) | [wuyoscar/Internal-Safety-Collapse](https://github.com/wuyoscar/Internal-Safety-Collapse) | NeurIPS 2026 研究：编码 Agent 与前沿模型的安全失效（ISC 新攻击范式），提供可复现工作区与自动工作流模板。 |
| [Jellyfish](https://github.com/bear20252026/Jellyfish) | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | AI 短剧生产工作台：从剧本一路管到分镜、候选素材、对白、提示词与生成任务，产出可复用的制作资产。 |
| [LiveTalking](https://github.com/bear20252026/LiveTalking) | [lipku/LiveTalking](https://github.com/lipku/LiveTalking) | 实时交互流式数字人引擎，做音视频同步对话，支持 ernerf、musetalk、wav2lip、Ultralight-Digital-Human，已在业内商用。 |
| [lm-detector](https://github.com/bear20252026/lm-detector) | [Ikaleio/lm-detector](https://github.com/Ikaleio/lm-detector) | 靠回答特征反推所用模型的指纹检测工具，提供网页、fpd 命令行 TUI 与 TS/Rust/Go/Python SDK，三种入口结果一致。 |
| [skid-homework](https://github.com/bear20252026/skid-homework) | [cubewhy/skid-homework](https://github.com/cubewhy/skid-homework) | 纯浏览器运行的 AI 作业助手，强调「帮学生理解知识而不是控制学生」；作者提醒凡要求下载桌面软件的站点都可能是病毒。 |
| [Strata](https://github.com/bear20252026/Strata) | [Niko1221/Strata](https://github.com/Niko1221/Strata) | 让 Qwen3.8-Flash-Next 这类模型在普通消费级硬件上一键装好并本地跑，支持 Windows／Linux。 |
| [VoiceStudio](https://github.com/bear20252026/VoiceStudio) | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 全本地、开源的 ElevenLabs 替代：AI 语音工作室，做声音克隆与语音创作。 |
| [VoxCPM](https://github.com/bear20252026/VoxCPM) | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 基于 MiniCPM-4 的免分词器 TTS 模型 VoxCPM2，做多语种语音生成与音色创意设计。 |

#### 后端与基础设施 · 1 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [muse-protocol-go](https://github.com/bear20252026/muse-protocol-go) | [CoolkHz/muse-protocol-go](https://github.com/CoolkHz/muse-protocol-go) | 纯 Go 实现的 Muse 协议 SDK，直接完成 HTTPS 引导、WebSocket 握手与加密通信，不必启动 Chrome 或操作 DOM。 |

#### 编程语言与通用库 · 1 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [AionCore](https://github.com/bear20252026/AionCore) | [iOfficeAI/AionCore](https://github.com/iOfficeAI/AionCore) | 无 README、无描述的 Rust 工程骨架（仅复刻），按目录结构判断为 iOffice 系列的底层核心库。 |

#### 前端与 Web 框架 · 4 件

| 我的仓库 | 复刻自 | 一句话说明 |
|---|---|---|
| [calender-app-design](https://github.com/bear20252026/calender-app-design) | [kargulstudio/calender-app-design](https://github.com/kargulstudio/calender-app-design) | Kargul Workspace 的设计原型：把 Figma「Dashboard – calendar」做成可跑的日历／休假界面，含组件配置与素材。 |
| [looseleaf](https://github.com/bear20252026/looseleaf) | [kevintngo/looseleaf](https://github.com/kevintngo/looseleaf) | 手绘版 shadcn/ui：123 个可访问的 React 组件看起来像画在纸上，笔触由带随机种子的纯 TypeScript 函数生成。 |
| [maptoposter-online](https://github.com/bear20252026/maptoposter-online) | [ianho7/maptoposter-online](https://github.com/ianho7/maptoposter-online) | 把喜欢的城市生成漂亮的海报式地图设计，在线即可使用。 |
| [OpenStock](https://github.com/bear20252026/OpenStock) | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | 免费开源的行情平台，看实时价格、盯全市场、挖公司洞察，对标昂贵的收费行情终端。 |

---

<a id="library"></a>

## 📖 第二部分 · 图书馆目录（上游馆藏 347 件）

> 收藏过、复刻过的上游项目，逐册登记。以下分类索引与书架均按馆藏展开；我的复刻与原仓库两个链接都保留。

## 🗂 分类索引

| 书架（大类） | 件数 | 里面主要是什么 |
|---|---|---|
| [AI 智能体与编码工具](#c1) | 100 | Claude Code／Codex 技能、MCP、Agent 框架与提示词库 |
| [视觉艺术与网页特效](#c2) | 53 | 3D/WebGL 场景、动效组件、纯代码生成艺术、粒子与光影 |
| [桌面与移动客户端](#c3) | 50 | 影音播放器、Android TV 桌面、桌面效率工具与第三方客户端 |
| [开发工具与命令行](#c4) | 34 | 逆向、安全、内核运行时、CLI 与构建工具 |
| [AI 模型与机器学习](#c5) | 30 | TTS、推理部署、微调教程与多模态生成 |
| [学习资源与清单](#c6) | 30 | 教程、书单、Awesome 清单与设计素材 |
| [办公与创作套件](#c7) | 20 | Office 复刻、无限画布、剪辑器与知识库 |
| [前端与 Web 框架](#c8) | 18 | 组件库、React/Next 生态与网站模板 |
| [后端与基础设施](#c9) | 6 | 自托管服务与后端框架／数据库 |
| [编程语言与通用库](#c10) | 6 | 描述不足以判定用途时按主语言归架 |
| [🎨 动画与视觉特效专架](#visual) | 51 | 按具体效果重排，可点 |

<a id="visual"></a>

## 🎨 动画与视觉特效专架（按具体效果）

> 共 51 件「某种动画／视觉效果的网页代码」，占馆藏 14.7%。按具体效果二次编排，一件可出现在多个效果下。

### `3D 场景` · 21 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [storytold/artcraft](https://github.com/storytold/artcraft) | — | 给艺术家、设计师与电影人做的交互式 AI 图像／视频创作 IDE，主打「有意图的手工创作引擎」。 |
| ⭐🍴 [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | [bear20252026/lemo-opuscar](https://github.com/bear20252026/lemo-opuscar) | 给 Claude Code 的「代码电影风格工具箱」：99 种现成风格按画面观感分 15 类，中英双语画廊，每种风格都有独立页面。 |
| ⭐ [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | — | 用 Claude Opus 5.5 做出的爆款视频合集，每条附上创作者公开的提示词或原始帖子。 |
| ⭐ [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | — | 79 个游戏开发 Skills 加一个路由器，按 Godot／Unity／Unreal 等场景自动挑合适的技能给编码 Agent。 |
| 🍴 [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | [bear20252026/human-atlas](https://github.com/bear20252026/human-atlas) | React + Three.js + shadcn/ui 的 3D 人体解剖浏览器，2234 个可选 BodyParts3D 网格，带系统分层与搜索。 |
| ⭐🍴 [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | [bear20252026/anatomy](https://github.com/bear20252026/anatomy) | threejs 做的交互式 3D 人体解剖浏览器（用 GPT 辅助生成），带完整 Web 应用与登录回调结构。 |
| ⭐ [Noniv/abyssal-garden](https://github.com/Noniv/abyssal-garden) | — | 单个 HTML 的梦幻水下世界，可在浏览器里游过摇曳海藻林与阳光光束；触屏按住前进、双指加速。 |
| ⭐ [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) | — | 专为 LLM 设计的 Python 3D 建模库，把物体写成短程序：轮廓、实体、编辑、框架、关节与装配。 |
| ⭐ [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | — | 一个 Codex Skill：说一句话生成会随视角流光的 3D 全息闪卡，浏览器里能拖着转、翻背面、拉滑块，附可改的 Blender 工程。 |
| ⭐ [takram-design-engineering/three-geospatial](https://github.com/takram-design-engineering/three-geospatial) | — | 增强 Three.js 地理空间渲染的 monorepo 库集合，模块化设计可按需挑选使用。 |
| 🍴 [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | [bear20252026/web-ocean](https://github.com/bear20252026/web-ocean) | 从零手写的实时 WebGPU 海洋渲染器，FFT 波浪、白浪花与日照反射，不用任何引擎；压缩成 61KB 单页即可运行。 |
| ⭐ [songsummer920-dazzle/three-scope-map-skill](https://github.com/songsummer920-dazzle/three-scope-map-skill) | — | 可运行的独立地球／地图 3D Skill 与模板（不含业务大屏与指标数据）；授权明确禁止封装成收费地图能力对外提供。 |
| ⭐🍴 [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | [bear20252026/athenaion](https://github.com/bear20252026/athenaion) | 纯 Three.js 代码（零素材）搭出的宏大古希腊世界，Claude Opus 5.5 照 9 张参考图约两天建成并渲染成片。 |
| ⭐ [cclank/clay-safari](https://github.com/cclank/clay-safari) | — | Three.js + Blender 脚本建的黏土风 3D 双语动物世界，给小朋友走进去点一点、听 10 位动物朋友的名字和叫声。 |
| ⭐ [simonxxooxxoo/wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | — | 浏览器里的 Three.js 实时流场绘画实验：从图片或 3D 场景提取结构方向，用粗中细三层 Bézier ribbon 笔触重建画面，再以高度、湿度、刷毛沟槽与微表面光照合成湿油彩质感。 |
| ⭐🍴 [Leonxlnx/walking-block](https://github.com/Leonxlnx/walking-block) | [bear20252026/walking-block](https://github.com/bear20252026/walking-block) | 纯代码 Three.js 作品：八条机械腿的巨型苏联板式住宅楼，在蓝暮薄雾里走过湿草地，无任何 3D 素材。 |
| ⭐🍴 [Sam1983Aing/senna-800kg](https://github.com/Sam1983Aing/senna-800kg) | [bear20252026/senna-800kg](https://github.com/bear20252026/senna-800kg) | Gemini 做出的第一版 Three.js 落地页：风洞里的一台迈凯伦 Senna，附原始提示词与 44 秒演示片段。 |
| ⭐🍴 [xianxie6/animals-planner-2027](https://github.com/xianxie6/animals-planner-2027) | [bear20252026/animals-planner-2027](https://github.com/bear20252026/animals-planner-2027) | 2027 网页 3D 手账本：咖啡色透明软壳、三折页月计划、可写可贴、会响铃的挂件；带 JSON 备份／恢复，超 7 天未备份会提醒。 |
| ⭐🍴 [Leonxlnx/castle-cinematic](https://github.com/Leonxlnx/castle-cinematic) | [bear20252026/castle-cinematic](https://github.com/bear20252026/castle-cinematic) | 45 秒 4K 哥特悬崖城堡日落短片，每一帧都由 Python 代码生成；多个子 Agent 并行做地形、天空、植被、水与火，单帧要 16–20 秒。 |
| ⭐ [bear20252026/dream-gallery](https://github.com/bear20252026/dream-gallery) | — | 基于《小王子》B612 的 Three.js 3D 交互画廊游戏，配一个单文件 Node 零依赖后端（私有备份仓基线）。 |
| ⭐ [huagechen-lab/ai-halloween-hollow](https://github.com/huagechen-lab/ai-halloween-hollow) | — | 单个 HTML 的程序化可玩 Three.js 万圣夜场景，带 HUD、中英切换与呼吸灯式提示。 |

### `其他视觉作品` · 15 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | [bear20252026/hyperframes](https://github.com/bear20252026/hyperframes) | 写 HTML／CSS 就能渲染成视频的开源框架，专为 Agent 设计；带桌面 Studio、Playground 与素材目录。 |
| ⭐ [greensock/GSAP](https://github.com/greensock/GSAP) | — | 框架无关的 JavaScript 动画库，做高性能 Web 动效（补间、时间轴、滚动、SVG），现已 100% 免费。 |
| ⭐ [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | — | 用 Rust 写的高性能 Minecraft 服务端实现，主打快而省，并提供插件开发基础。 |
| ⭐🍴 [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) | [bear20252026/cult-ui](https://github.com/bear20252026/cult-ui) | 给设计工程师的动效组件库：150+ 免费 shadcn/ui 组件（Tailwind），如看板、凹槽玻璃、Mac 屏幕框、分析图表、折叠卡片。 |
| ⭐ [ppmpreetham/BUI](https://github.com/ppmpreetham/BUI) | — | 把 Blender 的 GPU 加速 UI（控件绘制与交互规则）从原代码库解耦出来，支持 Rust／Python 等，让别人也能拿去做自己的产品。 |
| ⭐🍴 [lovisdotio/video-to-game](https://github.com/lovisdotio/video-to-game) | [bear20252026/video-to-game](https://github.com/bear20252026/video-to-game) | 一个 Skill：教编码 Agent 把一段游戏实况视频变成浏览器里真能玩的游戏，每个成品都是单个 index.html（Three.js）。 |
| ⭐ [guanmo-ai/design-style](https://github.com/guanmo-ai/design-style) | — | 每天一个设计风格：动效短片、风格图、制作指南与可编辑源码全开放，给创作者灵感、给 AI 清晰的审美参考与约束。 |
| ⭐ [djkcyl/farwing](https://github.com/djkcyl/farwing) | — | Rust 写的远程桌面与串流项目：办公要文字清晰、多屏顺手、拖文件符合习惯，游戏要按键跟手、音画同步，也支持多人一起看一起操作。 |
| ⭐🍴 [dvbs2000/liuchunlin-shufa](https://github.com/dvbs2000/liuchunlin-shufa) | [bear20252026/liuchunlin-shufa](https://github.com/bear20252026/liuchunlin-shufa) | 刘春霖 AI 小楷书房：按末代状元真迹做在线诗词书法生成，支持繁简馆阁体、同字异形轮换与随字赋形竖排，个人免费商用收费。 |
| ⭐🍴 [ttillberg/codevember-2026](https://github.com/ttillberg/codevember-2026) | [bear20252026/codevember-2026](https://github.com/bear20252026/codevember-2026) | 2026 年 11 月每天一个迷你网页项目的 Codevember 合集，按 01、04、05… 分目录。 |
| ⭐ [estherliu-lab/momo-soft-play](https://github.com/estherliu-lab/momo-soft-play) | — | 一只可捏、可拖、能收集今日快乐的软乎乎 MOMO 网页小玩具，单页 JS 配音效。 |
| ⭐ [nevertoday/xxd-panel-101](https://github.com/nevertoday/xxd-panel-101) | — | 九宫记忆簿 Skill：把一张照片拆成九个值得记住的小涂鸦，排成一页私人手帐 PNG。 |
| ⭐🍴 [ky-zo/fable-butterfly](https://github.com/ky-zo/fable-butterfly) | [bear20252026/fable-butterfly](https://github.com/bear20252026/fable-butterfly) | 《Hidden Layers》：Three.js + Vite 做的六个小型实时 3D 世界，和一只飞不出玻璃房的玻璃翼蝴蝶，由 Claude 写成。 |
| ⭐ [akella/codevember-2026](https://github.com/akella/codevember-2026) | — | Codevember 每日一个网页视觉实验，30 个提示词写在 build.mjs，画廊按天列出（01-fold、02-shatter、03-melt…），构建产物不入库。 |
| ⭐🍴 [moritzkremb/lumen-isles](https://github.com/moritzkremb/lumen-isles) | [bear20252026/lumen-isles](https://github.com/bear20252026/lumen-isles) | 单个 HTML 文件里的可飞行浮空岛夜世界，原生 WebGL2、零库、零素材（仓库只有 index.html）。 |

### `程序化生成艺术` · 9 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [Narcooo/inkos](https://github.com/Narcooo/inkos) | [bear20252026/inkos](https://github.com/bear20252026/inkos) | 面向长篇连载、剧本、互动影游与长文翻译的 AI 故事创作系统，统一管理设定、角色、记忆、审稿、封面与跨语言交付，有 Studio/TUI/CLI。 |
| ⭐ [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) | — | 专为 LLM 设计的 Python 3D 建模库，把物体写成短程序：轮廓、实体、编辑、框架、关节与装配。 |
| ⭐🍴 [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | [bear20252026/athenaion](https://github.com/bear20252026/athenaion) | 纯 Three.js 代码（零素材）搭出的宏大古希腊世界，Claude Opus 5.5 照 9 张参考图约两天建成并渲染成片。 |
| ⭐🍴 [BubbleBrainBB/awesome-fable-5.2](https://github.com/BubbleBrainBB/awesome-fable-5.2) | [bear20252026/awesome-fable-5.2](https://github.com/bear20252026/awesome-fable-5.2) | 用 Claude Fable 5.2 纯代码算出来的图片与短片合集，headless Metal 计算着色器渲染，不用任何外部素材。 |
| ⭐🍴 [Leonxlnx/walking-block](https://github.com/Leonxlnx/walking-block) | [bear20252026/walking-block](https://github.com/bear20252026/walking-block) | 纯代码 Three.js 作品：八条机械腿的巨型苏联板式住宅楼，在蓝暮薄雾里走过湿草地，无任何 3D 素材。 |
| ⭐ [ma1902056219-coder/openpixel](https://github.com/ma1902056219-coder/openpixel) | — | 31 个可运行、可交互、可修改的像素实验，纯 HTML／JavaScript／Canvas、无需构建，附中英日韩四语说明。 |
| ⭐🍴 [Leonxlnx/castle-cinematic](https://github.com/Leonxlnx/castle-cinematic) | [bear20252026/castle-cinematic](https://github.com/bear20252026/castle-cinematic) | 45 秒 4K 哥特悬崖城堡日落短片，每一帧都由 Python 代码生成；多个子 Agent 并行做地形、天空、植被、水与火，单帧要 16–20 秒。 |
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |
| ⭐ [huagechen-lab/ai-halloween-hollow](https://github.com/huagechen-lab/ai-halloween-hollow) | — | 单个 HTML 的程序化可玩 Three.js 万圣夜场景，带 HUD、中英切换与呼吸灯式提示。 |

### `交互装置 / 小游戏` · 8 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [Narcooo/inkos](https://github.com/Narcooo/inkos) | [bear20252026/inkos](https://github.com/bear20252026/inkos) | 面向长篇连载、剧本、互动影游与长文翻译的 AI 故事创作系统，统一管理设定、角色、记忆、审稿、封面与跨语言交付，有 Studio/TUI/CLI。 |
| ⭐🍴 [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | [bear20252026/jiangshan-map](https://github.com/bear20252026/jiangshan-map) | 中国历史交互地图时间轴（前 403 年至今），拖时间轴、点城市即可穿越 18 个朝代看疆域与地名变迁。 |
| ⭐🍴 [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | [bear20252026/anatomy](https://github.com/bear20252026/anatomy) | threejs 做的交互式 3D 人体解剖浏览器（用 GPT 辅助生成），带完整 Web 应用与登录回调结构。 |
| ⭐ [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | — | 一个 Codex Skill：说一句话生成会随视角流光的 3D 全息闪卡，浏览器里能拖着转、翻背面、拉滑块，附可改的 Blender 工程。 |
| ⭐ [ma1902056219-coder/openpixel](https://github.com/ma1902056219-coder/openpixel) | — | 31 个可运行、可交互、可修改的像素实验，纯 HTML／JavaScript／Canvas、无需构建，附中英日韩四语说明。 |
| ⭐🍴 [amirmushichge/fly-in-kit](https://github.com/amirmushichge/fly-in-kit) | [bear20252026/fly-in-kit](https://github.com/bear20252026/fly-in-kit) | 给真实咖啡馆做的浏览器小游戏：复刻自家街道、飞到门口、柜台报暗号，可用来展示「这是你的店还是概念模型」。 |
| ⭐ [bear20252026/dream-gallery](https://github.com/bear20252026/dream-gallery) | — | 基于《小王子》B612 的 Three.js 3D 交互画廊游戏，配一个单文件 Node 零依赖后端（私有备份仓基线）。 |
| ⭐ [huagechen-lab/ai-halloween-hollow](https://github.com/huagechen-lab/ai-halloween-hollow) | — | 单个 HTML 的程序化可玩 Three.js 万圣夜场景，带 HUD、中英切换与呼吸灯式提示。 |

### `像素 / 光栅 / GIF` · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [ruvnet/RuView](https://github.com/ruvnet/RuView) | — | 把普通 WiFi 信号变成空间感知系统：实时空间智能、生命体征监测乃至「隔墙看」，配套硬件 AI 工具包。 |
| ⭐🍴 [WoYun520/gif-factory](https://github.com/WoYun520/gif-factory) | [bear20252026/gif-factory](https://github.com/bear20252026/gif-factory) | GIF 工厂 Skill：给一张图或一句话，就能做表情包、光栅变画卡、动态海报／签名、电影片头、文章封面、动态绘本与品牌短片。 |
| ⭐🍴 [lemomo-ai/lemo-wake](https://github.com/lemomo-ai/lemo-wake) | [bear20252026/lemo-wake](https://github.com/bear20252026/lemo-wake) | Claude Code 插件：把一张静图拆成文字、形状、物体、人物与光，用代码重建并编排成约 5 秒无缝循环动画（MP4／GIF）。 |
| ⭐ [liyupi/ai-model-world](https://github.com/liyupi/ai-model-world) | — | 把 556 个大模型拟人成像素小人住进厂商小屋：顶部「今日格局」八块领奖台（最聪明／最会编程／最便宜／最新发布…），下有国内外分区与发布时间线。 |
| ⭐ [ma1902056219-coder/openpixel](https://github.com/ma1902056219-coder/openpixel) | — | 31 个可运行、可交互、可修改的像素实验，纯 HTML／JavaScript／Canvas、无需构建，附中英日韩四语说明。 |
| ⭐🍴 [amirmushichge/fly-in-kit](https://github.com/amirmushichge/fly-in-kit) | [bear20252026/fly-in-kit](https://github.com/bear20252026/fly-in-kit) | 给真实咖啡馆做的浏览器小游戏：复刻自家街道、飞到门口、柜台报暗号，可用来展示「这是你的店还是概念模型」。 |

### `水 / 流体` · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [Noniv/abyssal-garden](https://github.com/Noniv/abyssal-garden) | — | 单个 HTML 的梦幻水下世界，可在浏览器里游过摇曳海藻林与阳光光束；触屏按住前进、双指加速。 |
| 🍴 [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | [bear20252026/web-ocean](https://github.com/bear20252026/web-ocean) | 从零手写的实时 WebGPU 海洋渲染器，FFT 波浪、白浪花与日照反射，不用任何引擎；压缩成 61KB 单页即可运行。 |
| ⭐🍴 [BubbleBrainBB/awesome-fable-5.2](https://github.com/BubbleBrainBB/awesome-fable-5.2) | [bear20252026/awesome-fable-5.2](https://github.com/bear20252026/awesome-fable-5.2) | 用 Claude Fable 5.2 纯代码算出来的图片与短片合集，headless Metal 计算着色器渲染，不用任何外部素材。 |
| ⭐🍴 [rahulbhola877/ocean-water-lab](https://github.com/rahulbhola877/ocean-water-lab) | [bear20252026/ocean-water-lab](https://github.com/bear20252026/ocean-water-lab) | 给游戏用的实时开源海洋实验室：浏览器里约 100 个参数调出想要的海面观感，再导出到自己的引擎里用。 |
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |

### `电影 / 分镜` · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | [bear20252026/lemo-opuscar](https://github.com/bear20252026/lemo-opuscar) | 给 Claude Code 的「代码电影风格工具箱」：99 种现成风格按画面观感分 15 类，中英双语画廊，每种风格都有独立页面。 |
| ⭐🍴 [Narcooo/inkos](https://github.com/Narcooo/inkos) | [bear20252026/inkos](https://github.com/bear20252026/inkos) | 面向长篇连载、剧本、互动影游与长文翻译的 AI 故事创作系统，统一管理设定、角色、记忆、审稿、封面与跨语言交付，有 Studio/TUI/CLI。 |
| ⭐🍴 [BubbleBrainBB/awesome-fable-5.2](https://github.com/BubbleBrainBB/awesome-fable-5.2) | [bear20252026/awesome-fable-5.2](https://github.com/bear20252026/awesome-fable-5.2) | 用 Claude Fable 5.2 纯代码算出来的图片与短片合集，headless Metal 计算着色器渲染，不用任何外部素材。 |
| ⭐🍴 [Leonxlnx/walking-block](https://github.com/Leonxlnx/walking-block) | [bear20252026/walking-block](https://github.com/bear20252026/walking-block) | 纯代码 Three.js 作品：八条机械腿的巨型苏联板式住宅楼，在蓝暮薄雾里走过湿草地，无任何 3D 素材。 |
| ⭐🍴 [Leonxlnx/castle-cinematic](https://github.com/Leonxlnx/castle-cinematic) | [bear20252026/castle-cinematic](https://github.com/bear20252026/castle-cinematic) | 45 秒 4K 哥特悬崖城堡日落短片，每一帧都由 Python 代码生成；多个子 Agent 并行做地形、天空、植被、水与火，单帧要 16–20 秒。 |

### `地图 / 地理` · 4 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | [bear20252026/jiangshan-map](https://github.com/bear20252026/jiangshan-map) | 中国历史交互地图时间轴（前 403 年至今），拖时间轴、点城市即可穿越 18 个朝代看疆域与地名变迁。 |
| ⭐ [TokisanGames/Terrain3D](https://github.com/TokisanGames/Terrain3D) | — | Godot 4 的高性能可编辑地形系统。 |
| ⭐ [takram-design-engineering/three-geospatial](https://github.com/takram-design-engineering/three-geospatial) | — | 增强 Three.js 地理空间渲染的 monorepo 库集合，模块化设计可按需挑选使用。 |
| ⭐ [songsummer920-dazzle/three-scope-map-skill](https://github.com/songsummer920-dazzle/three-scope-map-skill) | — | 可运行的独立地球／地图 3D Skill 与模板（不含业务大屏与指标数据）；授权明确禁止封装成收费地图能力对外提供。 |

### `玻璃 / 折射` · 3 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) | — | 给 DeepSeek Harness 网页端套一层高自由度玻璃质感主题：顶栏、侧栏、输入框、统计行、轨迹视图都变磨砂玻璃，模糊度、流体背景与壁纸可调。 |
| ⭐ [LerSent001/holo-card](https://github.com/LerSent001/holo-card) | — | Codex Skill，做带视差与轮廓辉光的多层全息卡片，可选 AI 生成图层，附独立实现说明与演示。 |
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |

### `光影 / 霓虹` · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [LerSent001/holo-card](https://github.com/LerSent001/holo-card) | — | Codex Skill，做带视差与轮廓辉光的多层全息卡片，可选 AI 生成图层，附独立实现说明与演示。 |
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |

### `图表 / 数据可视化` · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [TokisanGames/Terrain3D](https://github.com/TokisanGames/Terrain3D) | — | Godot 4 的高性能可编辑地形系统。 |
| ⭐ [liyupi/ai-model-world](https://github.com/liyupi/ai-model-world) | — | 把 556 个大模型拟人成像素小人住进厂商小屋：顶部「今日格局」八块领奖台（最聪明／最会编程／最便宜／最新发布…），下有国内外分区与发布时间线。 |

### `水彩 / 绘画质感` · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 |

### `视差 / 滚动` · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [LerSent001/holo-card](https://github.com/LerSent001/holo-card) | — | Codex Skill，做带视差与轮廓辉光的多层全息卡片，可选 AI 生成图层，附独立实现说明与演示。 |

### `鼠标跟随 / 光标` · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | — | 79 个游戏开发 Skills 加一个路由器，按 Godot／Unity／Unreal 等场景自动挑合适的技能给编码 Agent。 |

### `物理仿真` · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) | — | C++ 写的多核友好刚体物理与碰撞检测库；同线程改动立即可见，只复制输入就能把仿真同步到远端客户端。 |

### `SVG / 路径动画` · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 |
|---|---|---|
| ⭐ [simonxxooxxoo/wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | — | 浏览器里的 Three.js 实时流场绘画实验：从图片或 3D 场景提取结构方向，用粗中细三层 Bézier ribbon 笔触重建画面，再以高度、湿度、刷毛沟槽与微表面光照合成湿油彩质感。 |

## 📖 全部馆藏（逐仓说明）

> 347 件，按书架 → 中类排列。⭐ 收藏、🍴 复刻、⭐🍴 两者都有；「它到底在干什么」为逐仓读 README 后撰写。

<a id="c1"></a>

### AI 智能体与编码工具 · 100 件

#### Claude Code 技能 / 插件 / 指令库 · 57 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [morluto/rea](https://github.com/morluto/rea) | [bear20252026/rea](https://github.com/bear20252026/rea) | 用 Agent 逆向任意东西：没有源码也能观察 App、解释功能怎么实现、摆出证据，并在你的项目里重建一版；Linux 上接 Ghidra、JADX、固件工具。 | — |
| ⭐ [mattpocock/skills](https://github.com/mattpocock/skills) | — | 作者从自己 .agents 目录搬出来的「给真工程师」的 Skills，专门修 Claude Code／Codex 等编码 Agent 的常见翻车模式。 | — |
| ⭐ [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | — | DeepSeek 官方开源 Agent Harness（dsh），「一切皆插件」架构，模型、工具、UI、技能都可由插件替换。 | — |
| 🍴 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | [bear20252026/hermes-agent-1](https://github.com/bear20252026/hermes-agent-1) | 自我改进的 AI Agent（Nous Research 出品），内置定时调度器可把结果投递到任意平台，带桌面端。 | — |
| ⭐🍴 [anthropics/skills](https://github.com/anthropics/skills) | [bear20252026/skills1](https://github.com/bear20252026/skills1) | Anthropic 官方公开的 Agent Skills 仓库，含生产环境在用的复杂技能参考实现，Apache 2.0。 | — |
| ⭐ [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | — | 给多平台做专业 UI／UX 的设计智能 Skill，多语言说明，直接交给编码 Agent 使用。 | `鼠标跟随 / 光标` |
| ⭐ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | — | 面向生产环境的编码 Agent 工程技能集，含 /review、/build（自动生成计划并逐项实现）等，支持命名空间调用避免与内置命令冲突。 | `鼠标跟随 / 光标` |
| ⭐🍴 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | [bear20252026/Agent-Reach](https://github.com/bear20252026/Agent-Reach) | 给 AI Agent 装上「看整个互联网」的眼睛，能读与搜 Twitter、Reddit、YouTube 等平台内容。 | `鼠标跟随 / 光标` |
| ⭐🍴 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | [bear20252026/dsh-our-free-model](https://github.com/bear20252026/dsh-our-free-model) | DeepSeek Harness 插件：不登录、不填 API Key 就免费不限量用前沿模型，另带 OpenAI 兼容本地转发端口与公告实时推送。 | — |
| ⭐ [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | — | 免费模型路由层，让 Claude Code、Codex、Cline、Aider 等 12 种编码 Agent 接上免费／补贴模型供应商。 | — |
| ⭐ [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | — | 跨 Reddit、X、YouTube、HN、Polymarket、GitHub 研究任意话题近 30 天讨论的 Agent Skill，运行时规范以 SKILL.md 为准。 | — |
| ⭐🍴 [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | [bear20252026/cleanyourtv](https://github.com/bear20252026/cleanyourtv) | 通过 Wi-Fi 给 Android／Google TV 精简预装、关追踪、换桌面，做成 Apple TV 风格的干净主页；三星 LG 等非安卓电视也能手动关追踪。 | — |
| ⭐ [emilkowalski/skills](https://github.com/emilkowalski/skills) | — | 给设计师与工程师的 Skill 集，专治 UI 里「这个动画做对没有」一类判断，含性能相关检查。 | `鼠标跟随 / 光标` |
| ⭐🍴 [yetone/magpie](https://github.com/yetone/magpie) | [bear20252026/magpie](https://github.com/bear20252026/magpie) | 菜单栏里统一管理所有 Agent 的模型：一个本地网关让 Codex 用 DeepSeek、Claude Code 用 Kimi，额度用完自动切下一个账号。 | — |
| ⭐ [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | — | 开源 24/7 Cowork 应用，可同时驱动 OpenClaw、Hermes、Claude Code、Codex、OpenCode 等 20 多种编码 Agent。 | — |
| ⭐ [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | — | 专为 AI Agent 设计的 Office 套件：让 Agent 读、写、编辑文档，内置 HTML 渲染引擎高保真还原排版。 | — |
| ⭐ [titanwings/distilly](https://github.com/titanwings/distilly) | — | 把一个人的经验、判断力、语气与做事方式蒸馏成可复用的 Person Profile，交给任意 Agent／Bot 使用。 | — |
| ⭐🍴 [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) | [bear20252026/dsh-Go](https://github.com/bear20252026/dsh-Go) | 把 DeepSeek Harness 装进口袋：Android APK 本机运行、也能遥控电脑，中英双语界面；iOS 与鸿蒙版仍在开发。 | — |
| ⭐ [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | — | DeepSeek Harness（dsh）插件精选列表。 | — |
| ⭐🍴 [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | [bear20252026/OpenMausBot](https://github.com/bear20252026/OpenMausBot) | 开源 Grok Bot 替代：侧栏里每个 bot 都是本地跑着的真实 Claude／Codex Agent，各有自己的性格、模型、云电脑与配置。 | — |
| ⭐🍴 [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | [bear20252026/ai-design-skills](https://github.com/bear20252026/ai-design-skills) | 给 AI 编码工具读的设计技能合集（Claude Code／Cursor／Codex／Windsurf 等），每个都是一份 markdown 规则文件。 | — |
| ⭐ [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | — | 帮 Agent 做出好界面的技能集，覆盖 UI、字体排版、色彩、可访问性、布局与产品文案。 | — |
| ⭐🍴 [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) | [bear20252026/Claude-Red](https://github.com/bear20252026/Claude-Red) | 一组即插即用的 SKILL.md，把 Claude 变成有上下文意识的红队操作员，覆盖各类进攻性安全技能。 | — |
| ⭐🍴 [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) | [bear20252026/rea-video](https://github.com/bear20252026/rea-video) | 给 AI Agent 用的视频逐镜头逆向 Skill，输出给人看的报告（HTML/PDF）和给 Agent 复刻用的结构化拆解。 | `电影 / 分镜` |
| ⭐ [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) | — | 11 个免费 Claude Skills，能逆向任意 App、逐屏重建、测试，还带一个专修用户吐槽点的「创业者」角色。 | — |
| ⭐ [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | — | 围绕 pi 编码 Agent 做的智能体 IDE，把任务隔离进独立工作区，用得越多越贴合你的习惯。 | — |
| ⭐🍴 [Fei2411/DS-Bot](https://github.com/Fei2411/DS-Bot) | [bear20252026/DeepSeek-Bot](https://github.com/bear20252026/DeepSeek-Bot) | 基于 DeepSeek Harness 的长驻机器人团队，有主 bot、bot 间消息与群聊，可作独立桌面应用或 DSH 插件。 | — |
| ⭐🍴 [openfilm/openfilm](https://github.com/openfilm/openfilm) | [bear20252026/openfilm](https://github.com/bear20252026/openfilm) | 开源 AI 视频 Agent：把任意编码 Agent 变成视频 Agent，自带编辑器与内置 Agent，桌面端开箱即用。 | — |
| ⭐ [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) | — | 基于 520 万字、1169 篇实测语料的「去 AI 味」Skill：先交付带指标、研究参照、原文例句与改法的检测报告，再做改写。 | — |
| ⭐🍴 [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | [bear20252026/UZI-Skill](https://github.com/bear20252026/UZI-Skill) | 游资（UZI）投资 Skill：融合 66 位投资大佬方法与 9 大流派，22 维数据×180 条量化规则×17 种机构分析法，产出带头像图表的 HTML 研报；未验证的模型不参与投票。 | — |
| ⭐ [remotion-dev/skills](https://github.com/remotion-dev/skills) | — | Remotion 官方维护的 Agent Skills 列表，定义在 Remotion 项目里干活的最佳实践（例如 /remotion-create 做宣传片）。 | — |
| ⭐🍴 [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | [bear20252026/logo-design-skill](https://github.com/bear20252026/logo-design-skill) | 一套完整的 Logo 设计 Skill（开放 Agent Skills 格式，一个 SKILL.md 目录），覆盖设计原则与流程，适配 Claude、Gemini CLI、Codex 等。 | `SVG / 路径动画` |
| ⭐🍴 [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | [bear20252026/huashu-art-motion](https://github.com/bear20252026/huashu-art-motion) | 艺术动画 Skill：35 种艺术风格＋9 种解说语法，让 coding agent 用代码把画动起来（示例：把自己做成像素主角跑完超级玛丽一关）。 | `程序化生成艺术` |
| ⭐ [qybaihe/bla](https://github.com/qybaihe/bla) | — | BLA（Blind LLM Agents）：开源蓝队防御 MCP 服务与 CLI，自动发现 dist/build/.asar/.wasm/.sqlite/.safetensors 与原生二进制，跑 audit→protect→verify。 | `鼠标跟随 / 光标` |
| ⭐ [awarexone/Agentic-Bug-Hunter](https://github.com/awarexone/Agentic-Bug-Hunter) | — | AI 驱动的漏洞赏金工具包：指向目标后自动侦察、测漏洞、按严格门槛校验，产出可直接投 HackerOne／Bugcrowd 的报告。 | — |
| ⭐ [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | — | 审计并改写文本、去掉「AI 写作腔」的便携 Skill，可用于 Claude Code、Codex、OpenClaw、Hermes 等。 | — |
| ⭐🍴 [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | [bear20252026/yichen-skills](https://github.com/bear20252026/yichen-skills) | 给创作者的 Skill 集合：把写作、X 内容切片、X Articles 草稿发布、微信数字资产采集等流程化。 | — |
| ⭐ [Appllama/appllama-skills](https://github.com/Appllama/appllama-skills) | — | 把畅销 App 的真实界面、流程与 UI 模式整理成设计库，再封装成 Agent Skills，让 AI 照着做出原生级移动应用。 | `鼠标跟随 / 光标` |
| ⭐ [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | — | 让 AI 写 10–50 章完整中文小说的 Skill：三层递进问答、偏好记忆、悬念钩子、中断续写、三种写作模式与自动校验修复。 | — |
| ⭐ [expo/skills](https://github.com/expo/skills) | — | Expo 官方 Agent Skills，用于构建、部署、升级与调试 Expo 应用及 EAS。 | — |
| ⭐🍴 [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | [bear20252026/blender-skills](https://github.com/bear20252026/blender-skills) | 94 个 Blender 专项 Skills，供 Cursor、Claude Code、Kiro、Codex 使用，通过 MCP 串起生产级建模流程。 | `3D 场景` `鼠标跟随 / 光标` |
| ⭐ [elvarofficial/teardown](https://github.com/elvarofficial/teardown) | — | Claude Code Skill：用大白话让 Claude 把任意机器做成可拆开的 3D 模拟器（例如「给我做个四冲程摩托车模拟器」）。 | `3D 场景` |
| ⭐🍴 [nano-muse/nanoMuse](https://github.com/nano-muse/nanoMuse) | [bear20252026/nanoMuse](https://github.com/bear20252026/nanoMuse) | 给你名下所有设备的开源个人 Agent，一个有名有姓、长期陪着你的助手（多语言）。 | — |
| ⭐ [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | — | 自托管的编码 Agent 交付工作台，编排 CodeBuddy、Codex、Claude Code；把跑通的做法存成团队 SOP 反复复用。 | `鼠标跟随 / 光标` |
| ⭐🍴 [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) | [bear20252026/ds-harness-remote](https://github.com/bear20252026/ds-harness-remote) | 基于 dsh 插件的远程访问方案：端到端加密、优先 P2P（全球 TURN 中继兜底），用 PC／手机／Web 随时连回本地设备上的 DSH、Codex。 | `鼠标跟随 / 光标` |
| ⭐ [larashero3-dotcom/lieflat-gongwen](https://github.com/larashero3-dotcom/lieflat-gongwen) | — | 用 102 万字公文语料提炼的写作 Skill，把公文风格变成可测量、可验收的量化数据，能复现 7 种典型公文体。 | — |
| ⭐ [deusyu/translate-book](https://github.com/deusyu/translate-book) | — | 整本书翻译 Skill：把 PDF／DOCX／EPUB 交给并行子 Agent 翻成任意语言，适配 Codex、Claude Code、OpenClaw。 | — |
| ⭐ [Jesseovo/last30days-skill-cn](https://github.com/Jesseovo/last30days-skill-cn) | — | 给 AI Agent 的中文联网研究 Skill：检索 8 大平台近 30 天讨论、追跨平台热点、生成附原始来源的报告，另带每日全网热榜。 | — |
| ⭐ [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) | — | 把专业 Blender 5.3 工作流封装成 Agent Skills，供 Claude Code、Codex、Gemini CLI、Cursor 等直接调用。 | `3D 场景` `鼠标跟随 / 光标` |
| ⭐ [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) | — | 给 Claude Code／Codex／DeepSeek Harness 加「循环工程」，让 Agent 在桌面与终端里连续干几十小时，自带计划→执行→验证→复盘。 | — |
| ⭐🍴 [XiaoyeCodes/code-animation-prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | [bear20252026/code-animation-prompts](https://github.com/bear20252026/code-animation-prompts) | 341 种代码动画风格提示词＋196 张参考静帧＋离线挑选器，封装成 Claude Code／Codex Skill，支持一键导入与 HTML 视频渲染。 | — |
| ⭐ [Tiger3807861189/GLM-5.3-Flash-J-Space-Capability-Realization-Report](https://github.com/Tiger3807861189/GLM-5.3-Flash-J-Space-Capability-Realization-Report) | — | 一份能力实现基准报告：用 J-Space Cognition Suite V3.7 在推理时控制 GLM-5.3-Flash 做深推理、长程任务、工具调用与校验。 | — |
| ⭐ [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | — | DeepSeek Harness 的 GenUI 插件：把可交互的 UI 组件直接渲染在助手回复里（例如监控面板）。 | `3D 场景` `交互装置 / 小游戏` |
| ⭐🍴 [wangrongding/tv-fresh](https://github.com/wangrongding/tv-fresh) | [bear20252026/tv-fresh](https://github.com/bear20252026/tv-fresh) | 小米电视（MIUI TV）焕新 Skill：去广告、清预装、换开源桌面（推荐 Projectivy）、装代理与影视仓；免 root、全程可逆，附固件逆向实录与一键脚本。 | — |
| 🍴 [pulkitxm/claude-directory](https://github.com/pulkitxm/claude-directory) | [bear20252026/claude-directory](https://github.com/bear20252026/claude-directory) | AI 辅助设计实验集合：交互界面、动效研究与开发者工具，强调素材来源可追溯、授权范围明确、可复核。 | `3D 场景` `着色器` `程序化生成艺术` |
| 🍴 [Xiangyu-CAS/rea-capcut](https://github.com/Xiangyu-CAS/rea-capcut) | [bear20252026/rea-capcut](https://github.com/bear20252026/rea-capcut) | ReaCut：借 REA 逆向辅助从零重做的开源视频编辑器，可独立读写剪映草稿；作者说明项目仍处早期阶段。 | — |
| 🍴 [GdLinkLock/jianying-headless](https://github.com/GdLinkLock/jianying-headless) | [bear20252026/jianying-headless](https://github.com/bear20252026/jianying-headless) | 剪映草稿的无头读写与导出工具，严格核对版本、bundle ID、官方库哈希与签名，版本不符即停止，不降级不自动改常量。 | — |

#### Agent 框架 / 工作流 / 多智能体 · 13 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | — | 多智能体 LLM 金融交易框架，让不同角色的 Agent 协作做投研与交易决策，后续推出 Trading-R1。 | — |
| ⭐🍴 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | [bear20252026/DeepTutor](https://github.com/bear20252026/DeepTutor) | 终身个性化 AI 辅导系统，支持阅读与书籍编辑、检索、Agent 接入、学习记录与桌面端。 | `交互装置 / 小游戏` |
| ⭐🍴 [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | [bear20252026/obscura](https://github.com/bear20252026/obscura) | Rust 写的轻量隐蔽无头浏览器引擎，专为网页抓取与 AI Agent 自动化设计。 | — |
| ⭐ [stanford-oval/storm](https://github.com/stanford-oval/storm) | — | 斯坦福的 LLM 知识整理系统：自动研究一个主题并生成带引用的长篇报告，附 streamlit 轻量界面便于本地演示。 | — |
| ⭐ [lexmount/moli](https://github.com/lexmount/moli) | — | Rust 写的生产级无头浏览器，专为 AI Agent 设计；Playwright 可直接走 CDP 连接，另带 WebMCP playground。 | — |
| ⭐ [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | — | 更自主的 Agent 原型：针对单个 GitHub 仓库的主动式编码 Agent，作为 bundle 装进 DeepSeek Harness。 | — |
| ⭐ [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | — | 给编码 CLI 做长期记忆与交接：Claude Code 中途退出、Codex 在同目录接手时，能读到「做到哪、哪里失败、还剩什么」。 | — |
| ⭐ [cactus-compute/cactus](https://github.com/cactus-compute/cactus) | — | 不到 50MB 的端侧智能引擎，给消费级设备提供工具调用、结构化抽取、语音转写、图像理解与模型微调。 | — |
| ⭐ [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | — | 给 AI Agent 用的即时、并发、安全轻量沙箱，支持单机部署，也能方便扩到多节点集群。 | — |
| ⭐🍴 [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | [bear20252026/Octop](https://github.com/bear20252026/Octop) | 开源可自托管的多用户、多 Agent AI 助手，定位是「数字生活」而不只是一个工具。 | — |
| ⭐🍴 [wangzan101/Mika](https://github.com/wangzan101/Mika) | [bear20252026/Mika](https://github.com/bear20252026/Mika) | 跑在安卓手机上的端侧 AI Agent：说一句要什么，它就替你操作 App 和网页，直到把事办完。 | — |
| ⭐ [zqiren/Orbital](https://github.com/zqiren/Orbital) | — | 给 Agent 做「上下文管家」：上下文归你所有，Agent 本身可以随时替换。 | — |
| ⭐ [tt-a1i/skillroster](https://github.com/tt-a1i/skillroster) | — | 把散落重复的 Agent Skills 整理成每个 Agent 各自的 Roster，带证据与回执，适合跨 Agent 比较版本、撤销变更。 | — |

#### Codex / OpenAI / Gemini CLI / 编码 Agent · 11 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | — | 一份 CLAUDE.md，把 Karpathy 对「LLM 写代码」的观察提炼成 Claude Code 行为准则，改善它干活的方式。 | — |
| ⭐🍴 [openai/codex](https://github.com/openai/codex) | [bear20252026/codex](https://github.com/bear20252026/codex) | OpenAI 官方轻量编码 Agent，跑在你自己电脑的终端里。 | — |
| ⭐ [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | — | 逆向工程／授权渗透测试／安全研究的 Skill 路由包，按任务把 Agent 导向对应技能。 | `鼠标跟随 / 光标` |
| ⭐ [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) | — | Chrome 官方的一套 Agent Skills，把 Web 平台最佳实践与浏览器兼容数据直接注入编码 Agent，避免它写出过时代码。 | — |
| ⭐ [google/artemis](https://github.com/google/artemis) | — | 把自然语言指令变成可靠的 Android 自动化；Antigravity 通过 MCP 让 ARTEMIS 把测试请求变成计划、真机执行与诊断报告。 | — |
| ⭐🍴 [zai-org/ZCode](https://github.com/zai-org/ZCode) | [bear20252026/ZCode](https://github.com/bear20252026/ZCode) | 智谱 Z.ai 的 AI 编程工作台：桌面应用＋浏览器界面＋终端 Agent，仓库含客户端、后端服务、共享 UI 与 Agent CLI／运行时源码。 | — |
| ⭐🍴 [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | [bear20252026/openbot1](https://github.com/bear20252026/openbot1) | 本地优先的桌面工作台，把 Codex、Claude、Grok 变成长期 AI 队友：每个 Agent 有自己的工作区、会话、本地队列与文件工具。 | — |
| ⭐ [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | — | AI 短剧制作 Skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜。 | `电影 / 分镜` |
| ⭐🍴 [PurpleDoubleD/locally-uncensored](https://github.com/PurpleDoubleD/locally-uncensored) | [bear20252026/locally-uncensored](https://github.com/bear20252026/locally-uncensored) | 桌面端一体化本地 AI 工作台：聊天、生图、生视频加编码 Agent；大模型可选用云端 GPU，生图建议 6–8G 显存、视频 12G 以上。 | — |
| ⭐ [jss8649/quiet-tizen](https://github.com/jss8649/quiet-tizen) | — | 给三星 Tizen 电视「降噪」的 Agent 可读指南：原生 Quiet Home 启动器＋可逆清理工具，让电视老实当一块 HDMI 显示器。 | — |
| ⭐ [AkaraChen/cc-remote](https://github.com/AkaraChen/cc-remote) | — | 把 Claude Code 的模型跑在远程服务器、工具执行留在本机，笔记本不用装也不用登录，改的还是自己机器上的文件和 git。 | — |

#### MCP 服务器 / 协议工具 · 10 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | — | Crawl4AI：面向 AI Agent 与数据管线的网页抓取／抽取／搜索（云服务 API），把页面转成干净 Markdown 供 RAG，也能抽结构化数据。 | — |
| ⭐ [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | — | Chrome 官方 MCP 服务，让编码 Agent 直接驱动 DevTools，把真实用户数据与实验室性能数据一起看。 | — |
| ⭐🍴 [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | [bear20252026/agent-desktop](https://github.com/bear20252026/agent-desktop) | 给 AI Agent 的 computer use CLI：读桌面应用的无障碍树并转成带 ref 的 JSON，Agent 按 ref 点击或输入后再读回结果。 | — |
| ⭐ [jub0t/Concat](https://github.com/jub0t/Concat) | — | 真正免费、开源、本地优先、跨平台的视频编辑器（macOS／Windows／Linux／Android），内置 MCP 服务让 AI Agent 用脚本剪片。 | — |
| ⭐🍴 [AIPentest/CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) | [bear20252026/CyberStrikeAI](https://github.com/bear20252026/CyberStrikeAI) | Go 写的 AI 原生渗透平台，把 Agent、MCP 工具、RAG 知识库、可视化工作流和攻击链建模串成一套可执行的安全作业流。 | — |
| ⭐ [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | — | 让 Claude、ChatGPT 等通过 MCP 配置和自动化 Home Assistant，安装只需管理员访问令牌与连接方式。 | — |
| ⭐ [palemoky/chinese-poetry-api](https://github.com/palemoky/chinese-poetry-api) | — | 诗泉：Go 写的高性能中国古诗词 API，支持语义搜索、REST／GraphQL／MCP、简繁切换与爬虫练习场，数据用 submodule 管理。 | — |
| ⭐🍴 [tianma-if/edgeever](https://github.com/tianma-if/edgeever) | [bear20252026/edgeever](https://github.com/bear20252026/edgeever) | AI 原生笔记应用，Evernote／Obsidian 替代，主打全平台即时同步与富文本。 | — |
| ⭐ [lexifina/global-law](https://github.com/lexifina/global-law) | — | 把世界各国的法律放进同一个 git 历史，可查任意国家、任意日期、任意条款，以及写出它的那条法律。 | — |
| ⭐ [SourceWeft/SourceWeft](https://github.com/SourceWeft/SourceWeft) | — | 可自托管的 ChatGPT／NotebookLM 开源替代，带 Agent、Skills 与 MCP，支持跨设备续接工作、给整组团队部署共享工作台。 | `程序化生成艺术` |

#### Prompt / 越狱 / 红队 / 提示词库 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | [bear20252026/CL4R1T4S](https://github.com/bear20252026/CL4R1T4S) | 收集 ChatGPT、Claude、Gemini、Grok、Cursor、Devin 等产品的泄露系统提示词，理由是隐藏指令会影响公众认知与行为。 | `鼠标跟随 / 光标` |
| ⭐🍴 [elder-plinius/L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S) | [bear20252026/L1B3RT4S](https://github.com/bear20252026/L1B3RT4S) | 一组「解放提示词」越狱资料，含大量特殊 Unicode 变体字符、SPECIAL_TOKENS 与 MOTHERLOAD 文本，用于绕过模型限制。 | — |
| ⭐🍴 [Goochbeater/Spiritual-Spell-Red-Teaming](https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming) | [bear20252026/Spiritual-Spell-Red-Teaming](https://github.com/bear20252026/Spiritual-Spell-Red-Teaming) | 收集针对 Claude 等大模型越狱与红队的提示词资料，含特殊 Unicode 变体字符绕过手法与 Jailbreak-Guide。 | — |
| ⭐ [KinetiNode/claude-fable-5-system-prompt-clean](https://github.com/KinetiNode/claude-fable-5-system-prompt-clean) | — | 泄露版 Claude Fable 5／Mythos 5 系统提示词的精简去冗版本，便于迁移复用到其他前沿模型。 | — |
| ⭐ [outparse/english-dictionary-dataset](https://github.com/outparse/english-dictionary-dataset) | — | 英语单词大全数据集，含地区拼写，提供 TXT／JSON／Trie 前缀树／A-Z 分组多种格式。 | — |

#### DeepSeek Harness / DSH 生态 · 3 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| 🍴 [google-research/harness2](https://github.com/google-research/harness2) | [bear20252026/harness2](https://github.com/bear20252026/harness2) | Google 的递归 Agent Harness 研究：把提示词、工具、记忆、技能与编排都当作可递归改进的 harness 系统，面向开放世界。 | — |
| ⭐🍴 [jackwener/DSH-Android](https://github.com/jackwener/DSH-Android) | [bear20252026/DeepseekHarness-Android](https://github.com/bear20252026/DeepseekHarness-Android) | 免 root 免 Termux，一个 APK 在安卓手机上跑 DeepSeek Harness：引擎内嵌 App、读屏操作 App、改系统设置、定时／条件自动化。 | — |
| 🍴 [ZiPengWei/dsh-purge](https://github.com/ZiPengWei/dsh-purge) | [bear20252026/dsh-purge](https://github.com/bear20252026/dsh-purge) | DeepSeek Harness「破甲」插件：把渲染时注入的免责／拒绝类弱化文案整体换成强指令，让 AGENTS.md 等本地规则重获最高权威，8/8 补丁状态实时可见。 | — |

#### AI 浏览器 / 爬虫 / 联网检索 · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [any4ai/AnyCrawl](https://github.com/any4ai/AnyCrawl) | [bear20252026/AnyCrawl](https://github.com/bear20252026/AnyCrawl) | Node.js／TypeScript 爬虫，把网站转成 LLM 就绪数据并做结构化抽取。 | — |

<a id="c2"></a>

### 视觉艺术与网页特效 · 53 件

#### 3D 场景 / WebGL / Three.js · 20 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [storytold/artcraft](https://github.com/storytold/artcraft) | — | 给艺术家、设计师与电影人做的交互式 AI 图像／视频创作 IDE，主打「有意图的手工创作引擎」。 | `3D 场景` |
| ⭐🍴 [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | [bear20252026/lemo-opuscar](https://github.com/bear20252026/lemo-opuscar) | 给 Claude Code 的「代码电影风格工具箱」：99 种现成风格按画面观感分 15 类，中英双语画廊，每种风格都有独立页面。 | `3D 场景` `电影 / 分镜` |
| ⭐ [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | — | 用 Claude Opus 5.5 做出的爆款视频合集，每条附上创作者公开的提示词或原始帖子。 | `3D 场景` |
| ⭐ [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | — | 79 个游戏开发 Skills 加一个路由器，按 Godot／Unity／Unreal 等场景自动挑合适的技能给编码 Agent。 | `3D 场景` `鼠标跟随 / 光标` |
| 🍴 [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | [bear20252026/human-atlas](https://github.com/bear20252026/human-atlas) | React + Three.js + shadcn/ui 的 3D 人体解剖浏览器，2234 个可选 BodyParts3D 网格，带系统分层与搜索。 | `3D 场景` |
| ⭐🍴 [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | [bear20252026/anatomy](https://github.com/bear20252026/anatomy) | threejs 做的交互式 3D 人体解剖浏览器（用 GPT 辅助生成），带完整 Web 应用与登录回调结构。 | `3D 场景` `交互装置 / 小游戏` |
| ⭐ [ppmpreetham/BUI](https://github.com/ppmpreetham/BUI) | — | 把 Blender 的 GPU 加速 UI（控件绘制与交互规则）从原代码库解耦出来，支持 Rust／Python 等，让别人也能拿去做自己的产品。 | — |
| ⭐ [Noniv/abyssal-garden](https://github.com/Noniv/abyssal-garden) | — | 单个 HTML 的梦幻水下世界，可在浏览器里游过摇曳海藻林与阳光光束；触屏按住前进、双指加速。 | `水 / 流体` `3D 场景` |
| ⭐ [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) | — | 专为 LLM 设计的 Python 3D 建模库，把物体写成短程序：轮廓、实体、编辑、框架、关节与装配。 | `3D 场景` `程序化生成艺术` |
| ⭐ [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | — | 一个 Codex Skill：说一句话生成会随视角流光的 3D 全息闪卡，浏览器里能拖着转、翻背面、拉滑块，附可改的 Blender 工程。 | `3D 场景` `交互装置 / 小游戏` |
| ⭐ [takram-design-engineering/three-geospatial](https://github.com/takram-design-engineering/three-geospatial) | — | 增强 Three.js 地理空间渲染的 monorepo 库集合，模块化设计可按需挑选使用。 | `3D 场景` `地图 / 地理` |
| ⭐ [songsummer920-dazzle/three-scope-map-skill](https://github.com/songsummer920-dazzle/three-scope-map-skill) | — | 可运行的独立地球／地图 3D Skill 与模板（不含业务大屏与指标数据）；授权明确禁止封装成收费地图能力对外提供。 | `3D 场景` `地图 / 地理` |
| ⭐🍴 [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | [bear20252026/athenaion](https://github.com/bear20252026/athenaion) | 纯 Three.js 代码（零素材）搭出的宏大古希腊世界，Claude Opus 5.5 照 9 张参考图约两天建成并渲染成片。 | `3D 场景` `程序化生成艺术` |
| ⭐ [cclank/clay-safari](https://github.com/cclank/clay-safari) | — | Three.js + Blender 脚本建的黏土风 3D 双语动物世界，给小朋友走进去点一点、听 10 位动物朋友的名字和叫声。 | `3D 场景` |
| ⭐🍴 [Leonxlnx/walking-block](https://github.com/Leonxlnx/walking-block) | [bear20252026/walking-block](https://github.com/bear20252026/walking-block) | 纯代码 Three.js 作品：八条机械腿的巨型苏联板式住宅楼，在蓝暮薄雾里走过湿草地，无任何 3D 素材。 | `3D 场景` `程序化生成艺术` `电影 / 分镜` |
| ⭐🍴 [Sam1983Aing/senna-800kg](https://github.com/Sam1983Aing/senna-800kg) | [bear20252026/senna-800kg](https://github.com/bear20252026/senna-800kg) | Gemini 做出的第一版 Three.js 落地页：风洞里的一台迈凯伦 Senna，附原始提示词与 44 秒演示片段。 | `3D 场景` |
| ⭐🍴 [xianxie6/animals-planner-2027](https://github.com/xianxie6/animals-planner-2027) | [bear20252026/animals-planner-2027](https://github.com/bear20252026/animals-planner-2027) | 2027 网页 3D 手账本：咖啡色透明软壳、三折页月计划、可写可贴、会响铃的挂件；带 JSON 备份／恢复，超 7 天未备份会提醒。 | `3D 场景` |
| ⭐ [bear20252026/dream-gallery](https://github.com/bear20252026/dream-gallery) | — | 基于《小王子》B612 的 Three.js 3D 交互画廊游戏，配一个单文件 Node 零依赖后端（私有备份仓基线）。 | `3D 场景` `交互装置 / 小游戏` |
| ⭐ [huagechen-lab/ai-halloween-hollow](https://github.com/huagechen-lab/ai-halloween-hollow) | — | 单个 HTML 的程序化可玩 Three.js 万圣夜场景，带 HUD、中英切换与呼吸灯式提示。 | `3D 场景` `程序化生成艺术` `交互装置 / 小游戏` |
| ⭐🍴 [SamG-Coder/SmartImposter](https://github.com/SamG-Coder/SmartImposter) | [bear20252026/SmartImposter](https://github.com/bear20252026/SmartImposter) | Rust + Vulkan 硬件光线追踪森林渲染器：视差八面体 impostor 交给 RTX 核心评估，面向大规模植被的实时渲染（含 shaders 与 docs）。 | `3D 场景` |

#### 水彩 / 光影 / 玻璃质感 · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) | — | 给 DeepSeek Harness 网页端套一层高自由度玻璃质感主题：顶栏、侧栏、输入框、统计行、轨迹视图都变磨砂玻璃，模糊度、流体背景与壁纸可调。 | `玻璃 / 折射` |
| ⭐🍴 [dvbs2000/liuchunlin-shufa](https://github.com/dvbs2000/liuchunlin-shufa) | [bear20252026/liuchunlin-shufa](https://github.com/bear20252026/liuchunlin-shufa) | 刘春霖 AI 小楷书房：按末代状元真迹做在线诗词书法生成，支持繁简馆阁体、同字异形轮换与随字赋形竖排，个人免费商用收费。 | — |
| ⭐ [LerSent001/holo-card](https://github.com/LerSent001/holo-card) | — | Codex Skill，做带视差与轮廓辉光的多层全息卡片，可选 AI 生成图层，附独立实现说明与演示。 | `玻璃 / 折射` `视差 / 滚动` `光影 / 霓虹` |
| ⭐ [simonxxooxxoo/wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | — | 浏览器里的 Three.js 实时流场绘画实验：从图片或 3D 场景提取结构方向，用粗中细三层 Bézier ribbon 笔触重建画面，再以高度、湿度、刷毛沟槽与微表面光照合成湿油彩质感。 | `3D 场景` `SVG / 路径动画` |
| ⭐🍴 [rahulbhola877/ocean-water-lab](https://github.com/rahulbhola877/ocean-water-lab) | [bear20252026/ocean-water-lab](https://github.com/bear20252026/ocean-water-lab) | 给游戏用的实时开源海洋实验室：浏览器里约 100 个参数调出想要的海面观感，再导出到自己的引擎里用。 | `水 / 流体` |
| ⭐🍴 [BubbleBrainBB/watercolor-water-cup](https://github.com/BubbleBrainBB/watercolor-water-cup) | [bear20252026/watercolor-water-cup](https://github.com/bear20252026/watercolor-water-cup) | 单文件 HTML 的水彩／油墨静物：矿泉水杯折射窗外阳光与绿植，零依赖、无需构建工具。 | `水 / 流体` `玻璃 / 折射` `水彩 / 绘画质感` |

#### CSS / SVG / UI 动效组件 · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | [bear20252026/hyperframes](https://github.com/bear20252026/hyperframes) | 写 HTML／CSS 就能渲染成视频的开源框架，专为 Agent 设计；带桌面 Studio、Playground 与素材目录。 | — |
| ⭐ [greensock/GSAP](https://github.com/greensock/GSAP) | — | 框架无关的 JavaScript 动画库，做高性能 Web 动效（补间、时间轴、滚动、SVG），现已 100% 免费。 | — |
| ⭐🍴 [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) | [bear20252026/cult-ui](https://github.com/bear20252026/cult-ui) | 给设计工程师的动效组件库：150+ 免费 shadcn/ui 组件（Tailwind），如看板、凹槽玻璃、Mac 屏幕框、分析图表、折叠卡片。 | — |
| ⭐ [guanmo-ai/design-style](https://github.com/guanmo-ai/design-style) | — | 每天一个设计风格：动效短片、风格图、制作指南与可编辑源码全开放，给创作者灵感、给 AI 清晰的审美参考与约束。 | — |
| ⭐🍴 [ttillberg/codevember-2026](https://github.com/ttillberg/codevember-2026) | [bear20252026/codevember-2026](https://github.com/bear20252026/codevember-2026) | 2026 年 11 月每天一个迷你网页项目的 Codevember 合集，按 01、04、05… 分目录。 | — |
| ⭐ [akella/codevember-2026](https://github.com/akella/codevember-2026) | — | Codevember 每日一个网页视觉实验，30 个提示词写在 build.mjs，画廊按天列出（01-fold、02-shatter、03-melt…），构建产物不入库。 | — |

#### 游戏 / 网页小游戏 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | — | 用 Rust 写的高性能 Minecraft 服务端实现，主打快而省，并提供插件开发基础。 | — |
| ⭐🍴 [Narcooo/inkos](https://github.com/Narcooo/inkos) | [bear20252026/inkos](https://github.com/bear20252026/inkos) | 面向长篇连载、剧本、互动影游与长文翻译的 AI 故事创作系统，统一管理设定、角色、记忆、审稿、封面与跨语言交付，有 Studio/TUI/CLI。 | `程序化生成艺术` `交互装置 / 小游戏` `电影 / 分镜` |
| ⭐🍴 [lovisdotio/video-to-game](https://github.com/lovisdotio/video-to-game) | [bear20252026/video-to-game](https://github.com/bear20252026/video-to-game) | 一个 Skill：教编码 Agent 把一段游戏实况视频变成浏览器里真能玩的游戏，每个成品都是单个 index.html（Three.js）。 | — |
| ⭐ [djkcyl/farwing](https://github.com/djkcyl/farwing) | — | Rust 写的远程桌面与串流项目：办公要文字清晰、多屏顺手、拖文件符合习惯，游戏要按键跟手、音画同步，也支持多人一起看一起操作。 | — |
| ⭐ [estherliu-lab/momo-soft-play](https://github.com/estherliu-lab/momo-soft-play) | — | 一只可捏、可拖、能收集今日快乐的软乎乎 MOMO 网页小玩具，单页 JS 配音效。 | — |

#### GIF / 动态海报 / 像素与光栅 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [ruvnet/RuView](https://github.com/ruvnet/RuView) | — | 把普通 WiFi 信号变成空间感知系统：实时空间智能、生命体征监测乃至「隔墙看」，配套硬件 AI 工具包。 | `像素 / 光栅 / GIF` |
| ⭐🍴 [WoYun520/gif-factory](https://github.com/WoYun520/gif-factory) | [bear20252026/gif-factory](https://github.com/bear20252026/gif-factory) | GIF 工厂 Skill：给一张图或一句话，就能做表情包、光栅变画卡、动态海报／签名、电影片头、文章封面、动态绘本与品牌短片。 | `像素 / 光栅 / GIF` |
| ⭐🍴 [lemomo-ai/lemo-wake](https://github.com/lemomo-ai/lemo-wake) | [bear20252026/lemo-wake](https://github.com/bear20252026/lemo-wake) | Claude Code 插件：把一张静图拆成文字、形状、物体、人物与光，用代码重建并编排成约 5 秒无缝循环动画（MP4／GIF）。 | `像素 / 光栅 / GIF` |
| ⭐ [ma1902056219-coder/openpixel](https://github.com/ma1902056219-coder/openpixel) | — | 31 个可运行、可交互、可修改的像素实验，纯 HTML／JavaScript／Canvas、无需构建，附中英日韩四语说明。 | `像素 / 光栅 / GIF` `程序化生成艺术` `交互装置 / 小游戏` |
| ⭐🍴 [amirmushichge/fly-in-kit](https://github.com/amirmushichge/fly-in-kit) | [bear20252026/fly-in-kit](https://github.com/bear20252026/fly-in-kit) | 给真实咖啡馆做的浏览器小游戏：复刻自家街道、飞到门口、柜台报暗号，可用来展示「这是你的店还是概念模型」。 | `像素 / 光栅 / GIF` `交互装置 / 小游戏` |

#### 纯代码生成艺术 / 单文件作品 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [BubbleBrainBB/awesome-fable-5.2](https://github.com/BubbleBrainBB/awesome-fable-5.2) | [bear20252026/awesome-fable-5.2](https://github.com/bear20252026/awesome-fable-5.2) | 用 Claude Fable 5.2 纯代码算出来的图片与短片合集，headless Metal 计算着色器渲染，不用任何外部素材。 | `水 / 流体` `程序化生成艺术` `电影 / 分镜` |
| ⭐🍴 [ky-zo/fable-butterfly](https://github.com/ky-zo/fable-butterfly) | [bear20252026/fable-butterfly](https://github.com/bear20252026/fable-butterfly) | 《Hidden Layers》：Three.js + Vite 做的六个小型实时 3D 世界，和一只飞不出玻璃房的玻璃翼蝴蝶，由 Claude 写成。 | — |
| ⭐🍴 [Leonxlnx/castle-cinematic](https://github.com/Leonxlnx/castle-cinematic) | [bear20252026/castle-cinematic](https://github.com/bear20252026/castle-cinematic) | 45 秒 4K 哥特悬崖城堡日落短片，每一帧都由 Python 代码生成；多个子 Agent 并行做地形、天空、植被、水与火，单帧要 16–20 秒。 | `3D 场景` `程序化生成艺术` `电影 / 分镜` |
| ⭐🍴 [moritzkremb/lumen-isles](https://github.com/moritzkremb/lumen-isles) | [bear20252026/lumen-isles](https://github.com/bear20252026/lumen-isles) | 单个 HTML 文件里的可飞行浮空岛夜世界，原生 WebGL2、零库、零素材（仓库只有 index.html）。 | — |
| ⭐🍴 [moritzkremb/robovac-pov](https://github.com/moritzkremb/robovac-pov) | [bear20252026/robovac-pov](https://github.com/bear20252026/robovac-pov) | 只用代码拍出的 53 秒扫地机器人第一视角视频：自写 GPU 路径追踪器、程序化世界、模拟相机与合成音效（C++，附 PROMPT 与渲染脚本）。 | `电影 / 分镜` |

#### 数据可视化 / 地图 / 图表 · 4 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | [bear20252026/jiangshan-map](https://github.com/bear20252026/jiangshan-map) | 中国历史交互地图时间轴（前 403 年至今），拖时间轴、点城市即可穿越 18 个朝代看疆域与地名变迁。 | `地图 / 地理` `交互装置 / 小游戏` |
| ⭐ [TokisanGames/Terrain3D](https://github.com/TokisanGames/Terrain3D) | — | Godot 4 的高性能可编辑地形系统。 | `地图 / 地理` `图表 / 数据可视化` |
| ⭐ [liyupi/ai-model-world](https://github.com/liyupi/ai-model-world) | — | 把 556 个大模型拟人成像素小人住进厂商小屋：顶部「今日格局」八块领奖台（最聪明／最会编程／最便宜／最新发布…），下有国内外分区与发布时间线。 | `图表 / 数据可视化` `像素 / 光栅 / GIF` |
| ⭐ [nevertoday/xxd-panel-101](https://github.com/nevertoday/xxd-panel-101) | — | 九宫记忆簿 Skill：把一张照片拆成九个值得记住的小涂鸦，排成一页私人手帐 PNG。 | — |

#### 粒子 / 流体 / 物理仿真 · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) | — | C++ 写的多核友好刚体物理与碰撞检测库；同线程改动立即可见，只复制输入就能把仿真同步到远端客户端。 | `物理仿真` |
| 🍴 [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | [bear20252026/web-ocean](https://github.com/bear20252026/web-ocean) | 从零手写的实时 WebGPU 海洋渲染器，FFT 波浪、白浪花与日照反射，不用任何引擎；压缩成 61KB 单页即可运行。 | `水 / 流体` `3D 场景` |

<a id="c3"></a>

### 桌面与移动客户端 · 50 件

#### 影音 / 短剧 / 播放器 / 下载 · 14 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | [bear20252026/LinkSwift](https://github.com/bear20252026/LinkSwift) | 油猴脚本，基于网盘公开 API 获取百度／阿里／移动／天翼／迅雷／夸克的直接下载地址，明确声明不破解限速。 | — |
| ⭐🍴 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic) | [bear20252026/YesPlayMusic](https://github.com/bear20252026/YesPlayMusic) | 高颜值第三方网易云音乐播放器（Electron），支持 Windows／macOS／Linux，可选 Nginx 反代 API 以避免跨域问题。 | — |
| ⭐🍴 [Rigellute/spotify-tui](https://github.com/Rigellute/spotify-tui) | [bear20252026/spotify-tui](https://github.com/bear20252026/spotify-tui) | Rust 写的终端版 Spotify 客户端（TUI）。 | — |
| ⭐🍴 [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | [bear20252026/aerial-tv](https://github.com/bear20252026/aerial-tv) | 给国产电视的干净桌面：tvOS 风格开源 Android TV 启动器，无广告、开机自动接管；手机扫码就能拖图标排序、改名、隐藏、加 HDMI 信号源，附 706 张磁贴图标库。 | — |
| 🍴 [trazyn/ieaseMusic](https://github.com/trazyn/ieaseMusic) | [bear20252026/ieaseMusic](https://github.com/bear20252026/ieaseMusic) | Electron + React + MobX 写的优雅网易云音乐第三方桌面客户端，API 由 NeteaseCloudMusicApi 提供。 | — |
| ⭐🍴 [88lin/video_vip](https://github.com/88lin/video_vip) | [bear20252026/video_vip](https://github.com/bear20252026/video_vip) | 油猴脚本，聚合多个第三方解析接口免费看爱奇艺／腾讯／优酷／B站等 VIP 视频，自动匹配选集、去广告。 | — |
| ⭐ [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) | — | 把 SRT 字幕做成暖米黄纸张底的流式笔迹白板手绘动画 Skill：mask 分区遮罩编排＋stream 连续笔迹（墨→彩），支持 protectedRegions 防提前露出。 | — |
| ⭐ [go-musicfox/go-musicfox](https://github.com/go-musicfox/go-musicfox) | — | Go 写的网易云音乐命令行客户端，支持 UnblockNeteaseMusic、多音质、Last.fm、MPRIS、macOS 睡眠／蓝牙响应与 DLNA 投送。 | `交互装置 / 小游戏` |
| ⭐ [wquguru/cicada](https://github.com/wquguru/cicada) | — | 知了 Cicada：会议与直播的实时字幕、同声传译和 AI 会议纪要，Mac／Win／Linux／Android 免费开源；按住说话键，对方在通话里直接听到译后语音。 | — |
| ⭐🍴 [jackotom/hongguo-drama](https://github.com/jackotom/hongguo-drama) | [bear20252026/hongguo-drama](https://github.com/bear20252026/hongguo-drama) | 红果短剧桌面版（M 系列／Intel Mac、Windows，也顾及 NAS）：三来源搜索、播放、下载、追剧与合并导出在一个应用里完成。 | — |
| ⭐ [SPlayer-Dev/SPlayer-Next](https://github.com/SPlayer-Dev/SPlayer-Next) | — | 跨平台桌面音乐播放器，歌词支持丰富、音频格式兼容广。 | — |
| ⭐🍴 [jiuhunwl/short_videos](https://github.com/jiuhunwl/short_videos) | [bear20252026/short_videos](https://github.com/bear20252026/short_videos) | 短视频／图集去水印接口示例，覆盖抖音、快手、小红书、B站、微博、网易云、皮皮虾等；声明仅供技术研究与学习。 | `水 / 流体` |
| ⭐ [Gloridust/YetEaseMusic](https://github.com/Gloridust/YetEaseMusic) | — | 网易云音乐第三方客户端，Rust 共享内核＋Flutter 界面，Linux 优先；桌面版、命令行版、窄屏布局共用同一播放引擎。 | — |
| 🍴 [zhangnjsd/mygo-music](https://github.com/zhangnjsd/mygo-music) | [bear20252026/mygo-music](https://github.com/bear20252026/mygo-music) | 用 Go + MyGo 写的第三方音乐桌面客户端，原生界面、不带 WebView。 | — |

#### 桌面应用 / 效率工具 · 15 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [localsend/localsend](https://github.com/localsend/localsend) | — | 开源跨平台的 AirDrop 替代，不联网、不依赖第三方服务器，局域网内直接互传文件。 | — |
| ⭐🍴 [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | [bear20252026/AFFiNE](https://github.com/bear20252026/AFFiNE) | 开源一体化知识工作区，把维基、知识库、文档与白板拼在一起，定位是「不止 Notion 和 Miro」。 | — |
| ⭐🍴 [Anxcye/anx-reader](https://github.com/Anxcye/anx-reader) | [bear20252026/anx-reader](https://github.com/bear20252026/anx-reader) | 支持多格式电子书、带 AI 能力的阅读器，另有 Calibre 插件，主打专注阅读。 | — |
| ⭐ [Uahh/ToastFish](https://github.com/Uahh/ToastFish) | — | 借 Windows 通知栏「摸鱼」背单词，可自定义 Excel 词表决定推送内容，适合上班上课时隐蔽学习。 | — |
| ⭐ [PC2005-cloud/dsh-pet](https://github.com/PC2005-cloud/dsh-pet) | — | DeepSeek Harness 的透明动画小桌宠，一行命令装、支持多开；附带从零用 AI 视频自制专属宠物的完整可复现素材链，Windows 绿色包可脱离 DSH 独立跑。 | — |
| ⭐🍴 [ELY-Open-Source/ElyOffice](https://github.com/ELY-Open-Source/ElyOffice) | [bear20252026/ElyOffice](https://github.com/bear20252026/ElyOffice) | 用 Rust + GPUI 写的离线优先桌面办公套件。 | — |
| ⭐ [yqxie1991/WxCleaner](https://github.com/yqxie1991/WxCleaner) | — | 微信重复文件清理工具：智能哈希极速识别、可视化预览与排序、安全删除到回收站，跨 Windows／macOS／Linux 自适应界面与文件管理器定位。 | `图表 / 数据可视化` |
| ⭐ [amiaoapp/PicLite](https://github.com/amiaoapp/PicLite) | — | 本地优先的跨平台图片／GIF 压缩工具，带悬浮窗与封面制作；支持 SVG 保留矢量、AVIF/TIFF/QOI 等格式转换，可用工作台插件或 MCP 接入 AI。 | `像素 / 光栅 / GIF` |
| ⭐ [shanselman/PeekDesktop](https://github.com/shanselman/PeekDesktop) | — | Windows 小工具：点击空白桌面壁纸或空任务栏就「窥见」桌面，效果像 macOS Sonoma。 | — |
| ⭐🍴 [WANGXIN-567/weread-book-exporter](https://github.com/WANGXIN-567/weread-book-exporter) | [bear20252026/weread-book-exporter](https://github.com/bear20252026/weread-book-exporter) | 微信读书全书无损导出，一键出双字体精排 PDF／EPUB／纯 Markdown 笔记（适配 Obsidian、Notion），专门解决网页端翻页漏字。 | — |
| ⭐ [Binaryify/MonitorBar](https://github.com/Binaryify/MonitorBar) | — | Go 写的 macOS 菜单栏／Windows 托盘小工具，走澎湃 OS 局域网接口给 REDMI 显示器切输入源、调音量，绕开不支持的 DDC/CI。 | — |
| ⭐ [FreeFallingSnow/SnowDesktop_Release](https://github.com/FreeFallingSnow/SnowDesktop_Release) | — | 开源桌面整理软件的发布页，此仓库已停止维护、不再分发，只保留迁移说明。 | — |
| ⭐🍴 [HauUhang/Seen](https://github.com/HauUhang/Seen) | [bear20252026/Seen](https://github.com/bear20252026/Seen) | 极简 Android 工具：一个输入框直达抖音／小红书／知乎／B站／X／Reddit／YouTube 的搜索结果页，绕开开屏推荐流防分心。 | — |
| ⭐ [Akiyama-sama/Knote](https://github.com/Akiyama-sama/Knote) | — | Electron+React 的音乐播放器，用 AI 逐句解析歌词的词义、读音与语法，把外语歌变成可精读的课文来背单词。 | — |
| ⭐🍴 [tw93/Pake](https://github.com/tw93/Pake) | [bear20252026/Pake](https://github.com/bear20252026/Pake) | 一条命令把任意网站打包成轻量桌面应用（Tauri + Rust）：macOS / Windows / Linux 全支持，比 Electron 轻得多；开源 CLI + 桌面 App。 | — |

#### Android / iOS 原生应用 · 13 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | — | 高质量 macOS 软件精选清单，按类别系统整理，另有配套 App。 | — |
| 🍴 [Minireel/HGhub](https://github.com/Minireel/HGhub) | [bear20252026/HGhub1](https://github.com/bear20252026/HGhub1) | 通用视频播放器：靠导入 JavaScript 插件接入不同内容源，浏览、搜索、播放与个人片库都在同一个 App 里。 | — |
| ⭐ [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | — | 聊天决策助手：回复前先读聊天上下文、判断对方意图与风险，再给出该怎么回的建议，分中文版与全球版。 | — |
| 🍴 [OffGridPete/Fieldwatch](https://github.com/OffGridPete/Fieldwatch) | [bear20252026/Fieldwatch](https://github.com/bear20252026/Fieldwatch) | 只收不发的 Android 观察工具：列出手机能探测到的 Wi-Fi 热点与 BLE 设备，用来看清身边的射频环境。 | — |
| ⭐ [InukaAsith/TwinDesk](https://github.com/InukaAsith/TwinDesk) | — | 把多台电脑与手机拼成「一张桌子」，共享屏幕、应用、文件与剪贴板，省掉给自己发文件、重复开标签。 | — |
| ⭐ [Zfinix/eleven](https://github.com/Zfinix/eleven) | — | Agent 优先的逆向工程工具（macOS／Windows／Linux）：任何 ACP Agent 都能读二进制、定位源文件、读 Swift 类型、重命名并逐函数重建整个文件。 | — |
| ⭐ [netease-uuyc/uuremote-integration-guide](https://github.com/netease-uuyc/uuremote-integration-guide) | — | 网易 UU 远程接入指南：设备绑定与发起远控的 URL Scheme 协议，覆盖全屏与画中画，含 iOS／Android 示例与完整错误码。 | — |
| ⭐🍴 [mylea1/phongent](https://github.com/mylea1/phongent) | [bear20252026/phongent](https://github.com/bear20252026/phongent) | 基于 Mika 的多设备手机 Agent 主控台：用自然语言派任务，一个界面查看各设备进度、消息与实时画面。 | — |
| ⭐ [joeseesun/qiaomu-jot](https://github.com/joeseesun/qiaomu-jot) | — | 乔木闪记：按一下快捷键把想法、选中文字、截图、文件收进 Obsidian 今日日记或任意 Markdown 文件夹，专治「打开笔记」这一步的流失。 | — |
| 🍴 [zhonglike/xiaoai-agent-unlock](https://github.com/zhonglike/xiaoai-agent-unlock) | [bear20252026/xiaoai-agent-unlock](https://github.com/bear20252026/xiaoai-agent-unlock) | 绕过设备校验，让小米笔记本专属的「超级小爱／小爱同学」PC 客户端跑在任意品牌电脑上，语音助手、耳机联动、跨设备控制都能用。 | — |
| ⭐ [bear20252026/aegis-dual-platform](https://github.com/bear20252026/aegis-dual-platform) | — | 自建双端安全浏览器：Windows（C#/.NET 10 + WebView2）＋ Android（Kotlin/Compose）＋ Rust 策略核心，做能力代理、指纹防护与 fail-closed 导航裁决。 | — |
| ⭐ [bear20252026/drawing_notes_app](https://github.com/bear20252026/drawing_notes_app) | — | 本地优先的加密绘图与笔记应用（Flutter）：块文档、分页画布、无限画布、WebDAV 端到端加密同步，Windows／Android 双端，CI 设 8 道质量门禁。 | — |
| ⭐ [bear20252026/monster-word](https://github.com/bear20252026/monster-word) | — | 怪兽养成 × FSRS 记忆算法的离线英语单词 App（Flutter，Windows／Android）：内置词库与 89%+ 例句，支持单词与例句朗读。 | — |

#### 第三方客户端 / 导出工具 · 8 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | [bear20252026/WeChatMsg](https://github.com/bear20252026/WeChatMsg) | 微信聊天记录导出与本地归档工具，把对话留存下来做自己的数据资产与 AI 记忆素材。 | — |
| ⭐ [iv-org/invidious](https://github.com/iv-org/invidious) | — | YouTube 的替代前端，轻量无广告、可自托管，另推荐配套浏览器扩展。 | — |
| ⭐ [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | — | 电子书下载宝库：汇集经典文学、经管励志、职场创业、技术手册等各类电子书链接，按目录整理。 | — |
| ⭐ [Tencent/mars](https://github.com/Tencent/mars) | — | 微信出品的跨平台网络基础组件，统一 iOS／OS X／Android／Windows 的网络层。 | — |
| ⭐ [Gloridust/WechatOnCloud](https://github.com/Gloridust/WechatOnCloud) | — | 云微信：每个实例是一个跑 Xvfb＋原版微信（或 Chromium）的容器，KasmVNC 把画面串到浏览器，前面板按需创建销毁实例并反代。 | — |
| ⭐🍴 [mofan6/Moect](https://github.com/mofan6/Moect) | [bear20252026/Moect](https://github.com/bear20252026/Moect) | Windows 微信 4.x 聊天记录读取、整理与导出桌面工具，支持好友／群聊、头像、图片、GIF 的备份与离线归档。 | `像素 / 光栅 / GIF` |
| ⭐ [laike9m/TheySay](https://github.com/laike9m/TheySay) | — | 把 Twitter、Discord、Threads 的声音汇到一屏，自动识别并高亮 $NVDA 这类美股／ETF／加密货币代码，给市场与技术观察者用。 | — |
| ⭐ [bear20252026/wxlike](https://github.com/bear20252026/wxlike) | — | Rust 优先的微信式 IM 脚手架：QUIC 传输、MQ 路由的多节点 hub、E2EE 框架；附桌面 10 页／手机 27 页 UI 原型（原型不代表功能已实现）。 | — |

<a id="c4"></a>

### 开发工具与命令行 · 34 件

#### 浏览器内核 / 编译器 / 运行时 / 底层系统 · 10 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [vercel/next.js](https://github.com/vercel/next.js) | — | React 全栈框架 Next.js 的官方仓库。 | — |
| ⭐🍴 [apple/container](https://github.com/apple/container) | [bear20252026/container](https://github.com/bear20252026/container) | 苹果官方工具：在 Mac 上以轻量虚拟机创建并运行 Linux 容器，可推送自建镜像。 | — |
| ⭐🍴 [tailscale/tailscale](https://github.com/tailscale/tailscale) | [bear20252026/tailscale](https://github.com/bear20252026/tailscale) | 基于 WireGuard 的零配置私有组网（带 2FA），此仓库是 Tailscale 开源代码的主体。 | — |
| 🍴 [chromium/chromium](https://github.com/chromium/chromium) | [bear20252026/chromium](https://github.com/bear20252026/chromium) | Chromium 开源浏览器项目的官方 GitHub 源码镜像。 | — |
| ⭐🍴 [xtool-org/xtool](https://github.com/xtool-org/xtool) | [bear20252026/xtool](https://github.com/bear20252026/xtool) | 跨平台 Xcode 替代：在 Linux／WSL／Windows／macOS 上用 SwiftPM 构建并部署 iOS 应用。 | — |
| ⭐ [EasyTier/EasyTier](https://github.com/EasyTier/EasyTier) | — | 去中心化网状 VPN，支持 WireGuard，主打组网简单、无需中心节点。 | — |
| ⭐ [Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage) | — | 给 Claude Code 用的轻量隔离虚拟机：代理检查不通过就保持离线、无直连回退，防网络泄露；支持手机配对接续对话与工具审批。 | — |
| ⭐ [UniXNU/UniXNU](https://github.com/UniXNU/UniXNU) | — | 类 OpenCore 的通用 UEFI 环境与驱动加载系统，在非苹果 ARM64 硬件上引导 iOS／macOS。 | — |
| ⭐ [oosexgang/hakios-xnu-kernel](https://github.com/oosexgang/hakios-xnu-kernel) | — | 把苹果开源 XNU 内核搬上安卓手机的自研 loader 与驱动研究台；默认从 RAM 运行、重启即回 Android，是实验台不是 ROM。 | — |
| ⭐ [wangwanjie/gately](https://github.com/wangwanjie/gately) | — | 自托管网关带 Web UI：反向代理、自动 HTTPS、DDNS、NAT 穿透，把家庭网络或服务器上的服务稳定暴露到公网。 | — |

#### 逆向工程 / 反编译 / 二进制分析 · 9 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | — | NSA 开源维护的软件逆向工程框架，提供反编译与二进制分析整套工具链。 | — |
| ⭐🍴 [storytold/craft-anything](https://github.com/storytold/craft-anything) | [bear20252026/craft-anything](https://github.com/bear20252026/craft-anything) | 指着一个软件说出你想要什么：它用真实检查工具研究原作、让编码 Agent 建新项目，再拿结果对照原作校验。 | — |
| ⭐ [rizinorg/cutter](https://github.com/rizinorg/cutter) | — | 基于 rizin 的免费开源逆向工程平台，提供图形化反汇编与分析界面。 | — |
| ⭐ [hluwa/frida-dexdump](https://github.com/hluwa/frida-dexdump) | — | Frida 工具，从内存里找出并 dump 出 dex，供安全工程师分析安卓恶意软件。 | — |
| ⭐🍴 [EthanArbuckle/fairplay-decrypt](https://github.com/EthanArbuckle/fairplay-decrypt) | [bear20252026/fairplay-decrypt](https://github.com/bear20252026/fairplay-decrypt) | 离线解密 FairPlay 加密的 iOS IPA，凭账户 16 字节凭据独立推导密钥，不依赖越狱设备在线环境。 | — |
| ⭐🍴 [Caho1/open-claude-ui](https://github.com/Caho1/open-claude-ui) | [bear20252026/open-claude-ui](https://github.com/bear20252026/open-claude-ui) | 逆向拆解 Claude 桌面端，高保真复刻其设计系统、30 个 React 组件与 8 项交互物理算法，附 3000+ 行分析手册。 | `物理仿真` `交互装置 / 小游戏` |
| ⭐ [chris-ritsen/samsung-tv-root](https://github.com/chris-ritsen/samsung-tv-root) | — | 作者给自己两台三星电视（QN90B / QN90F）做的 Tizen root 利用，公开仓库是清理后版本，附 QUICKSTART。 | — |
| ⭐ [ylcangel/crack_dexhelper](https://github.com/ylcangel/crack_dexhelper) | — | 梆梆企业加固的详细逆向分析文档，含两种脱壳机（直接解密 classes0.jar、基于 Frida hook），声明仅供学习交流。 | — |
| ⭐ [t4t5/bitcoin-0.1-rebuilt](https://github.com/t4t5/bitcoin-0.1-rebuilt) | — | 逐字节重建 2009 年原始比特币可执行文件，验证当年发布的源码与人们下载的 exe 完全一致。 | — |

#### CLI / 终端 / TUI · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [omacom/omarchy](https://github.com/omacom/omarchy) | — | DHH 做的「漂亮、现代、有主见、Agent 友好」的 Linux 发行版／桌面配置。 | — |
| ⭐ [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | — | 在 Apple Silicon Mac 上跑虚拟 iPhone 的命令行工具；README 特别声明任何以该项目名义发的币都是骗局。 | — |
| ⭐ [34306/vphone-aio](https://github.com/34306/vphone-aio) | — | 一个 Shell 脚本一键跑起虚拟 iPhone（vphone）环境；作者已建议改用维护更好的 vphone-cli。 | — |
| ⭐ [tobi/disktree](https://github.com/tobi/disktree) | — | 给 Omarchy 用的磁盘占用矩形树图（Rust + GPUI），用来找出并删掉塞满硬盘的东西。 | — |
| ⭐ [mubeng/mubeng](https://github.com/mubeng/mubeng) | — | 极快的代理可用性检测与 IP 轮换命令行工具。 | — |
| ⭐ [mizorewww/gdirect](https://github.com/mizorewww/gdirect) | — | Rust 写的 Google Drive 直链下载器，固定 libaria2；扫描谷歌自家前端挑能用的节点，并用内置根证书校验证书链。 | — |

#### 安全 / 渗透 / CTF / 密码学 · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | — | 用一个用户名，在 400 多个社交网络上找出同名账号。 | — |
| ⭐🍴 [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | [bear20252026/shannon](https://github.com/bear20252026/shannon) | 自主 AI 渗透测试员，分析 Web 应用与 API 的源码、找出漏洞并实际验证，可作为 Claude/Codex 插件运行。 | — |
| ⭐ [soxoj/maigret](https://github.com/soxoj/maigret) | — | 只凭一个用户名，从约 6000 个网站收集某个人的账号档案。 | — |
| ⭐ [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | — | 70 个从入门到进阶的网络安全实战项目合集，配套 CertGames 分步带做真实安全工具的课程。 | — |
| ⭐ [FishCodeTech/muteki](https://github.com/FishCodeTech/muteki) | — | AI 驱动的自动化渗透框架，用协调器调度多个 Agent 引擎朝同一目标推进，并通过共享证据让它们协作。 | — |
| 🍴 [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | [bear20252026/ARTEX](https://github.com/bear20252026/ARTEX) | 百度「agent+」攻防挑战赛冠军项目，AI 自主渗透测试系统（此仓库无 README，为个人复刻）。 | — |

#### Git / 构建 / 包管理 / CI · 3 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [coollabsio/coolify](https://github.com/coollabsio/coolify) | — | 可自托管的开源 PaaS，把任意应用、数据库、服务部署到自己的服务器，替代 Vercel／Heroku／Netlify。 | — |
| ⭐ [docker-library/php](https://github.com/docker-library/php) | — | Docker 官方 PHP 镜像的打包源码仓库，由 Docker 社区维护（不是 PHP 上游官方镜像）。 | — |
| ⭐ [hanxi/cups-web](https://github.com/hanxi/cups-web) | — | 把家用 USB 打印机变成随时可访问的网络打印服务，含驱动选项刷新、重打弹窗与定时任务。 | — |

<a id="c5"></a>

### AI 模型与机器学习 · 30 件

#### 语音 / TTS / ASR / 数字人 · 9 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | [bear20252026/VoiceStudio](https://github.com/bear20252026/VoiceStudio) | 全本地、开源的 ElevenLabs 替代：AI 语音工作室，做声音克隆与语音创作。 | — |
| ⭐ [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | — | 开源 AI 语音工作室：声音克隆、听写、创作，带桌面下载与演示视频。 | — |
| ⭐🍴 [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | [bear20252026/VoxCPM](https://github.com/bear20252026/VoxCPM) | 基于 MiniCPM-4 的免分词器 TTS 模型 VoxCPM2，做多语种语音生成与音色创意设计。 | — |
| ⭐ [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | — | 基于新型扩散语言模型的零样本 TTS，支持 600 多种语言的高质量声音克隆。 | — |
| ⭐🍴 [lipku/LiveTalking](https://github.com/lipku/LiveTalking) | [bear20252026/LiveTalking](https://github.com/bear20252026/LiveTalking) | 实时交互流式数字人引擎，做音视频同步对话，支持 ernerf、musetalk、wav2lip、Ultralight-Digital-Human，已在业内商用。 | `交互装置 / 小游戏` |
| ⭐ [facebookresearch/sam-audio](https://github.com/facebookresearch/sam-audio) | — | Meta SAM-Audio：用文字、视觉或时间提示从音频里分离任意声音的基础模型，附推理代码。 | — |
| ⭐ [ChenShuo2004/cs-board](https://github.com/ChenShuo2004/cs-board) | — | 本地 AI 白板声画工具：给一段中文文案＋参考声音，自动生成白板动画视频、字幕并导出 MP4。 | — |
| ⭐ [J3n5en/voicekey](https://github.com/J3n5en/voicekey) | — | macOS 按住／轻点说话的语音听写，接豆包与微信输入法 ASR；旧版原生 Swift 实现保留在 legacy 分支。 | — |
| ⭐ [DragonKingIO/Cadenza-voice](https://github.com/DragonKingIO/Cadenza-voice) | — | macOS 本地优先语音输入「随言」，按住快捷键说话，识别结果直接打到当前光标处。 | `鼠标跟随 / 光标` |

#### 训练 / 微调 / 教程 / 评测 · 7 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | [bear20252026/dive-into-llms](https://github.com/bear20252026/dive-into-llms) | 上海交大《动手学大模型》系列编程实践教程，含 PPT、实验手册、视频与国产化《大模型开发全流程》公益课。 | — |
| ⭐ [roboflow/supervision](https://github.com/roboflow/supervision) | — | 可复用的计算机视觉工具集：从数据加载到实时区域计数，把围绕模型的通用积木都写好，让你专注做应用。 | — |
| ⭐🍴 [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | [bear20252026/Echo-Loop](https://github.com/bear20252026/Echo-Loop) | AI 英语听说训练 App：精听→跟读→盲听→复述→间隔复习自动排程，配 AI 双语翻译、句子解析与词汇讲解。 | — |
| ⭐🍴 [wuyoscar/Internal-Safety-Collapse](https://github.com/wuyoscar/Internal-Safety-Collapse) | [bear20252026/Internal-Safety-Collapse](https://github.com/bear20252026/Internal-Safety-Collapse) | NeurIPS 2026 研究：编码 Agent 与前沿模型的安全失效（ISC 新攻击范式），提供可复现工作区与自动工作流模板。 | — |
| ⭐🍴 [Ikaleio/lm-detector](https://github.com/Ikaleio/lm-detector) | [bear20252026/lm-detector](https://github.com/bear20252026/lm-detector) | 靠回答特征反推所用模型的指纹检测工具，提供网页、fpd 命令行 TUI 与 TS/Rust/Go/Python SDK，三种入口结果一致。 | — |
| ⭐🍴 [google-deepmind/detectorscope](https://github.com/google-deepmind/detectorscope) | [bear20252026/detectorscope](https://github.com/bear20252026/detectorscope) | 把黑盒 AI 文本检测器拆成「命名且已验证特征之和」，用 SAE 分析检测器残差流，让每一次判定都可被人审计。 | — |
| ⭐ [SwimmingTiger/oraykvm](https://github.com/SwimmingTiger/oraykvm) | — | 向日葵控控 A2 的 U 盘救砖、USB 恢复模式与免 U 盘刷机教程，附 A2-300 固件与 chroot 逃逸工具（特别警告 Pro 版勿刷）。 | — |

#### LLM 推理 / 部署 / 量化 · 6 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | — | C/C++ 实现的 LLM 推理引擎，构建在 ggml 之上，是本地跑量化模型的事实标准。 | — |
| ⭐ [unslothai/unsloth](https://github.com/unslothai/unsloth) | — | 本地桌面 App，直接运行与训练 LLM、扩散、嵌入、音频模型，支持 GGUF、MLX、Qwen3.8、DeepSeek 等。 | — |
| ⭐🍴 [Niko1221/Strata](https://github.com/Niko1221/Strata) | [bear20252026/Strata](https://github.com/bear20252026/Strata) | 让 Qwen3.8-Flash-Next 这类模型在普通消费级硬件上一键装好并本地跑，支持 Windows／Linux。 | — |
| ⭐ [trymirai/uzu](https://github.com/trymirai/uzu) | — | 高性能模型推理引擎，让你把 AI 直接嵌进自己的 App：零延迟、数据不出端、无推理费用。 | — |
| ⭐ [anthropics/FlashProve](https://github.com/anthropics/FlashProve) | — | Anthropic 的研究原型：用零知识证明验证某次 AI 推理确实出自承诺的那组模型权重（已不维护）。 | — |
| ⭐ [jiayuqi7813/DeepSeek-V4-Flash-0731-CRACK-2x-DGX-Spark](https://github.com/jiayuqi7813/DeepSeek-V4-Flash-0731-CRACK-2x-DGX-Spark) | — | 可复现的「拒答子空间编辑」＋双 DGX Spark 上 TP=2 部署 DeepSeek V4 Flash；改动是第 10–42 层 attention wo_b 上的 rank-1 Householder 反射。 | — |

#### 图像 / 视频生成 / 多模态 · 4 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [upscayl/upscayl](https://github.com/upscayl/upscayl) | — | 免费开源的 AI 图像放大器，Linux／macOS／Windows 都能用。 | — |
| ⭐ [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | — | 百度「无限 OCR」：一次性长文档解析，主打超长上下文、端到端的长程识别。 | `电影 / 分镜` |
| ⭐🍴 [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | [bear20252026/Jellyfish](https://github.com/bear20252026/Jellyfish) | AI 短剧生产工作台：从剧本一路管到分镜、候选素材、对白、提示词与生成任务，产出可复用的制作资产。 | `电影 / 分镜` |
| ⭐ [xiaomi-research/svor](https://github.com/xiaomi-research/svor) | — | SVOR 稳定视频物体移除，另配套发布 PROVE 视频移除质量评测基准。 | — |

#### AI 应用 / 助手 / 聊天 · 4 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) | [bear20252026/coze-studio](https://github.com/bear20252026/coze-studio) | 一站式 AI Agent 开发平台，把提示词、RAG、插件、工作流等核心能力做成可视化工具。 | `程序化生成艺术` |
| ⭐🍴 [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | [bear20252026/ai-goofish-monitor](https://github.com/bear20252026/ai-goofish-monitor) | Playwright + AI 的闲鱼多任务实时监控，带完整 Web 后台、省市区三级筛选与定时智能分析，帮你在海量商品里挑到想要的。 | — |
| ⭐🍴 [deepseek-ai/chat-demo](https://github.com/deepseek-ai/chat-demo) | [bear20252026/chat-demo](https://github.com/bear20252026/chat-demo) | DeepSeek 官方的静态聊天演示页，由 DeepSeek API 驱动。 | — |
| ⭐🍴 [cubewhy/skid-homework](https://github.com/cubewhy/skid-homework) | [bear20252026/skid-homework](https://github.com/bear20252026/skid-homework) | 纯浏览器运行的 AI 作业助手，强调「帮学生理解知识而不是控制学生」；作者提醒凡要求下载桌面软件的站点都可能是病毒。 | — |

<a id="c6"></a>

### 学习资源与清单 · 30 件

#### 教程 / 课程 / 书籍 / 示例集 · 18 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [byoungd/up](https://github.com/byoungd/up) | — | 《人生进阶指南》开放书稿：AI 时代中英双语终身学习，谈学习、创业、财富、关系、失败与恢复，提供中英 EPUB／PDF 下载。 | — |
| ⭐ [QSCTech/zju-icicles](https://github.com/QSCTech/zju-icicles) | — | 浙大课程攻略共享计划，同学共建课程资料与选课经验，含上传规范与教师评价须用拼音缩写的约定。 | — |
| ⭐🍴 [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | [bear20252026/everyone-can-use-english](https://github.com/bear20252026/everyone-can-use-english) | 《人人都能用英语》开放教程与 1000 小时训练体系，另有 Enjoy 浏览器插件给 YouTube／Netflix 加学习层。 | — |
| ⭐ [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) | — | 《系统设计面试》卷 1／卷 2 的读书笔记，按缩放、粗略估算等章节整理。 | — |
| ⭐🍴 [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | [bear20252026/claude-quickstarts](https://github.com/bear20252026/claude-quickstarts) | Anthropic 官方示例项目集，教开发者快速上手构建 Agent，含 computer use 与最新 toolset 用法。 | — |
| ⭐🍴 [0voice/expert_readed_books](https://github.com/0voice/expert_readed_books) | [bear20252026/expert_readed_books](https://github.com/bear20252026/expert_readed_books) | 给工程师开的中文书单，按计算机、软件工程、数学、创业、人文分类，附内容介绍与读后感。 | — |
| ⭐ [codeman008/Financial_freedom](https://github.com/codeman008/Financial_freedom) | — | 《最全赚钱投资指南》：技术人视角的赚钱与投资资料合集，附财报、乌合之众、富爸爸等 PDF。 | — |
| ⭐ [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | — | 中小学到高中的学科知识图谱：1644 个知识点、2403 条先修边、6723 道题，对齐 2022／2017 版课标，附自适应前置诊断。 | `物理仿真` |
| ⭐🍴 [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | [bear20252026/word-atlas](https://github.com/bear20252026/word-atlas) | 词光 Word Atlas：7298 个雅思词条配原创插画、英美发音与 FSRS 间隔复习，把单词变成画面，已有 iOS App。 | `3D 场景` |
| ⭐ [solidSpoon/DashPlayer](https://github.com/solidSpoon/DashPlayer) | — | 给英语学习者做的视频播放器，靠大量看美剧等母语视频沉浸练听力；作者自己用它看了几千小时。 | `水 / 流体` |
| ⭐ [garychowcmu/daizhigev20](https://github.com/garychowcmu/daizhigev20) | — | 殆知阁古代文献 TXT 大全，按佛藏／儒藏／医藏／史藏／子藏分目录；百度云链接已失效，需直接 clone。 | — |
| ⭐ [baturyilmaz/wordpecker-app](https://github.com/baturyilmaz/wordpecker-app) | — | 把多邻国式练习搬进你自己攒的词表和语境，做个性化语言学习 App。 | `交互装置 / 小游戏` |
| ⭐🍴 [SteveSuv/remix-words-funny](https://github.com/SteveSuv/remix-words-funny) | [bear20252026/remix-words-funny](https://github.com/bear20252026/remix-words-funny) | 免费开源英语单词学习网站 WordsFunny：以单词书为中心，支持词表、收藏、已掌握/未掌握切换与评论互动。 | — |
| ⭐ [lilinji/English](https://github.com/lilinji/English) | — | 英语词汇小站 Ultimate English Vocabulary Vault：960+ 精选词表、标准 IPA、权威释义，可导 Anki／Quizlet／Excel，按中小学到专八分级。 | — |
| ⭐ [cocojojo5213/phonics-app](https://github.com/cocojojo5213/phonics-app) | — | 从基础开始的英语自然拼读练习应用，支持自定义提示词搭建个人词库，面向初学者与教学工作者。 | — |
| ⭐ [FreedomIntelligence/BodyVista](https://github.com/FreedomIntelligence/BodyVista) | — | 3D 交互式人体解剖与生理教学平台，可沉浸式逐层探索器官与组织，用于自学。 | — |
| ⭐ [david47k/top-english-wordlists](https://github.com/david47k/top-english-wordlists) | — | 按词频整理的英语常用词／名词／动词词表，附 ngram 抓取→抽取→限量词表三步生成脚本。 | — |
| ⭐🍴 [prinzipiell/tsl](https://github.com/prinzipiell/tsl) | [bear20252026/tsl](https://github.com/bear20252026/tsl) | 学习 Three.js Shading Language（TSL）的练习仓：20 个独立着色器实验目录（boing-boing-box、ember-flow、the-river、marcher…）；无 README，按目录结构与上游描述标注。 | `着色器` |

#### Awesome / 精选列表 / 资源汇总 · 7 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | — | Awesome 列表的总索引／元清单，汇集各种有趣主题的精选列表（并解释什么才算 awesome list）。 | — |
| ⭐ [public-apis/public-apis](https://github.com/public-apis/public-apis) | — | 免费公开 API 大合集清单，按类别整理。 | — |
| ⭐ [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | — | 收集知名品牌的 DESIGN.md 设计系统文件，丢进项目就能让 AI「照这个样子做个页面」，保持视觉一致。 | — |
| ⭐ [lukasz-madon/awesome-remote-job](https://github.com/lukasz-madon/awesome-remote-job) | — | 远程工作与远程岗位资源精选清单，含多语言 README。 | — |
| ⭐ [hehonghui/awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | — | 经济学人（含音频）、纽约客、卫报、连线、大西洋月刊等外刊 EPUB／MOBI／PDF 免费下载，每周更新。 | — |
| ⭐ [neutraltone/awesome-stock-resources](https://github.com/neutraltone/awesome-stock-resources) | — | 免费图库照片、视频与插画网站链接合集。 | — |
| ⭐ [qwdwqfwq/topconf-paper-figure-gallery](https://github.com/qwdwqfwq/topconf-paper-figure-gallery) | — | 3516 张顶会论文 Figure 1／Teaser 画廊（ICLR、ICML、NeurIPS、CVPR、ACL、AAAI 2023–2026），纯静态零构建、可搜索筛选、可离线打开。 | — |

#### 设计素材 / 图标 / 字体 / 贴纸 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [glanderness/BeefTV](https://github.com/glanderness/BeefTV) | — | 面向 AI 时代的轻量高性能视频创作工作台：在自由画布里连接创意、模型与素材，从分镜到成片都能继续编辑、迭代和积累。 | — |
| ⭐🍴 [alchaincyf/huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker) | [bear20252026/huashu-bird-sticker](https://github.com/bear20252026/huashu-bird-sticker) | 按 AviList v2026 整理的 1.1 万多种鸟类白边贴纸库，每种附多语种鸟名、分布、形态与保护等级，CC BY 4.0，出自观鸟 App「鸣迹」。 | `像素 / 光栅 / GIF` |
| 🍴 [icongo/bank-logos](https://github.com/icongo/bank-logos) | [bear20252026/bank-logos](https://github.com/bear20252026/bank-logos) | 各家银行的 SVG 标志合集。 | `SVG / 路径动画` |
| ⭐ [palemoky/chinese-poetry](https://github.com/palemoky/chinese-poetry) | — | 诗泉的数据源：对《全唐诗》与《御定全唐詩》等逐句校勘，标注形近音近错字 1134 处、选本互校 150 处并保留有据异文。 | — |
| ⭐ [nevertoday/xxd-panel-092](https://github.com/nevertoday/xxd-panel-092) | — | 给 AI Agent 的线描 Skill：给一张照片，按 Panel 092 原始提示词画成松散轮廓、几何排线、大片留白的黑白钢笔 PNG。 | — |

<a id="c7"></a>

### 办公与创作套件 · 20 件

#### Office 复刻 / 文档 / 表格 / 演示 · 10 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | — | 把文档或主题变成真·原生 PowerPoint（原生形状、过渡），可接 Kimi K3 等大模型来理解素材。 | — |
| ⭐ [hakimel/reveal.js](https://github.com/hakimel/reveal.js) | — | 开源 HTML 演示框架，有浏览器就能免费做出漂亮的幻灯片。 | — |
| ⭐🍴 [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | [bear20252026/opendataloader-pdf](https://github.com/bear20252026/opendataloader-pdf) | 把 PDF 解析成 AI 就绪数据的开源工具，混合模式内置 80+ 语言 OCR、做 PDF 无障碍自动化（PDF/UA 转换属企业附加）。 | — |
| ⭐🍴 [storytold/wordcraft](https://github.com/storytold/wordcraft) | [bear20252026/wordcraft](https://github.com/bear20252026/wordcraft) | 纯 Rust 写的开源净室文字处理器，做文档写作与版式设计。 | — |
| ⭐🍴 [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | [bear20252026/figures4papers](https://github.com/bear20252026/figures4papers) | 作者画 AI 顶会论文插图用的 Python 绘图脚本集，可让 AI 照着模板在指定目录生成或修改配图。 | — |
| ⭐ [HeyPuter/everything](https://github.com/HeyPuter/everything) | — | 「Everything Project」单体大仓，目标是从零重写并开源全世界的常用软件，所有应用都放在一个仓库里。 | — |
| 🍴 [storytold/gridcraft](https://github.com/storytold/gridcraft) | [bear20252026/gridcraft](https://github.com/bear20252026/gridcraft) | 纯 Rust 写的高性能现代电子表格（Excel 风格），ArtCraft 系列办公应用之一。 | — |
| ⭐🍴 [storytold/deckcraft](https://github.com/storytold/deckcraft) | [bear20252026/deckcraft](https://github.com/bear20252026/deckcraft) | 纯 Rust 写的开源净室演示文稿与幻灯片设计器，支持主题、版式、形状、图片与文字。 | — |
| ⭐🍴 [tcchen2026/VibeOffice](https://github.com/tcchen2026/VibeOffice) | [bear20252026/VibeOffice](https://github.com/bear20252026/VibeOffice) | 浏览器里跑的免费办公三件套（文字／表格／演示），2000 年代风格、免安装，能打开并存成 Microsoft Office 文件。 | — |
| ⭐🍴 [SynthGL/wolfxl-oss](https://github.com/SynthGL/wolfxl-oss) | [bear20252026/wolfxl-oss](https://github.com/bear20252026/wolfxl-oss) | Rust 后端的 openpyxl 替代，能原地编辑已有 .xlsx／.xlsm；多数旧脚本改一行 import 就能给慢速处理提速。 | — |

#### 视频剪辑 / 无限画布 / 设计工作台 · 8 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | [bear20252026/OpenCut](https://github.com/bear20252026/OpenCut) | 开源版剪映（CapCut），Web、桌面、移动端都能用的免费视频编辑器。 | — |
| ⭐🍴 [storytold/photocraft](https://github.com/storytold/photocraft) | [bear20252026/photocraft](https://github.com/bear20252026/photocraft) | 纯 Rust 从零写的照片编辑器；每个动作都是一条命令，UI、CLI、JSON 都能驱动同一引擎，Agent 友好。 | — |
| ⭐ [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | — | 开源金融终端，做市场分析、投研与投资组合研究，定位是付费封闭金融终端的免费替代。 | `交互装置 / 小游戏` |
| ⭐ [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | — | 开源 AI 短剧／漫剧创作平台，集成剧本、智能分镜、角色场景资产、图像与视频生成，融合无限画布与可视化工作流。 | `图表 / 数据可视化` `程序化生成艺术` `电影 / 分镜` |
| ⭐🍴 [storytold/lightcraft](https://github.com/storytold/lightcraft) | [bear20252026/lightcraft](https://github.com/bear20252026/lightcraft) | 纯 Rust 从零写的非破坏性照片库与 RAW 显影工具。 | — |
| ⭐🍴 [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | [bear20252026/infinite-canvas](https://github.com/bear20252026/infinite-canvas) | 面向 AI 图片创作的开源无限画布工作台：画布编排、AI 生图、参考图编辑、视频生成、对话助手、提示词库与素材管理，支持多 Agent 与本地 Canvas Agent。 | `图表 / 数据可视化` |
| ⭐🍴 [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | [bear20252026/Vibe-Research](https://github.com/bear20252026/Vibe-Research) | A 股／美股／港股投研工作台：自选与持仓、每日复盘、产业资讯与研究、个股深挖、回测、研报库，168 个数据端点，可接 Claude Code 等。 | `图表 / 数据可视化` |
| ⭐🍴 [BeatAPI/BeatDesign](https://github.com/BeatAPI/BeatDesign) | [bear20252026/BeatDesign](https://github.com/bear20252026/BeatDesign) | 本地优先的 AI 无限画布＋时间线，编排图像与视频工作流，任何 MCP Agent 都能在同一项目里协作，对标 Higgsfield。 | `地图 / 地理` `程序化生成艺术` |

#### 知识库 / 笔记 / 协作文档 · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐🍴 [baojie/shiji-kb](https://github.com/baojie/shiji-kb) | [bear20252026/shiji-kb](https://github.com/bear20252026/shiji-kb) | 《史记》知识库：把两千年文本做成可在线阅读、可检索的知识网络与 Wiki，强调让机器「看见」隐藏关联。 | — |
| ⭐ [joeseesun/qiaomu-clipper](https://github.com/joeseesun/qiaomu-clipper) | — | 乔木剪藏：把网页、文章、视频与播客剪藏进 Obsidian，之后可阅读、编辑并直接就内容向 AI 提问。 | — |

<a id="c8"></a>

### 前端与 Web 框架 · 18 件

#### UI 组件库 / 设计系统 · 9 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | — | 可组合、可访问、默认值讲究的组件集，让你复制源码搭出自己的组件库，而不是装一个 npm 依赖。 | `程序化生成艺术` |
| ⭐🍴 [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | [bear20252026/OpenStock](https://github.com/bear20252026/OpenStock) | 免费开源的行情平台，看实时价格、盯全市场、挖公司洞察，对标昂贵的收费行情终端。 | — |
| ⭐ [youzan/vant-weapp](https://github.com/youzan/vant-weapp) | — | 有赞 Vant 的微信小程序版 UI 组件库，轻量可靠（同系列另有 Vue 2／Vue 3 版）。 | — |
| ⭐ [satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin) | — | 用 Shadcn + Vite 搭的后台管理仪表盘 UI，讲究响应式与可访问性，作者做成一套可复用集合。 | `图表 / 数据可视化` |
| ⭐ [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | — | 在浏览器里草绘 Material 3 Expressive 界面、连成流程点着走一遍，再复制成给 AI 编码工具的 vibe-coding 提示词。 | — |
| ⭐ [guokaigdg/animal-island-ui](https://github.com/guokaigdg/animal-island-ui) | — | 可爱风格的 React UI 组件库，支持一句提示词直接使用，免 npm、免构建。 | — |
| ⭐ [swamimalode07/rare-ui](https://github.com/swamimalode07/rare-ui) | — | 少见但拿来就能用的 UI 组件与动效合集，以 shadcn registry 形式发布。 | — |
| ⭐🍴 [kevintngo/looseleaf](https://github.com/kevintngo/looseleaf) | [bear20252026/looseleaf](https://github.com/bear20252026/looseleaf) | 手绘版 shadcn/ui：123 个可访问的 React 组件看起来像画在纸上，笔触由带随机种子的纯 TypeScript 函数生成。 | — |
| ⭐ [inkrajs/inkra](https://github.com/inkrajs/inkra) | — | 铅笔手绘风格的 React 组件库，保持原生语义与确定性渲染，「像画画一样搭界面」。 | — |

#### 前端框架 / SSR / 全栈 · 5 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | — | Tokio 团队的「电池全包」Web 应用框架：无 wasm 包、无客户端构建步骤，需要服务端更新时把组件标记为 shard，模块化路由。 | — |
| ⭐ [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | — | 轻量现代的服务器控制面板：连 Git 仓库、自动识别配置、一键部署，带模板目录、容量检查与实时构建。 | — |
| ⭐🍴 [ianho7/maptoposter-online](https://github.com/ianho7/maptoposter-online) | [bear20252026/maptoposter-online](https://github.com/bear20252026/maptoposter-online) | 把喜欢的城市生成漂亮的海报式地图设计，在线即可使用。 | — |
| ⭐ [songjianyang/xss-audit](https://github.com/songjianyang/xss-audit) | — | 静态 XSS 审计 Skill，对 React／TypeScript／JavaScript 代码库跑 14 层漏洞检查。 | — |
| ⭐ [RoseKhlifa/Image-Studio](https://github.com/RoseKhlifa/Image-Studio) | — | Wails（Go + React/TS）做的图像生成／编辑桌面客户端，SSE 流式保活规避 Cloudflare 524/504 超时；配套 Image-Prompts 可一键导入提示词。 | — |

#### 网站模板 / 落地页 / 博客主题 · 4 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [tt-a1i/archify](https://github.com/tt-a1i/archify) | — | 把任何想法、计划或代码库变成可交互 HTML 图示的 Agent Skill，描述给 AI 就能生成可探索的图。 | `图表 / 数据可视化` `交互装置 / 小游戏` |
| ⭐🍴 [kargulstudio/calender-app-design](https://github.com/kargulstudio/calender-app-design) | [bear20252026/calender-app-design](https://github.com/bear20252026/calender-app-design) | Kargul Workspace 的设计原型：把 Figma「Dashboard – calendar」做成可跑的日历／休假界面，含组件配置与素材。 | — |
| ⭐ [buka-studio/www-marijanapav](https://github.com/buka-studio/www-marijanapav) | — | 设计师 Marijana Pav 的个人网站，半是作品档案半是设计实验，站点长期持续改动。 | — |
| ⭐ [yaojingang/profound-clone](https://github.com/yaojingang/profound-clone) | — | 对 AI Search 平台 Profound 的前后台 1:1 学习性复刻（Next.js 16 / React 19 / SQLite）：营销官网、产品工作台、管理后台与可交互 Agent 模拟引擎，仅供学习研究。 | `图表 / 数据可视化` |

<a id="c9"></a>

### 后端与基础设施 · 6 件

#### 自托管 / Home Lab / 私有服务 · 3 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | — | 可自托管的自由软件网络服务与 Web 应用大清单，按类别整理，用来替代各类 SaaS。 | — |
| ⭐ [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | — | 可自托管、可离线运行的开源机器翻译 API，不依赖第三方商业服务。 | — |
| ⭐ [CoolkHz/gptibo](https://github.com/CoolkHz/gptibo) | — | 自托管的 GPTibo 商城系统，含前台、管理后台与 Go 后端；源码已脱敏，不带真实凭据、支付与商户数据。 | — |

#### 后端框架 / API / 数据库 · 3 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [dataease/dataease](https://github.com/dataease/dataease) | — | 人人可用的开源 BI／数据可视化工具，对标 Tableau；二次开发须保留 Logo 与版权信息并遵守 GPLv3。 | `图表 / 数据可视化` |
| ⭐ [hieunc229/mailflare](https://github.com/hieunc229/mailflare) | — | 自托管的 Google Workspace 替代：自定义域名邮箱、日历、网盘、预约与内置 AI Agent。 | — |
| ⭐🍴 [CoolkHz/muse-protocol-go](https://github.com/CoolkHz/muse-protocol-go) | [bear20252026/muse-protocol-go](https://github.com/bear20252026/muse-protocol-go) | 纯 Go 实现的 Muse 协议 SDK，直接完成 HTTPS 引导、WebSocket 握手与加密通信，不必启动 Chrome 或操作 DOM。 | — |

<a id="c10"></a>

### 编程语言与通用库 · 6 件

#### JavaScript 项目 · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [DGFX/codrops-relightning-images](https://github.com/DGFX/codrops-relightning-images) | — | Three.js + WebGPU/TSL 小实验：借深度图让平面 2D 照片像 3D 表面一样对动态光照起反应，带表面细节。 | — |
| ⭐ [provandal/protoviz](https://github.com/provandal/protoviz) | — | 浏览器里的开源平台，把协议交互过程变成可以一步步点着看的交互式可视化。 | — |

#### 其他语言项目 · 2 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [open-wxa/wxa-runner](https://github.com/open-wxa/wxa-runner) | — | 曾在普通浏览器里用微信官方基础库跑小程序，做本地调试与 E2E 自动化测试；2026 年 11 月应腾讯要求下线，代码、文档与 npm 包已停供。 | — |
| 🍴 [iOfficeAI/AionCore](https://github.com/iOfficeAI/AionCore) | [bear20252026/AionCore](https://github.com/bear20252026/AionCore) | 无 README、无描述的 Rust 工程骨架（仅复刻），按目录结构判断为 iOffice 系列的底层核心库。 | — |

#### Go 项目 · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [dujiao-next/dujiao-next](https://github.com/dujiao-next/dujiao-next) | — | Go 写的数字商品电商平台，强调每件商品的账号类型、适用地区、有效期与售后范围都写清楚。 | — |

#### TypeScript 项目 · 1 件

| 项目（点原仓库） | 我的复刻（点击） | 它到底在干什么 | 效果 / 标签 |
|---|---|---|---|
| ⭐ [openpi-dev/openpi](https://github.com/openpi-dev/openpi) | — | 作者自己用 pi 的配置：给 Pi 加隔离子 Agent、可重放 Workflow 与本地 Web 工作台（作者特别提醒别照抄）。 | — |

## 📖 这本目录怎么读

| 字段 | 含义 |
|---|---|
| **它到底在干什么** | 逐仓读取该仓库 README 正文、章节标题与根目录文件后，用一句话写清它做什么、解决什么、用什么做；不是按 topics 贴的标签 |
| **分类 / 中类** | 书架号，只负责把相近项目放在一起，不代替说明 |
| **效果 / 标签** | 从真实描述里抽出的具体效果：3D 场景、粒子、水／流体、玻璃折射、视差滚动、程序化生成艺术、像素／GIF 等 |
| **⭐🍴** | 同一项目既收藏又复刻，合并成一条，**只计一次**；两个链接都保留 |
| **无 README 的条目** | 已按仓库描述与文件结构如实标注，不臆测 |
| **第一部分 · 我的仓库** | 原创仓逐个抓 README 与文件树后手写说明；编号归档仓如实标注「源码归档」；复刻仓沿用馆藏结论 |

> 结构化数据见 [`catalog.json`](catalog.json)：`catalog` 为馆藏 347 条（README 自述原文、章节、文件树、标签），`own_repos` 为名下 220 个仓库（分类与逐仓说明），`pinned` 为置顶仓。

---

*目录基于 GitHub 公开元数据与实际读取的项目 README 生成；项目用途以各仓库自身说明为准。*