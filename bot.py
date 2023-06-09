import telebot
from telebot import types

bot = telebot.TeleBot('6219044790:AAHBNwgpnY8NAhD1_8jCSTi032wRY1LRv_I')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Создать")
    item2 = types.KeyboardButton("Опубликованные")
    item3 = types.KeyboardButton("Входящие")
    item4 = types.KeyboardButton("Отчет 🌞")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Приветствие. Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Создать":
        # Обработка создания записи
        create_post(message.chat.id)
    elif message.text == "Опубликованные":
        # Переход на страницу с опубликованными записями
        published_posts(message.chat.id)
    elif message.text == "Входящие":
        # Переход на страницу с входящими записями
        incoming_posts(message.chat.id)
    elif message.text == "Отчет 🌞":
        # Переход на страницу с отчетами
        report_page(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Неверная команда. Попробуйте еще раз.")

def create_post(chat_id):
    # Логика создания записи
    pass

def published_posts(chat_id):
    # Логика отображения опубликованных записей
    pass

def incoming_posts(chat_id):
    # Логика отображения входящих записей
    pass

def report_page(chat_id):
    # Логика отображения отчетов
    pass

bot.polling()
