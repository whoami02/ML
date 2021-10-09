#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:04:48 2021

@author: abhishek
"""
import numpy as np
import random
import matplotlib.pyplot as plt

class environment(object):
    prices = np.random.randint(100, 500, 50)
    max_price_addon = random.randint(5,30)
    print(prices)
    print(max_price_addon)

    def __init__(self):
        self.time = 0
        self.paper = random.randint(10,31)
        self.HistPaper = []
        self.HistPrice = []

    def percept(self):
        Price = self.prices[range(len(self.prices))] + self.max_price_addon
        self.HistPrice.append(Price)
        self.HistPaper.append(self.paper)
        dict = {'Prices': Price, 'InStock':self.paper}
        return dict

    def do(self, action):
        self.time = self.time+1
        inflation = self.time*3
        B = action['buy_paper']
        self.paper = self.paper + B
        self.HistPaper.append(self.paper)
        #Price = self.prices[]

"""
class Agent(agent):
    def __init__(self):
        pass
"""

#Driver
env = environment()
print(env.percept())
#agent = Agent(env)

