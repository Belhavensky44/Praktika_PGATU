import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('Ключ')

@bot.message_handler(commands=['site'])
def site(message):
    site_url = "https://example.com"
    user_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Открыть сайт", url=site_url))
    bot.send_message(user_id, f"Нажмите на кнопку, чтобы открыть сайт: {site_url}", reply_markup=markup)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌Ошибка. {e}")