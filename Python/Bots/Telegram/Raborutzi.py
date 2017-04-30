import telebot

from credentials import Credentials

class Raborutzi(object):
    def __init__(self):
        self.credentials = Credentials('.credentials')
        self.bot = telebot.TeleBot(self.credentials.TOKEN)
        self.bot.send_message(self.credentials.USERID, "Bot started.")

    def send(self, text):
        self.bot.send_message(self.credentials.USERID, text)

if __name__ == "__main__":
    bot = Raborutzi()
    bot.send("test")
