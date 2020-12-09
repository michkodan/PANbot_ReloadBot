import requests

from config import MainConfig


class Events(MainConfig):
    def __init__(self, user_id: int, event_id: int):
        self.user_id = user_id
        self.event_id = event_id

    def confirm_entry(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=confirmEvent'
        params = {
            'telegramId': self.user_id,
            'eventId': self.event_id
        }
        try:
            request = requests.get(url, params=params, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            print(data)
            if data['status'] == 'success':
                return data['data']['message'] + ' ✅'
            else:
                return data['errors'][0]['message'] + ' ❌'
        except Exception as e:
            return 'Произошла ошибка 😢'

    def cancel_entry(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=confirmEvent'
        params = {
            'telegramId': self.user_id,
            'eventId': self.event_id
        }
        try:
            request = requests.get(url, params=params, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            print(data)
            if data['status'] == 'success':
                return data['data']['message'] + ' ✅'
            else:
                return data['errors'][0]['message'] + ' ❌'
        except Exception as e:
            return 'Произошла ошибка 😢'
