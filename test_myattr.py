import pytest
from my_attr import my_attr

class TestMyattr:
    def test_decorator(self):
        @my_attr.s
        class foo(object):
            a = 'bar'

        A = foo()
        assert A.a == 'bar'

    def test_add(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib()

        A = foo(None)
        assert 'bar' in foo.__dict__

    def test_val(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib()

        A = foo(bar = 5)
        assert A.bar == 5

    def test_def_val(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib(3)

        A = foo()
        assert A.bar == 3
