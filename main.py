import telebot
from Parse_VK import a
import keep_alive
import os

ACCESS_TOKEN = os.getenv('5274655524:AAEx8UjChU8eA9BRT11cUdDn_5D86rGvZHA')
bot = telebot.TeleBot(ACCESS_TOKEN)
keep_alive.keep_alive()

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('/start', '/help')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Привет, я твой помощник по поиску людей) . Пиши имя и фамилию!',
        reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, 'Метки для прочтения информации:')
    bot.send_message(
        message.from_user.id,
        'maiden_name: девичья фамилия; military:   unit (string) — номер части; unit_id — идентификатор части в базе данных; country_id — идентификатор страны, в которой находится часть;from — год начала службы; until — год окончания службы.'
    )
    bot.send_message(
        message.from_user.id,
        'military: unit (string) — номер части; unit_id — идентификатор части в базе данных; country_id — идентификатор страны, в которой находится часть;from — год начала службы; until — год окончания службы.'
    )
    bot.send_message(
        message.from_user.id,
        'occupation: информация о текущем роде занятия пользователя.  type — тип. Возможные значения: work — работа; school — среднее образование; university — высшее образование. id — идентификатор школы, вуза, сообщества компании (в которой пользователь работает); name — название школы, вуза или места работы'
    )
    bot.send_message(
        message.from_user.id,
        'last_seen: время последнего посещения. time — время последнего посещения в формате Unixtime. platform — тип платформы. Возможные значения: 1 — мобильная версия; 2 — приложение для iPhone; 3 — приложение для iPad; 4 — приложение для Android; 5 — приложение для Windows Phone; 6 — приложение для Windows 10; 7 — полная версия сайта.'
    )
    bot.send_message(
        message.from_user.id,
        'остальные поля мне лень описывать, думаю, вы поймете, что это за поля'
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if str(message.text[0:3]) == 'htt':
        try:
            bot.send_message(message.from_user.id, a.get_photos(message.text))
            bot.send_message(message.from_user.id,
                             a.get_information1(message.text))
        except:
            bot.send_message(
                message.from_user.id,
                'Мы не смогли найти о вас информацию: либо у вас закрытый аккаунт, либо про вас нет информации'
            )
        if a.get_information2(message.text) != [] and '' and None:
            bot.send_message(message.from_user.id,
                             a.get_information2(message.text))
    else:
        s = a.searching(message.text)
        print(message.text)
        bot.send_message(message.from_user.id, str(s[0]))
        bot.send_message(message.from_user.id, a.get_photos(str(s[0])))
        bot.send_message(message.from_user.id, a.get_information1((str(s[0]))))


bot.polling(none_stop=True)
