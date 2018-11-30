# coding=utf-8
import os
import telebot
import urllib
import json

bot = telebot.TeleBot(os.environ["SPACE_BOT_TOKEN"])


@bot.message_handler(commands=['start', 'help'])
def send_start_message(message):
    bot.reply_to(message, "Olá, eu sou o bot 'Quem está no espaço?'\n"
                          "Envie o comando /people para saber quais "
                          "pessoas estão no espaço nesse momento.")


@bot.message_handler(commands=['people'])
def send_people(message):
    bot.reply_to(message, get_reply_message())


def get_reply_message():
    n_people, people = get_people()
    message = "Existem " \
              + str(n_people) + \
              " pessoas no espaço neste momento, são elas: \n\n"
    for person in people:
        message += person["name"] + \
                   " na espaçonave " + person["craft"] + "\n\n"

    return message


def get_people():
    req = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    return obj["number"], obj["people"]


bot.polling()
