import requests

from config import MainConfig


class CheckConnect(MainConfig):
    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def connection_check(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=checkConnect'
        params = {
            'telegramId': self.chat_id
        }
        try:
            request = requests.get(url, params=params, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            if data['data']['status']:
                return True
            else:
                return False
        except Exception as e:
            return e
