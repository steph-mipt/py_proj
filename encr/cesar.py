"""
    File created by steph
    Last update: 31.03.2021
"""


def shift_letter(letter, offset: int):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in upper_alphabet:
        letter = upper_alphabet[(upper_alphabet.index(letter) + offset) % len(upper_alphabet)]
    elif letter in lower_alphabet:
        letter = lower_alphabet[(lower_alphabet.index(letter) + offset) % len(lower_alphabet)]
    return letter


def encode(in_data, out_data, offset: int):
    for line in in_data:
        out_line = ''
        for symb in line:
            out_line += shift_letter(symb, offset)
        out_data.write(out_line + "\n")


def decode(in_data, out_data, offset: int):
    encode(in_data, out_data, -offset)
