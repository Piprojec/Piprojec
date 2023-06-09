import telebot
from telebot import types

bot = telebot.TeleBot('6219044790:AAHBNwgpnY8NAhD1_8jCSTi032wRY1LRv_I')
# Список товаров
products = []

# Команда для администратора для публикации товара
@bot.message_handler(commands=['publish'])
def publish_product(message):
    chat_id = message.chat.id

    # Проверка, является ли пользователь администратором (можно настроить свою логику проверки)
    if is_admin(chat_id):
        # Получение данных о товаре от администратора (можно настроить свою логику ввода)
        product_name = input("Введите название товара: ")
        product_description = input("Введите описание товара: ")
        product_price = input("Введите цену товара: ")

        # Создание объекта товара и добавление его в список товаров
        product = {
            'name': product_name,
            'description': product_description,
            'price': product_price,
            'likes': 0
        }
        products.append(product)

        # Отправка уведомления об успешной публикации товара
        bot.send_message(chat_id, "Товар успешно опубликован!")
    else:
        # Уведомление, что только администратор может выполнять данную команду
        bot.send_message(chat_id, "У вас нет прав на выполнение данной команды!")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать в наш магазин!")

    # Вывод списка товаров
    for product in products:
        product_text = f"Название: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']}💰"
        like_button = types.InlineKeyboardButton("❤️", callback_data=f"like_{product['name']}")
        keyboard = types.InlineKeyboardMarkup().add(like_button)
        bot.send_message(chat_id, product_text, reply_markup=keyboard)

# Обработчик нажатия на кнопку "❤️"
@bot.callback_query_handler(func=lambda call: call.data.startswith('like_'))
def like_product(call):
    chat_id = call.message.chat.id
    product_name = call.data.split('_')[1]

    # Увеличение счетчика лайков для товара
    for product in products:
        if product['name'] == product_name:
            product['likes'] += 1

    # Отправка уведомления о нажатии на сердечко
    bot.send_message(chat_id, "Вы нажали на сердечко!")

# Функция для проверки, является ли пользователь администратором
def is_admin(chat_id):
    # Здесь можно реализовать свою логику проверки
    return chat_id == YOUR_ADMIN_CHAT_ID

# Запуск бота
bot.polling()
