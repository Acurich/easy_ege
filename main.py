import telebot
from telebot import types
import requests
from keyboards import *
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import json
matplotlib.use('Agg')

bot = telebot.TeleBot('6041032587:AAGW_Kozz084zCyvQHhLuy05qYz0VStUJWg')
with open('users.json') as f:
    users = json.load(f)# храним ответы на текущую задачу каждого пользователя


list_help = {'maths/1': 'https://www.youtube.com/watch?v=9McWvYvMOL0',
              'maths/2': 'https://www.youtube.com/watch?v=BJn1iOYfmfQ',
              'maths/3': 'https://www.youtube.com/watch?v=kbFdCKzWP5I',
              'maths/4': 'https://www.youtube.com/watch?v=kbFdCKzWP5I',
              'maths/5': 'https://www.youtube.com/watch?v=SyHA55ct4g0',
              'maths/6': 'https://www.youtube.com/watch?v=QJt16SXHfy0',
              'maths/7': 'https://www.youtube.com/watch?v=68v9uQwfrzg',
              'maths/8': 'https://www.youtube.com/watch?v=vI44OJYPOFo',
              'maths/9': 'https://www.youtube.com/watch?v=1mSl2PqWWHo',
              'maths/10': 'https://www.youtube.com/watch?v=f6kftWyhD0w',
              'maths/11': 'https://www.youtube.com/watch?v=qHKEcOJ_Z3U',
             'rus/1': 'https://rustutors.ru/egeteoriya/1134-zadanie-1.html',
             'rus/2': 'https://rustutors.ru/egeteoriya/1136-zadanie-2.html',
             'rus/3': 'https://rustutors.ru/egeteoriya/1135-zadanie-3.html',
             'rus/4': 'https://rustutors.ru/egeteoriya/1137-zadanie-4.html',
             'rus/5': 'https://rustutors.ru/egeteoriya/1138-zadanie-5.html',
             'rus/6': 'https://rustutors.ru/egeteoriya/1139-zadanie-6.html',
             'rus/7': 'https://rustutors.ru/egeteoriya/1140-zadanie-7.html',
             'rus/8': 'https://rustutors.ru/egeteoriya/1141-zadanie-8.html',
             'rus/9': 'https://rustutors.ru/egeteoriya/1142-zadanie-9.html',
             'rus/10': 'https://rustutors.ru/egeteoriya/1143-zadanie-10.html',
             'rus/11': 'https://rustutors.ru/egeteoriya/1144-zadanie-11.html',
             'rus/12': 'https://rustutors.ru/egeteoriya/1145-zadanie-12.html',
             'rus/13': 'https://rustutors.ru/egeteoriya/1146-zadanie-13.html',
             'rus/14': 'https://rustutors.ru/egeteoriya/1148-zadanie-14.html',
             'rus/15': 'https://rustutors.ru/egeteoriya/1147-zadanie-15.html',
             'rus/16': 'https://rustutors.ru/egeteoriya/1149-zadanie-16.html',
             'rus/17': 'https://rustutors.ru/egeteoriya/1150-zadanie-17.html',
             'rus/18': 'https://rustutors.ru/egeteoriya/1152-zadanie-18.html',
             'rus/19': 'https://rustutors.ru/egeteoriya/1151-zadanie-19.html',
             'rus/20': 'https://rustutors.ru/egeteoriya/1153-zadanie-20.html',
             'rus/21': 'https://rustutors.ru/egeteoriya/1154-zadanie-21.html',
             'rus/22': 'https://rustutors.ru/egeteoriya/1156-zadanie-22.html',
             'rus/23': 'https://rustutors.ru/egeteoriya/1155-zadanie-23.html',
             'rus/24': 'https://rustutors.ru/egeteoriya/1157-zadanie-24.html',
             'rus/25': 'https://rustutors.ru/egeteoriya/1158-zadanie-25.html',
             'rus/26': 'https://rustutors.ru/egeteoriya/1159-zadanie-26.html',
             'inf/1': 'https://www.youtube.com/watch?v=GV-zY20wJjg',
             'inf/2': 'https://www.youtube.com/watch?v=C3Et-oZ0j94',
             'inf/3': 'https://www.youtube.com/watch?v=UUxUc7oDHSY',
             'inf/4': 'https://www.youtube.com/watch?v=dvh5Dqtak84',
             'inf/5': 'https://www.youtube.com/watch?v=Y6tMd9rwJpw',
             'inf/6': 'https://www.youtube.com/watch?v=P1URZzdGvWk',
             'inf/7': 'https://www.youtube.com/watch?v=N_PM40gtDFQ',
             'inf/8': 'https://www.youtube.com/watch?v=DM6bE_QZBnU',
             'inf/9': 'https://www.youtube.com/watch?v=zxAjdeIQT74',
             'inf/10': 'https://www.youtube.com/watch?v=ZEsZ9ykEfjM',
             'inf/11': 'https://www.youtube.com/watch?v=hB4gPk_oakw',
             'inf/12': 'https://www.youtube.com/watch?v=kLAEaxh5yXY',
             'inf/13': 'https://www.youtube.com/watch?v=OWzy0mIkFgg',
             'inf/14': 'https://www.youtube.com/watch?v=wYEe2jog-q4',
             'inf/15': 'https://www.youtube.com/watch?v=F0MaFc73S9E',
             'inf/16': 'https://www.youtube.com/watch?v=iZbUtN9xB-Q',
             'inf/17': 'https://www.youtube.com/watch?v=2uUSrOPVQfg',
             'inf/18': 'https://www.youtube.com/watch?v=ZUwE_qB8o-I',
             'inf/192021': 'https://www.youtube.com/watch?v=h1rcEJHADb0',
             'inf/22': 'https://www.youtube.com/watch?v=KJJOESYkHVc',
             'inf/23': 'https://www.youtube.com/watch?v=xri6r4BYJoE',
             'inf/24': 'https://www.youtube.com/watch?v=ghFBQekGx3g',
             'inf/25': 'https://www.youtube.com/watch?v=qwuQOcthMGA',
             'inf/26': 'https://www.youtube.com/watch?v=UDir215idrw',
             'inf/27': 'https://www.youtube.com/watch?v=SB_ilJl3LaQ',
             }


def save():
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)


def replace_every_second(string, old, new):
    parts = string.split(old)
    counter = 0
    res = ''
    for i in parts[:-1]:
        if counter % 2 == 0:
            res += i + old
        else:
            res += i + new
        counter += 1
    return res + parts[-1]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"Чтобы воспользоваться ботом, открой меню в левом нижнем углу экрана, либо напечатай одну из следующих команд: \n\n <b> /problems </b> — выбрать конкретное задание для тренировки \n\n <b> /tests </b> — прорешать целый вариант ЕГЭ \n\n <b> /profile </b> — узнать личную статистику \n\n <b> /help </b> — помощь", parse_mode='html')


@bot.message_handler(commands=['start'])  # обработка первой интеракции с ботом
def start(message):
    try:  # получаем пользователя по его Telegram username
        user = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/users/find/{message.chat.username}').json()
    except:  # или создаем, если в базе данных его еще нет
        user = requests.post('http://ege-scrapper-bot.na4u.ru/api/users', json={
          "tg_id": message.chat.username,
          "name": message.chat.first_name,
          "surname": message.chat.last_name,
          "score": 0,
          "maths": [0, 0, 0],
          "rus": [0, 0, 0],
          "inf": [0, 0, 0],
            "latest": 0,
            "priv": "public"
        }, headers={'content-type': 'application/json'}).json()
    if user['tg_id'] not in list(users.keys()):
        users[user['tg_id']] = {'profile': user, 'ans': None, 'sub': None, 'test': {}, "profile_msg": []}
        bot.send_message(message.chat.id, f'Привет, {user["name"]}!\nЭтот бот поможет тебе подготовиться к ЕГЭ: потренировать отдельные задания или прорешать варианты целиком. Открой меню в левом нижнем углу экрана, либо воспользуйся командой <b>/help</b>', parse_mode='html')
        save()



@bot.message_handler(commands=['problems'])  # выбор предмета для решения отдельных задач
def problems(message):
    if message.chat.username not in list(users.keys()):
        start(message)
    bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=problems_keyboard())
    save()


@bot.message_handler(commands=['tests'])
def tests(message):
    if message.chat.username not in list(users.keys()):
        start(message)
    bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=tests_keyboard())
    save()


@bot.callback_query_handler(func=lambda call: True)  # обрабатываем нажатия всех Inline кнопок
def problems_query(call):
    if call.message.chat.username not in list(users.keys()):
        start(call.message)
    if call.data == 'problems/maths':  # проверяем, из какого предмета пользователь хочет порешать задания
        bot.send_message(call.message.chat.id,'Примечание: телеграм неидеально отображает LaTeX. Учтите, что: frac - дробь ({1}/{2}). log_a{b}, a - основание, b - ф-ия. Индексы пишутся через нижнее подчеркивание (A_1, x_0)')
        bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=problems_math_keyboard())
    if call.data == 'problems/rus':
        bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=problems_rus_keyboard())
    if call.data == 'problems/inf':
        bot.send_message(call.message.chat.id, 'Примечание: если ответ содержит несколько чисел, разделяйте их пробелами')
        bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=problems_inf_keyboard())

    if call.data == 'tests/inf':
        if users[call.message.chat.username]['test'] == {}:
            bot.send_message(call.message.chat.id,'Примечание: если ответ содержит несколько чисел, разделяйте их пробелами')
            users[call.message.chat.username]['test'] = {}
            users[call.message.chat.username]['test']['sub'] = 'inf'
            print(users)
            for i in range(1, 19):
                task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/inf/find/{i}').json())
                users[call.message.chat.username]['test'][str(i)] = [task['id'], [], task['answer']]
            print(users)
            task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/inf/find/{192021}').json())
            users[call.message.chat.username]['test']['192021'] = [task['id'], [], task['answer']]
            print(users)
            for i in range(22, 28):
                print(i)
                task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/inf/find/{i}').json())
                users[call.message.chat.username]['test'][str(i)] = [task['id'], [], task['answer']]
            print(users)
            users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=tests_inf_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []
        else:
            bot.send_message(call.message.chat.id, 'У вас уже есть незаконченный тест!')
            if users[call.message.chat.username]['test']['sub'] == 'inf':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_inf_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'maths':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_math_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'rus':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_rus_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []
    if 'tests/rus' in call.data:
        if users[call.message.chat.username]['test'] == {}:
            users[call.message.chat.username]['test'] = {}
            users[call.message.chat.username]['test']['sub'] = 'rus'
            all_texts = requests.get('http://ege-scrapper-bot.na4u.ru/api/text').json()
            rng_text = random.choice(all_texts)
            if rng_text['id'] % 2 == 0:
                small_text = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/text/{rng_text["id"] - 1}').json()
                big_text = rng_text
            else:
                small_text = rng_text
                big_text = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/text/{rng_text["id"] + 1}').json()
            first_tasks = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/rus/text/{small_text["id"]}').json()
            last_tasks = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/rus/text/{big_text["id"]}').json()
            for i in first_tasks:
                users[call.message.chat.username]['test'][str(i["task_type"])] = [i["id"], [], i["answer"]]
            for i in range(4, 22):
                task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/rus/find/{i}').json())
                users[call.message.chat.username]['test'][str(i)] = [task['id'], [], task['answer']]
            for i in last_tasks:
                users[call.message.chat.username]['test'][str(i["task_type"])] = [i["id"], [], i["answer"]]
            users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=tests_rus_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []
        else:
            bot.send_message(call.message.chat.id, 'У вас уже есть незаконченный тест!')
            if users[call.message.chat.username]['test']['sub'] == 'inf':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_inf_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'maths':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_math_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'rus':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_rus_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []

    if 'tests/math' in call.data:
        if users[call.message.chat.username]['test'] == {}:
            bot.send_message(call.message.chat.id,
                             'Примечание: телеграм неидеально отображает LaTeX. Учтите, что: frac - дробь ({1}/{2}). log_a{b}, a - основание, b - ф-ия. Индексы пишутся через нижнее подчеркивание (A_1, x_0)')

            users[call.message.chat.username]['test'] = {}
            users[call.message.chat.username]['test']['sub'] = 'maths'
            for i in range(1, 19):
                task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/maths/find/{i}').json())
                users[call.message.chat.username]['test'][str(task["task_type"])] = [task["id"], [], task["answer"]]
            users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание', reply_markup=tests_math_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []
        else:
            bot.send_message(call.message.chat.id, 'У вас уже есть незаконченный тест!')
            if users[call.message.chat.username]['test']['sub'] == 'inf':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_inf_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'maths':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_math_keyboard(users[call.message.chat.username]['test'])).message_id
            if users[call.message.chat.username]['test']['sub'] == 'rus':
                users[call.message.chat.username]['test_msg'] = bot.send_message(call.message.chat.id, 'Выбери задание',reply_markup=tests_rus_keyboard(users[call.message.chat.username]['test'])).message_id
            users[call.message.chat.username]['test']['messages'] = []

    if call.data == 'end/inf':
        bot.delete_message(chat_id=call.message.chat.id, message_id=users[call.message.chat.username]['test_msg'])
        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []
        messages = ''
        for i in list(users[call.message.chat.username]['test'].keys()):
            test = users[call.message.chat.username]['test'][i]
            if i != 'sub' and i != 'messages' and i != 'curr':
                if i == '25':
                    if sorted(test[1]) == sorted(test[2]):
                        messages += f'№{i} ✅. Ваш ответ: {" ".join(test[1])}\n'
                        users[call.message.chat.username]['profile']['inf'][0] += 1
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = users[call.message.chat.username]['profile'][
                                                                               'score'] + 1
                    else:
                        messages += f'№{i} ❌. Ваш ответ: {" ".join(test[1])} Правильный ответ: {" ".join(test[2])}\n'
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = users[call.message.chat.username]['profile'][
                                                                               'score'] - 1
                elif i != '192021':
                    if test[1] == test[2]:
                        messages += f'№{i} ✅. Ваш ответ: {" ".join(test[1])}\n'
                        users[call.message.chat.username]['profile']['inf'][0] += 1
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = users[call.message.chat.username]['profile'][
                                                                               'score'] + 1
                    else:
                        messages += f'№{i} ❌. Ваш ответ: {" ".join(test[1])} Правильный ответ: {" ".join(test[2])}\n'
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = users[call.message.chat.username]['profile'][
                                                                               'score'] - 1
                else:
                    ans = test[2]
                    del ans[ans.index('1)')]
                    del ans[ans.index('2)')]
                    del ans[ans.index('3)')]
                    if test[1] == ans:
                        messages += f'№19-21 ✅. Ваш ответ: {" ".join(test[1])}\n'
                        users[call.message.chat.username]['profile']['inf'][0] += 1
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = \
                        users[call.message.chat.username]['profile'][
                            'score'] + 1
                    else:
                        messages += f'№19-21 ❌. Ваш ответ: {" ".join(test[1])} Правильный ответ: {" ".join(ans)}\n'
                        users[call.message.chat.username]['profile']['inf'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = \
                        users[call.message.chat.username]['profile']['score'] - 1
        messages += f'Новый рейтинг: {users[call.message.chat.username]["profile"]["score"]}'
        bot.send_message(chat_id=call.message.chat.id, text=messages)
        users[call.message.chat.username]['test'] = {}
        requests.put(f'http://ege-scrapper-bot.na4u.ru/api/users', json=users[call.message.chat.username]['profile'],
                     headers={'content-type': 'application/json'})

    if 'end/rus' in call.data:
        bot.delete_message(chat_id=call.message.chat.id, message_id=users[call.message.chat.username]['test_msg'])
        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []
        messages = ''
        for i in list(users[call.message.chat.username]['test'].keys()):
            test = users[call.message.chat.username]['test'][i]
            if i != 'sub' and i != 'messages' and i != 'curr':
                if test[1] == test[2]:
                    messages += f'№{i} ✅. Ваш ответ: {" ".join(test[1])}\n'
                    users[call.message.chat.username]['profile']['rus'][0] += 1
                    users[call.message.chat.username]['profile']['rus'][1] += 1
                    users[call.message.chat.username]['profile']['score'] = \
                    users[call.message.chat.username]['profile'][
                        'score'] + 1
                else:
                    messages += f'№{i} ❌. Ваш ответ: {" ".join(test[1])} Правильный ответ: {" ".join(test[2])}\n'
                    users[call.message.chat.username]['profile']['rus'][1] += 1
                    users[call.message.chat.username]['profile']['score'] = \
                    users[call.message.chat.username]['profile'][
                        'score'] - 1
        messages += f'Новый рейтинг: {users[call.message.chat.username]["profile"]["score"]}'
        bot.send_message(chat_id=call.message.chat.id, text=messages)
        users[call.message.chat.username]['test'] = {}
        requests.put(f'http://ege-scrapper-bot.na4u.ru/api/users', json=users[call.message.chat.username]['profile'],
                     headers={'content-type': 'application/json'})

    if 'end/maths' in call.data:
        bot.delete_message(chat_id=call.message.chat.id, message_id=users[call.message.chat.username]['test_msg'])
        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []
        messages = ''
        for i in list(users[call.message.chat.username]['test'].keys()):
            test = users[call.message.chat.username]['test'][i]
            if i != 'sub' and i != 'messages' and i != 'curr':
                if int(i) < 12:
                    if test[1] == test[2]:
                        messages += f'№{i} ✅. Ваш ответ: {" ".join(test[1])}\n'
                        users[call.message.chat.username]['profile']['maths'][0] += 1
                        users[call.message.chat.username]['profile']['maths'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = \
                        users[call.message.chat.username]['profile'][
                            'score'] + 1
                    else:
                        messages += f'№{i} ❌. Ваш ответ: {" ".join(test[1])} Правильный ответ: {" ".join(test[2])}\n'
                        users[call.message.chat.username]['profile']['maths'][1] += 1
                        users[call.message.chat.username]['profile']['score'] = \
                        users[call.message.chat.username]['profile'][
                            'score'] - 1
                else:
                    messages += f'№{i} Правильный ответ: {" ".join(test[2])}\n'
        messages += f'Новый рейтинг: {users[call.message.chat.username]["profile"]["score"]}'
        bot.send_message(chat_id=call.message.chat.id, text=messages)
        users[call.message.chat.username]['test'] = {}
        requests.put(f'http://ege-scrapper-bot.na4u.ru/api/users', json=users[call.message.chat.username]['profile'], headers={'content-type': 'application/json'})

    if 'maths/' in call.data and 't/maths' not in call.data:  # тут пользователь выбрал задание в одном из трех предметов
        num = int(call.data.lstrip('maths/'))
        users[call.message.chat.username]['latest'] = call.data
        task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/maths/find/{num}').json())
        bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, task['task'][0])
        try:
            bot.send_photo(call.message.chat.id,  task['task_img'][0])
        except:
            pass
        users[call.message.chat.username]['ans'] = [task['answer'][0].lstrip('Ответ: ').rstrip('.')]  # сохраняем в отдельный словарь текущий правильный ответ для каждого пользователя
        users[call.message.chat.username]['sub'] = 'maths'
        if num > 11:
            users[call.message.chat.username]['ans'][0] += 'no'
        print(users[call.message.chat.username])
    if 'rus/' in call.data and 't/rus' not in call.data:  # аналогично еще два раза
        num = int(call.data.lstrip('rus/'))
        users[call.message.chat.username]['latest'] = call.data
        task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/rus/find/{num}').json())
        if task['text'] != "0":
            text1 = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/text/{task["text"]}').json()['text'].replace('**', '*') + '\n\n'
            bot.send_message(call.message.chat.id, f'{text1}', parse_mode='markdown')

        task['task'][0] = replace_every_second(task['task'][0], '**', '</b>')
        task['task'][0] = task['task'][0].replace('**', '<b>')
        print(task['task'][0])
        bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b> \n\n {task["task"][0]}', parse_mode='html')
        users[call.message.chat.username]['ans'] = [task['answer'][0].rstrip('.')]
        print([task['answer'][0].rstrip('.')])
        users[call.message.chat.username]['sub'] = 'rus'
    if 'inf/' in call.data and 't/inf' not in call.data:
        num = int(call.data.lstrip('inf/'))
        users[call.message.chat.username]['latest'] = call.data
        task = random.choice(requests.get(f'http://ege-scrapper-bot.na4u.ru/api/inf/find/{num}').json())
        bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, '\n'.join(task['task']))
        if task['task_img']:
            if task['task_img'][0][-1] == 'f':
                # print(task['task_img'])
                bot.send_photo(call.message.chat.id, task['task_img'][0])
            else:
                bot.send_message(call.message.chat.id, '\n'.join(task['task_img']))
        if num == 192021:
            ans = task['answer']
            del ans[ans.index('1)')]
            del ans[ans.index('2)')]
            del ans[ans.index('3)')]
            users[call.message.chat.username]['ans'] = ans
            users[call.message.chat.username]['sub'] = 'inf'
        else:
            users[call.message.chat.username]['ans'] = task['answer']
            users[call.message.chat.username]['sub'] = 'inf'
        print(users[call.message.chat.username])
    if 't/inf' in call.data:

        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []

        task = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/inf/{users[call.message.chat.username]["test"][str(call.data.lstrip("t/inf"))][0]}').json()
        users[call.message.chat.username]['test']['messages'] = []
        print(task)
        users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b>',
                         parse_mode='html').message_id)
        users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, '\n'.join(task['task'])).message_id)
        users[call.message.chat.username]['test']['curr'] = task['task_type']
        print(users)
        if task['task_img']:
            if task['task_img'][0][-1] == 'f':
                # print(task['task_img'])
                users[call.message.chat.username]['test']['messages'].append(bot.send_photo(call.message.chat.id, task['task_img'][0]).message_id)
            else:
                users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, '\n'.join(task['task_img'])).message_id)
        if users[call.message.chat.username]['test'][str(users[call.message.chat.username]['test']['curr'])][1]:
            users[call.message.chat.username]['test']['messages'].append(bot.send_message(chat_id=call.message.chat.id, text=f'<b>Ваш ответ: {"".join(users[call.message.chat.username]["test"][users[call.message.chat.username]["test"]["curr"]][1])}</b>', parse_mode='html').message_id)
    if 't/rus' in call.data:
        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []

        task = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/rus/{users[call.message.chat.username]["test"][str(call.data.lstrip("t/rus"))][0]}').json()
        users[call.message.chat.username]['test']['messages'] = []
        users[call.message.chat.username]['test']['curr'] = task['task_type']
        if task['text'] != "0":
            text1 = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/text/{task["text"]}').json()['text'].replace('**', '*') + '\n\n'
            users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, f'{text1}', parse_mode='markdown').message_id)

        task['task'][0] = replace_every_second(task['task'][0], '**', '</b>')
        task['task'][0] = task['task'][0].replace('**', '<b>')
        users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b> \n\n {task["task"][0]}', parse_mode='html').message_id)
        if users[call.message.chat.username]['test'][str(users[call.message.chat.username]['test']['curr'])][1]:
            users[call.message.chat.username]['test']['messages'].append(bot.send_message(chat_id=call.message.chat.id, text=f'<b>Ваш ответ: {"".join(users[call.message.chat.username]["test"][str(users[call.message.chat.username]["test"]["curr"])][1])}</b>', parse_mode='html').message_id)
    if 't/maths' in call.data:
        for i in users[call.message.chat.username]['test']['messages']:
            bot.delete_message(chat_id=call.message.chat.id, message_id=i)
        users[call.message.chat.username]['test']['messages'] = []
        task = requests.get(f'http://ege-scrapper-bot.na4u.ru/api/maths/{users[call.message.chat.username]["test"][str(call.data.lstrip("t/maths"))][0]}').json()
        users[call.message.chat.username]['test']['messages'] = []
        users[call.message.chat.username]['test']['curr'] = task['task_type']
        users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, f'<a>Задание №{task["task_id"]}</a>\n<b>Тип {task["task_type"]}</b>',parse_mode='html').message_id)
        users[call.message.chat.username]['test']['messages'].append(bot.send_message(call.message.chat.id, task['task'][0]).message_id)
        try:
            users[call.message.chat.username]['test']['messages'].append(bot.send_photo(call.message.chat.id,  task['task_img'][0]).message_id)
        except:
            pass
        if users[call.message.chat.username]['test'][str(users[call.message.chat.username]['test']['curr'])][1]:
            users[call.message.chat.username]['test']['messages'].append(bot.send_message(chat_id=call.message.chat.id, text=f'<b>Ваш ответ: {"".join(users[call.message.chat.username]["test"][str(users[call.message.chat.username]["test"]["curr"])][1])}</b>', parse_mode='html').message_id)

    if 'private' in call.data:
        if users[call.message.chat.username]['profile']['priv'] == 'private':
            users[call.message.chat.username]['profile']['priv'] = 'public'
            dop_msg = 'Теперь ваш профиль <b>публичный</b>. Это значит, что теперь все видят ваше имя пользователя, если вы в топе рейтинга'
        else:
            users[call.message.chat.username]['profile']['priv'] = 'private'
            dop_msg = 'Теперь ваш профиль <b>приватный</b>. Это значит, что теперь все видят ваше имя пользователя, если вы в топе рейтинга'
        save()
        requests.put(f'http://ege-scrapper-bot.na4u.ru/api/users', json=users[call.message.chat.username]['profile'], headers={'content-type': 'application/json'})
        profile(call.message, dop_msg=dop_msg)

    if 'chat' in call.data:
        if len(users[call.message.chat.username]['profile_msg']) != 3:
            # bot.delete_message(chat_id=call.message.chat.id, message_id=users[call.message.chat.username]['profile_msg'][-1])
            users[call.message.chat.username]['profile_msg'].append(bot.send_message(call.message.chat.id, '<b>⭐️ПРИСОЕДИНЯЙСЯ В НАШУ ГРУППУ!</b>\n\nв этих группах вы сможете обсудить задания ЕГЭ из бота, задавать вопросы и познакомится с единомышленниками!\n\n🪄волшебная ссылочка: https://t.me/ege_easy_talk\n\np.s. в группе работают модераторы, не употребляйте ненормативную  лексику и будьте добры к другу другу!', parse_mode='html').message_id)

    save()


@bot.message_handler(commands=['profile'])  # выводим статистику пользователя
def profile(message, dop_msg=None):

    if message.chat.username not in list(users.keys()):
        start(message)

    for i in users[message.chat.username]['profile_msg']:
        bot.delete_message(chat_id=message.chat.id, message_id=i)
    users[message.chat.username]['profile_msg'] = []

    if users[message.chat.username]['profile']['maths'][1] != 0:  # проверяем на деление на 0 :DDD
        msg = 'правильный ответ'
        if int(users[message.chat.username]['profile']['maths'][0]) in [2, 3, 4]:
            msg = 'правильных ответа'
        if int(users[message.chat.username]['profile']['maths'][0]) > 4 or int(users[message.chat.username]['profile']['maths'][0]) == 0:
            msg = 'правильных ответов'
        maths = f"{users[message.chat.username]['profile']['maths'][0]} {msg} ({(users[message.chat.username]['profile']['maths'][0] * 100 // users[message.chat.username]['profile']['maths'][1])}%)"
    else:
        maths = f"Не приступал"
    if users[message.chat.username]['profile']['rus'][1] != 0:
        msg = 'правильный ответ'
        if int(users[message.chat.username]['profile']['rus'][0]) in [2, 3, 4] :
            msg = 'правильных ответа'
        if int(users[message.chat.username]['profile']['rus'][0]) > 4 or int(users[message.chat.username]['profile']['rus'][0]) == 0:
            msg = 'правильных ответов'
        rus = f"{users[message.chat.username]['profile']['rus'][0]} {msg} ({(users[message.chat.username]['profile']['rus'][0] * 100 // users[message.chat.username]['profile']['rus'][1])}%)"
    else:
        rus = f"Не приступал"
    if users[message.chat.username]['profile']['inf'][1] != 0:
        msg = 'правильный ответ'
        if int(users[message.chat.username]['profile']['inf'][0]) in [2, 3, 4]:
            msg = 'правильных ответа'
        if int(users[message.chat.username]['profile']['inf'][0]) > 4 or int(users[message.chat.username]['profile']['inf'][0]) == 0:
            msg = 'правильных ответов'
        inf = f"{users[message.chat.username]['profile']['inf'][0]} {msg} ({(users[message.chat.username]['profile']['inf'][0] * 100 // users[message.chat.username]['profile']['inf'][1 ])}%)"
    else:
        inf = f"Не приступал"
    all_users = requests.get('http://ege-scrapper-bot.na4u.ru/api/users').json()  # лидерборд
    all_users.sort(key=lambda x: int(x['score']), reverse=True)
    print(all_users, users[message.chat.username]['profile'])
    index = all_users.index(users[message.chat.username]['profile']) + 1
    msg = 'Топ 5 по рейтингу:\n'
    for i in range(len(all_users[:5])):
        if all_users[i]['priv'] == 'public':
            msg += f'#{i + 1} @{all_users[i]["tg_id"]} — {all_users[i]["score"]}'
        if all_users[i]['priv'] == 'private':
            if all_users[i]["surname"]:
                msg += f'#{i + 1} {all_users[i]["name"]} {all_users[i]["surname"]} — {all_users[i]["score"]}'
            else:
                msg += f'#{i + 1} {all_users[i]["name"]} — {all_users[i]["score"]}'
        if i == index - 1:
            msg = '<b>' + msg + '</b>'
        msg += '\n'
    if index > 5:
        msg += f'...\n<b>#{index} @{users[message.chat.username]["profile"]["tg_id"]} — {users[message.chat.username]["profile"]["score"]}</b>\n'


    try:
        val1 = users[message.chat.username]['profile']['maths'][2:]
        val2 = users[message.chat.username]['profile']['rus'][2:]
        val3 = users[message.chat.username]['profile']['inf'][2:]
        time = range(0, len(val1))

        plt.plot(time, val1, label='Математика')
        plt.plot(time, val2, label='Русский')
        plt.plot(time, val3, label='Информатика')

        plt.xlabel('Время')
        plt.ylabel('Рейтинг')
        plt.title('Диаграмма изменения рейтинга каждого предмета')

        plt.legend()
        plt.savefig('rating.png')
        plt.clf()
        users[message.chat.username]['profile_msg'].append(bot.send_photo(message.chat.id, open('rating.png', 'rb')).message_id)
    except Exception as e:
        print(e)

    users[message.chat.username]['profile_msg'].append(bot.send_message(message.chat.id, f"  <b>{users[message.chat.username]['profile']['name']} {users[message.chat.username]['profile']['surname']}</b>🧑‍🎓 \n\n{msg}\n <b>Математика:</b> {maths} \n\n <b>Русский язык:</b> {rus} \n\n <b>Информатика:</b> {inf}", parse_mode='html', reply_markup=privacy_keyboard(users[message.chat.username]['profile']['priv'])).message_id)
    if dop_msg is not None:
        users[message.chat.username]['profile_msg'].append(bot.send_message(message.chat.id, dop_msg, parse_mode='html').message_id)

    save()


@bot.message_handler()  # анализ сообщений общего характера
def text(message):
    if message.chat.username not in list(users.keys()):
        start(message)
    if message.chat.username in list(users.keys()):  # ответы на задания принимаются без команды, поэтому анализируются здесь. Для этого и храним в отдельном словаре ответы.
        if users[message.chat.username]['ans']:
            answer_sorted = users[message.chat.username]['ans']
            msg_sorted = message.text.split()
            if 'inf/25' in users[message.chat.username]['latest']:
                answer_sorted = sorted(users[message.chat.username]['ans'])
                msg_sorted = sorted(message.text.split())
                print(msg_sorted, answer_sorted)
            if users[message.chat.username] == {}:
                pass
            elif 'no' in users[message.chat.username]['ans'][0]:
                bot.send_message(message.chat.id, f'✅ Правильный ответ: {" ".join(users[message.chat.username]["ans"]).rstrip("n o")}')
            elif ''.join(message.text.split()).lower().split() == users[message.chat.username]['ans'] or answer_sorted == msg_sorted:
                print(users)
                if users[message.chat.username]['sub'] == 'maths':
                    users[message.chat.username]['profile']['maths'][0] += 1
                    users[message.chat.username]['profile']['maths'][1] += 1
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1] + 1)
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1])
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1])
                if users[message.chat.username]['sub'] == 'rus':
                    users[message.chat.username]['profile']['rus'][0] += 1
                    users[message.chat.username]['profile']['rus'][1] += 1
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1] + 1)
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1])
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1])
                if users[message.chat.username]['sub'] == 'inf':
                    users[message.chat.username]['profile']['inf'][0] += 1
                    users[message.chat.username]['profile']['inf'][1] += 1
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1] + 1)
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1])
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1])

                users[message.chat.username]['profile']['score'] = users[message.chat.username]['profile']['score'] + 1
                bot.send_message(message.chat.id, f'✅ Правильный ответ! Новый рейтинг: {users[message.chat.username]["profile"]["score"]}')
            else:
                if users[message.chat.username]['sub'] == 'maths':
                    users[message.chat.username]['profile']['maths'][1] += 1
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1] - 1)
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1])
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1])
                if users[message.chat.username]['sub'] == 'rus':
                    users[message.chat.username]['profile']['rus'][1] += 1
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1] - 1)
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1])
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1])
                if users[message.chat.username]['sub'] == 'inf':
                    users[message.chat.username]['profile']['inf'][1] += 1
                    users[message.chat.username]['profile']['inf'].append(users[message.chat.username]['profile']['inf'][-1] - 1)
                    users[message.chat.username]['profile']['maths'].append(users[message.chat.username]['profile']['maths'][-1])
                    users[message.chat.username]['profile']['rus'].append(users[message.chat.username]['profile']['rus'][-1])

                users[message.chat.username]['profile']['score'] = users[message.chat.username]['profile']['score'] - 1
                bot.send_message(message.chat.id, f'❌ Неверно! Правильный ответ: {" ".join(users[message.chat.username]["ans"])} \n\n Справочные материалы по заданию: {list_help[users[message.chat.username]["latest"]]} \n\nНовый рейтинг: {users[message.chat.username]["profile"]["score"]}', reply_markup=again_keyboard(users[message.chat.username]['latest']))
            users[message.chat.username]['ans'] = []
            users[message.chat.username]['sub'] = []
            requests.put(f'http://ege-scrapper-bot.na4u.ru/api/users', json=users[message.chat.username]['profile'], headers={'content-type': 'application/json'})
        elif users[message.chat.username]['test'] != {}:
            if message.text == 'Завершить тест':
                pass
            else:
                if users[message.chat.username]['test']['sub'] == 'inf':
                    users[message.chat.username]['test'][str(users[message.chat.username]['test']['curr'])][1] = message.text.split()
                    bot.edit_message_text(chat_id=message.chat.id ,message_id=users[message.chat.username]['test_msg'], text='Выбери задание', reply_markup=tests_inf_keyboard(users[message.chat.username]['test']))
                    print(users[message.chat.username]['test']['messages'])
                    for i in users[message.chat.username]['test']['messages']:
                        bot.delete_message(chat_id=message.chat.id, message_id=i)
                    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
                    users[message.chat.username]['test']['messages'] = []
                if users[message.chat.username]['test']['sub'] == 'rus':
                    users[message.chat.username]['test'][str(users[message.chat.username]['test']['curr'])][1] = [''.join(message.text.split())]
                    try:
                        bot.edit_message_text(chat_id=message.chat.id ,message_id=users[message.chat.username]['test_msg'], text='Выбери задание', reply_markup=tests_rus_keyboard(users[message.chat.username]['test']))
                    except:
                        pass
                    for i in users[message.chat.username]['test']['messages']:
                        bot.delete_message(chat_id=message.chat.id, message_id=i)
                    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
                    users[message.chat.username]['test']['messages'] = []
                if users[message.chat.username]['test']['sub'] == 'maths':
                    users[message.chat.username]['test'][str(users[message.chat.username]['test']['curr'])][1] = message.text.split()
                    try:
                        bot.edit_message_text(chat_id=message.chat.id ,message_id=users[message.chat.username]['test_msg'], text='Выбери задание', reply_markup=tests_math_keyboard(users[message.chat.username]['test']))
                    except:
                        pass
                    print(users[message.chat.username]['test']['messages'])
                    for i in users[message.chat.username]['test']['messages']:
                        bot.delete_message(chat_id=message.chat.id, message_id=i)
                    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
                    users[message.chat.username]['test']['messages'] = []
        else:
            bot.send_message(chat_id=message.chat.id, text='Извините, я не понимаю. Используйте /help для получения инструкции')
    save()




bot.polling(none_stop=True)
