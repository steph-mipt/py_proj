"""
    File created by steph
    Last update: 31.03.2021
"""


import sys
from encr import cesar

""" only cesar encryption available """
encode = cesar.encode
decode = cesar.decode


def main():
    try:
        input_file = sys.argv[1]
        action = sys.argv[2]
        shift = int(sys.argv[3])
    except IndexError:
        print("Передайте, пожалуйста, название input file, action и shift")
        print("ex: main.py file_name encode/decode 10")
        return
    with open(input_file, "r") as file:
        input_data = file.read().splitlines()
    if action == "encode":
        out_file = input_file.split(".")[0] + ".csr"
        with open(out_file, "w") as out:
            encode(input_data, out, shift)
    elif action == "decode":
        out_file = input_file.split(".")[0] + ".dccsr"
        with open(out_file, "w") as out:
            decode(input_data, out, shift)
        pass


if __name__ == '__main__':
    main()
