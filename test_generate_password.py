import generatePassword
import pytest

def test_password_size():
    size = 10
    password = generatePassword.getPassword(size)()

    assert len(password) == size

def test_get_random_numbers():
    size = 15
    password = generatePassword.getRandomNumbers(size)

    assert len(password) == size

def test_join_list():
    def list():
        def generate():
            return ['a', 'b', 'c']

        return generate

    joinList = generatePassword.joinList(list())

    assert joinList == 'abc'

