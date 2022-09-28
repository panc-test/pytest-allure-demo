"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : pytest-allure-demo
@File : test_demo.py
@Author : 057776
@Time : 2022/9/9 15:54

"""
import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')
