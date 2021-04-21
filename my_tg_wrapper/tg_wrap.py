"""
    File created by steph
    Last update: 21.04.2021
"""

import my_tg_wrapper.tg_const as tg_const
import telebot
from my_encr import caesar, vernam, vigenere
import os
from my_tg_wrapper.hidden import TOKEN

encr_bot = telebot.TeleBot(TOKEN)

caesar_shift_default = 14
vernam_key_default = 'a'
vigenere_key_default = 'a'


@encr_bot.message_handler(commands=['start'])
def send_welcome(message):
    encr_bot.send_message(message.chat.id, tg_const.MSG_WELCOME_00)
    encr_bot.send_message(message.chat.id, tg_const.MSG_WELCOME_01)


@encr_bot.message_handler(commands=['help'])
def send_welcome(message):
    encr_bot.send_message(message.chat.id, tg_const.MSG_HELP)


@encr_bot.message_handler(commands=['menu'])
def send_welcome(message):
    menu_keyboard = telebot.types.InlineKeyboardMarkup()
    menu_keyboard.row_width = 3
    caesar_button = telebot.types.InlineKeyboardButton(text="Цезаря", callback_data="caesar")
    vernam_button = telebot.types.InlineKeyboardButton(text="Вернам", callback_data="vernam")
    vigenere_button = telebot.types.InlineKeyboardButton(text="Виженера", callback_data="vigenere")
    menu_keyboard.add(caesar_button, vernam_button, vigenere_button)
    encr_bot.send_message(message.chat.id, tg_const.MSG_MENU, reply_markup=menu_keyboard)


""" 
 Caesar processing
"""


@encr_bot.callback_query_handler(func=lambda call: call.data == "caesar")
def caesar_menu(call):
    menu_keyboard = telebot.types.InlineKeyboardMarkup()
    menu_keyboard.row_width = 2
    decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="caesar_encode")
    encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="caesar_decode")
    menu_keyboard.add(decode_button, encode_button)
    encr_bot.send_message(call.message.chat.id, tg_const.MSG_CHOICE, reply_markup=menu_keyboard)


""" Caesar decode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "caesar_decode")
def caesar_decode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_CS_SHIFT)
    encr_bot.register_next_step_handler(msg, caesar_get_data_decode)


def caesar_get_data_decode(message):
    global caesar_shift_default
    caesar_shift_default = int(message.text)
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, caesar_finish_decode)


def caesar_finish_decode(message):
    global caesar_shift_default
    if message.content_type == "text":
        out = caesar.decode(message.text.split("\n"), caesar_shift_default)
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_message(message.chat.id, out)

        return
    elif message.content_type == "document":

        raise InterruptedError


""" Caesar encode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "caesar_encode")
def caesar_encode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_CS_SHIFT)
    encr_bot.register_next_step_handler(msg, caesar_get_data_encode)


def caesar_get_data_encode(message):
    global caesar_shift_default
    caesar_shift_default = int(message.text)
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, caesar_finish_encode)


def caesar_finish_encode(message):
    global caesar_shift_default
    if message.content_type == "text":
        out = caesar.encode(message.text.split("\n"), caesar_shift_default)
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_message(message.chat.id, out)

        return
    elif message.content_type == "document":

        raise InterruptedError


""" 
 Vernam processing
"""


@encr_bot.callback_query_handler(func=lambda call: call.data == "vernam")
def vernam_menu(call):
    menu_keyboard = telebot.types.InlineKeyboardMarkup()
    menu_keyboard.row_width = 2
    decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="vernam_encode")
    encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="vernam_decode")
    menu_keyboard.add(decode_button, encode_button)
    encr_bot.send_message(call.message.chat.id, tg_const.MSG_CHOICE, reply_markup=menu_keyboard)


""" Vernam decode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vernam_decode")
def vernam_decode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    encr_bot.register_next_step_handler(msg, vernam_get_data_decode)


def vernam_get_data_decode(message):
    global vernam_key_default
    vernam_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vernam_finish_decode)


def vernam_finish_decode(message):
    global vernam_key_default
    if message.content_type == "text":
        raise InterruptedError
    elif message.content_type == "document":
        file = encr_bot.get_file(message.document.file_id)
        downloaded_file = encr_bot.download_file(file.file_path)

        print(downloaded_file)

        raise NotImplementedError

        # if len(message.text) != len(vernam_key_default):
        #     msg = encr_bot.send_message(message.chat.id, tg_const.MSG_LEN_NOT_EQ)
        #     encr_bot.register_next_step_handler(msg, vernam_finish_decode)
        #     return
        #
        # out = vernam.decode(message.text.split("\n"), vernam_key_default)
        # print(out)
        # encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        # encr_bot.send_message(message.chat.id, out)
        #
        # return


""" Vernam encode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vernam_encode")
def vernam_encode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    encr_bot.register_next_step_handler(msg, vernam_get_data_encode)


def vernam_get_data_encode(message):
    global vernam_key_default
    vernam_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vernam_finish_encode)


def vernam_finish_encode(message):
    global vernam_key_default
    if message.content_type == "text":
        if len(message.text) != len(vernam_key_default):
            msg = encr_bot.send_message(message.chat.id, tg_const.MSG_LEN_NOT_EQ)
            encr_bot.register_next_step_handler(msg, vernam_finish_encode)
            return

        out = vernam.encode(message.text.split("\n"), vernam_key_default)
        f = open("tmp.tmp", "wb")
        f.write(out)
        f.close()
        f = open("tmp.tmp", "rb")

        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, f)
        f.close()
        os.remove("tmp.tmp")

        return
    elif message.content_type == "document":

        raise InterruptedError


""" 
 Vigenere processing
"""


@encr_bot.callback_query_handler(func=lambda call: call.data == "vigenere")
def vigenere_menu(call):
    menu_keyboard = telebot.types.InlineKeyboardMarkup()
    menu_keyboard.row_width = 2
    decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="vigenere_encode")
    encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="vigenere_decode")
    menu_keyboard.add(decode_button, encode_button)
    encr_bot.send_message(call.message.chat.id, tg_const.MSG_CHOICE, reply_markup=menu_keyboard)


""" Vigenere decode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vigenere_decode")
def vigenere_decode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    encr_bot.register_next_step_handler(msg, vigenere_get_data_decode)


def vigenere_get_data_decode(message):
    global vigenere_key_default
    vigenere_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vigenere_finish_decode)


def vigenere_finish_decode(message):
    global vigenere_key_default
    if message.content_type == "text":
        if len(message.text) != len(vigenere_key_default):
            msg = encr_bot.send_message(message.chat.id, tg_const.MSG_LEN_NOT_EQ)
            encr_bot.register_next_step_handler(msg, vernam_finish_decode)
            return

        out = vigenere.decode(message.text.split("\n"), vigenere_key_default)
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_message(message.chat.id, out)

        return
    elif message.content_type == "document":

        raise InterruptedError


""" Vigenere encode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vigenere_encode")
def vigenere_encode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    encr_bot.register_next_step_handler(msg, vigenere_get_data_encode)


def vigenere_get_data_encode(message):
    global vigenere_key_default
    vigenere_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vigenere_finish_encode)


def vigenere_finish_encode(message):
    global vigenere_key_default
    if message.content_type == "text":
        if len(message.text) != len(vigenere_key_default):
            msg = encr_bot.send_message(message.chat.id, tg_const.MSG_LEN_NOT_EQ)
            encr_bot.register_next_step_handler(msg, vernam_finish_decode)
            return

        out = vigenere.encode(message.text.split("\n"), vigenere_key_default)
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_message(message.chat.id, str(out))

        return
    elif message.content_type == "document":

        raise InterruptedError
