#!/usr/bin/python

class ObjectTypeWrapper(object):
    def __init__(self, val):
        self.val = val

# why do you put everything into a class? If you use "attrs", you just do
# "import attr; @attr.s", NOT "from attr import attr".
class my_attr:

    @staticmethod
    def s(cls):
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
            if type(obj) is ObjectTypeWrapper:
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

    # what's the point of defining a function which always instantiate a
    # class? You could simply use a class directly
    @staticmethod
    def ib(val = None):
        return ObjectTypeWrapper(val)
