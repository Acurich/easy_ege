from telebot import types


def problems_keyboard():
    kb = types.InlineKeyboardMarkup()
    maths = types.InlineKeyboardButton(text='Математика', callback_data='problems/maths')
    rus = types.InlineKeyboardButton(text='Русский язык', callback_data='problems/rus')
    inf = types.InlineKeyboardButton(text='Информатика', callback_data='problems/inf')
    kb.add(maths, rus, inf)
    return kb


def tests_keyboard():
    kb = types.InlineKeyboardMarkup()
    maths = types.InlineKeyboardButton(text='Математика', callback_data='tests/maths')
    rus = types.InlineKeyboardButton(text='Русский язык', callback_data='tests/rus')
    inf = types.InlineKeyboardButton(text='Информатика', callback_data='tests/inf')
    kb.add(maths, rus, inf)
    return kb


def problems_math_keyboard():
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 19):
        keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f'maths/{i}'))
    kb.add(*keys)
    return kb


def problems_rus_keyboard():
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 27):
        keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f'rus/{i}'))
    kb.add(*keys)
    return kb


def problems_inf_keyboard():
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 19):
        keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f'inf/{i}'))
    keys.append(types.InlineKeyboardButton(text='19-21', callback_data=f'inf/192021'))
    for i in range(22, 28):
        keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f'inf/{i}'))
    kb.add(*keys)
    return kb


def tests_math_keyboard(test):
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 19):
        if test[str(i)][1]:
            keys.append(types.InlineKeyboardButton(text=str(i) + ' ✅', callback_data=f't/maths/{i}'))
        else:
            keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f't/maths/{i}'))
    keys.append(types.InlineKeyboardButton(text='Закончить тест', callback_data=f'end/maths'))
    kb.add(*keys)
    return kb


def tests_rus_keyboard(test):
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 27):
        if test[str(i)][1]:
            keys.append(types.InlineKeyboardButton(text=str(i) + ' ✅', callback_data=f't/rus/{i}'))
        else:
            keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f't/rus/{i}'))
    keys.append(types.InlineKeyboardButton(text='Закончить тест', callback_data=f'end/rus'))
    kb.add(*keys)
    return kb


def tests_inf_keyboard(test):
    kb = types.InlineKeyboardMarkup()
    keys = []
    for i in range(1, 19):
        if test[str(i)][1]:
            keys.append(types.InlineKeyboardButton(text=str(i) + ' ✅', callback_data=f't/inf/{i}'))
        else:
            keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f't/inf/{i}'))
    if test['192021'][1]:
        keys.append(types.InlineKeyboardButton(text='19-21' + ' ✅', callback_data=f't/inf/192021'))
    else:
        keys.append(types.InlineKeyboardButton(text='19-21', callback_data=f't/inf/192021'))
    for i in range(22, 28):
        if test[str(i)][1]:
            keys.append(types.InlineKeyboardButton(text=str(i) + ' ✅', callback_data=f't/inf/{i}'))
        else:
            keys.append(types.InlineKeyboardButton(text=str(i), callback_data=f't/inf/{i}'))
    keys.append(types.InlineKeyboardButton(text='Закончить тест', callback_data=f'end/inf'))
    kb.add(*keys)
    return kb


def again_keyboard(num):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Решить еще один номер того же типа', callback_data=f'{num}'))
    return kb


def privacy_keyboard(s):
    kb = types.InlineKeyboardMarkup()

    if s == 'private':
        s = 'Приватный'
    else:
        s = 'Публичный'

    key = types.InlineKeyboardButton(text='Статус профиля: ' + s, callback_data=f'private')
    key2 = types.InlineKeyboardButton(text='Чат с обсуждением', callback_data=f'chat')
    kb.add(key)
    kb.add(key2)
    return kb
