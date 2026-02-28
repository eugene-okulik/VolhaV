# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished" после выполнения декорированной функции.

def finish_me(func):
    def wrapper():
        func()
        print('after')

    return wrapper



@finish_me
def decor_func():
    print("Превед, медвед")


decor_func()
