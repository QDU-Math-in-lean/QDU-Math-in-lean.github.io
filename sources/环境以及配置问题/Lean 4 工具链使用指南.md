以下是根据您提供的链接整理的 Lean 4 工具链使用指南的 Markdown 文档，适用于 Obsidian 等笔记软件。文档内容涵盖了 `elan`、`lake` 和 `lean` 的基本用法，便于您在本地开发环境中参考和使用。

---

# Lean 4 工具链使用指南

本文介绍 Lean 4 的三大核心工具：版本管理器 `elan`、包管理器和构建工具 `lake`，以及 Lean 语言本身的核心组件 `lean` 的基本用法。

## 1. `elan`：Lean 版本管理器

`elan` 是 Lean 的版本管理器，用于安装、管理和切换不同版本的 Lean。

### 常用命令

```bash
# 查看 elan 版本
elan --version

# 更新 elan 自身
elan self update

# 显示当前使用的 Lean 版本
elan show

# 安装指定版本的 Lean
elan install leanprover/lean4:v4.10.0

# 设置默认使用的 Lean 版本
elan default leanprover/lean4:stable

# 切换默认的 Lean 版本
elan default leanprover/lean4:v4.11.0-rc1

# 在当前目录下设置使用的 Lean 版本
elan override set leanprover/lean4:stable
```

### 使用指定版本运行命令

```bash
# 查看 lake 版本
lake --version

# 使用指定版本运行 lake
elan run leanprover/lean4:v4.10.0 lake --version

# 使用指定版本运行 lean
elan run leanprover/lean4:v4.10.0 lean --version

# 使用指定版本创建新项目
elan run leanprover/lean4:v4.10.0 lake new package
```

### 配置文件位置

- 配置文件：`~/.elan/settings.toml`
    
- Windows 下的 elan 管理目录：`%USERPROFILE%\.elan\bin`
    
- Linux/Mac 下的管理目录：`$HOME/.elan`
    

## 2. `lake`：Lean 包管理器和构建工具

`lake` 是 Lean 4 的包管理器和构建工具，用于创建 Lean 项目、构建 Lean 包和编译 Lean 可执行文件。

### 创建新项目

```bash
# 创建新项目
lake new your_project_name

# 或者手动创建一个新文件夹并在原地建立项目
mkdir your_folder_name && cd your_folder_name && lake init your_project_name
```

项目结构示例：

```
your_project_name
├── YourProjectName
│   └── Basic.lean
├── lakefile.lean
├── lean-toolchain
├── Main.lean
├── YourProjectName.lean
```

- `lakefile.lean`：项目的配置文件
    
- `lean-toolchain`：项目使用的 Lean 版本
    

### 引用 Mathlib4

在 `lakefile.lean` 文件末尾添加：

```lean
require mathlib from git
  "https://github.com/leanprover-community/mathlib4"
```

保存后，VS Code 可能会提示 "Restart Lean"，可根据需要选择重启。

### 下载 Mathlib

确保终端路径在项目文件夹下，运行以下命令：

```bash
curl -L https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain -o lean-toolchain
lake update
```

可选：下载运行缓存以加快编译速度

```bash
lake exe cache get
```

### 验证 Mathlib 安装

创建一个测试文件，内容如下：

```lean
import Mathlib.Data.Real.Basic

example (a b : ℝ) : a * b = b * a := by
  rw [mul_comm a b]
```

如果 Lean infoview 没有报错，并且光标放在文件最后一行时提示 "No goals"，则说明 Mathlib 安装成功。

### 更新 Mathlib

```bash
curl -L https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain -o lean-toolchain
lake update
lake exe cache get
```

### 其他常用命令

```bash
# 构建项目可执行文件
lake build

# 运行可执行文件
lake exe hello

# 清理构建文件
lake clean

# 更新依赖
lake update

# 运行 lakefile.lean 的脚本
lake run <script>
```

## 3. `lean`：Lean 核心组件

`lean` 是 Lean 语言本身的核心组件，通常不需要直接与其交互，但在某些情况下可能需要运行 Lean 脚本或验证 Lean 代码。

### 运行 Lean 脚本

创建一个名为 `hello.lean` 的文件，内容如下：

```lean
def main : IO Unit := IO.println s!"Version: {Lean.versionString}"
```

在终端中运行：

```bash
lean --run hello.lean
```

---

请将上述内容保存为 `.md` 文件，并在 Obsidian 中打开以便于阅读和管理。如需进一步的帮助，请随时告知。