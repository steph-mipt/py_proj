"""
    File created by steph
    Last update: 16.04.2021
"""


def shift_letter(letter, offset: int):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in upper_alphabet:
        letter = upper_alphabet[(upper_alphabet.index(letter) + offset) % len(upper_alphabet)]
    elif letter in lower_alphabet:
        letter = lower_alphabet[(lower_alphabet.index(letter) + offset) % len(lower_alphabet)]
    return letter


def count_letters(in_data):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = [0] * len(lower_alphabet)
    for line in in_data:
        for letter in line:
            if letter in lower_alphabet or letter in upper_alphabet:
                count[ord(letter.lower()) - ord(lower_alphabet[0])] += 1
    return count
