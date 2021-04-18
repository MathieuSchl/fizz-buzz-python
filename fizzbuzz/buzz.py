# -*- coding: utf-8 -*-
from fizzbuzz.game import Game

class Buzz(Game) :
    def __init__(self) :
        Game.__init__(self, "Buzz")

    def testIfNumberIncludes5(self,number):
        strNumber = str(number)
        for i in strNumber:
            if(i=="5"):
                return True
        return False

    def testIfNumberIsAMultipleOf5(self,number):
        intNumber = int(number)
        return intNumber%5==0

    def startGame(self, number):
        resultTestIncludes = self.testIfNumberIncludes5(number)
        resultTestMultiple = self.testIfNumberIsAMultipleOf5(number)

        if(resultTestIncludes or resultTestMultiple):
            return "Buzz"
        return str(number)