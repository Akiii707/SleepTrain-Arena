# SleepTrain Arena 🤖💤

[![ManiSkill Challenge](https://img.shields.io/badge/Challenge-ManiSkill-blue)](https://maniskill.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  项目简介

**SleepTrain Arena** 是一个具身智能打榜工具，让你在睡眠中自动训练强化学习智能体并提交到 ManiSkill 排行榜！

### 核心功能

- 🌙 **睡前定义任务** - 用自然语言描述你想训练的任务（如 "train a robot to pick up a cube"）
- 🔧 **自动环境配置** - LLM 自动解析并生成 ManiSkill 兼容的 YAML 配置
- 🧠 **智能算法选择** - 根据任务类型自动推荐 PPO/SAC/DQN 等 RL 算法
- ⚡ **夜间训练循环** - 利用睡眠时间进行 6-8 小时不间断训练
- 📊 **一键提交榜单** - 训练完成后自动打包模型并提交到 ManiSkill Leaderboard
-  **排名追踪** - 醒来即可查看你的全球排名！

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行示例

```bash
# 使用预设任务快速测试
python sleep_train.py --task pick_cube --algorithm PPO

# 自定义自然语言任务
python sleep_train.py --prompt "train a robot arm to stack two blocks"
```

### 输出示例

```
 SleepTrain Arena 启动中...
 解析任务："train a robot to pick up a cube"
🔧 生成配置：pick_cube.yaml
🧠 选择算法：PPO (适合连续控制任务)
 开始训练... (预计 6 小时)
━━━━━━━━━━━━━━━━━━━━━━
Epoch 1/100: reward=45.2
Epoch 50/100: reward=78.9
Epoch 100/100: reward=92.3 ✓
━━━━━━━━━━━━━━━━━━━━━━
📦 打包模型文件...
🚀 提交到 ManiSkill Leaderboard...
🏆 成功！当前排名：#47/156
💤 训练完成，好好休息吧！
```

## 📁 项目结构

```
SleepTrain-Arena/
├── README.md              # 项目说明文档
├── sleep_train.py         # 主程序入口
├── requirements.txt       # Python 依赖包
├── configs/               # 任务配置文件
│   ├── pick_cube.yaml
│   └── stack_blocks.yaml
├── models/                # 训练好的模型文件
└── submit_leaderboard.py  # 排行榜提交脚本
```

## ️ 技术架构

### 核心组件

1. **LLM 环境生成器** (`env_generator.py`)
   - 将自然语言任务转化为 ManiSkill 配置
   - 支持 20+ 种预定义任务模板

2. **RL 算法库** (`rl_algorithms/`)
   - 集成 Stable Baselines3
   - 支持 PPO, SAC, DQN, TD3 等主流算法
   - 自动超参数调优建议

3. **自动化提交器** (`submit_leaderboard.py`)
   - 调用 ManiSkill API 上传模型
   - 自动生成提交说明和元数据
   - 实时获取排名反馈

4. **训练监控器** (`training_monitor.py`)
   - 实时记录训练曲线
   - 自动保存检查点
   - 失败重试机制

## 📊 预期性能

| 任务类型 | 训练时长 | 目标排名 | 成功率 |
|---------|---------|---------|-------|
| Pick Cube (简单) | 2-3 小时 | Top 30% | 95%+ |
| Stack Blocks (中等) | 4-6 小时 | Top 50% | 85%+ |
| Open Door (困难) | 8-12 小时 | Top 70% | 70%+ |

*基于 NVIDIA RTX 3080 / M1 Pro 测试环境*

##  演示视频

查看项目演示视频：[Bilibili 链接待更新]

视频内容包括：
- 项目理念介绍
- 实际运行演示
- 技术细节讲解
- 排行榜提交过程

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！

### 开发环境设置

```bash
git clone https://github.com/Akiii707/SleepTrain-Arena.git
cd SleepTrain-Arena
pip install -e .
```

### 提交自定义任务

如果你有创意任务想法，欢迎提交到 `configs/` 目录！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

##  致谢

- [ManiSkill](https://maniskill.org/) - 提供优秀的具身智能评测平台
- [Stable Baselines3](https://stable-baselines3.readthedocs.io/) - 强化学习算法库
- [SAPIEN](https://sapien.ucsd.edu/) - 仿真引擎支持

---

**Star ⭐ 这个项目，一起打造最强的睡眠训练智能体！**

*最后更新：2026-05-04*





































































































