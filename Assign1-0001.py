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
    max_price_addon = random.randint(0,30)
    """  print(prices)
    print(max_price_addon)"""

    def __init__(self):
        self.time = 0
        self.paper = random.randrange(25)
        self.HistPaper = []                                 #Paper available in stock History
        self.HistPrice = []                                 #Price History

    def initial_percept(self):
        Price = self.prices[random.randrange(len(self.prices))] + random.randrange(self.max_price_addon)
        self.HistPrice.append(Price)
        self.HistPaper.append(self.paper)
        self.dict = {'Prices': Price, 'InStock':self.paper}
        return dict

    def do(self, action):
        self.time = self.time + 1
        inflation = self.time * 3
        B = action['buy_paper']
        self.paper = self.paper + B
        self.HistPaper.append(self.paper)
        #Price = self.prices[len(self.prices)]+inflation
        Price = self.prices[self.time] + inflation + random.randrange(self.max_price_addon)
        self.HistPrice.append(Price)
        self.dict = {'Price': Price, 'InStock':self.paper}
        return dict

class agent(object):
    def __init__(self, env):
        self.money_used = 0
        self.env = env
        percepts = env.initial_percept()
        self.paper_price = percepts['Prices']
        self.instock = percepts['InStock']

    def go(self, n):
        Number_of_papers_to_buy = random.randrange(env.dict['InStock'])
        for i in range(n):
            self.money_used = self.money + Number_of_papers_to_buy * self.paper_price
            percepts = env.do({'buy_paper':Number_of_papers_to_buy})
            self.temp = self.paper_price
            self.paper_price = percepts['Prices']
            self.temp = self.temp + (self.paper_price - self.temp)//2
            self.instock = percepts['InStock']


#Driver
env = environment()
bot = agent(env)
bot.go(20)



