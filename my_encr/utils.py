"""
    File created by steph
    Last update: 16.04.2021
"""


def shift_letter(letter, offset: int):
    lower_alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    upper_alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if letter in upper_alphabet_eng:
        letter = upper_alphabet_eng[(upper_alphabet_eng.index(letter) + offset) % len(upper_alphabet_eng)]
    elif letter in lower_alphabet_eng:
        letter = lower_alphabet_eng[(lower_alphabet_eng.index(letter) + offset) % len(lower_alphabet_eng)]
    elif letter in upper_alphabet_ru:
        letter = upper_alphabet_ru[(upper_alphabet_ru.index(letter) + offset) % len(upper_alphabet_ru)]
    elif letter in lower_alphabet_ru:
        letter = lower_alphabet_ru[(lower_alphabet_ru.index(letter) + offset) % len(lower_alphabet_ru)]

    return letter


def count_letters(in_data):
    lower_alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    upper_alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    count = [0] * len(lower_alphabet_eng)
    for line in in_data:
        for letter in line:
            if letter in lower_alphabet_eng or letter in upper_alphabet_eng:
                count[ord(letter.lower()) - ord(lower_alphabet_eng[0])] += 1
            elif letter in lower_alphabet_ru or letter in upper_alphabet_ru:
                count[ord(letter.lower()) - ord(lower_alphabet_ru[0])] += 1
    return count
