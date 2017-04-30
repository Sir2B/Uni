import telebot

def get_credentials():
    token = ""
    with open('.credentials', 'r') as cred_file:
        line = cred_file.readline()
    return line.splitlines()[0]

bot = telebot.TeleBot(get_credentials())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()