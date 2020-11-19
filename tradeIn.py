import requests

from config import MainConfig


class TradeIn(MainConfig):

    def trade_in(self):
        url = MainConfig.URL + 'trade.in.ajax&mode=class&action=getTradeIn'
        try:
            request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            return data['data']['tradeIn']
        except Exception as e:
            return e
