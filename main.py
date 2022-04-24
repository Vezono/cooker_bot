from telebot import types, TeleBot
from lambdas import *
from config import token

bot = TeleBot(token)
forbid = '"'


def link(tg_user):
    return f"<a href='tg://user?id={tg_user.id}'>{tg_user.first_name.replace(forbid, '')}</a>"

def meal_keyboard(reciever):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Съесть', callback_data=f"m?eat {reciever.id}"), 
                 types.InlineKeyboardButton('Отказаться', callback_data=f"m?decline {reciever.id}"))
    keyboard.add(types.InlineKeyboardButton('Выбросить', callback_data=f"m?trash {reciever.id}"))
    return keyboard


def tea_keyboard(reciever):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Выпить', callback_data=f"t?drink {reciever.id}"), 
                 types.InlineKeyboardButton('Отказаться', callback_data=f"t?decline {reciever.id}"))
    keyboard.add(types.InlineKeyboardButton('Вылить', callback_data=f"t?spill {reciever.id}"))
    return keyboard


@bot.message_handler(commands=['get_info'])
def get_info_handler(m):
    bot.send_message(m.from_user.id, str(m))


@bot.message_handler(commands=['cook'], func=need_space)
def cook_handler(m):
    meal = m.text.split(' ', 1)[1].replace(forbid, '')
    cooker = m.from_user

    if not m.reply_to_message:
        bot.send_message(m.chat.id, f'{link(cooker)} приготовил(а) себе "{meal}"!', parse_mode="HTML")
        return

    reciever = m.reply_to_message.from_user
    keyboard = meal_keyboard(reciever)
    
    bot.send_message(m.chat.id, f'{link(cooker)} приготовил(а) "{meal}" для вас, {link(reciever)}!',
                     reply_to_message_id=m.reply_to_message.message_id, reply_markup=keyboard, parse_mode="HTML")


@bot.message_handler(commands=['tea'], func=need_space)
def tea_handler(m):
    tea = m.text.split(' ', 1)[1].replace(forbid, '')
    cooker = m.from_user

    if not m.reply_to_message:
        bot.send_message(m.chat.id, f'{link(cooker)} заварил(а) себе чай "{tea}"!', parse_mode="HTML")
        return

    reciever = m.reply_to_message.from_user
    keyboard = tea_keyboard(reciever)
    
    bot.send_message(m.chat.id, f'{link(cooker)} заварил(а) чай "{tea}" для вас, {link(reciever)}!',
                     reply_to_message_id=m.reply_to_message.message_id, reply_markup=keyboard, parse_mode="HTML")


@bot.callback_query_handler(func=tea_drink)
def tea_drink_handler(c: types.CallbackQuery):
    tea = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, 'Это не ваш чайок!')
        return

    bot.edit_message_text(f'{link(c.from_user)} выпил чай "{tea}"!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


@bot.callback_query_handler(func=tea_decline)
def tea_decline_handler(c: types.CallbackQuery):
    tea = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, 'Это не ваш чайок!')
        return

    bot.edit_message_text(f'{link(c.from_user)} отказался пить чай "{tea}"!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


@bot.callback_query_handler(func=tea_spill)
def tea_spill_handler(c: types.CallbackQuery):
    tea = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, 'Выливать чужой чайок запрещено Женевской конвенцией!', show_alert=True)
        return

    bot.edit_message_text(f'{link(c.from_user)} вылил нафик чай "{tea}"!!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


@bot.callback_query_handler(func=meal_eat)
def meal_eat_handler(c: types.CallbackQuery):
    meal = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, f'Это не ваше "{meal}"!')
        return

    bot.edit_message_text(f'{link(c.from_user)} съел "{meal}"!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


@bot.callback_query_handler(func=meal_decline)
def meal_decline_handler(c: types.CallbackQuery):
    meal = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, f'Это не ваше "{meal}"!')
        return

    bot.edit_message_text(f'{link(c.from_user)} отказался от "{meal}"!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


@bot.callback_query_handler(func=meal_trash)
def meal_decline_handler(c: types.CallbackQuery):
    meal = c.message.text.split('"')[1]
    reciever = int(c.data.split(' ')[1])

    if c.from_user.id != reciever:
        bot.answer_callback_query(c.id, f'❌Выкидывать чужие вкусняшки НЕЛЬЗЯ.❌', show_alert=True)
        return

    bot.edit_message_text(f'{link(c.from_user)} выбросил нафик "{meal}"!!', c.message.chat.id, c.message.message_id, parse_mode="HTML")


bot.polling()