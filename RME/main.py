from rme_modes import rme_random, rme_choice, rme_cascade


def random():
    return print(rme_random())


def choice(x):
    return print(rme_choice(x))


def cascade(y):
    return print(rme_cascade(y))
