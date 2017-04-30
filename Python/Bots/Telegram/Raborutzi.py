import telebot

class Credentials(object):
    def __init__(self):
        self.TOKEN = None
        self.USERID = None

class Raborutzi(object):
    def __init__(self):
        self.credentials = self.get_credentials()
        self.bot = telebot.TeleBot(self.credentials.TOKEN)
        self.bot.send_message(self.credentials.USERID, "Bot started.")

    @staticmethod
    def get_credentials():
        cred = Credentials()
        with open('.credentials', 'r') as cred_file:
            lines = cred_file.read().splitlines()
            for line in lines:
                words = line.split(": ")
                setattr(cred, words[0], words[1])
        return cred

    def send(self, text):
        self.bot.send_message(self.credentials.USERID, text)

if __name__ == "__main__":
    bot = Raborutzi()
    bot.send("test")
