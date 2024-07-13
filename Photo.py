import telebot
import webbrowser
from telebot import types

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('удалить', callback_data='delete')
    btn2 = types.InlineKeyboardButton('редактировать', callback_data='edit')
    markup.row(btn2, btn1)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌Произошла ошибка. {e}")