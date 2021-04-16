"""
    File created by steph
    Last update: 31.03.2021
"""

import my_tg_wrapper.tg_const as tg_const
import telebot
from my_encr import caesar, vernam, vigenere
import os

encr_bot = telebot.TeleBot(TOKEN)

caesar_shift_default = 14
vernam_key_default = 'b'
vigenere_key_default = 'c'


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
    decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="caesar_decode")
    encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="caesar_encode")
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
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        caesar.decode(message.text.split("\n"), output_file, caesar_shift_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

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
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        print(output_file)
        caesar.encode(message.text.split("\n"), output_file, caesar_shift_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

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
    decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="vernam_decode")
    encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="vernam_encode")
    menu_keyboard.add(decode_button, encode_button)
    encr_bot.send_message(call.message.chat.id, tg_const.MSG_CHOICE, reply_markup=menu_keyboard)


""" Vernam decode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vernam_decode")
def vernam_decode(call):
    raise InterruptedError

    # msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    # encr_bot.register_next_step_handler(msg, vernam_get_data_decode)


def vernam_get_data_decode(message):
    global vernam_key_default
    vernam_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vernam_finish_decode)


def vernam_finish_decode(message):
    global vernam_key_default
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        vernam.decode(message.text.split("\n"), output_file, vernam_key_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

        return
    elif message.content_type == "document":

        raise InterruptedError


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
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        vernam.encode(message.text.split("\n"), output_file, vernam_key_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

        return
    elif message.content_type == "document":

        raise InterruptedError


""" 
 Vigenere processing
"""


@encr_bot.callback_query_handler(func=lambda call: call.data == "vigenere")
def vigenere_menu(call):
    raise InterruptedError

    # menu_keyboard = telebot.types.InlineKeyboardMarkup()
    # menu_keyboard.row_width = 2
    # decode_button = telebot.types.InlineKeyboardButton(text="Зашифровать", callback_data="vigenere_decode")
    # encode_button = telebot.types.InlineKeyboardButton(text="Расшифровать", callback_data="vigenere_encode")
    # menu_keyboard.add(decode_button, encode_button)
    # encr_bot.send_message(call.message.chat.id, tg_const.MSG_CHOICE, reply_markup=menu_keyboard)


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
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        vigenere.decode(message.text.split("\n"), output_file, vigenere_key_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

        return
    elif message.content_type == "document":

        raise InterruptedError


""" Vernam encode """


@encr_bot.callback_query_handler(func=lambda call: call.data == "vigenere_encode")
def vigenere_encode(call):
    msg = encr_bot.send_message(call.message.chat.id, tg_const.MSG_VR_KEY)
    encr_bot.register_next_step_handler(msg, vigenere_get_data_encode)


def vigenere_get_data_encode(message):
    global vernam_key_default
    vernam_key_default = message.text
    msg = encr_bot.send_message(message.chat.id, tg_const.MSG_INVITE)
    encr_bot.register_next_step_handler(msg, vigenere_finish_encode)


def vigenere_finish_encode(message):
    global vigenere_key_default
    os.remove("tmp.tmp")
    if message.content_type == "text":
        output_file = open("tmp.tmp", "w")
        vigenere.encode(message.text.split("\n"), output_file, vigenere_key_default)
        output_file.close()
        output_file = open("tmp.tmp", "rb")
        encr_bot.send_message(message.chat.id, tg_const.MSG_CS_FINISH)
        encr_bot.send_document(message.chat.id, output_file)
        output_file.close()

        return
    elif message.content_type == "document":

        raise InterruptedError
