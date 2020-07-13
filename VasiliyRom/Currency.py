import requests
from bs4 import BeautifulSoup
import telebot
import datetime
from telebot import types

now = datetime.datetime.now()

URL = 'https://rulya-bank.com.ua/'
URL_COVID = 'https://covid19.gov.ua/'
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


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Курс")
    button2 = types.KeyboardButton("Covid-19")
    markup.add(button1, button2)

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
        bot.send_message(message.chat.id, final_mess, parse_mode='html')
    except:
        final_mess = 'Error'
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

bot.polling(none_stop=True)
