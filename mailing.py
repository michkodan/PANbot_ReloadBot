import requests

from config import MainConfig


class GetUsers(MainConfig):

    def get_users(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=getConnectedUsers'
        try:
            request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            return data['data']['connectedUsers']
        except Exception as e:
            return e
