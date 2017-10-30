#!/usr/bin/python

# classes are usually CamelCase in Python
#
# this name is horrible. Moreover, see comments on ib() below
class foowrap(object):
    def __init__(self, val):
        self.val = val

# why do you put everything into a class? If you use "attrs", you just do
# "import attr; @attr.s", NOT "from attr import attr".
class my_attr:

    @staticmethod
    def s(cls):
        def put_init():
            coma = '' # never used
            _sign_str = []
            _assign_str = []
            # it is debatable whether it is better to use dir or
            # cls.__dict__.items(). The main difference is that dir()
            # also looks inside superclasses, which might (or not) be what you
            # want.
            for attr in dir(cls):
                obj = getattr(cls, attr)
                # better to use isinstance(obj, foowrap)
                ## Why? do we need hineritance somehow ?
                if type(obj) is foowrap:
                    # this is no Pythonic at all. Moreover, concatenating
                    # strings like this is O(n**2). Much better to do
                    # something like:
                    #     names = []
                    #     names.append('x')
                    #     names.append('y')
                    #     ', '.join(names)
                    _sign_str.append(', ')
                    _sign_str.append(attr)
                    #
                    # You already know about this: what if I want to use None
                    # as a default value?
                    if obj.val is not None:
                        _sign_str.append('=')
                        # no, str() is NOT ok. See also
                        # test_arbitrary_default_value
                        _sign_str.append(str(obj.val))
                    _assign_str.append('    self.')
                    _assign_str.append(attr)
                    _assign_str.append(' = ')
                    _assign_str.append(attr)
                    _assign_str.append('\n')
            assign_str = "".join(_assign_str)
            if assign_str == '':
                assign_str = '    pass'
            sign_str = "".join(_sign_str)
            _magic_str = []
            _magic_str.append('def __init__(self')
            _magic_str.append(sign_str)
            _magic_str.append('):\n')
            _magic_str.append(assign_str)
            magic_str = "".join(_magic_str)

            context = {}
            exec magic_str in context
            cls.__init__ = context['__init__']
            return cls

        # what's the point of defining a function which is called only once
        # and immediately? You could just do the work inside "s", and be
        # happy.
        return put_init()

    # what's the point of defining a function which always instantiate a
    # class? You could simply use a class directly
    @staticmethod
    def ib(val = None):
        return foowrap(val)


# it seems that while developing, you tested your code by running
# "./my_attr.py": WRONG WRONG WRONG! Why didn't you just write a test and used
# py.test to run it?
@my_attr.s
class foo(object):
    bar = my_attr.ib(5)

A = foo(5)
