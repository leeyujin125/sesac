from util import company_lists, plot_line_graph
from random import random
import os
from collections import defaultdict

class Stock:
    HISTORY_DIR = 'stock_history'
    def __init__(self, name):
        self.name = name 
        self.initial_price = 10000
        self.price_history = [10000]
        self.momentum = 0
        self.momentum_upper_bound = max(abs(random()-0.5), 0.5)
        self.momentum_lower_bound = -max(abs(random()-0.5), 0.5)
        self.price = self.initial_price

    def __hash__(self):
        return hash(self.name)
    
    def step(self, market):
        if random() < 0.05:
            self.price = self.price * 1.10
        elif random() > 0.95:
            self.price = self.price * 0.80
        else:
            self.momentum += (random() - 0.5) * 0.1 #+ self.momentum
            if self.momentum_upper_bound < self.momentum:
                self.momentum = self.momentum_lower_bound
            elif self.momentum_lower_bound > self.momentum:
                self.momentum = self.momentum_lower_bound
            delta = random() - 0.5 + self.momentum + market.momentum 
            self.price += self.momentum * self.price 
        self.price_history.append(self.price)

    def plot_history(self):
        if not os.path.exists(Stock.HISTORY_DIR):
            os.makedirs(Stock.HISTORY_DIR)
        
        plot_line_graph(self.price_history, save_to = f'stock_history/{self.name}.png', title = f'Price graph of {self.name}', x_label = 'time', y_label = '{self.name} Asset')
         

class StockMarket:
    def __init__(self, listed_stocks):
        self.listed_stocks = listed_stocks
        self.momentum = 0.01

    def step(self):
        for stock in self.listed_stocks:
            stock.step(self)

class Investor:
    def __init__(self, name = 'investor1', initial_asset = 10000000, strategy = lambda investor, market:None):
        self.name = name 
        self.asset = initial_asset
        self.cash = initial_asset 
        self.asset_history = [initial_asset]
        self.portfolio = defaultdict(float)
        self.strategy = strategy

    def buy(self, stock, amount):
        if self.cash - stock.price * amount >= 0:
            self.portfolio[stock] += amount
            self.cash -= stock.price * amount
        else:
            print('Out of money')

    def sell(self, stock, amount):
        if stock in self.portfolio and self.portfolio[stock] >= amount:
            self.portfolio[stock] -= amount 
            self.cash += stock.price * amount 
        else:
            print('Not enough stocks')

    def buy_or_sell(self, market):
        self.strategy(self, market) #살지 말지 결정하는 strategy
        stock_asset = 0
        for stock, amount in self.portfolio.items():
            stock_asset += stock.price * amount
        self.asset = stock_asset + self.cash 
        self.asset_history.append(self.asset)

    def plot_history(self):
        plot_line_graph(self.asset_history, save_to = f'{self.name}.png', title = f'Asset History of {self.name}', x_label = 'time', y_label = '{self.name} Asset')

def simulate(strategy = lambda investor, market:None, n_steps = 100, n_company = 10): # 주식시장에서 어떻게 플레이 할거냐의 전략
    #n_steps: 몇 스텝 돌거야? n_company: 어떤 회사? 
    investor = Investor(strategy=strategy)
    stocks = []
    
    company_list = []

    if not os.path.exists(Stock.HISTORY_DIR):
        company_list = company_lists(n_company)
    else:
        company_list = [e.strip('.png') for e in os.listdir(Stock.HISTORY_DIR)]
        
        if len(company_list) > n_company:
            company_list = company_list[:n_company]
        else:
            company_list = company_list + company_lists(n_company - len(company_list))

    for name in company_list:
        stocks.append(Stock(name))

    market = StockMarket(stocks)

    for step in range(n_steps):
        market.step() # == StockMarket.step(market, )
        investor.buy_or_sell(market)

    for stock in stocks:
        stock.plot_history()
    investor.plot_history()

def my_strategy(investor, market):
    # 가장 적은 금액에서 사기
    if investor.cash > 0:
        cheap_stock = min(market.listed_stocks, key=lambda s: s.price)

        amount_to_buy = int(investor.cash // cheap_stock.price)
        if amount_to_buy > 0:
            investor.buy(cheap_stock, amount_to_buy)

    # 가장 높은 금액에서 팔기
    if investor.portfolio:
        expensive_stock = max(investor.portfolio.keys(), key=lambda s: s.price)

        amount_to_sell = investor.portfolio[expensive_stock]
        if amount_to_sell > 0:
            investor.sell(expensive_stock, amount_to_sell)

if __name__ == '__main__':
    simulate(strategy=my_strategy) # simulate 함수 호출
