# -*- coding: utf-8 -*-
from functools import reduce
        
class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)
    
    def div(self, a, b):
        return a / b if b else float('inf')
    
    def avg(self, array, ut=None, lt=None):
        array = array if ut is None else [n for n in array if n <= ut]
        array = array if lt is None else list(filter(lambda n: True if n >= lt else False, array))

        return sum(array) / len(array) if array else 0
