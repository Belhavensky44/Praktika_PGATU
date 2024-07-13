import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('Key')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Hello!':
        bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌Error!. {e}")