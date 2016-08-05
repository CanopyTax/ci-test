from source import greeter


def my_input(prompt):
    return 'bob'

args = None
def my_print(*args_):
    global args
    args = args_


greeter.input = my_input
greeter.print = my_print


def test_greet():
    greeter.greet()
    assert args == ('Hello', 'bob')
