"""
This module contains the TelegramBot class to send updates to the users.
"""
from threading import Thread
from time import sleep
import json
import requests
from settings.telegram_token import TOKEN

with open("settings/bot_interactions.json", encoding="UTF-8") as f:
    BOT_INTERACTIONS_DICT = json.load(f)

with open("version.json", encoding="UTF-8") as f:
    version = json.load(f)


class TelegramBot:
    """
    This class is used to send updates to the users, automatically or
    upon request.
    - Args:
        - token: the token of the bot.
        - max_messages_in_memory: the maximum number of received messages to be
        stored in memory.
    """
    token = TOKEN
    updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
    raw_dicts = []
    last_update = {}

    @staticmethod
    def async_look_for_updates() -> None:
        """
        This method starts a thread to look for updates.
        """
        looking_thread = Thread(target=TelegramBot.__look_for_updates)
        looking_thread.start()

    @staticmethod
    def __look_for_updates() -> None:
        """
        This method looks for updates.
        """
        updates_dict = {}
        while True:
            sleep(1)
            updates_dict = (requests.get(
                TelegramBot.updates_url, timeout=10
            ).json())
            try:
                res = updates_dict["result"][-1]
            except IndexError:
                continue
            if res and res not in TelegramBot.raw_dicts:
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
                TelegramBot.last_update = {
                        "chat_id": chat_id,
                        "fristname": fristname,
                        "lastname": lastname,
                        "username": username,
                        "text": text
                    }
                TelegramBot.raw_dicts.append(res)
                TelegramBot.__process_requests()

    @staticmethod
    def __process_requests() -> dict:
        """
        This method processes the requests saved in the updates_list.
        """
        try:
            msgs = BOT_INTERACTIONS_DICT[TelegramBot.last_update["text"]]
            if TelegramBot.last_update["text"] == "/start":
                msgs = BOT_INTERACTIONS_DICT["/start"].format(
                    version=version["version"],
                    name=TelegramBot.last_update["fristname"]
                )
            if TelegramBot.last_update["text"] == "/about":
                msgs = BOT_INTERACTIONS_DICT["/about"].format(
                    version=version["version"]
                )
            if isinstance(msgs, str) or msgs[0] == "one_msg":
                if msgs[0] == "one_msg":
                    msgs = str().join(msgs[1:])
                TelegramBot.__send_message(
                    chat_id=TelegramBot.last_update["chat_id"],
                    message=msgs
                )
            elif isinstance(msgs, list):
                for msg in msgs:
                    TelegramBot.__send_message(
                        chat_id=TelegramBot.last_update["chat_id"],
                        message=msg
                    )
        except KeyError:
            TelegramBot.__send_message(
                chat_id=TelegramBot.last_update["chat_id"],
                message=(
                    "Comando non riconosciuto"
                )
            )

    @staticmethod
    def __send_message(chat_id: str, message: str) -> None:
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
        requests.get(url, timeout=10).json()
