import os
import datetime


"""задача 1"""


def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open("main.log", "a") as f:
            f.write(f"{datetime.datetime.now()}\n")
            f.write(f"{old_function.__name__}\n")
            f.write((f"{args, kwargs}\n"))
            f.write(f"{result}\n")
            return result

    return new_function


def test_1():
    path = "main.log"
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return "Hello World"

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert "Hello World" == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), "Должно вернуться целое число"
    assert result == 4, "2 + 2 = 4"
    result = div(6, 2)
    assert result == 3, "6 / 2 = 3"

    assert os.path.exists(path), "файл main.log должен существовать"

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert "summator" in log_file_content, "должно записаться имя функции"
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f"{item} должен быть записан в файл"


if __name__ == '__main__':
    test_1()


""" задача 2"""

import os


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(f"{path}", "a") as f:
                f.write(f"{datetime.datetime.now()}\n")
                f.write(f"{old_function.__name__}\n")
                f.write((f"{args, kwargs}\n"))
                f.write(f"{result}\n")
                return result

        return new_function

    return __logger


def test_2():
    paths = ("log_1.log", "log_2.log", "log_3.log")

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return "Hello World"

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert "Hello World" == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), "Должно вернуться целое число"
        assert result == 4, "2 + 2 = 4"
        result = div(6, 2)
        assert result == 3, "6 / 2 = 3"
        summator(4.3, b=2.2)

    for path in paths:
        assert os.path.exists(path), f"файл {path} должен существовать"

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert "summator" in log_file_content, "должно записаться имя функции"

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f"{item} должен быть записан в файл"


if __name__ == '__main__':
    test_2()


"""Задача 3"""


def test_3():
    paths = ("#Plog_1.log", "#Plog_2.log", "#Plog_3.log")

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def flat_generator(list_of_lists):
            result = [j for i in list_of_lists for j in i]
            for item in result:
                yield item

        list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]
        flat_generator(list_of_lists_1)


if __name__ == "__main__":
    test_3()
