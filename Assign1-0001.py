
"""
Created on Fri Oct  8 22:04:48 2021

@author: abhishek
"""
import numpy as np
import random
#import matplotlib.pyplot as plt


class environment(object):
    prices = np.random.randint(100, 500, 50)
    max_price_addon = random.randint(0,30)
    """  print(prices)
    print(max_price_addon)"""

    def __init__(self):
        self.T = 0                                        #tiem counter
        self.paper = random.randrange(25)            #initial stock of papers to buy from
        self.HistPaper = []                                 #Paper available in stock History
        self.HistPrice = []                                 #Price History

    def initial_percept(self):
        P = self.prices[random.randrange(len(self.prices))] + random.randrange(self.max_price_addon)
        #Price = 200
        self.HistPrice.append(P)

        self.HistPaper.append(self.paper)
        self.dict = {'Prices': P, 'InStock':self.paper}
        return dict

    def do(self, Buy):
        self.T = self.T + 1
        self.inflation = self.T * 3
        B = Buy['buy_paper']
        self.paper = self.paper + B
        self.HistPaper.append(self.paper)
        #Price = self.prices[len(self.prices)]+inflation
        Price = self.prices[self.T] + self.inflation + random.randrange(self.max_price_addon)
        self.HistPrice.append(Price)
        self.dict = {'Price': Price, 'InStock':self.paper}
        return dict

class agent(object):
    def __init__(self, env):
        self.money_used = 0
        self.env = env
        percept = env.initial_percept()
        self.paper_price = percept['Prices']
        """self.paper_price = percept"""
        self.instock = percept['InStock']

    def go(self, n):
        Number_of_papers_to_buy = random.randrange(env.dict['InStock'])
        for i in range(n):
            self.money_used = self.money_used + Number_of_papers_to_buy * self.paper_price
            percept = env.do({'buy_paper':Number_of_papers_to_buy})
            self.temp = self.paper_price
            self.paper_price = percept['Prices']
            self.temp = self.temp + (self.paper_price - self.temp)//2
            self.instock = percept['InStock']


#Driver
env = environment()
#print(type(env)
bot = agent(env)
bot.go(20)
#print(env.initial_percept())
#print(env.do())
