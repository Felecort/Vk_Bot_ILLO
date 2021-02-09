
import vk_api
import time
# from vk_api.longpoll import VkLongPoll, VkEventType
# from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from pprint import pprint


# ILLO
def main():
    vk_session = vk_api.VkApi(token="d9f3390ee15fb487125b4f7f5cba5e077e8aecd2b021b0d6fc37355028b12b2bf04c6d5fd4cd13e85c9c2")
    longpoll = VkBotLongPoll(vk_session, group_id=202461859)
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
