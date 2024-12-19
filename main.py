import telebot
import config
from random import choice

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['fact'])
def fact_handler(message):
    fact = choice(["Земля не идеальной сферической формы.", "Притяжение на Земле не везде одинаково.", "В качестве единственного спутника Земли выступает Луна."])
    bot.reply_to(message, fact)

bot.infinity_polling() 
