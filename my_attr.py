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
