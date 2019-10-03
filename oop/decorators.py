from time import time,sleep


def timer(my_var):
    def decorate(func):
        def decorate2(*args, **kwargs):
            print("Doing smth")
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            print('decorate')
            print(round(end_time-start_time, my_var))

            return result
        return decorate2
    return decorate

@timer(3)
def foo():
    start_time = time()
    sleep(2)
    end_time = time()
    print('func')
    print(end_time-start_time)


def custom_decoration(obj):
    def decor(*args, **kwargs):
        start_time = time()
        #print(obj)
        print(*args)
        result = obj(args[0])
        end_time = time()
        #print('decorator')
        #print(end_time - start_time)
        return round(result, args[1])
    return decor


class myTimer(object):

    class decorate:
        pass
    
    my_var = 3

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        start_time = time()
        result = self.func(*args, **kwargs)
        end_time = time()
        print('decorator')
        self.timing = end_time-start_time
        print(self.round1())
        return result

    @custom_decoration
    def round1(self, my_var):
        return self.timing

@myTimer
def bar():
    start_time = time()
    sleep(2)
    end_time = time()
    print('func')
    print(end_time-start_time)

def lose_money(cls):
    original_show_moneys = cls.show_moneys
    def deco(*args,**kwargs):
        return 'You had ' + str(original_show_moneys(args[0])) + ' moneys, but now you have: 0'
    cls.show_moneys = deco
    return cls
@lose_money
class OneXbet:
    def __init__(self):
        self.my_moneys = 0

    def push_moneys(self, money):
        self.my_moneys = money

    def show_moneys(self):
        return self.my_moneys
if __name__ == '__main__':
    player = OneXbet()
    player.push_moneys(150)
    print(player.show_moneys())
    # start_time = time()
    # bar()
    # end_time = time()
    # print('main')
    # print(end_time - start_time)

