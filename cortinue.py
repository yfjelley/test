#!/usr/bin/env python
#
# -*- coding : utf-8 -*-

from tornado.ioloop import IOLoop
from tornado import gen
import time

class test(object):
    def __init__(self, d):
        self.d = d
    @gen.coroutine
    def add(self):
        for i in range(100):
            time.sleep(1)
            self.d[i] = [i]
@gen.coroutine
def run():
    d= {'key': {}}
    r = yield test(d['key']).add()
    print r

if __name__ == "__main__":
    ioloop = IOLoop.instance()
    ioloop.add_callback(run)
    ioloop.start()

