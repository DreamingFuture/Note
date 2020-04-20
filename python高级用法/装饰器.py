import time


def display_time1(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)

    return wrapper


def display_time2(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print(t2 - t1)
        return result

    return wrapper


def display_time3(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2 - t1)
        return result

    return wrapper


@display_time1
def test1():
    for i in range(1000000):
        pass
    print("hello world!")


@display_time2
def test2():
    for i in range(1000000):
        pass
    print("hello world!")
    return 222


@display_time3
def test3(num1, num2):
    for i in range(1000000):
        pass
    print(num2 - num1)
    return 333


test1()
print('-' * 10)

a = test2()
print(a)
print('-' * 10)

b = test3(1, 0)
print(b)
