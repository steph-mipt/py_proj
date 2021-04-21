"""
    File created by steph
    Last update: 31.03.2021
"""

import my_encr.utils as utils


def encode(in_data, offset: int):
    out = ""
    for line in in_data:
        out_line = ''
        for symb in line:
            out_line += utils.shift_letter(symb, offset)
        out += out_line + "\n"
    return out


def decode(in_data, offset: int):
    return encode(in_data, -offset)


def hack(in_data):
    freq = utils.count_letters(in_data)
    e_index = freq.index(max(freq))
    offset = ord('e') - ord('a') - e_index
    return encode(in_data, offset)
