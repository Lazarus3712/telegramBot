import telebot
import constants

bot = telebot.TeleBot(constants.token)

def log(message):
    from datetime import datetime
    print(datetime.now())
    text = ("Повідомлення від {0} {1}; (id = {2}) \n Текст - {3}\n\n".
        format(message.from_user.first_name, message.from_user.last_name,
        str(message.from_user.id), message.text))

    print(text)

    f = open("messages.txt", "a")
    f.writelines(text)
    f.close()

@bot.message_handler(content_types=["text"])
def handle_message(message):
    log(message)

    text = str(message.text).lower()

    if (text == "привіт"):
        bot.send_message(message.chat.id, "Привіт!")
    elif(text == "як справи?"):
        bot.send_message(message.chat.id, "норм а в тебе?")
    else:
        bot.send_message(message.chat.id, "Я не розумію тебе, бо розробник лінива жопа і не навчив мене людської мови(((")


bot.polling(none_stop=True, interval=1)