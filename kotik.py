import telebot  #преамбула - импортируем нужные библиотеки
from telebot import types
import argparse
from random import randrange

import os

#создаем переменную для записи бота
bot = telebot.TeleBot("1145880562:AAFvfDIwCdjGEmJPizW6f7fPbfPLVheD6n8")
#интерфейс командной строки при помощи argparse
parser = argparse.ArgumentParser()
parser.add_argument('--pictures_path', type=str,
                    help='Путь к папке с картинками',
                    default='pics/')  #путь к папке с картинками
args = parser.parse_args()
picture_files = os.listdir(args.pictures_path)  #для работы с картинками
picture_files = [os.path.join(args.pictures_path, i) for i in picture_files]


#описываем реакцию бота на команду /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    #вводим кнопку 'Получить' в интерфейс бота
    item = types.KeyboardButton('/Получить')
    markup.row(item)
    #реакция бота на /start
    bot.send_message(chat_id, "Привет! Хочешь кота?", reply_markup=markup)


#ответ бота на наш запрос 'Получить'
@bot.message_handler(commands=['Получить'])
def echo_all(message):
    chat_id = message.chat.id
    #выбирается рандомная картинка из папки, путь к которой написан выше
    i = randrange(len(picture_files))
    bot.send_photo(chat_id, open(picture_files[i], 'rb'))


bot.polling()
