import pytest
from my_attr import my_attr

class TestMyattr:
    def test_decorator(self):
        # general rule: class names are CamelCase, variables are
        # lowercase. UPPERCASE is mostly used for module-level constants. "A =
        # foo()" looks just wrong to me :)

        @my_attr.s
        class foo(object):
            a = 'bar'

        A = foo()
        # I am not sure to understand what you want to test here. Let me
        # guess: you want to check that "A" is an instance of foo (and thus
        # has the "a" attribute). See test_decorator_2 for how I would test
        # it.
        assert A.a == 'bar'

    def test_decorator_2(self):
        class foo(object):
            pass

        foo2 = my_attr.s(foo)
        assert foo is foo2

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
