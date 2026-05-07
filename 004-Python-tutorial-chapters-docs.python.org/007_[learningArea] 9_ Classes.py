    # 9. Classes
    # 9.1. A Word About Names and Objects
    # 9.2. Python Scopes and Namespaces
    # 9.2.1. Scopes and Namespaces Example
# 
# def adef():
#     s2 = 23423
#     def a2def():
#         s = 324324
#         nonlocal s2 #
#         s2 = 2342
#     a2def()
#     print(s2)
# adef()


    # 9.3. A First Look at Classes
    # 9.3.1. Class Definition Syntax
    # 9.3.2. Class Objects
# class Name:
#     def __init__(self,x,y):
#         self.x=x #
#         self.y=y #
#     def print(self):
#         return print(self.x,self.y)
# n = Name(3.2,5.0)
# n.print()
# print(n.x,n.y)
# 
# #
# 
# class dog:
#     feet = 4 # feet = for all objects
#     def a(self):
#         self.feet = 24332
#         print(self.feet)
# d = dog()
# d.a()
# #


    # 9.3.3. Instance Objects
    # 9.3.4. Method Objects
    # 9.3.5. Class and Instance Variables
    # 9.4. Random Remarks
    # 9.5. Inheritance
#
# class animal:
#     def s(self):
#         print("animal")
# class sf(animal):
#     def sft(self):
#         # animal.s(self)
#         # self.s()
#         super().s() #
# sf().sft()
# 
# #
# 
# class Animals: #
#     def sound(self):
#         raise NotImplementedError("def is empty")
# class Dog(Animals):
#     def sound(self):
#         return "dogdog"
# class Cat(Animals):
#     def sound(self):
#         return "catcat"
# def make_all_sound(animals):
#     for animal in animals:
#         print(animal.sound())
# zoo = [Dog(),Cat()]
# make_all_sound(zoo)
# print(isinstance(zoo[0],Animals)) #
#
# #
#
# class Animals11:
#     def hungry(self,somthing):
#         if self.IsItFood(somthing): 
#             print("i'm full! " + self.name + " said") #
#         else:
#             print("i'm hungry " + self.name + " said") #
#     def IsItFood(self,somthing):
#         return somthing == "fish"
# class Hamed(Animals11):
#     def __init__(self):
#         self.name = "hamed" # 
# class Ali(Animals11):
#     def __init__(self):
#         self.name = "Ali" #
# for pet in [Hamed,Ali]:
#     pet_state = pet()
#     pet_state.hungry("fish")
# 
# #
# 
# from abc import ABC, abstractmethod
# class Animals10(ABC):
#     @abstractmethod # it means = do it NOW , Implement It
#     def sound(self):
#         pass
# class Fish(Animals10):
#     pass # TypeError
# # fish = Fish()


    # 9.5.1. Multiple Inheritance
    # 9.6. Private Variables
#
# class underlineFunc:
#     def __init__(self):
#         self.__runOnStartup()
#     def runOnStartup(self):
#         print("it runs")
#     __runOnStartup = runOnStartup
# underlineFunc() #
# class Child(underlineFunc):
#     def child_def(self):
#         print("it runs (Child)")
# # Child() # if child doesn't have any __init__ , it runs the parent __init__
# class Child2(underlineFunc):
#     def __init__(self):
#         super().__init__()
#     def child_def(self):
#         print("it runs (Child)")
# Child2().child_def() #


    # 9.7. Odds and Ends
# 
# # # record class
# from dataclasses import dataclass
# @dataclass
# class Em:
#     name: str
#     age: int
# Em("mamad",30)


    # 9.8. Iterators
    # 9.9. Generators
    # 9.10. Generator Expressions
#
# # # __iter__ & __next__ & yield --SKIP--
