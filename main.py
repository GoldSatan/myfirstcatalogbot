import config
import telebot
from telebot import types
import tests
import random
import shelve
import lib_url

# @myfirstcatalogbot

bot = telebot.TeleBot(config.TOKEN)


def fin(call):
    FILENAME = "URLs"
    data = str(call.data)
    print(data)
    with shelve.open(FILENAME) as states:
        url = states[data]
    cars = tests.parse(url)
    n = len(cars)
    car = cars[random.randint(0, n - 1)]

    title = car['title']
    link = car['link']
    usd_price = car['usd_price']
    ua_price = car['ua_price']

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Інший варіант із цієї категорії", callback_data=call.data)
    item2 = types.InlineKeyboardButton("Рандомний автомобіль 🎲", callback_data='class_random')
    markup.add(item1, item2)

    bot.send_message(call.message.chat.id,
                     text=f'Ось один із варіантів - {title}\n\nЦіна в долларах: {usd_price}  \n\nЦіна в гривнях: {ua_price}\n\n\nLink for car: {link}',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti_hello = open('static/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_hello)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🧐 Знайти автомобіль')

    markup.add(item1)

    bot.send_message(message.chat.id,
                     "Привіт, {0.first_name}!\nЯ ваш персональний - <b>{1.first_name}</b>. Давайте допоможу вам підібрати автомобіль.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def blablabla(message):
    if message.chat.type == 'private':
        if message.text == '🧐 Знайти автомобіль':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Для роботи 🚛")
            item2 = types.KeyboardButton("Для розваг 🏎")

            markup.add(item1, item2)
            markup.add(row_width=2)
            item3 = types.KeyboardButton("У меню ")
            markup.add(item3)

            bot.send_message(message.chat.id, "Для чого вам потрібен автомобіль?", parse_mode='html',
                             reply_markup=markup)

        if message.text == 'Для роботи 🚛':
            markup = types.InlineKeyboardMarkup(row_width=3)

            item1 = types.InlineKeyboardButton("Спецтехніка", callback_data='work_B')
            item2 = types.InlineKeyboardButton("Вантажний", callback_data='work_C')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Автомобіль якої категорії вас цікавить?", reply_markup=markup)

        if message.text == 'Для розваг 🏎':
            markup = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("Легкові", callback_data='FT_B')
            item2 = types.InlineKeyboardButton("Водний транспорт", callback_data='FT_water')
            item3 = types.InlineKeyboardButton("Мото", callback_data='FT_A')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Що саме вас цікавить?", reply_markup=markup)
        if message.text == 'У меню':
            welcome(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            if call.data == 'class_random':
                call.data = random.choice(lib_url.all_url_array)
                fin(call)
            """~~~~~~~~~new~~~~~~~~~~other~~~~~~~~~~~old~~~~~~~~~~~"""

            if call.data == 'work_B':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Вживаний", callback_data='work_B_old')
                item2 = types.InlineKeyboardButton("Новий", callback_data='work_B_new')
                item3 = types.InlineKeyboardButton("Під пригон", callback_data='work_B_other')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Який автомобіль вас цікавить?", reply_markup=markup)

            if call.data == 'work_C':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Вживаний", callback_data='work_C_old')
                item2 = types.InlineKeyboardButton("Новий", callback_data='work_C_new')
                item3 = types.InlineKeyboardButton("Під пригон", callback_data='work_C_other')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Який автомобіль вас цікавить?", reply_markup=markup)

            """~~~~~~~~~new~~~~~~~~~~other~~~~~~~~~~~old~~~~~~~~~~~"""

            if call.data == 'FT_B':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Вживаний", callback_data='FT_B_old')
                item2 = types.InlineKeyboardButton("Новий", callback_data='FT_B_new')
                item3 = types.InlineKeyboardButton("Під пригон", callback_data='FT_B_other')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Який автомобіль вас цікавить?", reply_markup=markup)

            if call.data == 'FT_A':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Вживаний", callback_data='FT_A_old')
                item2 = types.InlineKeyboardButton("Новий", callback_data='FT_A_new')
                item3 = types.InlineKeyboardButton("Під пригон", callback_data='FT_A_other')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Який автомобіль вас цікавить?", reply_markup=markup)

            if call.data == 'FT_water':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Вживаний", callback_data='FT_water_old')
                item2 = types.InlineKeyboardButton("Новий", callback_data='FT_water_new')
                item3 = types.InlineKeyboardButton("Під пригон", callback_data='FT_water_other')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Який автомобіль вас цікавить?", reply_markup=markup)

            """~~~~~~~~~~~~~~~~~~~price~~~~~~~~~~~~~~~~~~~~~~"""

            if call.data == 'FT_water_other':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_water_other_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_water_other_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_water_other_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_water_new':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_water_new_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_water_new_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_water_new_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_water_old':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_water_old_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_water_old_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_water_old_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)

            if call.data == 'FT_B_other':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_B_other_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_B_other_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_B_other_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_B_old':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_B_old_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_B_old_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_B_old_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_B_new':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_B_new_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_B_new_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_B_new_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)

            if call.data == 'FT_A_other':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_A_other_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_A_other_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_A_other_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_A_old':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_A_old_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_A_old_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_A_old_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'FT_A_new':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='FT_A_new_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='FT_A_new_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='FT_A_new_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)

            if call.data == 'work_C_other':
                markup = types.InlineKeyboardMarkup(row_width=2)

                # item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_C_other_cheap')
                # item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_C_other_expensive')

                # markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_C_other_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'work_C_old':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_C_old_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_C_old_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_C_old_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'work_C_new':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_C_new_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_C_new_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_C_new_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)

            if call.data == 'work_B_other':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_B_other_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_B_other_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_B_other_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'work_B_old':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_B_old_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_B_old_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_B_old_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)
            if call.data == 'work_B_new':
                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Від дешевих 💵  ", callback_data='work_B_new_cheap')
                item2 = types.InlineKeyboardButton("Від дорогих 💰  ", callback_data='work_B_new_expensive')

                markup.add(item1, item2)
                markup.add(row_width=1)
                item3 = types.InlineKeyboardButton("Звичайне ✔️", callback_data='work_B_new_normal')
                markup.add(item3)

                bot.send_message(call.message.chat.id, "Введіть сортування  ☺️",
                                 reply_markup=markup)

            if call.data == 'FT_water_other_cheap' or call.data == 'FT_water_other_expensive' or call.data == 'FT_water_other_normal' \
                    or call.data == 'FT_water_new_cheap' or call.data == 'FT_water_new_expensive' or call.data == 'FT_water_new_normal' \
                    or call.data == 'FT_water_old_cheap' or call.data == 'FT_water_old_expensive' or call.data == 'FT_water_old_normal' \
                    or call.data == 'FT_B_other_cheap' or call.data == 'FT_B_other_expensive' or call.data == 'FT_B_other_normal' \
                    or call.data == 'FT_B_old_cheap' or call.data == 'FT_B_old_expensive' or call.data == 'FT_B_old_normal' \
                    or call.data == 'FT_B_new_cheap' or call.data == 'FT_B_new_expensive' or call.data == 'FT_B_new_normal' \
                    or call.data == 'FT_A_other_cheap' or call.data == 'FT_A_other_expensive' or call.data == 'FT_A_other_normal' \
                    or call.data == 'FT_A_old_cheap' or call.data == 'FT_A_old_expensive' or call.data == 'FT_A_old_normal' \
                    or call.data == 'FT_A_new_cheap' or call.data == 'FT_A_new_expensive' or call.data == 'FT_A_new_normal' \
                    or call.data == 'work_C_other_normal' \
                    or call.data == 'work_C_old_cheap' or call.data == 'work_C_old_expensive' or call.data == 'work_C_old_normal' \
                    or call.data == 'work_C_new_cheap' or call.data == 'work_C_new_expensive' or call.data == 'work_C_new_normal' \
                    or call.data == 'work_B_other_cheap' or call.data == 'work_B_other_expensive' or call.data == 'work_B_other_normal' \
                    or call.data == 'work_B_old_cheap' or call.data == 'work_B_old_expensive' or call.data == 'work_B_old_normal' \
                    or call.data == 'work_B_new_cheap' or call.data == 'work_B_new_expensive' or call.data == 'work_B_new_normal':
                fin(call)

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Підбераємо автомобіль.. ")

        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="",
                              reply_markup=None)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
