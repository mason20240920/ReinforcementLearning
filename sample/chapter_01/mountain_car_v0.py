#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : reinforce learning
@File    : mountain_car_v0.py
@Author  : Barry Allen
@Date    : 2025/11/1 19:07
@Desc    :
"""
import gym
env = gym.make("MountainCar-v0")
print('观测空间 = {}'.format(env.observation_space))
print('动作空间 = {}'.format(env.action_space)) # 离散空间还是连续空间
print('观测范围 = {} ~ {}'.format(env.observation_space.low, env.observation_space.high))
print("动作数 = {}".format(env.action_space.n))