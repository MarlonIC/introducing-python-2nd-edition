from random import choice

answers = ['Yes!', 'No!', 'Reply hazy', 'Sorry, what?']


def give():
    """Returns random advice"""
    return choice(answers)
