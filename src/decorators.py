from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Декоратор для логирования вызовов функций."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with open(filename, "w") as f:
                result = func(*args, **kwargs)
                try:
                    result == sum(args)
                    f.write("my_function ok")
                    print("my_function ok")
                except Exception as e:
                    f.write(f"my_function error: {e}. Inputs:{args}, {kwargs}")
                    print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Суммирует два целых числа."""

    return x + y


my_function(int("1"), int("2"))
