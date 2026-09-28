import os

from corneddonuts import Donuts
# import pyTelegramBotAPI
import telebot
from telebot import types
from pathlib import Path

token = os.environ.get('TELEGRAM_BOT_TOKEN', '').strip()
if not token:
    raise RuntimeError('TELEGRAM_BOT_TOKEN is required')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать смену✅')
    markup.add(btn1)

    bot.send_message(message.chat.id, text='Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == 'Начать смену✅' or 'Остатки пончиков🍩'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Остатки пончиков🍩')
        btn2 = types.KeyboardButton(text='Закрыть смену❌')
        btn3 = types.KeyboardButton(text='Пополнить пончики➕')
        btn4 = types.KeyboardButton(text='Выложить пончики➖')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
    if (message.text == 'Начать смену✅'):
        bot.send_message(message.chat.id, text='Смена началась + остатки пончиков.')
        new_smena = Donuts()
        donutscorner = new_smena.StartNew()
        donuts = new_smena.Info(donutscorner)
        bot.send_message(message.chat.id, donuts, reply_markup=markup)
    elif (message.text == 'Остатки пончиков🍩'):
        new_smena = Donuts()
        donutscorner = new_smena.StartNew()
        donuts = new_smena.Info(donutscorner)
        bot.send_message(message.chat.id, donuts, reply_markup=markup)

    elif (message.text == 'Пополнить пончики➕'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Розовые')
        btn2 = types.KeyboardButton(text='Карамельные')
        btn3 = types.KeyboardButton(text='Ванильные')
        btn4 = types.KeyboardButton(text='Шоколадные')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup2.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text='Какие пончики приехали?', reply_markup=markup2)

    elif (message.text == 'Выложить пончики➖'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Розовые(выкладка)')
        btn2 = types.KeyboardButton(text='Карамельные(выкладка)')
        btn3 = types.KeyboardButton(text='Ванильные(выкладка)')
        btn4 = types.KeyboardButton(text='Шоколадные(выкладка)')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup2.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text='Какие выложили?', reply_markup=markup2)


    if (message.text == 'Розовые(выкладка)'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Розовые')
        btn2 = types.KeyboardButton(text='Карамельные')
        btn3 = types.KeyboardButton(text='Ванильные')
        btn4 = types.KeyboardButton(text='Шоколадные')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup2.add(btn1, btn2, btn3, btn4, btn5)
        name = 'Розовые'
        count = bot.send_message(message.chat.id, 'Сколько пончиков выложили?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Minuser, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Карамельные(выкладка)'):
        name = 'Карамельные'
        count = bot.send_message(message.chat.id, 'Сколько пончиков выложили?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Minuser, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Ванильные(выкладка)'):
        name = 'Ванильные'
        count = bot.send_message(message.chat.id, 'Сколько пончиков выложили?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Minuser, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Шоколадные(выкладка)'):
        name = 'Шоколадные'
        count = bot.send_message(message.chat.id, 'Сколько пончиков выложили?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Minuser, name)
        bot.load_next_step_handlers()


#--------------------ПОПОЛНЕНИЕ----------------------
    if (message.text == 'Розовые'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Розовые')
        btn2 = types.KeyboardButton(text='Карамельные')
        btn3 = types.KeyboardButton(text='Ванильные')
        btn4 = types.KeyboardButton(text='Шоколадные')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup2.add(btn1, btn2, btn3, btn4, btn5)
        name = message.text
        count = bot.send_message(message.chat.id, 'Сколько коробок приехало?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Updater, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Карамельные'):
        name = message.text
        count = bot.send_message(message.chat.id, 'Сколько коробок приехало?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Updater, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Ванильные'):
        name = message.text
        count = bot.send_message(message.chat.id, 'Сколько коробок приехало?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Updater, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Шоколадные'):
        name = message.text
        count = bot.send_message(message.chat.id, 'Сколько коробок приехало?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Updater, name)
        bot.load_next_step_handlers()
    elif (message.text == 'Шоколадные'):
        name = message.text
        count = bot.send_message(message.chat.id, 'Сколько коробок приехало?')
        bot.enable_save_next_step_handlers(delay=5)
        bot.register_next_step_handler(count, Updater, name)
        bot.load_next_step_handlers()

    if (message.text == 'Вернуться в главное меню'):
        bot.send_message(message.chat.id, text='Возвращаю в главное меню', reply_markup=markup)

    elif (message.text == 'Закрыть смену❌'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Точно закрываю смену')
        btn2 = types.KeyboardButton(text='Я передумал')
        markup2.add(btn1)
        markup2.add(btn2)
        bot.send_message(message.chat.id, text='Вы уверены, что хотите закрыть смену?', reply_markup=markup2)
    elif (message.text == 'Я передумал'):
        bot.send_message(message.chat.id, text='Возвращаю в главное меню', reply_markup=markup)
    elif (message.text == 'Точно закрываю смену'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Начать смену✅')
        markup2.add(btn1)
        bot.send_message(message.chat.id, text='Смена закрыта', reply_markup=markup2)
        new_smena = Donuts()
        donutscorner = new_smena.StartNew()
        donuts = new_smena.Info(donutscorner)
        bot.send_message(message.chat.id, text='Остатки почников на КОНЕЦ смены:')
        bot.send_message(message.chat.id, donuts, reply_markup=markup2)

def Updater(message, name):
    try:
        new_smena = Donuts()
        name = name
        count_box = message.text
        count_donuts = int(count_box) * 36
        new_smena.StartEnd(name, count_donuts)
        bot.send_message(message.chat.id, 'Успешно!')
        func(message)
    except AttributeError:
        func(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Введно неверное значение!')
        func(message)


def Minuser(message, name):
    try:
        new_smena = Donuts()
        name = name
        count = message.text
        new_smena.MinusDonuts(int(count), name)
        bot.send_message(message.chat.id, 'Успешно!')
        func(message)
    except AttributeError:
        func(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Введно неверное значение!')
        func(message)



bot.enable_save_next_step_handlers(delay=5)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
