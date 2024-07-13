import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('Ключ')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌Ошибка. {e}")