def logger(func):

    def wrapper(*args):
        print("Logging...")
        func(*args)

    return wrapper


@logger
def add(a, b):
    print(a + b)

add(10, 20)