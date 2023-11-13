import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "приветствие")


@bot.message_handler(commands=['graph'])
def send_graph(message):
    photo = open('олег.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


if __name__ == "__main__":
    bot.infinity_polling()
