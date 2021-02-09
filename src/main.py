
import vk_api
from API_key import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
from pprint import pprint


# ILLO
def main():
    vk_session = vk_api.VkApi(token=my_token)
    longpoll = VkBotLongPoll(vk_session, group_id=my_group_id)
    vk = vk_session.get_api()
    print("start")
    for event in longpoll.listen():
        # print(event.type)
        # print(VkBotEventType.MESSAGE_NEW)
        if event.type == VkBotEventType.MESSAGE_NEW and isinstance(event.message["text"], str):
            if event.message["text"] == "s":
                if event.from_user:  # Если написали в ЛС
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message='Yes, sir!',
                        random_id=time.time()
                    )
                elif event.from_chat:  # Если написали в Беседе
                    vk.messages.send(  # Отправляем собщение
                        chat_id=event.chat_id,
                        message='Yes, sir!',
                        random_id=time.time()
                    )


if __name__ == "__main__":
    main()
