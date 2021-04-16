import my_encr.utils as utils

def encode(in_data, out_data, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    for line in in_data:
        out_line = ''
        for symb in line:
            if symb.isalpha():
                symb = utils.shift_letter(symb, ord(key[key_pos]) - ord('A'))
                key_pos = (key_pos + 1) % key_len
            out_line += symb
        out_data.write(out_line)


def decode(in_data, out_data, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    for line in in_data:
        out_line = ''
        for symb in line:
            if symb.isalpha():
                symb = utils.shift_letter(symb, ord('A') - ord(key[key_pos]))
                key_pos = (key_pos + 1) % key_len
            out_line += symb
        out_data.write(out_line)
