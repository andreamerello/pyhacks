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

        A = foo()
        assert 'bar' in foo.__dict__
