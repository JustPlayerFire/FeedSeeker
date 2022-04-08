import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from data import db_session
from data.users import User


def main_botwork():

    with open('secret.txt', 'r') as f:
        f = f.read().split()
        TOKEN = f[0]
        ID = f[1]

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, ID)
    db_session.global_init("db/global.db")
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Проверка связи',
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main_botwork()