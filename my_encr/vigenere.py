"""
    File created by steph
    Last update: 21.04.2021
"""

import my_encr.utils as utils


def encode(in_data, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    out = ""
    for line in in_data:
        out_line = ''
        for symb in line:
            if symb.isalpha():
                symb = utils.shift_letter(symb, ord(key[key_pos]) - ord('A'))
                key_pos += 1
                key_pos %= key_len
            out_line += symb

        out += out_line + "\n"
    return out


def decode(in_data, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    out = ""
    for line in in_data:
        out_line = ''
        for symb in line:
            if symb.isalpha():
                symb = utils.shift_letter(symb, ord('A') - ord(key[key_pos]))
                key_pos = (key_pos + 1) % key_len
            out_line += symb
        out += out_line + "\n"
    return out
