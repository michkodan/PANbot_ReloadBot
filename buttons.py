from telebot import types

# Приветственные кнопки
welcome_buttons = types.InlineKeyboardMarkup(row_width=2)
partner_false = types.InlineKeyboardButton('Нет, но хочу 🚩', callback_data='partner_false')
partner_true = types.InlineKeyboardButton('Да, я ваш партнер✅', callback_data='partner_true')
welcome_buttons.add(partner_true, partner_false)

# Подключение бота (повторное)
bot_reconnect = types.InlineKeyboardMarkup(row_width=1)
bot_reconnect_check = types.InlineKeyboardButton('Попробовать снова ↩️', callback_data='bot_reconnect')
bot_reconnect.add(bot_reconnect_check)

# Кнопки для авторизованного пользователя
main_buttons_full = types.InlineKeyboardMarkup(row_width=1)
# btn8 = types.InlineKeyboardButton('👩 ‍Контакты', callback_data='contacts')
# btn2 = types.InlineKeyboardButton('🏗 Застройщики', callback_data='developers')
# btn3 = types.InlineKeyboardButton('ТОП-5️⃣ переуступок', callback_data='top_assignments')
# btn4 = types.InlineKeyboardButton('☎ Обратный звонок', callback_data='call_back')
# btn5 = types.InlineKeyboardButton('📅 Наши мероприятия', callback_data='get_events')
# btn6 = types.InlineKeyboardButton('🚘 АвтоПАН', callback_data='auto_pan')
# btn7 = types.InlineKeyboardButton('💼 Переговорные', callback_data='rooms')
btn9 = types.InlineKeyboardButton('🔁 ПАН Trade-In', callback_data='trade_in')
# btn10 = types.InlineKeyboardButton('Поиск ЖК', callback_data='building')
# btn11 = types.InlineKeyboardButton('Файлы', callback_data='files')
main_buttons_full.add(btn9)


# Кнопки для авторизованного пользователя
main_buttons = types.InlineKeyboardMarkup(row_width=2)
call_back = types.InlineKeyboardButton('☎ Обратный звонок', callback_data='call_back')
# btn10 = types.InlineKeyboardButton('Поиск ЖК', callback_data='building')
# btn11 = types.InlineKeyboardButton('Файлы', callback_data='files')
main_buttons.add(call_back)

hide_buttons = types.ReplyKeyboardRemove()

