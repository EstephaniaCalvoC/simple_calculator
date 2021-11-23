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
