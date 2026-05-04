#!/usr/bin/env python3
"""LLM Environment Generator - Converts natural language to ManiSkill config"""

import os
import yaml
from typing import Dict, Any

class EnvGenerator:
    def __init__(self):
        self.task_templates = {
            'pick_cube': {'env_name': 'PickCube-v0', 'episode_len': 100},
            'stack_blocks': {'env_name': 'StackBlocks-v0', 'episode_len': 200},
            'open_door': {'env_name': 'OpenDoor-v0', 'episode_len': 150}
        }
    
    def parse_task(self, desc: str) -> str:
        desc = desc.lower()
        if 'stack' in desc: return 'stack_blocks'
        if 'door' in desc: return 'open_door'
        return 'pick_cube'
    
    def generate_config(self, description: str) -> Dict[str, Any]:
        task = self.parse_task(description)
        config = self.task_templates.get(task, self.task_templates['pick_cube']).copy()
        return {'task': task, 'config': config}
    
    def save_yaml(self, config: Dict, path: str):
        with open(path, 'w') as f:
            yaml.dump(config, f)
        print(f"✅ Config saved to {path}")

def main():
    gen = EnvGenerator()
    config = gen.generate_config("pick up a cube")
    gen.save_yaml(config, 'configs/task_config.yaml')
    print(f"Task: {config['task']}")

if __name__ == "__main__":
    main()

































