from source import foobar


def mytest1(self):
    print(2)

foobar.User.mytest = mytest1

a = foobar.User()
a.mytest()
