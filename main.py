"""
    File created by steph
    Last update: 21.04.2021
"""

from my_tg_wrapper.tg_wrap import encr_bot


def main():
    encr_bot.polling(none_stop=True)

    """ infinity cycle for telegram bot """
    while True:
        pass


if __name__ == '__main__':
    main()
