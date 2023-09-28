

def me_decorator(func):
    def wrapper():
        print('Оберточка')
        x = func()
        print('Оберточка')
    return wrapper()


@me_decorator
def me_function():
    x = 'Я функция'
    print(x)
    return x


# me_function()
