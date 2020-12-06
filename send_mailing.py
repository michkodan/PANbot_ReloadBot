import telebot
from config import MainConfig
from mailing import GetUsers
from telebot import types
import requests
import datetime

TOKEN_DEV = '722289223:AAFeCCpDo4KMfEwaVjbNfTBwrUJSyII_jT0'
TOKEN_PROD = '1153458429:AAHG3t6S9rin--wkduqQMLdk2w5bHbJQ4tA'

bot = telebot.TeleBot(TOKEN_PROD)

users = GetUsers()

text = '''
БУМ 💣
На портале <b>panpartner.ru</b> появился раздел вторичной недвижимости😱

Вторичка на panpartner это:

🔴 Возможность отправить динамическую подборку квартир клиенту. 

🔴 Удобная система фильтров, которая поможет найти квартиру даже по самым специфическим параметрам.

🔴 А еще комиссия. Мы за взаимовыгодное сотрудничество, поэтому предлагаем нашим партнерам наилучшие условия.

💌 Есть идеи? Пиши на почту <b>support@1-an.ru</b>, мы открыты для предложений!
'''

link = 'https://new.panpartner.ru/secondary'

link_btn = types.InlineKeyboardMarkup(row_width=1)
btn = types.InlineKeyboardButton(text="Раздел вторички", url=link)
link_btn.add(btn)


def get_users(self):
    url = MainConfig.URL + 'telegram.bot.ajax&mode=class&action=getConnectedUsers'
    try:
        request = requests.get(url, auth=(MainConfig.LOGIN, MainConfig.PASSWORD))
        data = request.json()
        return data['data']['connectedUsers']
    except Exception as e:
        return e


def send_test():
    try:
        bot.send_message(MainConfig.ADMIN_ID, text=text, reply_markup=link_btn, parse_mode=['html'])
    except Exception as e:
        print(e)


def send_mailing():
    for user in users.get_users():
        try:
            bot.send_message(user, text=text, reply_markup=link_btn, parse_mode=['html'])
        except Exception as e:
            print(e)
    bot.send_message(MainConfig.ADMIN_ID, text='Рассылка завершена!')


if telebot.TeleBot(TOKEN_PROD):
    ask = input('Подтверди отправку на прод: ')
    if ask == 'y':
        send_test()
    else:
        print('Рассылка не была отправлена')
