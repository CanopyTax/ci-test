
import requests


def do_some_crazy_stuff(val):
    r = requests.get('https://api.github.com/user/{}'.format(val))
    return r.json()


def use_some_crazy_stuff(val):
    return do_some_crazy_stuff(val)


if __name__ == '__main__':
    print(use_some_crazy_stuff('nhumrich'))
