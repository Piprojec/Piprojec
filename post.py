import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['post'])
def create_post(message):
    # Логика создания поста
    pass

@bot.message_handler(commands=['edit'])
def edit_post(message):
    # Логика редактирования поста
    pass

bot.polling()
