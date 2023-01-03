#new objects are defined using the class statement
class Account:
    """A simple bank Account
    """
    owner:str      #type hints
    balance:float  #type hints

    def __init__(self, owner, balance): #special or magic methods
        self.owner = owner
        self.balance = balance
    
    def __rep__(self):
        return f'Account {self.owner!r}, {self.balance!r}'
    
    def deposit(self, amount):  #method
        self.balance += amount

    def withdraw(self, amount): #method
        self.balance -= amount
    
    def inquiry(self) -> float: #method , '->' a type hint
        return self.balance

#instances
a = Account('eva', 1000) #calls Account.__init__(a, 'eva', 1000)
b = Account('John', 500)

a.deposit(100)           #calls Account.deposit(a, 100)
b.withdraw(50)
owner = a.owner          #get account owner

print(vars(a))           #you can view instance variabels by vars
print(vars(b))
print(owner)

print(type(a))           #associated class
print(type(b.withdraw))
print(type(a).deposit)

#attribute access, there are only three basic operations that can
#be performed on the any an instance: getting, setting, deleting.

print(a.owner)                  #get

a.balance = 750                 #set
print(a.balance)

#del a.balance                  #delete
print(a.balance)

#you can create new attribute after it's creation
a.creation_date = '2020-5-31'
a.nickname = 'evy'

print(a.creation_date)
print(a.nickname)

#instead of using dot method you can use some other function to get access
#to the attributes

print(getattr(a, 'owner'))

setattr(a, 'balance', 600)

print(getattr(a, 'balance'))

#delattr(a, 'balance')

print(hasattr(a, 'you'))         #for existence of an attribute

#if you want to check the attribute if it exits, or not
print(getattr(a, 'balance', 'unknown'))
print(getattr(a, 'you', 'unknown'))

#bound method
w = a.withdraw
print(w)
print(type(w))
w(100)                           #account.withdraw(a, 100)
print(a.balance)

#operator overload and protocols

#inheritance; one use of inheritance extending the existing class
class MyAccount(Account):
    def panic(self):
        self.withdraw(self.balance) #withdraw all the money

c = MyAccount('Chris', 1000)

c.withdraw(20)
print(c.balance)

c.panic()
print(c.balance)                     #nothing in balance

#inheritance also redefines the already existed melthod
import random
class EvilAccount(Account):          #redefining the method inquiry
    def inquiry(self):
        if random.randint(0,4) == 1: #randint()	Returns a random number between the given range
            return self.balance * 1.10
        else:
            return self.balance

d = EvilAccount('Guido', 1000)
d.deposit(50)                    #calls Account.deposit(d, 50)
available = d.inquiry()
print(available)                 #calls EvilAccount.inquiry(d)

#if you want to call the original method defined before
class EvilAccount(Account):
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return 1.10 * super().inquiry()
        else:
            return super().inquiry

#less common but inheritance can be used to add additional attributes
#to instances
class EvilAccount(Account):
    def __init__(self, owner, balance, factor):
        super().__init__(owner, balance)
        self.factor = factor
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.factor * super().inquiry
        else:
            return super().inquiry()
    def __rep__(self):           #mostly for debbuging
        return f'{type(self).__name__}({self.owner}, {self.balance})'

print(type(d))

#avoiding inheritance via composition
class Stack(list):
    def push(self, item):
        self.append(item)

#example
s = Stack()
s.push(1)
s.push(2) 
s.push(3)
s.push(4)
print(s)

s.pop()
s.pop()
print(s)

#A better approach is composition instead of inheritance from a list
import array #for loose coupling
class Stack:
    def __init__(self):
        self._items = list()
    
    def push(self, item):
        return self._items.append(item)
    def pop(self):
        return self._items.pop()
    def __len__(self):
        return len(self._items)

s = Stack()
s.push(4)
s.push(6)
s.push(7)
s.push(8)

print(s._items)
print(s.__len__())

# one benefit loose coupling
#e = Stack(container=array.array('i')) #getting error
#e.push(1)
#e.push(2)
#e.push('a lot')      #typo error

#if you can avoid then try to avoid iheritance and use functions

#Dynamic binding and duck typing

