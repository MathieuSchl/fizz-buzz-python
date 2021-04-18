# -*- coding: utf-8 -*-
from fizzbuzz.game import Game
from fizzbuzz.fizz import Fizz
from fizzbuzz.buzz import Buzz

class FizzBuzz(Game) :
    def __init__(self) :
        Game.__init__(self, "FizzBuzz")

    def setFizzAndBuzz(self,isFizz,isBuzz):
        if(isFizz and isBuzz):
            return "FizzBuzz"
        elif(isFizz and not isBuzz):
            return "Fizz"
        elif(not isFizz and isBuzz):
            return "Buzz"
        else:
            return False

    def testIfMultipleOf2Or5(self,number):
        fizzGame = Fizz()
        buzzGame = Buzz()
        isFizz = fizzGame.testIfNumberIncludes2(number)
        isBuzz = buzzGame.testIfNumberIncludes5(number)
        return self.setFizzAndBuzz(isFizz,isBuzz)

    def testIfInclude2Or5(self,number):
        fizzGame = Fizz()
        buzzGame = Buzz()
        isFizz = fizzGame.testIfNumberIsAMultipleOf2(number)
        isBuzz = buzzGame.testIfNumberIsAMultipleOf5(number)
        return self.setFizzAndBuzz(isFizz,isBuzz)

    def startGame(self, number):
        resMultiple = self.testIfMultipleOf2Or5(number)
        resIncludes = self.testIfInclude2Or5(number)

        if(resMultiple == "FizzBuzz" or resIncludes == "FizzBuzz"):
            return "FizzBuzz"
        elif(resMultiple == "Fizz" or resIncludes == "Fizz"):
            return "Fizz"
        elif(resMultiple == "Buzz" or resIncludes == "Buzz"):
            return "Buzz"
        else:
            return str(number)