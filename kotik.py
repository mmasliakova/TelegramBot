import telebot #преамбула - импортируем нужные библиотеки 
from telebot import types
import argparse
from random import randrange

import os


bot = telebot.TeleBot("TOKEN") #создаем переменную для записи бота
parser = argparse.ArgumentParser()
parser.add_argument('--pictures_path', type=str,
                    help='Путь к папке с картинками', default='pics/') #путь к папке с картинками
args = parser.parse_args()
picture_files = os.listdir(args.pictures_path) #для работы с картинками
picture_files = [os.path.join(args.pictures_path, i) for i in picture_files]


@bot.message_handler(commands=['start', 'help']) #описываем реакцию бота на команду /start
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    item = types.KeyboardButton('/Получить') #вводим кнопку 'Получить' в интерфейс бота
    markup.row(item)
    bot.send_message(chat_id, "Привет! Хочешь кота?", reply_markup=markup) #реакция бота на /start


@bot.message_handler(commands=['Получить']) #ответ бота на наш запрос 'Получить'
def echo_all(message):
    chat_id = message.chat.id
    i = randrange(len(picture_files)) #выбирается рандомная картинка из папки, путь к которой написан выше
    bot.send_photo(chat_id, open(picture_files[i], 'rb'))


bot.polling()
