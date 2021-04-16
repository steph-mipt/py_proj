"""
    File created by steph
    Last update: 31.03.2021
"""

import my_encr.utils as utils


def encode(in_data, out_data, offset: int):
    for line in in_data:
        out_line = ''
        for symb in line:
            out_line += utils.shift_letter(symb, offset)
        out_data.write(out_line + "\n")
    print("\n\n")
    print(out_data)
    print("\n\n")


def decode(in_data, out_data, offset: int):
    encode(in_data, out_data, -offset)


def hack(in_data, out_data):
    freq = utils.count_letters(in_data)
    e_index = freq.index(max(freq))
    offset = ord('e') - ord('a') - e_index
    encode(in_data, out_data, offset)
