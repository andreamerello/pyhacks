import pytest
from my_attr import my_attr

class TestMyattr:
    def test_decorator_returns_same_instance_of_original_class(self):
        class foo(object):
            pass

        foo2 = my_attr.s(foo)
        assert foo is foo2

    def test_adding_field_do_really_add_it_regardless_its_value(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib()

        foo_obj = foo(None)
        assert 'bar' in foo.__dict__

    def test_added_field_gets_val_passed_to_ctor(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib()

        foo_obj = foo(bar = 5)
        assert foo_obj.bar == 5

    def test_added_field_assumes_default_val_when_val_not_specified_in_ctor(self):
        @my_attr.s
        class foo(object):
            bar = my_attr.ib(3)

        foo_obj = foo()
        assert foo_obj.bar == 3

    # xfail: eXpected to fail: the test is still run, but pytest still shows a
    # green line. You should delete the xfails one by one, and fix them
    @pytest.mark.xfail
    def test_default_None(self):
        @my_attr.s
        class Foo(object):
            bar = my_attr.ib(None)

        f = Foo()
        assert f.bar is None

    @pytest.mark.xfail
    def test_default_keyword(self):
        @my_attr.s
        class Foo(object):
            bar = my_attr.ib(default=None)

        f = Foo()
        assert f.bar is None

    @pytest.mark.xfail
    def test_attribute_order(self):
        # this is a difficult test to write, because the dictionary order is
        # undefined, so it might happen that the attributes are in the correct
        # order by chance, even if you don't do anything to sort them.
        # Moreover, dir() returns attributes in alphabetical order.
        #
        # To minimize the probability to pass the test "by chance", we define
        # two classes with the attributes in reverse order.
        @my_attr.s
        class Point1(object):
            x = my_attr.ib()
            y = my_attr.ib()
            z = my_attr.ib()

        p = Point1(1, 2, 3)
        assert p.x == 1
        assert p.y == 2
        assert p.z == 3

        @my_attr.s
        class Point2(object):
            z = my_attr.ib()
            y = my_attr.ib()
            x = my_attr.ib()

        p = Point2(1, 2, 3)
        assert p.z == 1
        assert p.y == 2
        assert p.x == 3

    @pytest.mark.xfail
    def test_arbitrary_default_value(self):
        # this is a bit hard, but with enough effort you can probably do
        sentinel = object()

        @my_attr.s
        class Foo(object):
            x = my_attr.ib(default=sentinel)

        f = Foo()
        assert f.x is sentinel
