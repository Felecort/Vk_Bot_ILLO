
from generator_sentences import *
from API_key import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time
import json


def base_update(new_data, peer_id):
    pass


# ILLO
def main():
    vk_session = vk_api.VkApi(token=my_token)
    longpoll = VkBotLongPoll(vk_session, group_id=my_group_id)
    vk = vk_session.get_api()
    print("start")
    for event in longpoll.listen():
        # pprint(event.chat_id + 2000000000)  # ID беседы
        # pprint(event.message)               # Информация о сообщении
        print(event.message.text)          # Текст сообщения

        # print(event.type)
        # print(VkBotEventType.MESSAGE_NEW)
        if event.type == VkBotEventType.MESSAGE_NEW and isinstance(event.message["text"], str):

            if event.message["text"] == "s":
                if event.from_chat:  # Если написали в Беседе
                    vk.messages.send(  # Отправляем собщение
                        chat_id=event.chat_id,
                        message='♂Yes, sir♂!',
                        random_id=time.time()
                    )
                # elif event.from_user:     # Если написали в ЛС
                #     pass


if __name__ == "__main__":
    main()
