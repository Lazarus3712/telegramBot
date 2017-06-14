import requests


class Bot:
    __URL = ""
    __token = ""

    def __init__(self, token):
        self.__token = token
        self.__URL = "https://api.telegram.org/bot" + token

    def get_token(self) -> str:
        return self.__token

    def get_updates(self) -> object:
        return requests.get(self.__URL + '/getUpdates').json()

    def get_last_message(self) -> dict:
        data = self.get_updates()
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        text = data["result"][-1]["message"]["text"]

        try:
            reply_to_message_text = data["result"][-1]["message"]["reply_to_message"]["text"]
            reply_to_message_id = data["result"][-1]["message"]["reply_to_message"]["chat"]["id"]

        except KeyError:
            reply_to_message_text = ""
            reply_to_message_id = ""

        return {"chat_id": chat_id, "text": text,
                "reply_to_message_text": reply_to_message_text, "reply_to_message_id": reply_to_message_id}

    def get_last_message_position(self) -> int:
        data = self.get_updates()
        message_id = data["result"][-1]["message"]["message_id"]
        return message_id

    def send_message(self, chat_id, text):
        requests.get(self.__URL + '/sendMessage?chat_id={0}&text={1}'.format(chat_id, text))
