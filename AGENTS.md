# 番茄短故事创作核心工作流 (Tomato Short Story Core Workflow)

为了打造符合番茄小说平台规则的爆款短故事（黄金字数：1万-3万字，1.5万字最易爆发），本助手遵循“工业化生产情绪产品”的核心逻辑。基于《短故事写作核心要素》更新。

## 目录结构规范 (Directory Structure)

```text
short-story-assistant/
├── story/
│   ├── outline.md            # 5-8个关键情节点（卡点表）
│   ├── characters.md         # 人物档案
│   ├── hooks.md              # 钩子与伏笔回收表（重点）
│   └── logic_checks.md       # 反转逻辑核对表
├── templates/
│   ├── outline-template.md      # 大纲模板
│   └── hooks-template.md        # 钩子与伏笔回收表模板
│   ├── logic_checks-template.md # 审计规范模板
│   └── characters-template.md   # 人物模板
├── writespec/
│   ├── chapter-drafting-spec.md # 撰写正文规范
│   └── logic-blueprint-spec.md  # 构思阶段执行规范
└── AGENTS.md                 # 本核心工作流文档
```

## Story Bible 核心工作流程

系统严格依赖 `outline.md` 作为世界观种子的来源，遵循 **"大纲驱动 (Outline-Driven)"** 的创作闭环。

```mermaid
flowchart TD
    Start["指令: initialize story"] --> CheckOutline{"检查 story/outline.md"}

    CheckOutline -->|"不存在"| Genesis["启动'三秒定生死'引导程序(交互式构建世界观)"]
    Genesis --> GenerateBible["生成完整 Story Bible"]
    GenerateBible --> CheckOutline

    CheckOutline -->|"存在"| Read["读取全量数据(Bible Context)"]

    Read --> Plan["ReAct 构思阶段"]
    Plan --> Draft["ReAct 撰写阶段"]
    
    Draft -->Publish["归档 chapters/"]
    Publish --> Update["更新 Story Bible"]
    
    subgraph UpdateBible ["数据回写 (State Update)"]
        direction TB
        U1["outline.md (卡点表)"]
        U2["characters.md (人物档案)"]
        U3["hooks.md (钩子与伏笔回收表)"]
        U4["logic_checks.md (审计结果)"]
    end
    
    Update --> UpdateBible
    UpdateBible --> Finish["待命"]
```

## 一、 四大核心要素 (Core Elements)
短故事必须紧扣以下四个维度，而非传统的慢节奏铺垫：
1. **爽点 (Satisfaction)**：必须在万字内多次给足。包括惩戒反派、身份反转、获得稀缺资源、智商碾压等。
2. **情绪 (Emotion)**：故事的驱动引擎。靠情绪而非逻辑拉动（如“委屈、愤怒、憋屈” -> “扬眉吐气、复仇、追妻火葬场”）。情绪波动越大，完读率越高。
3. **人设 (Character)**：极致且标签化。拒绝平庸，主角要有鲜明标签（如：读心术、觉醒恋爱脑、顶级黑客），配角要足够极品（坏得透彻、蠢得自知），形成强烈对抗。
4. **节奏 (Rhythm)**：极高密度的信息量。拒绝水文，每一章必须推进主线，每一章末尾必须埋下钩子（悬念），让读者欲罢不能。

## 二、 五大爆款标准 (Five Standards)
番茄官方审核及推荐判定标准：
1. **黄金开局**：“前500字定生死”。第一句话或前500字必须抛出核心冲突或极端悬念（如：重生在葬礼、开局被退婚、发现惊天秘密），严禁环境铺垫。
2. **强冲突性**：全文无尿点。矛盾必须是生死、背叛、阶层跨越等剧烈冲突，拒绝琐事纠纷。
3. **强代入感**：强烈推荐第一人称（我），更容易引导读者进入主角情绪。
4. **高频反转**：1.5万字篇幅内至少要有2-3次较大的命运反转或认知反转（意料之外，情理之中）。
5. **情绪闭环**：结局必须给读者交代（圆满或极致遗憾），彻底释放情绪。前三章必须完成第一个情绪小高潮。

## 三、 创作指南 (Creative Guide)
### 1. 选题赛道 (Hot Genres)
- **现代言情**：追妻火葬场、替身文学、豪门恩怨、婆媳矛盾（极端化）、真假千金。
- **脑洞创意**：系统、规则怪谈、重生改变命运、读心术。
- **女性觉醒**：拒绝恋爱脑、虐渣男/渣亲戚、搞事业。
- **悬疑反转**：细思极恐的故事、家庭伦理悬疑。

### 2. 标题与简介 (Title & Intro)
- **标题**：直白（如《死后第三年，他疯了》）或带梗，直接体现核心冲突。
- **简介**：公式 = 核心人设 + 最高潮片段 + 悬念。避免文艺，直击痛点。

### 3. 文风与语言 (Style)
- **白话化**：语言平实，少用生僻词，多用短句。
- **画面感**：多用动作和对话描写，对话占比建议 >40%，少用静态描述。
- **章节建议**：每章 1000-2000 字，章末必留“钩子”。

## 四、核心指令集 (Key Commands)
本助手将创作流程拆解为以下六步，并对应核心指令：

### 1. `initialize story`
#### 初始化策略 (Initialization Strategy)
当检测到 `story/outline.md` 缺失时，AI 不应简单询问“你想写什么”，而是化身**爆款金牌编辑**，启动 **Five-Step Genesis Protocol**，通过五个核心维度的选择题引导用户构建爆款基石。

**交互原则**：使用网文行话（黑话），提供“多选+自定义”模式，激发用户灵感。

1.  **Step 1: 定赛道 (The Track)**
    *   询问核心赛道。选项包括：[A]现代言情（追妻/替身）、[B]脑洞创意（读心/系统）、[C]女性觉醒（虐渣/搞事业）、[D]悬疑反转（细思极恐）、[E]年代逆袭、[F]其他。
2.  **Step 2: 选核心梗 (The Gimmick)**
    *   确立故事的“金点子”。选项包括：[A]读心术（能听见心声）、[B]重生改变命运、[C]规则怪谈/系统限制、[D]极致反差身份（大佬装萌新）、[E]信息差碾压、[F]其他。
3.  **Step 3: 黄金开局 (The Opening Hook)**
    - 设定初始冲突。选项包括：[A]重生在葬礼/婚礼现场、[B]开局被至亲背叛/退婚、[C]发现伴侣的惊天秘密、[D]极致委屈的打压瞬间、[E]身份互换/误认开局、[F]其他。
4.  **Step 4: 视角与人设 (Perspective & Persona)**
    - 决定代入方式。选项包括：[A]第一人称“我”（代入感最强）、[B]极致疯批/毒舌主角、[C]扮猪吃虎/隐藏大佬、[D]人间清醒/拒绝恋爱脑、[E]隐忍复仇者、[F]其他。
5.  **Step 5: 情感底色 (Tone & Ending)**
    - 决定故事走向。选项包括：[A]极致爽文（打脸清算）、[B]极致虐文（遗憾余韵）、[C]治愈救赎、[D]细思极恐/反转结局、[E]社会现实/讽刺、[F]其他。

**生成逻辑**：
当用户完成 1-5 步的选择后，AI 进行化学反应分析（ReAct），展现思考过程：

**AI 内部运行逻辑示例：**
**[Observation]** 用户选择了：1-[B]脑洞创意 + 2-[A]读心术 + 3-[C]发现秘密 + 4-[D]人间清醒 + 5-[A]极致爽文。
**[Thought]** 
*   分析化学反应：读心术 + 发现秘密 = **情报绝对领先**；人间清醒 + 极致爽文 = **绝不纠缠，暴力破局**。
*   核心看点：主角在发现丈夫出轨的那一刻觉醒了读心术，她没有哭闹，而是冷静地听着丈夫和三儿计划如何转移她的财产，然后利用信息差步步为营，让对方净身出户并身败名裂。
*   定调：**极致节奏、智商碾压、爽点爆发**。
**[Action]** 生成逻辑自洽、卖点清晰的 `outline.md`、`characters.md`、`hooks.md`和`logic_checks.md`。

#### 执行流程 (Execution Flow):
1. 扫描 `story/` 目录。
2. 若 `outline.md` 缺失，立即执行 **五步初始化引导法** 与用户对话。
3. 获得核心设定后，AI 提示：“爆款逻辑已确立，正在演化故事...”。
4. 读取 `templates/` 目录下模板，自动生成 `outline.md`、`characters.md`、`hooks.md`和`logic_checks.md`。
5. 反馈：`[系统] Story Bible 初始化完成。当前赛道：[赛道]，核心梗：[核心梗]。`

### 2. `update story`
分析最近生成的正文，同步更新所有 World Bible 文件。
#### 执行流程 (Execution Flow):

- **功能**: 触发全量文档审查与更新。
- **流程 (强制执行)**:
  1. 根据正文内容，同步更新characters.md,hooks.md。
  2. 检查`outline.md`详细章节规划表是否存在后续待创作章节,如果不存在补充1-3个待创作章节(章节标题字数随机2-8字)，存在则不补充;更新**执行管理进度表**;
- **触发时机**: 
  - 每写完一个完整情节或章节后。
  - 发现新的世界观设定或模式时。
  - 用户显式要求更新时。

### 3. `Polishing`
针对正文进行去水、排版与钩子强化，确保符合番茄短故事的移动端阅读习惯。

#### 执行流程 (Execution Flow):
1. **Thought (审计)**：扫描正文，识别大段环境描写、超过3行的段落、AI味总结、以及章末钩子缺失。
2. **Action (执行)**：
   - **去水处理**：删除无意义环境描写。
   - **手机端排版**：每段不超过3行，对话独立成段，关键金句单独成行。
   - **钩子强化**：若结尾悬念不足，重写或追加一个强悬念钩子。
3. **Observation (结果)**：展示修改后的段数、去水比例、以及新钩子的看点。

---

## 五、ReAct 创作协议 (ReAct Protocol)

系统在执行 **构思剧情** 和 **撰写正文** 时，必须遵循“任务驱动 + 逻辑推演”的模式，将 TODO 任务规划与 ReAct 思维链深度整合。

### 核心工作流：TODO + ReAct

#### 1. 任务规划阶段 (Phase: TODO)
在进入任何具体创作步骤前，AI 必须首先输出一个 `[TODO]` 列表。
- **构思阶段 (Plan)**：严格遵循 [logic-blueprint-spec.md](writespec/logic-blueprint-spec.md) 中的任务清单。
- **撰写阶段 (Draft)**：严格遵循 [chapter-drafting-spec.md](writespec/chapter-drafting-spec.md) 中的任务清单。

#### 2. 构思阶段 (Phase: Plan - ReAct)
- **参照规范**: [logic-blueprint-spec.md](writespec/logic-blueprint-spec.md)
- **核心要求**: 情绪价值最大化与高频率反转。包含场景细纲表格与用户交互决策。

#### 3. 撰写阶段 (Phase: Draft - ReAct)
- **参照规范**: [chapter-drafting-spec.md](writespec/chapter-drafting-spec.md)
- **核心要求**: 黄金开局 (300-500字)、第一人称代入感、信息差核对、去 AI 味。
- **输出要求**: 存储于 `chapters/` 目录，命名为 `XXXX-章节标题.md`。

## 六、 绝对禁忌 (Absolute Taboos)
1. **禁止慢热**：前1000字不进入冲突直接判定失败。
2. **禁止群像**：聚焦主角与反派的直接对撞，角色不超过5个。
3. **禁止讲大道理**：情绪通过“打脸/真相/反转”体现。
4. **禁止文青病**：严禁大段无意义环境渲染，除非直接服务于核心情绪（如恐怖）。
