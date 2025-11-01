#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : reinforcement_learning
@File    : main.py
@Author  : Barry Allen
@Date    : 2025/11/1 18:35
@Desc    :
"""
# 观测Observation => 输出动作Action => 环境Environment => 执行动作Action => 向前走一步
import gym
env = gym.make("Taxi-v3")
observation = env.reset() # 观测
agent = load_agent() # 加载Agent
for step in range(100):  # 进行步数读取
    action = agent(observation)  # 观测Action
    observation, reward, done, info = env.step(action)