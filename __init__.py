import math

class calculator:
    total = 0

    @classmethod
    def add(cls, x):
        '''Addition. Adds x to memorized number.'''
        cls.total += x
        print(float(cls.total))

    @classmethod
    def substract(cls, x):
        '''Subtraction. Substracts x from memorized number.'''
        cls.total -= x
        print(float(cls.total))

    @classmethod
    def multiply(cls, x):
        '''Multiplication. Multiples the memorized number by x'''
        cls.total *= x
        print(cls.total)

    @classmethod
    def divide(cls, x):
        '''Division. Divides memorized number by x'''
        cls.total /= x
        print(cls.total)

    @classmethod
    def root(cls):
        '''Root. Takes a square root of memorized number'''
        cls.total = math.sqrt(cls.total)
        print(cls.total)

    @classmethod
    def reset(cls):
        '''Reset memory. Memorized number is reset to zero'''
        cls.total = 0.0
        print(cls.total)