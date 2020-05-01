import telebot
from telebot import types
import argparse
from random import randrange

import os


bot = telebot.TeleBot("TOKEN")
parser = argparse.ArgumentParser()
parser.add_argument('--pictures_path', type=str, help='Путь к папке с картинками', default='pics/')
args = parser.parse_args()
picture_files = os.listdir(args.pictures_path)
picture_files = [os.path.join(args.pictures_path, i) for i in picture_files]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    item = types.KeyboardButton('/Получить')
    markup.row(item)
    bot.send_message(chat_id, "Привет! Хочешь кота?", reply_markup=markup)


@bot.message_handler(commands=['Получить'])
def echo_all(message):
    chat_id = message.chat.id
    i = randrange(len(picture_files))
    bot.send_photo(chat_id, open(picture_files[i], 'rb'))


bot.polling()
