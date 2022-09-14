from ast import Sub
from cgi import print_arguments
from itertools import count
from pickle import TRUE
import re
from time import time
from turtle import clear

"""
text = "{} is my country. All Indians are my brothers and sisters".format("India")
print(text)

count = text.count('India')
print("No of occurrances of 'india' = {}".format(count))

myString = 'superman'
print(myString.endswith('man'))
print(myString.endswith('man',3)) #start checking from index 3 onwards
print(myString.endswith('man',2,6)) #starts from index 2 till 6-1
print(myString.endswith(('man','ma'),2,6)) #starts from index 2 till 6-1

mystring="Good Morning"
print(mystring.find('Mo'))
print(mystring.find('Mo',3))
print(mystring.find('Mo',3,7))
print(mystring.find('Mon',3,7))
print(mystring.index('Mo'))
print(mystring.index('Moo'))

#join() method to join items in a tuple with a separator
separator='-'
myTuple=('h','e','l','l','o')
newString = separator.join(myTuple)
print(newString)


#replace and split methods
mystring="Hello world"
mystring=mystring.replace('o','i')
print(mystring)
mystring=mystring.replace('i','o',1) #replaces 1 occurance
print(mystring)
myStringSplit = mystring.split(' ')
print(myStringSplit)

#regular expressions functions
txt="bits of paper, bits of paper"
x = re.findall('bi',txt)
print(x)
x = re.search('bi',txt)
print(x)
print(x.span())
print(txt.split())
x = re.sub(' ','-',txt)
print(x)

#search using metacharacters
txt='Hello world'
#find all lower case characters between 'a' and 'm'
print(re.findall("[a-m]",txt))

txt = "James Bond is 007"
#find all the digits
print(re.findall("\d",txt))

x=re.findall("J...s",txt)
print(x)
#look for a substr starting with 'James' using metacharacter ^
print(re.findall(r"^James",txt)) 
#look if string ends with '007'using metacharacter $
print(re.findall("007$",txt))
print(re.findall("007",txt))
#look for a substr starting with 'Jam' using special sequence \A
print(re.findall("\AJam",txt)) 
#look if any of the word in string starts with '00' using special sequence \b
#r is for raw string, do not consider the special sequences
print(re.findall(r"\b007",txt))

#matching an email within a string using special sequence
mystring = "my email is abhi@abhi.com hope you will note it down"

#regular expression to match email
#check for non space chars before and after '@'
regex = '\S+@\S+'
x = re.findall(regex, mystring)
print(x)


#Python lists and list access options
studentsAges = [18,21,23,20,21]
print(studentsAges)
print(studentsAges[2]) #print particular index
print(studentsAges[2:4]) #prints from index 2 to 4
print(studentsAges[1:5:2]) #starting from 1 to 5-1, every second element
print(studentsAges[:3]) #starting from index 0 till 3-1
print(studentsAges[::-1]) #reverse the list
print(studentsAges[-2]) #accessing second last 

#append to add a value to the end of the list
studentsAges.append(16)
studentsAges.append('hi')
print(studentsAges)
#delete values from the list
del studentsAges[-1]
print(studentsAges)

#combine two list using extend
studentsName = ['Anu','Binu','Sinu']
studentsAges.extend(studentsName)
print(studentsAges)

#To check if a variable is in the list using 'in' operator
print('Anu' in studentsName)
print('Anushka' in studentsName)

#to get number of items in the list
print(len(studentsName))

#reverse the contents of the list destructively
studentsName.reverse()
print(studentsName)
studentsName.reverse()
print(studentsName)

#to sort the items alphabetically or numerically
studentsAges = [18,21,23,20,21]
studentsAges.sort()
print(studentsAges)
studentsName.sort()
print(studentsName)

#list concatenation using + operator
print(studentsName+studentsName)

#list duplication or multiplication using * operator
print(studentsName*3)

#Tuples in python
months = ("Jan", "Feb","Mar")
print(months[0])
print(months[-1])
#months[0] = "test"  gives error

#Tuples methods in python
print(len(months))
print("Jan" in months)
#del months
print (months)
print(months+months)
print(months*3)

#DICTIONARY in python

#dictionary declaration
#method 1
myStudents = {"Abhi":30, "Sibi":28, "Subi":"not updated"}
#method 2
myStudents = dict(Abhi=30, Sibi=28, Subi="not updated")
#method 3
myStudents = dict({"Abhi":30,"Sibi":28,"Subi":"not updated"})
print(myStudents["Sibi"])

#Dictionary methods
print(myStudents.get("Subi")) #returns the corresponding value
print(myStudents.items()) #returns dict items as array of tuples
print(myStudents.keys()) #returns keys
print(myStudents.values()) #returns values
print("Abhi" in myStudents) # check if key is present 
print(30 in myStudents.values()) # check if value is present 
print(len(myStudents))

myStudents2 = {"Abhi":31, "Binu":26}
myStudents.update(myStudents2) #join together dictionary by overwriting duplicate keys
print(myStudents)

myStudents.clear() #clear all the values in dict
print(myStudents)
del myStudents #deletes dict along with the varibale
print(myStudents)

#Set in python

#declaration
#method 1
months = {"Jan", "Feb", "Mar"}
#method 2
months = set(["Jan","Feb","Mar"])
print(months)
print(type(months))

#Looping through elements in a set
for i in months:
    print(i)

#declare an empty set
days = set()
#add values to set
days.add("Mon") #add method can take only one value
days.add("Tue")
days.add("wed")

for i in days:
    print(i)

days.update(["Thu","Fri"]) #insert multiple items
for i in days:
    print(i)

#remove items from the set
#using discard() method. Will remove item, not display error if item doesnt exist
days.discard("Thu")
for i in days:
    print(i)
#using remove() method. Will remove item, display error if item doesnt exist
days.remove("Thu")
for i in days:
    print(i) 
#clear elements in the set
days.clear()
for i in days:
    print(i) 

months1 = {"Jan", "Feb", "Mar"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#unioin operation
months4 = months1 | months2
print(months3)

#Intersection operation
months4 = months1 & months2
print(months3)

#intersection_update method
#months1.intersection_update(months2,months3)
#print(months1)

#difference operator
months4 = months1 - months2
print(months4)

#symmetric difference operation
#will retain all the elements of two sets except the common ones
months4 = months1 ^ months2
print(months4)


months1 = {"Jan", "Feb", "Mar","Apr","May","Jun"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}

#Set comparison operators
#checking if months1 is a superset of months2
print(months1 > months2)
print(months1 < months2)
#check if two sets are equal(no of elements and elements itself should be same)
print(months2 == months3)
#check if two sets are equal as well as month1 is a superset of month2
print(months1 >= months2)
#check if two sets are equal as well as month2 is a superset of month1
print(months1 <= months2)

#Frozen Set
months4frozen = frozenset(["nov","dec"]) #immutable set
print(months4frozen)
print(type(months4frozen))
months4frozen.add("Oct") #AttributeError: 'frozenset' object has no attribute 'add'

#input and output funcitons inp python
studName = input('Enter you name: ')
studAge = input('Enter you age: ')
print(studName)
print(studAge)

#variation of print statement 
print("The student name is", studName,"and the age is",studAge)
print("The student name is %s and the age is %s" %(studName,studAge))
print("The student name is {} and the age is {}" .format(studName,studAge))

#print in multiple lines
print('''Hello World
How are you''')
#print in new line
print('Hello World\nHow are you')

#escape characters
print('This is a backslash \\') #to print \
print('I am 5\' 5\" tall') #to print ' and "

#Control Flow statements
#Conditional Statements
#If condition
userInputNo = input('Enter either 1 or 2: ')
if(userInputNo == '1'):
    print('You entered 1')
    print('And you are the no 1')
elif(userInputNo == '2'):
    print('You entered 2')
    print('And you are the no 2')
else:
    print('You didnt enter 1 or 2')

#Inline if statement
B=12
A=12 if B==10 else 13
print(A)

print("B is ten" if B==10 else "B is not 10")

#Python match case statement example
#define  a function
def http_status(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "page not found"
        case _:  #_ stands for default
            return "unknown error occurred"
#calling the function
print(http_status(404))

#Looping in Python
#Use for loop to loop through a list in python
fruits = ['apples','oranges','banana','cherry']
for fruit in fruits:
    print(fruit)

#to display the index also using the enumerate function
for index, fruit in enumerate(fruits):
    print(index, fruit)

#use for loop to generate a series of numbers
#using range function
for i in range(10):
    print(i)

#While loop example 
counter = 5
while counter > 0:
    print("counter = ", counter)
    counter -= 1

#Break and Continue statements
#Break example
j=0
for i in range(10):
    j=j+2
    print('i=',i,'j=',j)
    if(j==6):
        break

#Continue example
j=0
for i in range(10):
    j=j+2
    print('i=',i,'j=',j)
    if(j==6):
        continue
    print('j value is  ',j)

#try except similar to try catch in python
try:
    answer=12/0
    print(answer)
except:
    print("some friendly error message")


#Python function example
#define a function
def checkIfPrime(numberToCheck):
    for x in range(2,numberToCheck):
        if(numberToCheck % x==0):
            return False
    return True
print(checkIfPrime(5))

#Fuction returning multiple values
def calculations(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a % b
    return (add,sub,mul,div)
#calling calculations function
output = calculations(40,30)
print("Add Result",output[0])
print("Sub Result",output[1])
print("Mul Result",output[2])
print("Div Result",output[3])

#Generator is a function that returns an iterator
#iterator is something that we can loop through using a looping statement
def calculationsYield(a,b):
    add = a + b
    yield add
    sub = a - b
    yield sub
    mul = a * b
    yield mul
    div = a % b
    yield div
#using a for loop we can loop through the returned value from the function
for value in calculationsYield(30,40):
    print(value)

#demonstrating varible scope
#declaring a global variable
message1 = "Just a global variable"

def myfunction():
    global message1 #in case to modify a global variable inside local area
    print("reached inside function")
    print(message1)
    message2 = "Its a local variable"
    print(message2)
    message1 = "Just modifying the global variable" #cannot modify global variable inside a local area
    print(message1)

myfunction()
#print(message1)
#print(message2) #gives error as it is a local variable

#demonstsrate the arbitary list of arguments into the function
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with folowing toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(12,"pepperoni")
make_pizza(12,"mushrooms","green pepper")

#passing arguments as required and keyword args
def printInfo(name, age):
    print("name:",name)
    print("age:",age)

#calling with required
printInfo("Tom",10)
#calling with keyword arguments
printInfo(age=12,name="Winnie")

#lambda functions in python
sum = lambda num1, num2:num1+num2
#calling the lambda function
print("Sum 2 + 3 =", sum(2,3))

#Python modules 

#importing a module
from random import randrange, randint
#calling function inside the  module
print(randrange(1,10))

#the random built in module
import random
print(random.random())
print(random.randint(5,20))
print(random.choice(["head","tail"]))

myShirtColors = ['blue','red','black','yellow','green']
random.shuffle(myShirtColors)
print(myShirtColors)

random.seed(10)
print(random.random())

#python time module
import time
print(time.time()) #seconds passed from jan 1 1970
print(time.localtime(time.time())) #get the multiple time values as a tuple
time.sleep(5) #delays program executin by specified number of seconds
print(time.asctime(time.localtime(time.time()))) #gives in human readable form

#datetime module
import datetime
print(datetime.datetime.now()) #return current date time object
#Creating custom datetime object 
birthDay = datetime.datetime(2022,7,20)
print(birthDay)
birthDay = datetime.datetime(2022,7,20,10,15,50) #shows date and time
print(birthDay)

#time comparison demo
from datetime import datetime as dt
if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
    print("Working hours")
else:
    print("Shift Completed")

import calendar
myCalendar = calendar.month(2022,7) #get calendar for a month
print(myCalendar)
myCalendar = calendar.prcal(33)#get calendar for a year
print(myCalendar)

import math
#finding the exponential of a number, then its bsolute, then its log, them convert to the base of 10
number = 2e-7
print(math.log(math.fabs(number),10))
print(math.log10(math.fabs(number)))
print(math.pow(4,3))
print(math.floor(15.34254))
print(math.ceil(15.054))
print(math.fabs(-5)) #absolute of the number
print(math.factorial(10))
print(math.modf(3.14)) #returns separated fractional and integer part as a tuple

#calling the custom module created
import prime
answer = prime.checkIfPrime(13)
print(answer)

#rights of a function in python is similar to the rights of a variable

#1. we can assign a function to a variable
def myFunc1():
    print("This is my function 1")
#assign the function to a variable
myMyFunction = myFunc1
myFunc1() #call function directly
myMyFunction() #call via the variable

#2. We can pass a function as an argument into another function
def myFunc2(receivedFn):
    receivedFn()
    receivedFn()
myFunc2(myFunc1)

#3. we can return a function from another function
def returnToUpperFn(str):
    return str.upper()
upperReferene = returnToUpperFn
print(upperReferene("hello world"))

#4. We can define functions inside another function
def outer():
    print("The outer function")

    def firstInner():
        print("First Inner Function")

    def secondInner():
        print("First Second Function")

    firstInner()
    secondInner()
outer()

#5. The inner functions can access the enclosing function variables
def myOuter(myGreeting):
    print("The outer function says",myGreeting)

    def myFirstInner():
        print("First Inner Function says", myGreeting)

    return myFirstInner
myOuterVariable = myOuter("peace to the world")
myOuterVariable()

#Python DECORATORS - a function which accepts another function, enhance it with a wrapper function and return the enhanced function back

#define the decorator
def myDecorator(myFunc):
    def innerWrapper(): #wrapper function 'decorates' the function received
        print("Before the Function Call")
        myFunc()
        print("After the Function Call")
    return innerWrapper
#defining a simple fn to pass into the decorator
def myFnToPass():
    print("A simple function to pass into decorator")
#calling the decorator
myDecoratorDemo = myDecorator(myFnToPass)
#execute the decorator
myDecoratorDemo()

#defining another simple fn to pass into the decorator
#here we are using a more nicer syntax introduced in latest python version
@myDecorator
def newmyFnToPass():
    print("A new simple function to pass into decorator")
newmyFnToPass()

#Define a simple class with a constructor that can aaccept two variables
class Employee:
    #defining a global variabl (data member)
    empCount = 0
    #defining a constructor
    #that can accept two values name and salary
    #save those values into self(self is an instance of the class)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1 #increment the emp count when a new object is created
    #define simple member function
    def displayEmpCount(self):
        print("Total no of employees: ",Employee.empCount)
    #define one more simple member function
    def displayEmployeeDetails(self):
        print("Name: ",self.name)
        print("Name: ",self.salary)

#create an object of employee class
employee1 = Employee('Tom',2000)
#calling the function using the object
employee1.displayEmpCount()
employee2 = Employee('Jerry',3000)
employee2.displayEmpCount()
employee2.displayEmployeeDetails()
employee1.displayEmployeeDetails()
# accessing the variables directly from the class w/o object (not recommended)
print("Total employee count: ", Employee.empCount)


#Demonstrating class INHERITANCE
#creating base class
class Rocket:
    #defining constructor
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    #defining a member function
    def launch(self):
        return "%s has reached %s" %(self.name,self.distance)

#Defining a derived class
class MarsRover(Rocket): #inheriting from the Rocket class
    def __init__(self, name, distance, maker, vehicleCode):
        Rocket.__init__(self, name, distance) #calling the base class constructor
        self.maker = maker
        #define a private varicle
        self.__vehicleCode = vehicleCode

    def printMaker(self):
        return "%s launched by %s" %(self.name, self.maker)

    def getVehicleCode(self):
        return self.__vehicleCode

#Create object(instance) for main class Rocket
x = Rocket("Small rocket", "till stratosphere")
y = MarsRover("mars rover", "till mars", "ISRO", "12345")

print(x.launch())
print(y.launch())
print(y.printMaker())
#due to encapsulation a private variable cannot be accessed directly
#print(y.__vehicleCode)
print(y.getVehicleCode())#this is the correct method to access a private variable


#define the decorator
def myDecorator(myFunc):
    def innerWrapper(): #wrapper function 'decorates' the function received
        print("Before the Function Call")
        myFunc()
        print("After the Function Call")
    return innerWrapper

#defining another simple fn to pass into the decorator
#here we are using a more nicer syntax introduced in latest python version
@myDecorator
def newmyFnToPass():
    #Sample doc string for our newmyFnToPass() funciton
    print("A new simple function to pass into decorator")
newmyFnToPass()

print(newmyFnToPass.__name__)
help(newmyFnToPass)


#Demonstrating class decorating methods in python
#Defining the main class
class Hero:
    #define the decorator @classmethod
    @classmethod
    def say_class_hello(cls): #since it class method, will receive class referene as implicit first argument
        if(cls.__name__ == "HeroSon"):
            print("Hi Prince, called from HeroSon")
        elif(cls.__name__ == "HeroDaughter"):
            print("Hi Princess, called from HeroDaughter")
    #define the decorator @staticmethod
    @staticmethod
    def say_hello():
        print("Hello..")

class HeroSon(Hero):
    def say_son_hello(self): #first implicit arg will be self since it is a regular method
        print("Hello Son from subclass HeroSon")

class HeroDaughter(Hero):
    def say_daughter_hello(self): #first implicit arg will be self since it is a regular method
        print("Hello Daughter from subclass HeroDaughter")

testHeroSon = HeroSon()
testHeroSon.say_class_hello()
testHeroSon.say_hello()

testHeroDaughter = HeroDaughter()
testHeroDaughter.say_class_hello()
testHeroDaughter.say_hello()


class House:
    #constructor
    def __init__(self, price):
        self.__price = price #keeping price as private

    #creting the getter method with the property decorator, for fetching the attribute value in a class
    @property
    def price(self):
        return self.__price

    #creating a setter method decorator, for saving the attribute value in a class
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    #creating a deleter method decorator
    @price.deleter
    def price(self):
        del self.__price

#typical access and update will be like this:
house = House(500000) #create obj
print(house.price) #access attribute
house.price = 1000000 #modifying the attribute
print(house.price) #access attribute
del house.price #delete attribute of the house instance
print(house.price) #access attribute


#File Handling Demo using Python
#opening a file in the same directory
#using open() method get the file object
myfile = open("myfile.txt", "r")
#to read the contents, use the read() method
#print(myfile.read(10))
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())


#A simple example for higher order function which can accept atleast one function and return a function

#a simple fn with a print statement
def greet(name):
    return "Hello {}".format(name)

#defining the higher order fn which can accept fn
def print_greetings(fn,param):
    print(fn(param))

#calling the higher order fn
print_greetings(greet,"Peter!")


#map() fn - a higher order fn which can accept a fn and also a list of iterable params.
#Each param will be applied to the fn and the result will be returned back as a map object
#we can later convert this map into set/tuple

#defining a simple fn
def mymapfunction(a):
    return a*a

#calling the map fn, passing the fn as well as the iterables
x = map(mymapfunction,(1,2,3,4,5))
print(tuple(x))


#using lambda fn in map and the iterables are passed
x = map(lambda x:x*x,(1,2,3,4,5))
print(tuple(x))


#filter function which filters the iterables based on condition it accepts the fn and also the iterables as parameters

#defining a filter condition fuction
def func(x):
    if x>=3:
        return x

#calling the filter fn passing the condition fn and the iterables
y = filter(func,(1,2,3,4))
#converting the returned filter objects to tuple/ list/ set
print(list(y))

#calling the filter fn passing the condition fn and the iterables
y = filter(lambda x:(x>=3),(1,2,3,4))
#converting the returned filter objects to tuple/ list/ set
print(list(y))

#reduce fn to reduce the list of values based on the operation we give
#it will accept the fn (preferably lambda) and the itereables
from functools import reduce
x = reduce(lambda a,b: a+b,[23,21,45,98])
print(x)


#class and regular fns without abstract class
class Lion:
    def give_food(self):
        print("Feeding lion with raw meet")

class Panda:
    def feed_animal(self):
        print("Feeding a panda with bamboo")

class Snake:
    def feed_snake(self):
        print("Feeding a snake with mice")

#creating objects for animals to feed
simba = Lion()
kungfupanda = Panda()
kingkobra = Snake()

#calling the feeding functions
simba.give_food()
kungfupanda.feed_animal()
kingkobra.feed_snake()


#imiporting the abstract class and the decorator ftom the abc module
from abc import ABC, abstractmethod

#declaring the Abstract Base class from ABC
class Animal(ABC):
    @abstractmethod   #decorator for abstract method
    def feed(self,action): 
        pass  #just a placeholder to escape the empty function error

    #define a diet property using the decorator 
    #and abstract method
    @property
    @abstractmethod
    def diet(self): #define diet property
        pass
    
    @property
    def food_eaten(self):  
        #define the food_eaten property
        #food_eaten property's gettter
        return self.__food

    #having the setter for food_eaten
    @food_eaten.setter
    def food_eaten(self,food):
        if food in self.diet:
            self.__food = food    
        else:
            raise ValueError(f"this animal doesn't eat this")
    
    @abstractmethod   #decorator for abstract method
    def do(self,action): #action is an abstract function parameter
        pass  #just a placeholder to escape the empty function error


#class and regular fns inheriting abstract class
class Lion(Animal):
    @property
    def diet(self):
        return ["antelope","cheetah","buffalo"]

    def feed(self):
        print(f"Feeding a lion with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} lion with raw meet at {time}")

class Panda(Animal):
    @property
    def diet(self):
        return ["bamboo","leaves"]

    def feed(self):
        print(f"Feeding a panda with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} panda with bamboo at {time}")

class Snake(Animal):
    @property
    def diet(self):
        return ["mice","rabbit"] 

    def feed(self):
        print(f"Feeding a snake with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} snake with mice at {time}")

simba = Lion()
simba.food_eaten="buffalo"
simba.feed()
kungfupanda = Panda()
kingkobra = Snake()

'''
#instead of calling method repeat like the above,
#we can have a for loop for the list of classes
#It is more efficient method
zoo_class_list = [Lion(), Panda(), Snake()]

for animal in zoo_class_list:
    animal.feed()
    animal.do(action="feeding",time="10am")
'''


#reading contents of file line by line using for loop
myfile = open("myfile.txt", "r")
for line in myfile:
    print(line)

myfile.close()  #we need to close the file cursor or object once we complete the operation associated with it

myfile = open("myfile.txt", "r")
#read all the lines and return as a list
myFileContentsList = myfile.readlines()
print(myFileContentsList)

myfile.close()


#opening the file cursor in append mode
#cotents written will be apppended to the end of the file
myfile = open("myfile.txt", "a")
#write() method is used to write 
myfile.write("humpty dumpty sat on a wall\n")


#opening the file cursor in write mode
#cotents written will be apppended to the end of the file
myfile = open("myfile.txt", "w")
#write() method is used to write 
myfile.write("humpty dumpty sat on a wall\n")


#getting the position of the cursor
myfile = open("myfile.txt", "r")
print("the file pointer is now at ",myfile.tell())
myFileContentsList = myfile.readlines()
print("the file pointer is now at ",myfile.tell())
myfile.close()
#print("the file pointer is now at ",myfile.tell()) gives error as the file is already closed


myfile = open("myfile.txt", "r")
print(myfile.readline())
print("the file pointer is now at ",myfile.tell())

#change the file pointer offset using seek()
myfile.seek(50)
print("the file pointer is now at ",myfile.tell())
myFileContentsList = myfile.readlines()
print(myFileContentsList)
myfile.close()


#renaming a file using python os module
import os
if os.path.exists("myfilenew.txt"):
    os.rename("myfilenew.txt", "myfile.txt")
    print("rename success")
else:
    print("The file doesn't exist")

#deleting the file
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("delete success")
else:
    print("The file doesn't exist")


import os
#create a new directory
#os.mkdir("mydir")
#print current wirking directory
print(os.getcwd())
#change current working directory
os.chdir("mydir")
print(os.getcwd())

#to go back the directory
os.chdir("..")
print(os.getcwd())

#delete directory that we created
os.rmdir("mydir")


import os

#to list files and folders in the directory
result = os.listdir(os.getcwd())
print(result)


#run an external python file (fileoutputsave.py)
#save its results as txt file

import subprocess
with open("myfile.txt","wb") as f:
    subprocess.check_call(["python","fileoutputsave.py"],stdout=f)


#A simple demonstration of exception handling in python
#using the try, except, finally blocks(clause)
try:
    div = 4/0
    print(div)
except ZeroDivisionError:
    print("Cant divide by zero")
except:
    print("sorry some error occured")
finally:
    print("Inside the final statement")


#printing name and details of the exception
try:
    div = 4//2
    print(div)
except Exception as e:
    print("Cant divide by zero")
    print(f"{type(e).__name__} was occurred. More details below: ")
    print(e) #print the entire details of the exception
else: #else executes if try statements are sucessful
    print("division completed and result is ", div)
finally:
    print("Inside the final statement")


#nested try except statements in python: a file handling scenario
try:
    f=open('somefile.txt')
    try:
        f.write("Hello world")
    except:
        print('some write error occurred')
    finally:
        f.close()
except:
    print('the file cannot be opened')


#importing pyodbc module
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-CSCIVVL\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(myConString)

try:
    #get the cursor object
    mycursor = myconn.cursor()

    #using cursor, execute SQL commands
    mycursor.execute('''create table EmployeeMaster3
    (
        Id INT IDENTITY PRIMARY KEY,
        EmployeeCode VARCHAR(10),
        Employeename VARCHAR(25),
        DepartmentCode VARCHAR(10),
        LocationCode VARCHAR(10),
        Salary INT
        )''')
except Exception as e:
    print("Cannot create the table because: ")
    print(f"{type(e).__name__} was occurred. More details below: ")
    print(e)
#myconn.commit()#commiting the transaction required for all write/update/delete statements

for row in mycursor:
    print(row)

employees = [{'empcode':row[1],'empname':row[2]} for row in mycursor.fetchall()]
print(employees)

myconn.close()


#connect py and mssql
# Set-ExecutionPolicy -Scope CurrentUser 
# Unrestricted 
# -ExecutionPolicy Unrestricted
import pyodbc
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-CSCIVVL\SQLEXPRESS;
    Database=employee_db;
    Trusted_Connection=yes;
''')
# try:
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE EmployeeMaster3(
#         Id INT IDENTITY PRIMARY KEY,
#         EmployeeCode VARCHAR (10),
#         EmployeeName VARCHAR (25),
#         DepartmentCode VARCHAR (10),
#         LocationCode VARCHAR (10),
#         Salary INT
#     );
#     ''')
# except Exception as e:
#     print(type(e).__name__)
# # for row in cursor:
# #     print(row)

print("Checkpoint 1")
try:
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM EmployeeMaster;
    ''')
    # for row in cursor.fetchall():
    #    print(row[0],row[2])
    emp=[{'EmployeeCode':row[1],'EmployeeName':row[2]} for row in cursor.fetchall()]
    print(emp)

    # cursor.execute('''
    #     Insert into EmployeeMaster3(EmployeeCode,EmployeeName,DepartmentCode,LocationCode,Salary)
    #     values(?,?,?,?,?);'''
    #     ,('E002','Johnny','D002','L002',20000))
    # cursor.execute('''
    #     Select * from EmployeeMaster3;
    # ''')
    # for row in cursor.fetchall():
    #     print(row)
except:
    print("error in selecting")

conn.commit()
conn.close()

#user raising an exception explicitly for conditions
x=0
if x==0:
    #using raise keyword you can manually raise exception
    raise Exception("The number cant be zero") #this will terminate the program


x="hello"
if not type(x) is int:
    raise TypeError("Int valeus are allowed")


#Creating a user defined Exception Class
#Exceptions should be derived from the built-in exception class

#creating a class inheriting the built-in Exception class
class myError(Exception):
    #creating the constructor
    def __init__(self, value):
        self.value = value
        #the __str__ dunder method
        def __str__(self):
            return(repr(self.value))
#__str__ magic fn is used to get the informal string that represents the object

#using the class that we just created
try:
    x = 0
    if x==0:
        raise(myError("Number cant be zero"))
except myError as error:
    print('A new exception occured:', error)

print('Hello')

#the exception derived class being inherited by another class
class myError(Exception):
    #base class for exceptions
    pass

class DivideByZero(myError):
    pass

try:
    x = 0
    if x==0:
        raise DivideByZero
except DivideByZero:
    print('A new exception occured')

print('Hello')


#magic methods / dunder methods in python
#special methods that are already defined or builtin in the python classes
#We are overloading them to use in our program

#to view the available dunder methods in an object, we can use the dir() method
# print(dir(int)) #shows the dunder methods of the int object in python

# creating a class and its object is implicitly inheritting an Object class which is built into the python interpreter
# when we print() an object, it is actually invoking the dunder repper __repr__() of the built in object class 
# Here is a demo
class Car:
    pass

car = Car()
print(car.__repr__())
# <__main__.Car object at 0x000001BF7FE8AF20> is the output


#if we want to change the behaviour of the dunder repper __repr__() we need to override it in the class
class Car:
    def __repr__(self):
        return f"{self.__class__.__qualname__}"
    

car = Car()
print(car.__repr__())
print(car.__str__())


# math dunder method example
#creating a class called RndomNumbers which can accept two numbers per object
class RandomNumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

#create object for our RandomNumbers
rand_obj_a = RandomNumbers(3,5)
rand_obj_b = RandomNumbers(6,8)

#trying to add the two random numbers
print(rand_obj_a + rand_obj_b)
#above statement gives the error:
#TypeError:unsupported operand type(s) for +: 'RandomNumbers' and 'RandomNumbers' 


#trying to override the __add__dunder method which is called implicitly when we use the '+' operator
class RandomNumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    #override the __add__ dunder method
    def __add__(self,other):
        #returning the sum of two left digits and two right digits converted to random number object
        return RandomNumbers(other.a + self.a, other.b + self.b)

    #to represent as string using __repr__ dunder method
    #overriing the dunder __repr__ function of RandomNumbers class
    def __repr__(self):
        return f"{self.__class__.__qualname__} ({self.a},{self.b})"

rand_obj_a = RandomNumbers(3,5)
rand_obj_b = RandomNumbers(6,8)

print(rand_obj_a + rand_obj_b)


#demonstrating the class dunder methods
#creating a class with empty list of software  names and an empty dict of software name and version as key value pair
class Softwares:
    names = []
    versions = {} #hold the key value pair of sw and sw version

    #defining (overrriding) the constructor
    #invoked when we create an object and give the names list
    # sw1 = Softwares(['ps','msword','mspaint'])
    def __init__(self,names): #getting sw names as a list
        if names:  # if names is not empty
            self.names = names.copy() #create a copy of the list
            for name in names:
                self.versions[name] = 1 #initialie sw version to 1 for all software names
        else:
            raise Exception("Names cant be empty")
    
    #overriding the str dunder for displaying the list of sws
    #will be invoked when calling print(objname)
    #sw1 = Softwares(['ps','msword','mspaint'])
    #print(sw1)
    def __str__(self):
        #loop through the dictionary and print the list
        s="The list of softwares and its versions are: \n"
        for key,value in self.versions.items():
            s += f"{key} : {value} \n"
        return s

    #overriding the __setitem__ dunder method
    #this will be invoked when for eg. sw1['msword']=2
    def __setitem__(self,name,version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("S/w name doesnt exist")

    #overriding the __getitem__dunder method
    #this will be invoked when 
    #print(sw1['msword'])
    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("S/w name doesnt exist")

    #overriding the __delitem__ dunder method
    #this will be invoked when 
    #del sw1['msword']
    def __delitem__(self,name):
        if name in self.versions:
            #delete that item from the dictionary versions
            del self.versions[name]
            #delete the items from the names list
            self.names.remove(name)
        else:
            raise Exception("S/w name doesnt exist")

    #overriding the __len__ dunder method
    #this will be invoked when calling print(len(sw1))
    def __len__(self):
        return len(self.names)

    #overriding the __contains__ dunder method
    #this will be invoked when calling
    #if 'msword' in sw1: if yes, will return true, else false
    def __contains__(self, name):
        if name in self.versions:
            return True
        else:
            return False


#creating the software class object
sw1 = Softwares(['ps','msword','mspaint'])
#print the software class object
print(sw1)
#trying to set new version for msword
sw1['msword']=2
print(sw1)
#tring to print the version number of msword
print(sw1['msword'])
#delete item from dictionary
del sw1['msword']
# #tring to print the version number of msword
# print(sw1['msword'])
#tring to print the length of names list in sw1
print(len(sw1))
#checking if the given sw in sw1
if 'ps' in sw1:
    print("software exists")
else:
    print("s/w doesnt exist")


#create a copy of a list with some processing/condition checks
#without implementing the comprehension just using a loop
words = ["Hello", "world", "how", "are", "you"]
newlist = [] #new list to hold all words with a loop

#traditional for loop is used here:
for word in words:
    if 'o' in word:
        newlist.append(word)

print(newlist)

#we will use list comprehension for the same task
#syntax: [expression for item in iterable if condition]
words = ["Hello", "world", "how", "are", "you"]
newlist = [word for word in words if 'w' in word]
print(newlist)

#using comprehension to generate list of 20 numbers
numlist = [x for x in range(20)]
print(numlist)

numlist = [x for x in range(20) if x<15]
print(numlist)

#using expression to change all the items to upper case
words = ["Hello", "world", "how", "are", "you"]
newlist = [word.upper() for word in words if 'w' in word]
print(newlist)

#generate a new list with item 'hello' for all the items
newlist = ['hello' for word in words]
print(newlist)

newlist = [word if word!="Hello" else "hi" for word in words]
print(newlist)


#Working with csv files using python 
#using the csv module reader() method
import csv  #imiporting the csv module/library

#opening the csv file
file = open("mycsvfile.csv")
#using the csv.reader to read the file obj
csvreader = csv.reader(file)

#declaring empty header and rows list
header = []
rows =[]

#using the next()method to read the current line and stop at the start of next line
header = next(csvreader)
print(header)

#using a for loop read the rows below header
for row in csvreader:
    rows.append(row)
print(rows)

#close the file handler
file.close()
"""

#opening csv file without importing any modules
with open('mycsvfile.csv') as file:
    content = file.readlines()

#using stip to strip the unwanted char
#using the list comprehension
content = [i.strip() for i in content]
#header will be the first index value
header = content[:1]
#rows will be from first index
rows = content[1:]
print(header)
print(rows)

import csv
#performing write to the csv file
header = ['Names','Experience','Salary']
data = [['Anu',9,40000],['Vinu',8,30000],['Manu',5,25000]]

with open('mycsvfile.csv','w',newline="") as file:
    csvwriter = csv.writer(file) #creting the csv writer object
    csvwriter.writerow(header) #write the header contents
    csvwriter.writerows(data) #write the row contents
