# -*- coding: utf-8 -*-
from fizzbuzz.game import Game

class Fizz(Game) :
    def __init__(self) :
        Game.__init__(self, "Fizz")

    def testIfNumberIncludes2(self,number):
        strNumber = str(number)
        for i in strNumber:
            if(i=="2"):
                return True
        return False

    def testIfNumberIsAMultipleOf2(self,number):
        intNumber = int(number)
        return intNumber%2==0

    def startGame(self, number):
        resultTestIncludes = self.testIfNumberIncludes2(number)
        resultTestMultiple = self.testIfNumberIsAMultipleOf2(number)

        if(resultTestIncludes or resultTestMultiple):
            return "Fizz"
        return str(number)