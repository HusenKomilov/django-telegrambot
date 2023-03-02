from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from api_url import create_user, create_feedback
from settings import *

bot = TeleBot(TOKEN)


def buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Takliflar")
    markup.add(btn)
    return markup


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Salom {message.from_user.first_name}", reply_markup=buttons())
    create_user(username=message.from_user.username, name=message.from_user.first_name, user_id=message.chat.id)


@bot.message_handler(regexp='Takliflar')
def feedback(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Takliflaringizni yuboring!")
    bot.register_next_step_handler(msg, feedback_text)


def feedback_text(message: Message):
    chat_id = message.chat.id
    text = message.text
    # print(text)
    create_feedback(user_id=chat_id, body=text)
    bot.send_message(chat_id, "Taklifingiz ko'rib chiqish uchun adminga yuborildi")


bot.polling()
