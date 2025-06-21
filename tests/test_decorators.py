import os
import tempfile

import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


def test_log(capsys):
    my_function(1, 4)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


@log()
def my_function_2(x, y):
    return x + y


def test_log_1(capsys):
    my_function_2(1, 6)
    captured = capsys.readouterr()
    assert captured.out == "my_function_2 ok\n"


@log()
def test_my_function_3(x, y):
    raise Exception("test_my_function_3 error: ZeroDivisionError. Inputs: (2, 0), {}")

    with pytest.raises(Exception, match="test_my_function_3 error: ZeroDivisionError. Inputs: (2, 0), {}"):
        test_my_function_3(2, 0)


@log()
def my_function_4(a, b):
    raise Exception("test_my_function_4 error: ZeroDivisionError. Inputs: (1, 0), {}")


def test_log_2(capsys):
    try:
        my_function_4(1, 0)
    except Exception:
        pass
    captured = capsys.readouterr()
    assert "my_function_4 error: Exception. Inputs: (1, 0), {}\n" in captured.out


@log(filename="mylog.txt")
def test_function_5(x, y):
    return x + y


with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    filename = temp_file.name

try:

    @log(filename=filename)
    def test_function_6(x, y):
        return x + y

    test_function_5(1, 2)

    with open(filename, "r") as file:
        logs = file.read()
        assert "test_function_5 ok" in logs
finally:
    os.remove(filename)
