# -*- coding:utf8 -*-
def dector(fn):
    def test(*args):
        print "ha,ha,ha"
        return fn(*args)
    return test
@dector
def other(a,b):
    print "the value is :%s"%(a**2+b**2)
if __name__ == "__main__":
    other(4,3)
