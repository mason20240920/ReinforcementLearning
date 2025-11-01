#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : reinforcement_learning
@File    : env_space.py
@Author  : Barry Allen
@Date    : 2025/11/1 19:03
@Desc    : Gym 已注册的环境
"""
from gym import envs
env_specs = envs.registry.all()
env_ids = [env_spec.id for env_spec in env_specs]
print(env_ids)