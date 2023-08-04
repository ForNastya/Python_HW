# Hапишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте 
# его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def function (**kwargs):
    for k in kwargs.keys():
        print(f"key: {k}")
    for v in kwargs.values():
        print(f"value: {v}")

if __name__ == "__main__":
    function(a=9, b=7, c=5)