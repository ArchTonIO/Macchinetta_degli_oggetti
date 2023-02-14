"""
This module contains the TelegramBot class to send updates to the users.
"""
from threading import Thread
from time import sleep
import requests
from settings.telegram_token import TOKEN
from settings.bot_interactions import BOT_INTERACTIONS_DICT


class TelegramBot:
    """
    This class is used to send updates to the users, automatically or
    upon request.
    - Args:
        - token: the token of the bot.
        - max_messages_in_memory: the maximum number of received messages to be
        stored in memory.
    """
    def __init__(self, token: str = TOKEN):
        self.updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
        self.raw_dicts = []
        self.last_update = {}

    def async_look_for_updates(self) -> None:
        """
        This method starts a thread to look for updates.
        """
        looking_thread = Thread(target=self.__look_for_updates)
        looking_thread.start()

    def __look_for_updates(self) -> None:
        """
        This method looks for updates.
        """
        res = {}
        while True:
            sleep(1)
            updates_dict = (requests.get(self.updates_url, timeout=10).json())
            res = updates_dict["result"][-1]
            if res and res not in self.raw_dicts:
                chat_id = res["message"]["chat"]["id"]
                fristname = (
                    res["message"]["chat"]["first_name"]
                )
                lastname = (
                    res["message"]["chat"]["last_name"]
                )
                username = (
                    res["message"]["chat"]["username"]
                )
                text = res["message"]["text"]
                self.last_update = {
                        "chat_id": chat_id,
                        "fristname": fristname,
                        "lastname": lastname,
                        "username": username,
                        "text": text
                    }
                self.raw_dicts.append(res)
                self.__process_requests()

    def __process_requests(self) -> dict:
        """
        This method processes the requests saved in the updates_list.
        """
        try:
            msgs = BOT_INTERACTIONS_DICT[self.last_update["text"]]
            if self.last_update["text"] == "/start":
                msgs = BOT_INTERACTIONS_DICT["/start"].format(
                    name=self.last_update["fristname"]
                )
            if isinstance(msgs, str):
                self.__send_message(
                    chat_id=self.last_update["chat_id"],
                    message=msgs
                )
            elif isinstance(msgs, list):
                for msg in msgs:
                    self.__send_message(
                        chat_id=self.last_update["chat_id"],
                        message=msg
                    )
        except KeyError:
            self.__send_message(
                chat_id=self.last_update["chat_id"],
                message=(
                    "Comando non riconosciuto"
                    ", se lo implemento ti avviso!"
                )
            )

    def __send_message(self, chat_id: str, message: str) -> None:
        """
        This method sends a message to a specific user.
        - Args:
            - chat_id: the chat_id of the user.
            - message: the message to be sent.
        """
        url = (
            f"https://api.telegram.org/bot{TOKEN}/send"
            f"Message?chat_id={chat_id}&text={message}"
        )
        send = requests.get(url, timeout=10).json()
        del send
