#!/usr/bin/python

class foowrap(object):
    def __init__(self, val):
        self.val = val

class my_attr:
    @staticmethod
    def s(cls_deco):
        def put_init():
            coma = ''
            sign_str = ''
            assign_str = ''
            for attr in dir(cls_deco):
                obj = getattr(cls_deco, attr)
                if type(obj) is foowrap:
                    sign_str += ', ' + attr
                    if obj.val is not None:
                        sign_str += "=" + str(obj.val) # is str() ok ?
                    assign_str += '    self.' + attr + ' = ' + attr + '\n'
            if assign_str == '':
                assign_str = '    pass'
            magic_str = 'def magic_wand(self' + sign_str + '):\n' + assign_str
            print magic_str
            exec magic_str in globals(), locals()
            cls_deco.__init__ = magic_wand

            return cls_deco

        return put_init()

    @staticmethod
    def ib(val = None):
        return foowrap(val)


@my_attr.s
class foo(object):
    bar = my_attr.ib(5)

A = foo(5)
