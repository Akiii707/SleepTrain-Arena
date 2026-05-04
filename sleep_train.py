#!/usr/bin/env python3
"""
SleepTrain Arena - Embodied AI Leaderboard Tool
睡前定义任务，醒来收获训练好的智能体，自动提交到 ManiSkill 排行榜！
"""

import argparse
import os
import time
import json
import requests
from datetime import datetime
from stable_baselines3 import PPO, SAC, DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import CheckpointCallback, EvalCallback
import gymnasium as gym

# ============================================================================
# 核心组件 1: LLM 环境生成器（将自然语言任务转化为 ManiSkill 配置）
# ============================================================================

class TaskConfigGenerator:
    """根据任务名称自动生成 ManiSkill 环境配置"""
    
    TASK_TEMPLATES = {
        "pick_cube": {
            "env_name": "PickCube-v0",
            "description": "抓取立方体任务 - 基础操作任务",
            "reward_threshold": 0.8,
            "max_steps": 200,
        },
        "stack_blocks": {
            "env_name": "StackCube-v0",
            "description": "堆叠积木任务 - 中级操作任务",
            "reward_threshold": 0.7,
            "max_steps": 300,
        },
        "open_door": {
            "env_name": "OpenDoor-v0",
            "description": "开门任务 - 高级操作任务",
            "reward_threshold": 0.6,
            "max_steps": 400,
        },
        "pour_liquid": {
            "env_name": "PourLiquid-v0",
            "description": "液体倾倒任务 - 精细操作任务",
            "reward_threshold": 0.65,
            "max_steps": 350,
        }
    }
    
    @classmethod
    def get_config(cls, task_name: str) -> dict:
        """获取任务配置"""
        if task_name in cls.TASK_TEMPLATES:
            return cls.TASK_TEMPLATES[task_name]
        else:
            # 自定义任务：使用默认配置
            return {
                "env_name": task_name,
                "description": f"自定义任务：{task_name}",
                "reward_threshold": 0.5,
                "max_steps": 200,
            }


# ============================================================================
# 核心组件 2: RL 训练器（支持多种算法一键切换）
# ============================================================================

class SleepTrainer:
    """睡眠训练器 - 自动化 RL 训练流程"""
    
    ALGORITHMS = {
        "PPO": PPO,
        "SAC": SAC,
        "DQN": DQN,
    }
    
    def __init__(self, task_name: str, algorithm: str = "PPO", 
                 total_timesteps: int = 100000, verbose: int = 1):
        self.task_name = task_name
        self.algorithm_name = algorithm
        self.total_timesteps = total_timesteps
        self.verbose = verbose
        
        # 获取任务配置
        self.config = TaskConfigGenerator.get_config(task_name)
        self.env_name = self.config["env_name"]
        
        # 创建日志目录
        self.log_dir = f"./logs/{task_name}_{algorithm}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(self.log_dir, exist_ok=True)
        
        print(f"🎯 任务：{self.config['description']}")
        print(f"🤖 算法：{algorithm}")
        print(f"️  训练步数：{total_timesteps:,}")
        print(f"📁 日志目录：{self.log_dir}")
    
    def create_environment(self):
        """创建向量化环境"""
        try:
            # 尝试加载 ManiSkill 环境
            env = make_vec_env(self.env_name, n_envs=1)
            print(f"✅ 环境加载成功：{self.env_name}")
            return env
        except Exception as e:
            print(f"⚠️  ManiSkill 环境不可用，使用模拟环境：{e}")
            # 回退到 Gym 内置环境作为演示
            env = make_vec_env("CartPole-v1", n_envs=1)
            print("✅ 使用 CartPole-v1 作为演示环境")
            return env
    
    def train(self) -> object:
        """执行训练"""
        print("\n🚀 开始训练...")
        start_time = time.time()
        
        # 创建环境
        env = self.create_environment()
        
        # 选择算法
        algo_class = self.ALGORITHMS.get(self.algorithm_name, PPO)
        
        # 初始化模型
        if self.algorithm_name == "DQN":
            model = algo_class(
                "MlpPolicy", env, 
                learning_rate=3e-4,
                buffer_size=10000,
                learning_starts=1000,
                batch_size=64,
                gamma=0.99,
                target_update_interval=10,
                verbose=self.verbose,
                tensorboard_log=self.log_dir,
            )
        else:
            model = algo_class(
                "MlpPolicy", env,
                learning_rate=3e-4,
                n_steps=2048,
                batch_size=64,
                n_epochs=10,
                gamma=0.99,
                gae_lambda=0.95,
                clip_range=0.2,
                verbose=self.verbose,
                tensorboard_log=self.log_dir,
            )
        
        # 设置回调函数
        checkpoint_callback = CheckpointCallback(
            save_freq=10000,
            save_path=self.log_dir,
            name_prefix="checkpoint",
        )
        
        # 开始训练
        model.learn(
            total_timesteps=self.total_timesteps,
            callback=checkpoint_callback,
            progress_bar=True,
        )
        
        training_time = time.time() - start_time
        print(f"\n✅ 训练完成！耗时：{training_time/60:.2f} 分钟")
        
        # 保存最终模型
        model_path = f"{self.log_dir}/final_model"
        model.save(model_path)
        print(f"💾 模型已保存：{model_path}.zip")
        
        return model


# ============================================================================
# 核心组件 3: ManiSkill 排行榜提交器
# ============================================================================

class LeaderboardSubmitter:
    """自动提交到 ManiSkill 排行榜"""
    
    LEADERBOARD_API = "https://maniskill.ai/api/v1/submit"
    
    def __init__(self, task_name: str, model_path: str, author: str = "SleepTrain-Arena"):
        self.task_name = 
















































































































































































