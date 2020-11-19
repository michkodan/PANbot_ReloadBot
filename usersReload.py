import requests

from config import MainConfig


class UsersReload(MainConfig):

    def reload(self):
        url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=reloadUsers'
        try:
            request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            return data['data']['status']
        except Exception as e:
            return e
