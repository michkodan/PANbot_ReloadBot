import requests

from config import MainConfig


class UsersOnline(MainConfig):

    def get_online_users(self):
        url = MainConfig.URL + 'system.auth.form&mode=class&action=getCountOnline'
        try:
            request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
            data = request.json()
            return data['data']['countOnline']
        except Exception as e:
            return e
