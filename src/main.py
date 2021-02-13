
from generator_sentences import *
from handler_database import *
from API_key import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time


# ILLO
def main():
    data = get_database()
    vk_session = vk_api.VkApi(token=my_token)
    longpoll = VkBotLongPoll(vk_session, group_id=my_group_id)
    vk = vk_session.get_api()
    print("start")
    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW and\
                    isinstance(event.message["text"], str) and\
                    event.message["from_id"] > 0:
                if str(event.chat_id) not in data:
                    data[str(event.chat_id)] = {
                        "config": {
                            "chance": 20,
                            "min": 5,
                            "max": 20
                        },
                        "markov_chains": {}
                    }
                    set_database(data)
                if len(event.message["text"].split(" ")) >= 2:
                    data = add_to_dict(event.message["text"], data, str(event.chat_id))
                if event.message["text"] == "gen":
                    message = generate_message(data, str(event.chat_id))
                    if event.from_chat:  # Если написали в Беседе
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            message=message,
                            random_id=time.time()
                        )
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
