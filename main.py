import telebot

bot = telebot.TeleBot('6142962089:AAHY38-QZlbOuJ19Z_anyddIgtCWDCZTryg')


@bot.message_handler()
def hi(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Здаров")
    if message.text.lower() == '/hello-world':
        bot.send_message(message.chat.id, 'Привет!')


bot.polling(none_stop=True)