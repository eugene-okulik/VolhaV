# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция

# @repeat_me
# def example(text):
#     print(text)
# example('print me', count=2)
#  В результате работы будет такое:
# print me
#
# print me


def repeat_me(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)

    return wrapper


@repeat_me
def value_repeat(text):
    print(text)


value_repeat('print me', 3)
