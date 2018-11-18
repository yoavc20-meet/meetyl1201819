#problem1
'''
import tkinter as tk
from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ("Arrr!"):
    print("Go away, pirate.")
elif():
	print("Greetings, hater of pirates!")
'''
#problem2

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).
'''
import tkinter as tk
from tkinter import simpledialog

year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin? ", parent=tk.Tk().withdraw()))
if(year <= 1900):
    print ("Woah, that's the past!")
elif((year > 1900) and (year < 2020)):
	print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
'''
#problem 3
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".
'''
class Person(object):
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
  def speak(self):
  	print("My name is " +  self.first_name + " " + self.last_name)
me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
'''
#problem 4
import tkinter as tk
from tkinter import simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average    Grade
# 90+    A
# 80-89    B
# 70-79    C
# 60-69    D
# 0-59    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.
'''
exam_one = int(simpledialog.askstring("Input", " exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input", "exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring("Input", "exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two, exam_three]

sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":
    print("Student is failing.")
else:
    print ("Student is passing.")
'''

#problem 5
'''
class Person(object):
   def __init__(self, name, fav_food, age, color):
       self.name = name
       self.fav_food = fav_food
       self.age = age
#def define_color(self, color):
       self.color = color

   def print_info(self, color):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16, "black")
#a.define_color("Black")
a.print_info(a.color)

b = Person("Jake", "cookies", 15, "red")
b.print_info(b.color)
'''
#problem 6
'''
class Bear(object):
    def __init__(self, name):
       self.name = name
       print("A new bear created. Its name is:"  + self.name)
    
    def say_hi(self):
        print("Hi! I’m a bear. My name is" + self.name)
my = Bear("Danny")
my.say_hi()
'''
#problem 7
'''
balloons = 5
name = "Ron"
color = "Yellow"
print("This is a tale about " + str(balloons) + " balloons. The first kid is " + name + " who got a " + color + " balloon")
'''
#problem 8
'''
class Cake(object):
    def __init__(self, flavor):
        self.flavor = flavor

    def eat(self):
        print("Yummy!!! Eating a" + self.flavor + " cake" )

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
'''
#problem 9 
class Cat(object):
	def __init__(self, age, name):
		self.name = name
		self.age = age 
	def birthday(self, age):
		self.age += 1
		if self.age >= 100:
		    print("Dong dong, the cat is dead!")
		else:
			print(self.name + " is having its " + str(self.age) + " birthday!")

my_cat = Cat(52, "Salem")
my_cat.birthday(8)
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)




