# -*- coding: utf-8 -*-

import math
from fizzbuzz.exception import ArgsException

class Game :
    def __init__(self, name):
        self.name = name
    
    def accept(self, game):
        if game is None:
            return False
        return game==self.name
        
    def testIfNaN(self,number):
        return (number != number)

    def play(self, number):
        if(self.testIfNaN(number)):
            raise ArgsException
        return self.startGame(number)