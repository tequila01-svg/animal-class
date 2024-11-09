from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
    
class Human(Animal):
    def move(self):
        print("human walk")

class Snake(Animal):
    def move(self):
        print("snake crawl")
        
class Dog(Animal):
    def move(self):
        print("i can bark")
        
class Lion(Animal):
    def move(self):
        print("i can roar")
        
        
R=Human()
R.move()

K=Snake()
K.move()

R=Dog()
R.move()

K=Lion()
K.move()