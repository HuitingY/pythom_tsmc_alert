# stock_module.py
import twstock
import requests


def get_setting():
    try:
        with open('stock123.txt') as f:
            slist = f.readlines()
            print('讀入', slist)
            res = []
            for lst in slist:
                s = lst.split(',')
                res.append([s[0].strip(), float(s[1]), float(s[2])])
    except:
        print('stock123.txt讀檔錯誤')
        return None
    return res


def get_price(stockid):
    rt = twstock.realtime.get(stockid)
    if (rt['success']):
        return (rt['info']['name'], float(rt['realtime']['latest_trade_price']))
    else:
        return (False, False)


def get_best(stockid):
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    if (bp):
        return ('買進' if bp[0] else '賣出', bp[1])
    else:
        return (False, False)


def send_ifttt(v1, v2, v3):
    url = ('https://maker.ifttt.com/trigger/hey/with/' +
           'key/bV28LJOTDP69egS_8wi8Sv' +
           '?value1=' + str(v1) +
           '&value2=' + str(v2) +
           '&value3=' + str(v3))
    r = requests.get(url)
    if r.text[:5] == 'Congr':
        print('Send( ' + str(v1) + ', ' + str(v2) + ', ' + str(v3) + ')到Line')
    return r.text

