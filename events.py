import requests

from config import MainConfig


class Events(MainConfig):
    def __init__(self, user_id: int, event_id: int):
        self.user_id = user_id
        self.event_id = event_id

    def confirm_entry(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=checkConnect'
        params = {
            'user_id': self.user_id,
            'event_id': self.event_id
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

    def cancel_entry(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=checkConnect'
        params = {
            'user_id': self.user_id,
            'event_id': self.event_id
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