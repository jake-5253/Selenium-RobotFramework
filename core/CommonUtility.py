from random import choice
from string import ascii_uppercase
import random

class CommonUtility:

    @staticmethod
    def string_generator(length):
        return ''.join(choice(ascii_uppercase) for i in range(length))

    @staticmethod
    def random_number_generator(length):
        range_start = 10 ** (length - 1)
        range_end = (10 ** length) - 1
        return random.randint(range_start, range_end)
