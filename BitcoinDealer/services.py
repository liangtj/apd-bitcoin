# from TradingStrategy import autoTrade
from BitcoinDealer import basicServices
import json

'''
Market data API
'''
    
def get_kline(period,size=150):
    return basicServices.get_Kline("btcusdt", period, size)

def get_trade():
    return basicServices.get_trade("btcusdt")

# 获取 Market Detail 24小时成交量数据
def get_detail():
    return basicServices.get_detail("btcusdt")

'''
Trade/Account API
'''

# buy-market：市价买, sell-market：市价卖	
def send_order(request, amount, source, symbol, _type):
    return basicServices.send_order(request, amount, "api", "btcusdt", _type)

def orders_submitted_history():
    return basicServices.orders_matchresults(request, "btcusdt")

# def auto_trade(
#     request, buying_decline, selling_gain,
#     purchase_quantity, min_num_of_positions,
#     max_num_of_positions, stop_loss_ratio,
#     take_profit_ratio, monitoring_time):
# 
#     accountBalanceLists = basicServices.get_balance(request)["data"]["list"]
#     bal = list(filter(lambda x: x["currency"]=="usdt" and x["type"] == 'trade', accountBalanceLists))
# 
#     if bal[0] > purchase_quantity:
#         return json.dumps({status: "failed", msg: "purchase_quantity is too large"})
#     return TradingStrategy.autoTrade(
#         request, buying_decline, selling_gain,
#         purchase_quantity, min_num_of_positions,
#         max_num_of_positions, stop_loss_ratio,
#         take_profit_ratio, monitoring_time
#     )