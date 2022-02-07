#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import warnings
import sys
import os
import sqlite3
from src.{{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name}}

# ******************FIXTURES ***************************
# fixture moved to conftest

@pytest.fixture(name='cursor')
def db_setup():
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT unique)''')
    cursor.execute('''INSERT INTO users(name, email)
                      VALUES(?,?)''', ("{{ cookiecutter.author_name }}", "{{ cookiecutter.email }}"))
    db.commit()
    yield cursor
    db.close()


# Inbuilt fixture - tmpdir_factory
@pytest.fixture(scope="session")
def text_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("bigfile.txt")
    fn.write("content")
    return fn


# Inbuilt fixture - request (Parametrized fixture)
data = [(3, 'cat'), (3, 'dog'), (7, 'hamster'), (6, 'gerbil')]


@pytest.fixture(params=data)
def gen_data(request):
    return request.param


# ======= START PYTEST FIXTURES TESTS =============================================================
# Using Fixture for SETUP and TEARDOWN.....Uses conftest.py
def test_get_db_record(cursor):
    cursor.execute('''SELECT name, email FROM users''')
    user1 = cursor.fetchone()
    assert user1 == ("{{ cookiecutter.author_name }}", "{{ cookiecutter.email }}")


# Inbuilt fixture - tmpdir
def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1


# Inbuilt fixture - tmpdir_factory
def test_create_file2(text_file):
    assert text_file.read() == "content"


# Inbuilt fixture - request
def test_func(gen_data):
    assert gen_data[0] == len(gen_data[1])


# Inbuilt fixture -  capsys
def test_output(capsys):
    {{cookiecutter.pkg_name}}.check_output()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
    assert captured.err == ''


# Inbuilt fixture - recwarn
def test_lame_function(recwarn):
    {{cookiecutter.pkg_name}}.lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


# ======= MONKEY PATCHING =========================================================================

'''
Original function may call a real API or access the network, or access a real database etc etc.
Monkey patching is useful for replacing this behaviour with a mock behaviour that is non-invasive etc
'''


def getssh():  # monkeypatch this function - this Original function is not changed in anyway
    return os.path.join(os.path.expanduser("~admin"), 'ssh')


# Inbuilt fixture - monkeypatch
def test_mytest(monkeypatch):
    # 1 - setup the mock that will be used instead of the actual function
    def mockreturn(object):
        return '\\abc'

    # 2 - Redirect actual function to mock function (i.e 'os.path.expanduser' ---> mockreturn)
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)

    # 3 - now test the actual function
    x = getssh()
    assert x == '\\abc\\ssh'


# ======= START BASIC TESTS =======================================================================
def test_doubleit():
    assert {{cookiecutter.pkg_name}}.doubleit(10) == 20


# ======= START PYTEST FUNCTIONS ==================================================================
# pytest.raises
def test_doubleit_except_type():
    with pytest.raises(TypeError):
        {{cookiecutter.pkg_name}}.doubleit('hello')


# pytest.raises
def test_doubleit_except_message():
    with pytest.raises(TypeError, match='Enter an Integer'):
        {{cookiecutter.pkg_name}}.doubleit('hello')


# pytest.warns - Alternative way to check warnings
def test_lame_function_warns():
    with pytest.warns(DeprecationWarning, match='.*Please stop using this.*'):
        {{cookiecutter.pkg_name}}.lame_function()


# pytest.approx
def test_approx():
    assert {{cookiecutter.pkg_name}}.addit(0.1, 0.2) == pytest.approx(0.3)

# ======= START EXCEPTION TESTS ===================================================================
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        {{cookiecutter.pkg_name}}.div_by_zero()


def test_check_message():
    with pytest.raises(ValueError) as excinfo:
        {{cookiecutter.pkg_name}}.check_message("dog")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "pet must be cat"


def test_manual_exc():
    with pytest.raises(ValueError):
        if {{cookiecutter.pkg_name}}.manual_exception() > 5:
            raise ValueError("value must be <= 5")

# ======= START MARKING TESTS =====================================================================
@pytest.mark.skip(reason='misunderstood the API')
def test_ignore_this():
    assert 1 == 2


@pytest.mark.skipif("{{ cookiecutter.version }}" < "0.3.0", reason="not supported until version 0.3.0")
def test_ignore_this2():
    assert 1 == 2


# skip imperatively during test execution
def test_if_not_windows():
    if sys.platform.startswith("win"):
        pytest.skip("skipping windows-only tests")


@pytest.mark.xfail(reason='not supported until version 0.3.0')
def test_expected_fail_and_fails():
    assert 1 == 2


@pytest.mark.parametrize(
    'length, pet', [
        (3, 'cat'),
        (3, 'dog'),
        (7, 'hamster'),
        (6, 'gerbil'),
    ]
)
def test_param_example(length, pet):
    assert length == len(pet)


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_userwarning():
    warnings.warn("this is a warning", UserWarning)
