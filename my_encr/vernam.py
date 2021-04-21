"""
    File created by steph
    Last update: 21.04.2021
"""


def encode(in_data, key: str):
    inp = ''
    for line in in_data:
        inp += line
    out = b''
    key_pos = 0
    key_len = len(key)
    for symb in inp:
        code = ord(symb) ^ ord(key[key_pos])
        symb = bytes([code])
        out += symb
        key_pos = (key_pos + 1) % key_len
    return out


def decode(in_data, key: str):
    inp = b''
    for line in in_data:
        inp += str.encode(line)
    out = ''
    key_pos = 0
    key_len = len(key)
    for symb in inp:
        code = symb ^ ord(key[key_pos])
        symb = chr(code)
        out += symb
        key_pos = (key_pos + 1) % key_len
    return out
