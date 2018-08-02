from BitcoinSDK import HuobiServices
from .env import ENV

def getAccessKey(request):
    # if(ENV == 'dev'):
    #     return 'bb3a0e08-7ad6be2b-4ab32336-eecf7'
    return request.session['ACCESS_KEY']

def getSecretKey(request):
    # if(ENV == 'dev'):
    #     return '17497c8e-781c132b-00cf96d4-457c4'
    return request.session['SECRET_KEY']

'''
Market data API
'''

# 获取KLine
def get_kline(symbol, period, size=150):
    """
    :param symbol
    :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
    :param size: 可选值： [1,2000]
    :return:
    """
    return HuobiServices.get_kline(symbol, period, size)


# 获取marketdepth
def get_depth(symbol, type):
    """
    :param symbol
    :param type: 可选值：{ percent10, step0, step1, step2, step3, step4, step5 }
    :return:
    """
    return HuobiServices.get_depth(symbol, type)


# 获取tradedetail
def get_trade(symbol):
    """
    :param symbol
    :return:
    """
    return HuobiServices.get_trade(symbol)


# 获取merge ticker
def get_ticker(symbol):
    """
    :param symbol: 
    :return:
    """
    return HuobiServices.get_ticker(symbol)


# 获取 Market Detail 24小时成交量数据
def get_detail(symbol):
    """
    :param symbol
    :return:
    """
    return HuobiServices.get_detail(symbol)

# 获取  支持的交易对
def get_symbols(request, long_polling=None):
    return HuobiServices.get_symbols(
        long_polling, 
        getAccessKey(request),
        getSecretKey(request)
    )

'''
Trade/Account API
'''


def get_accounts(request):
    return HuobiServices.get_accounts(
        getAccessKey(request),
        getSecretKey(request)
    )

# ACCOUNT_ID = 0
# 获取当前账户资产
# def get_balance(acct_id=None):
def get_balance(request):
    return HuobiServices.get_balance(
        getAccessKey(request),
        getSecretKey(request)
    )


# 下单

# 创建并执行订单
def send_order(request, amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: 如果使用借贷资产交易，请在下单接口,请求参数source中填写'margin-api'
    :param symbol: 
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price: 
    :return: 
    """
    return HuobiServices.send_order(
        amount, source,
        symbol, _type,
        getAccessKey(request),
        getSecretKey(request),
        price
    )

# 撤销订单
def cancel_order(request, order_id):
    return HuobiServices.cancel_order(
        order_id,
        getAccessKey(request),
        getSecretKey(request)
    )


# 查询某个订单
def order_info(request, order_id):
    return HuobiServices.order_info(
        order_id,
        getAccessKey(request),
        getSecretKey(request)
    )


# 查询某个订单的成交明细
def order_matchresults(request, order_id):
    return HuobiServices.order_matchresults(
        order_id,
        getAccessKey(request),
        getSecretKey(request)
    )


# 查询当前委托、历史委托
def orders_list(
    request, 
    symbol, states, 
    types=None, start_date=None, 
    end_date=None, _from=None, 
    direct=None, size=None
    ):
    """
    
    :param symbol: 
    :param states: 可选值 {pre-submitted 准备提交, submitted 已提交, partial-filled 部分成交, partial-canceled 部分成交撤销, filled 完全成交, canceled 已撤销}
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: 可选值{prev 向前，next 向后}
    :param size: 
    :return: 
    """
    return HuobiServices.orders_list(
        symbol, states,
        getAccessKey(request),
        getSecretKey(request),
        types, start_date,
        end_date, _from,
        direct, size
    )


# 查询当前成交、历史成交
def orders_matchresults(
    request,
    symbol, types=None, 
    start_date=None, end_date=None, 
    _from=None, direct=None, 
    size=None
    ):
    """
    
    :param symbol: 
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: 可选值{prev 向前，next 向后}
    :param size: 
    :return: 
    """
    return HuobiServices.orders_matchresults(
        symbol,
        getAccessKey(request),
        getSecretKey(request),
        types, start_date,
        end_date, _from,
        direct, size
    )



# 申请提现虚拟币
def withdraw(
    request, address,
    amount, currency,
    fee=0, addr_tag=""
    ):
    """

    :param address_id: 
    :param amount: 
    :param currency:btc, ltc, bcc, eth, etc ...(火币Pro支持的币种)
    :param fee: 
    :param addr-tag:
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    return HuobiServices.withdraw(
        address, amount, currency,
        getAccessKey(request),
        getSecretKey(request),
        fee, addr_tag
    )

# 申请取消提现虚拟币
def cancel_withdraw(request, address_id):
    """

    :param address_id: 
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    return HuobiServices.cancel_withdraw(
        address_id,
        getAccessKey(request),
        getSecretKey(request)
    )


'''
借贷API
'''

# 创建并执行借贷订单


def send_margin_order(request, amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: 'margin-api'
    :param symbol: 
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price: 
    :return: 
    """
    return HuobiServices.send_margin_order(
        amount, source,
        symbol, _type,
        getAccessKey(request),
        getSecretKey(request),
        price
    )

# 现货账户划入至借贷账户


def exchange_to_margin(symbol, currency, amount, request):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    return HuobiServices.exchange_to_margin(
        symbol, currency, amount
        getAccessKey(request),
        getSecretKey(request)
    )

# 借贷账户划出至现货账户


def margin_to_exchange(request, symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    return HuobiServices.margin_to_exchange(
        symbol, currency,
        amount,
        getAccessKey(request),
        getSecretKey(request)
    )

# 申请借贷
def get_margin(request, symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    return HuobiServices.get_margin(
        symbol, currency, amount,
        getAccessKey(request),
        getSecretKey(request)
    )

# 归还借贷
def repay_margin(request, order_id, amount):
    """
    :param order_id: 
    :param amount: 
    :return: 
    """
    return HuobiServices.repay_margin(
        order_id, amount,
        getAccessKey(request),
        getSecretKey(request)
    )

# 借贷订单
def loan_orders(
    request,
    symbol, currency, start_date="", 
    end_date="", start="", direct="", 
    size=""):
    """
    :param symbol: 
    :param currency: 
    :param direct: prev 向前，next 向后
    :return: 
    """
    return HuobiServices.loan_orders(
        symbol, currency,
        getAccessKey(request),
        getSecretKey(request),
        start_date, end_date,
        start, direct,
        size
    )


# 借贷账户详情,支持查询单个币种
def margin_balance(request, symbol):
    """
    :param symbol: 
    :return: 
    """
    return HuobiServices.margin_balance(
        symbol,
        getAccessKey(request),
        getSecretKey(request)
    )


if __name__ == '__main__':
    print (get_symbols())
