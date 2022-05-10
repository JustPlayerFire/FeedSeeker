import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from data import db_session
from data.users import User
from requests import get


def main_botwork():
    def add_groups(ev):
        current_event = ev
        text = 'Введи ID групп через пробел, которые ты хочешь добавить\n' \
               'Пример: ID группы https://vk.com/public212539965 будет public212539965\n' \
               'Если ты передумал, то скажи мне "Нет".'
        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))

        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if str(event.obj.message['text']).capitalize() == 'Нет':
                    text = 'Как хочешь...'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'NONE'
                else:
                    text = 'Группы добавлены!'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return event.obj.message['text']

    def delete_groups(ev):
        current_event = ev
        text = 'Введи группы, которые ты хочешь удалить.\n' \
               'Пример: ID группы https://vk.com/public212539965 будет public212539965\n' \
               'Если ты хочешь убрать все, то скажи мне "Все".\n' \
               'Если ты передумал, то скажи мне "Нет".'
        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if str(event.obj.message['text']).capitalize() == 'Нет':
                    text = 'Как хочешь...'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'NONE'

                elif str(event.obj.message['text']).capitalize() == 'Все':
                    text = 'Все группы удалены'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'ALL'
                else:
                    text = 'Группы удалены!'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return event.obj.message['text']

    def add_hashtags(ev):
        current_event = ev
        text = 'Введи плохие хештеги, которые ты хочешь добавить\n' \
               'Пример: #dog #animals #nature #игры #новость\n' \
               'Если ты передумал, то скажи мне "Нет".'
        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if all([word[0] == '#' for word in str(event.obj.message['text']).split()]):
                    text = 'Плохие хештеги добавлены!'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return event.obj.message['text']

                elif str(event.obj.message['text']).capitalize() == 'Нет':
                    text = 'Как хочешь...'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'NONE'
                else:
                    text = 'Кажется, ты неправильно ввёл хештеги\n' \
                           'Вот пример, как надо ввести хэштеги: #dog #animals #nature #игры #новость\n' \
                           'Если ты передумал, то скажи мне "Нет".'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

    def delete_hashtags(ev):
        current_event = ev
        text = 'Введи плохие хештеги, которые ты хочешь удалить.\n' \
               'Пример: #dog #animals #nature #игры #новость.\n' \
               'Если ты хочешь убрать все, то скажи мне "Все".\n' \
               'Если ты передумал, то скажи мне "Нет".'
        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if all([word[0] == '#' for word in str(event.obj.message['text']).split()]):
                    text = 'Плохие хештеги удалены!'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return event.obj.message['text']

                elif str(event.obj.message['text']).capitalize() == 'Нет':
                    text = 'Как хочешь...'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'NONE'

                elif str(event.obj.message['text']).capitalize() == 'Все':
                    text = 'Все плохие хештеги удалены'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    return 'ALL'

                else:
                    text = 'Кажется, ты неправильно ввёл хештеги\n' \
                           'Вот пример, как надо ввести хэштеги: #dog #animals #nature #игры #новость\n' \
                           'Если не хочешь вводить, то скажи мне "нет"'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

    def new_user(new_id, ev):
        current_event = ev
        user = User()
        user.id = new_id

        text = 'Кажется, я впервые тебя вижу! Укажи сперва ID групп через пробел, откуда ты хочешь находить посты.\n' \
               'Пример: ID группы https://vk.com/public212539965 будет public212539965'

        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                if all(str(word).isascii() for word in event.obj.message['text'].split()):
                    user.group_id = event.obj.message['text']

                    text = 'Отлично, теперь ты по желанию можешь ввести те хештеги, по которым я буду ИГНОРИРОВАТЬ' \
                           ' определённые посты (даже если там нужные хештеги)\n' \
                           'Пример: #dog #animals #nature #игры #новость\n' \
                           'Если не хочешь вводить, то скажи мне "нет"'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                else:
                    text = 'Ты неправильно ввёл группы.\nПример: ID группы https://vk.com/public212539965 будет public212539965'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

        print('BAD HASHTAG')

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                if all([word[0] == '#' for word in str(event.obj.message['text']).split()]):
                    user.bad_hashtags = event.obj.message['text']
                    text = f'Всё готово! Тебе лишь остаётся написать мне необходимые хештеги и кол-во постов, ' \
                           f'которые нужно найти'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                elif event.obj.message['text'].capitalize() == 'Нет':
                    text = f'Всё готово! Тебе лишь остаётся написать мне необходимые хештеги и кол-во постов,' \
                           f' которые нужно найти'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                else:
                    text = 'Кажется, ты неправильно ввёл хештеги\n' \
                           'Вот пример, как надо ввести хештеги: #dog #animals #nature #игры #новость\n' \
                           'Если не хочешь вводить, то скажи мне "нет"'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

        db_sess.add(user)
        all_users.append(user.id)
        db_sess.commit()

    with open('secret.txt', 'r', encoding='utf-8') as f:
        f = f.read().split()
        TOKEN = f[0]
        ID = f[1]
        ACC_TOKEN = f[2]

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, ID)
    db_session.global_init("db/global.db")

    db_sess = db_session.create_session()

    all_users = []
    for user in db_sess.query(User).all():
        all_users.append(user.id)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.obj.message['from_id'] not in all_users:
                new_user(event.obj.message['from_id'], event)
                print('New user! ' + str(event.obj.message['from_id']))
            else:
                inp = str(event.obj.message['text']).split()
                if all(word[0] == '#' for word in inp[:len(inp) - 1]) and inp[-1].isnumeric() and 0 < int(inp[-1]) <= 40:
                    groups = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        groups.append(user.group_id)
                        bad_hashtags = user.bad_hashtags
                    try:
                        bad_hashtags = bad_hashtags.split()
                        if any(inp[k] in bad_hashtags for k in range(len(inp))):
                            text = 'Один из хештегов, который ты ввёл, есть в списке плохих хештегов!'
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=text,
                                             random_id=random.randint(0, 2 ** 64))
                            continue
                    except AttributeError:
                        pass
                    group_name = ' '.join(groups).split()
                    for i in range(len(group_name)):
                        params = {
                            'count': inp[-1],
                            'domain': group_name[i],
                            'query': inp[:len(inp) - 1],
                            'access_token': ACC_TOKEN,
                            'v': '5.103'
                        }

                        site = f'https://api.vk.com/method/wall.search?'
                        request = get(site, params=params).json()
                        try:
                            if request['error']:
                                text = f'Группы {group_name[i]} не существует!'
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=text,
                                                 random_id=random.randint(0, 2 ** 64))
                                continue
                        except KeyError:
                            pass

                        if len(request['response']['items']) <= 0:
                            text = f'Нету постов из группы {group_name[i]} по запросу: ' \
                                   f'{" ".join(inp[:len(inp) - 1])}.'

                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=text,
                                             random_id=random.randint(0, 2 ** 64))
                            continue
                        for k in range(len(request['response']['items'])):
                            try:
                                if any([bad_hashtags[p] in request['response']['items'][k]['text'] for p in
                                        range(len(bad_hashtags))]):
                                    text = f'В посте номер {str(k + 1)} из группы {group_name[i]} замечен ' \
                                           f'плохой хештег!'

                                    vk.messages.send(user_id=event.obj.message['from_id'],
                                                     message=text,
                                                     random_id=random.randint(0, 2 ** 64))
                                    continue
                            except TypeError:
                                pass
                            att = f"wall{request['response']['items'][k]['from_id']}_{request['response']['items'][k]['id']}"
                            text = f'Пост номер {str(k + 1)} из группы {group_name[i]} по запросу: ' \
                                   f'{" ".join(inp[:len(inp) - 1])}.'

                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=text,
                                             attachment=att,
                                             random_id=random.randint(0, 2 ** 64))

                elif str(event.obj.message['text']).capitalize() == 'Плохие хештеги':
                    hashtags = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        hashtags.append(user.bad_hashtags)

                    text = 'Хэштеги, по которым я игнорирую посты: ' + ' '.join(hashtags)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                elif str(event.obj.message['text']).capitalize() == 'Добавить плохие хештеги':
                    user = User()
                    user.id = event.obj.message['from_id']
                    hashtags = ''

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        hashtags += user.bad_hashtags

                    text = 'Хэштеги, по которым я игнорирую посты: ' + hashtags
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                    result = add_hashtags(event)
                    if result == 'NONE':
                        continue
                    hashtags += ' ' + result
                    user.bad_hashtags = hashtags
                    db_sess.add(user)
                    db_sess.commit()

                elif str(event.obj.message['text']).capitalize() == 'Удалить плохие хештеги':
                    user = User()
                    user.id = event.obj.message['from_id']
                    hashtags = ''

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        hashtags += user.bad_hashtags

                    text = 'Хэштеги, по которым я игнорирую посты: ' + ' '.join(hashtags)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                    result = set(delete_hashtags(event).split())
                    if result == 'NONE':
                        continue
                    elif result == 'ALL':
                        user.bad_hashtags = ''
                        db_sess.add(user)
                        db_sess.commit()
                        continue

                    user.bad_hashtags = ' '.join(list(set(hashtags.split()) - set(result)))
                    db_sess.add(user)
                    db_sess.commit()

                elif str(event.obj.message['text']).capitalize() == 'Группы':
                    groups = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        groups.append(user.group_id)

                    text = 'Группы, в которых я ищу посты: ' + ' '.join(groups)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                elif str(event.obj.message['text']).capitalize() == 'Добавить группы':
                    user = User()
                    user.id = event.obj.message['from_id']
                    groups = ''

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        groups += user.group_id

                    text = 'Группы, в которых я ищу посты: ' + groups
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                    result = add_groups(event)
                    if result == 'NONE':
                        continue
                    groups += ' ' + result
                    user.group_id = groups
                    db_sess.add(user)
                    db_sess.commit()

                elif str(event.obj.message['text']).capitalize() == 'Удалить группы':
                    user = User()
                    user.id = event.obj.message['from_id']
                    groups = ''

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        groups += user.group_id

                    text = 'Группы, в которых я ищу посты: ' + groups
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                    result = delete_groups(event)
                    if result == 'NONE':
                        continue
                    elif result == 'ALL':
                        user.group_id = ''
                        db_sess.add(user)
                        db_sess.commit()
                        continue

                    user.group_id = ' '.join(list(set(groups.split()) - set(result.split())))
                    db_sess.add(user)
                    db_sess.commit()

                elif str(event.obj.message['text']).capitalize() == 'Помощь':
                    text = 'Я могу помочь тебе вывести посты с определенных групп с введенными хештегами.\n' \
                           'Доступные команды: \n' \
                           '* "(Хештеги через пробел) (число)" - я покажу тебе определенное число постов с введёнными '\
                           'хештегами (Пример: #Игры #Видео 5)\n' \
                           '* "Плохие хештеги" - вывод хештегов, по которым я игнорирую посты\n' \
                           '* "Группы" - вывод групп, с которых я собираю посты\n' \
                           '* "Добавить плохие хештеги" - добавление плохих хештегов к их общему списку\n' \
                           '* "Добавить группы" - добавление групп к их общему списку\n' \
                           '* "Удалить плохие хештеги" - удаление выбранных плохих хештегов с их списка\n' \
                           '* "Удалить группы" - удаление групп с их списка\n' \

                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    text = 'Я тебя не понял. Чтобы узнать, какие команды я понимаю, набери "Помощь".'
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main_botwork()