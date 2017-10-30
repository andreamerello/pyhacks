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
            sign_str = ''
            assign_str = ''
            # it is debatable whether it is better to use dir or
            # cls.__dict__.items(). The main difference is that dir()
            # also looks inside superclasses, which might (or not) be what you
            # want.
            for attr in dir(cls):
                obj = getattr(cls, attr)
                # better to use isinstance(obj, foowrap)
                if type(obj) is foowrap:
                    # this is no Pythonic at all. Moreover, concatenating
                    # strings like this is O(n**2). Much better to do
                    # something like:
                    #     names = []
                    #     names.append('x')
                    #     names.append('y')
                    #     ', '.join(names)
                    sign_str += ', ' + attr
                    #
                    # You already know about this: what if I want to use None
                    # as a default value?
                    if obj.val is not None:
                        # no, str() is NOT ok. See also
                        # test_arbitrary_default_value
                        sign_str += "=" + str(obj.val) # is str() ok ?
                    assign_str += '    self.' + attr + ' = ' + attr + '\n'
            if assign_str == '':
                assign_str = '    pass'
            magic_str = 'def magic_wand(self' + sign_str + '):\n' + assign_str
            print magic_str
            exec magic_str in globals(), locals()
            cls.__init__ = magic_wand
            # the lines above are a bit ugly; moreover, cls.__init__.__name__
            # == 'magic_wand', which is a bit weird. Suggestion:
            #
            # code = "def __init__(self): pass"
            # d = {}
            # exec code in d
            # cls.__init__ = d['__init__']
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
