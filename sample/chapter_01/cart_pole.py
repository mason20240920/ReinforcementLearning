#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : reinforcement_learning
@File    : cart_pole.py
@Author  : Barry Allen
@Date    : 2025/11/1 18:54
@Desc    :
"""
import gym
env = gym.make("CartPole-v0")  # 进行运行
env.reset()
for _ in range(1000):
    env.render() # 显示图形界面
    action = env.action_space.sample() # 从动作空间中随机选取一个动作
    observation, reward, done, info = env.step(action)
    # Env: S -> A -> R -> S' 的过程
    # State => Action => Reward => New State
    print(observation)
env.close()