def log(filename=None):
    """Декоратор с параметрами внешняя функция, которая принимает аргументы для декоратора"""

    def decorator(func):
        """Декоратор функции который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки, и выводит в консоль или в файл если такой задан"""

        def wrapper(*args, **kwargs):
            """Обертка функции"""
            try:
                """Выполняется если функция работает"""
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                """Выполняется если функция выдает ошибку"""
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

        return wrapper

    return decorator
