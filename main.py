# - *- coding: utf- 8 - *-

import telebot
import buttons
from connectionCheck import CheckConnect
from mailing import GetUsers
from telebot import types
from config import MainConfig
from usersOnline import UsersOnline
from usersReload import UsersReload

bot = telebot.TeleBot(MainConfig.TOKEN)
bot.get_updates(allowed_updates=['channel_post', 'message', 'callback_query'])


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    if connected_check(msg):
        bot.send_message(msg.chat.id, MainConfig.CONNECTION_TEXT, parse_mode=['html'])
    else:
        bot.send_message(msg.chat.id, 'Вы наш партнер?',
                         reply_markup=buttons.welcome_buttons)


@bot.channel_post_handler(content_types=['text', 'photo', 'video'])
def posts_from_channels(msg):
    users = GetUsers()
    try:
        if msg.content_type == 'photo':
            if '#стартпродаж' in msg.caption:
                photo_data = msg.json
                photo_id = photo_data['photo'][1]['file_id']
                for user in users.get_users():
                    try:
                        bot.send_photo(user, photo_id, caption=msg.caption)
                    except Exception as e:
                        bot.send_message(MainConfig.ADMIN_ID,
                                         f'ID {user} не найден при попытке отправить инфу про старты\n'
                                         f'Ошибка: {e}')
        else:
            if '#стартпродаж' in msg.text:
                for user in MainConfig.ADMINS:
                    try:
                        bot.send_message(user, msg.text)
                    except Exception as e:
                        bot.send_message(MainConfig.ADMIN_ID,
                                         f'ID {user} не найден при попытке отправить инфу про старты\n'
                                         f'Ошибка: {e}')
    except Exception as e:
        bot.send_message(MainConfig.ADMIN_ID, f'Бот упал при поптыке отправить информацию о стартах:\n'
                                              f'{e}')


# Административные команды
@bot.message_handler(content_types='text')
def admin(msg):
    if msg.from_user.id in MainConfig.ADMINS:
        if 'mailing' in msg.text:
            msg_text = msg.text
            msg_text_format = msg_text.replace('mailing', '')
            users = GetUsers()
            try:
                for user in users.get_users():
                    try:
                        bot.send_message(user, msg_text_format)
                    except Exception as e:
                        bot.send_message(MainConfig.ADMIN_ID, f'Бот не отправил расслыку. Упало на пользователе: {user}'
                                                              f'. Ошибка: {e}')
            except Exception as e:
                bot.send_message(MainConfig.ADMIN_ID, f'При попытке отправить рассылку возникла проблема с запросом.'
                                                      f'Ошибка: {e}')

        if 'count' in msg.text:
            users = GetUsers()
            try:
                bot.send_message(msg.from_user.id, text='Кол-во пользователей: ' + str(len(users.get_users())))
            except Exception as e:
                bot.send_message(msg.from_user.id, text=e)

        if 'online' in msg.text:
            users_online = UsersOnline()
            try:
                bot.send_message(msg.from_user.id, text='Кол-во пользователей онлайн: ' +
                                                        str(users_online.get_online_users()))
            except Exception as e:
                bot.send_message(msg.from_user.id, text=e)

        if 'reload' in msg.text:
            users_reload = UsersReload()
            try:
                bot.send_message(msg.from_user.id, text='Статус: ' + str(users_reload.reload()))
            except Exception as e:
                bot.send_message(msg.from_user.id, text=e)


@bot.callback_query_handler(func=lambda msg: 'confirm' in msg.data)
def events_approve(msg):
    print(msg.data.replace('confirm ', ''))
    print(msg.from_user.id)
    bot.answer_callback_query(msg.id, show_alert=True, text='Test')
    bot.send_message(msg.from_user.id, text='Запись подтверждена!')


@bot.callback_query_handler(func=lambda msg: 'cancel' in msg.data)
def events_approve(msg):
    print(msg.data.replace('cancel ', ''))
    print(msg.from_user.id)
    bot.answer_callback_query(msg.id, show_alert=True, text='Test2')
    bot.send_message(msg.from_user.id, text='Запись отменена!')


# Подкючение к боту
@bot.callback_query_handler(func=lambda msg: msg.data == 'partner_true' or msg.data == 'bot_reconnect')
def new_user_btn(msg):
    bot.send_message(MainConfig.ADMIN_ID, f'Попытка подключится к боту!')
    link = 'new.panpartner.ru/bot/' + str(msg.from_user.id)
    bot_connected = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Подключится к боту 🤖", url=link)
    connected_button = types.InlineKeyboardButton('Проверить подключение *️⃣', callback_data='connected_check')
    bot_connected.add(url_button, connected_button)
    bot.send_message(msg.message.chat.id, f'Для подключение бота к Вашему аккаунту panpartner, '
                                          f' перейдите по<a href="{link}"> ссылке!</a>',
                     parse_mode=['html'], reply_markup=bot_connected)


# Стать партнером
@bot.callback_query_handler(func=lambda msg: msg.data == 'partner_false')
def be_partner_btn(msg):
    partner_reg = types.InlineKeyboardMarkup(row_width=1)
    partner_button = types.InlineKeyboardButton("Cтать партнером 🤝", url='panpartner.ru')
    partner_reg.add(partner_button)
    bot.send_message(msg.message.chat.id, MainConfig.NEW_PARTNER_TEXT, parse_mode=['html'], reply_markup=partner_reg)


# Ошибка подключения
@bot.callback_query_handler(func=lambda msg: msg.data == 'connected_check')
def connection_check_btn(msg):
    try:
        if connected_check(msg):
            bot.send_message(msg.from_user.id, text=MainConfig.CONNECTION_TEXT, parse_mode=['html'])
        else:
            bot.send_message(msg.from_user.id, text='Вы еще не подключены к боту 😞',
                             reply_markup=buttons.bot_reconnect)
            bot.send_message(MainConfig.ADMIN_ID, 'Попытка проверить подключение, до синхронизации с ботом.')
    except Exception as e:
        bot.send_message(msg.message.chat.id, f'Ой, схемы замкнуло 🤖\nНажмите на кнопку ниже, '
                                              f'чтобы перезапустить меня ⬇️',
                         parse_mode=['html'], reply_markup=buttons.bot_reconnect)
        bot.send_message(MainConfig.ADMIN_ID, f'Бот упал после попытки проверить подключение:\n'
                                              f'{e}')


# Проверка наличия поключения к базе
def connected_check(msg):
    user_id = CheckConnect(msg.from_user.id)
    return user_id.connection_check()


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)
