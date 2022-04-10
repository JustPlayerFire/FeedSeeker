import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from data import db_session
from data.users import User


def main_botwork():
    def new_user(new_id, ev):
        current_event = ev
        user = User()
        user.id = new_id

        text = 'Кажется, я впервые тебя вижу! Укажи сперва ID группы, откуда ты хочешь находить посты.\n' \
               'Пример: ID группы https://vk.com/public212539965 будет 212539965 \n' \
               'Или воспользуйся сайтом https://regvk.com/id/'

        vk.messages.send(user_id=current_event.obj.message['from_id'],
                         message=text,
                         random_id=random.randint(0, 2 ** 64))

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                user.group_id = event.obj.message['text']

                text = 'Теперь укажи хэштеги, по которым я буду находить посты\n' \
                       'Пример: #dog #animals #nature #игры #новость'

                vk.messages.send(user_id=current_event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
                break

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                if all([word[0] == '#' for word in str(event.obj.message['text']).split()]):
                    user.hashtags = event.obj.message['text']
                    text = 'Отлично, теперь ты по желанию можешь ввести те хэштеги, по которым я буду ИГНОРИРОВАТЬ' \
                           ' определённые посты (даже если там нужные хэштеги)\n' \
                           'Пример: #dog #animals #nature #игры #новость\n' \
                           'Если не хочешь вводить, то скажи мне "нет"'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                else:
                    text = 'Кажется, ты неправильно ввёл хэштеги' \
                               'Вот пример, как надо ввести хэштеги: #dog #animals #nature #игры #новость' \
                               'Если не хочешь вводить, то скажи мне "нет"'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                if all([word[0] == '#' for word in str(event.obj.message['text']).split()]):
                    user.bad_hashtags = event.obj.message['text']
                    text = 'Хорошо, теперь ты можешь ввести время по которому я буду высылать посты' \
                           ' в формате ЧАСЫ:МИНУТЫ\n' \
                           'Пример: 12:00\n' \
                           'Если не хочешь вводить, то скажи мне "нет"'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                else:
                    text = 'Кажется, ты неправильно ввёл хэштеги' \
                           'Вот пример, как надо ввести хэштеги: #dog #animals #nature #игры #новость' \
                           'Если не хочешь вводить, то скажи мне "нет"'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.message['text'][1] == ':' or event.obj.message['text'][2] == ':':
                    user.period = event.obj.message['text']
                    text = f'Всё готово! Тебе лишь остаётся сказать мне "Покажи мне посты" или ждать {user.period}'
                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                    break

                else:
                    text = 'Кажется, ты неправильно ввёл время' \
                           'Вот пример, как надо ввести время: 12:00' \
                           'Если не хочешь вводить, то скажи мне "нет"'

                    vk.messages.send(user_id=current_event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
        db_sess.add(user)
        all_users.append(user.id)
        db_sess.commit()

    with open('secret.txt', 'r') as f:
        f = f.read().split()
        TOKEN = f[0]
        ID = f[1]

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
                if str(event.obj.message['text']).capitalize() == 'Покажи мне посты':
                    text = 'Пока что в разработке!'
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))
                elif str(event.obj.message['text']).capitalize() == 'Хэштеги':
                    hashtags = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        hashtags.append(user.hashtags)

                    text = 'Хэштеги, по которым я ищу посты: ' + ' '.join(hashtags)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                elif str(event.obj.message['text']).capitalize() == 'Плохие хэштеги':
                    hashtags = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        hashtags.append(user.bad_hashtags)

                    text = 'Хэштеги, по которым я игнорирую посты: ' + ' '.join(hashtags)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                elif str(event.obj.message['text']).capitalize() == 'Группы':
                    groups = []

                    for user in db_sess.query(User).filter(User.id == event.obj.message['from_id']):
                        groups.append(user.group_id)

                    text = 'ID групп, в которых я ищу посты: ' + ' '.join(groups)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main_botwork()