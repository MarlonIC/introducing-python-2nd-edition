places = ['McDonalds', 'KFC', 'Burger King', 'Taco Bell', 'Wendys', 'Arbys', 'Pizza Hut']


def pick():
    """Return random fast food place"""
    import random
    return random.choice(places)
