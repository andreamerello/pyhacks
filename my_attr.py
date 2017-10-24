#!/usr/bin/python

class foowrap(object):
    def __init__(self, val):
        self.val = val

class my_attr:
    inits = []
    @staticmethod
    def s(cls_deco):
        def magic_wand(self):
            for attr in dir(self):
                obj = getattr(self, attr)
                if type(obj) is foowrap:
                    setattr(self, attr, obj.val)
        def put_init():
            cls_deco.__init__ = magic_wand
            return cls_deco

        return put_init()

    @staticmethod
    def ib(val = None):
        return foowrap(val)

@my_attr.s
class foo(object):
    aaa = my_attr.ib()
    bbb = my_attr.ib(3)

@my_attr.s
class bar(object):
    a = my_attr.ib()
    b = my_attr.ib(5)


A = foo()
print A.aaa
print A.bbb

print '..'

B = bar()
print B.a
print B.b
#print B.aaa
