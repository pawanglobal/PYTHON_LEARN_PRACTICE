#static methods : it doesn't have any cls or self argument

class Ops:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
#you don't normally create instances for this call
#you directly call the functions
a = Ops.add(5, 6)
print(a)

#Data encapsulation and Private attributes
#to solve the problem of every attribute and method is public
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   #you put underscore to protect a attribute

    def __repr__(self):
        return f'Account({self.owner!r}, {self._balance!r})' 
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        self._balance -= amount
    def inquiry(self):
        return self._balance

#type hinting

#properties
import string
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected str')
        if not all(c in string.ascii_uppercase for c in value):
            raise ValueError('Must be uppercase ASCII')
        if len(value) > 10:
            raise ValueError('Must be 10 characters or less')
        self._owner = value

a = Account('GUIDO', 1000.0)
a.owner = 'EVA'
#a.owner = 42                #this will raise type error

#

#Multiple inheritances, interfaces, and Mixins
#Multiple inheritance
class Duck:
    def walk(self):
        print('Waddle')
class Trombonist:
    def noise(self):
        print('Blat!')

class DuckBonist(Duck, Trombonist):
    pass

d = DuckBonist()
print(d.walk())
print(d.noise())

#Type based approach

#Descriptors

#class definition process

#Dynamic class creation

#Metaclasses
print(isinstance(Account, object))  #True
print(Account.__class__)cd