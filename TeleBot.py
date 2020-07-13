# -*- coding: utf-8 -*-
#
import requests
from bs4 import BeautifulSoup
import telebot
import datetime
from telebot import types

now = datetime.datetime.now()

URL = 'https://rulya-bank.com.ua/'
URL_COVID = 'https://covid19.gov.ua/'
url_weather = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
bot = telebot.TeleBot('1365895387:AAEX_wESm_0LxqCjexX1QTR8EGuTzGfODx8')

def get_covid19():
    full_page = requests.get(URL_COVID, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convent = soup.findAll('div', {"class": "one-field light-box info-count", "class": "field-value"})
    test = ("Протестовано: " + convent[1].text.strip())
    patients = ("Хворих: " + convent[2].text.strip())
    recovered = ("Одужало: " + convent[3].text.strip())
    lethal = ("Летальних випадків: " + convent[4].text.strip())
    time_info = (convent[5].text.strip().split('\n')[0])

    return test, patients, recovered, lethal, time_info


def get_currency():
    full_page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convent = soup.findAll('td', {"class": "tbl", "class": "tbl", "align": "center"})
    buy_usd = ("Купівля: " + convent[0].text)
    sell_usd = ("Продаж: " + convent[1].text)
    buy_eur = ("Купівля: " + convent[2].text)
    sell_eur = ("Продаж: " + convent[3].text)

    return buy_usd, sell_usd, buy_eur, sell_eur


def get_weather():
    full_page = requests.get(url_weather, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convent_temp_today = soup.findAll('div', {"class": "main"})[0].text.strip().split('    ')
    convent_title_today = soup.findAll('div', {"class": "weatherIco"})[0]["title"]
    info_day_light = soup.findAll('div', {"class": "lSide", "class": "infoDaylight"})[0].text
    today = ("Сьогодні " + convent_temp_today[0]), convent_temp_today[1], convent_title_today, info_day_light

    convent_temp_tomorrow = soup.findAll('div', {"class": "main"})[1].text.strip().split('    ')
    convent_title_tomorrow = soup.findAll('div', {"class": "weatherIco"})[1]["title"]
    tomorrow = ("Завтра " + convent_temp_tomorrow[0]), convent_temp_tomorrow[1], convent_title_tomorrow

    convent_temp_tomorrow1 = soup.findAll('div', {"class": "main"})[2].text.strip().split('    ')
    convent_title_tomorrow1 = soup.findAll('div', {"class": "weatherIco"})[2]["title"]
    tomorrow_next = ("Післязавтра " + convent_temp_tomorrow1[0]), convent_temp_tomorrow1[1], convent_title_tomorrow

    return today, tomorrow, tomorrow_next


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Курс")
    button2 = types.KeyboardButton("Covid-19")
    button3 = types.KeyboardButton("Погода сьогодні")
    button4 = types.KeyboardButton("Погода завтра")
    button5 = types.KeyboardButton("Погода на 3 дня")
    markup.add(button1, button2, button3, button4, button5)

    send_mess = f"<b>Привіт {message.from_user.first_name}!</b>"
    print(send_mess)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    try:
        get_mess_bot = message.text.strip().lower()
        if get_mess_bot == 'курс':
            final_mess = (f"<b>Rulya Kurs\n{now.strftime('%d-%m-%Y %H:%M:%S')}\n\nUSD\n{get_currency()[0]}\n{get_currency()[1]}" \
                          f"\n\nEUR\n{get_currency()[2]}\n{get_currency()[3]}</b>")
        elif get_mess_bot == 'covid-19':
            final_mess = f"<b>Офіційна статистика Covid-19 в Україні\n{get_covid19()[4]}\n\n{get_covid19()[0]}\n" \
                         f"{get_covid19()[1]}\n{get_covid19()[2]}\n{get_covid19()[3]}</b>"
        elif get_mess_bot == 'погода сьогодні':
            final_mess = f"<b>Sinoptik.ua\n{get_weather()[0][0]}\n{get_weather()[0][1]}\n{get_weather()[0][2]}\n{get_weather()[0][3]}</b>"
        elif get_mess_bot == 'погода завтра':
            final_mess = f"<b>Sinoptik.ua\n{get_weather()[1][0]}\n{get_weather()[1][1]}\n{get_weather()[1][2]}</b>"
        elif get_mess_bot == 'погода на 3 дня':
            final_mess = f"<b>Sinoptik.ua\n{get_weather()[0][0]}\n{get_weather()[0][1]}\n{get_weather()[0][2]}\n\n" \
                         f"{get_weather()[1][0]}\n{get_weather()[1][1]}\n{get_weather()[1][2]}\n\n{get_weather()[2][0]}\n" \
                         f"{get_weather()[2][1]}\n{get_weather()[2][2]}</b>"

        bot.send_message(message.chat.id, final_mess, parse_mode='html')
    except:
        final_mess = '<b>Error</b>'
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

bot.polling(none_stop=True)









