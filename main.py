"""
    File created by steph
    Last update: 31.03.2021
"""

import sys
from my_tg_wrapper.tg_wrap import encr_bot


def main():
    encr_bot.polling(none_stop=True)

    """ infinity cycle for telegram bot """
    while True:
        pass


if __name__ == '__main__':
    main()
