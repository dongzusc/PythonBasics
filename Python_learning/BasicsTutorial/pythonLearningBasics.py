
#"""
#Created on Fri Mar 20 19:34:31 2020

#@author: Donaldlax
#"""

#############################################
## Beginner Tutorial
#############################################

#  Madlibs

part_of_the_body = input("input a part of the body: ")
adjective1 = input("input an adjective: ")
print("You would think that the Girls' lanai would be 
the perfect place to relax and clear your "+part_of_the_body+",")
print("but it seems that something " + adjective1 +" is always happening out there!")
print("I went to the Zoo")
adjective_1 = input("input an adjective: ")
noun_1 = input("input an animal: ")
verb_1 = input("input a verb(past form): ")
adverb_1 = input("input an adverb: ")
adjective_2 = input("input an adjective: ")
noun_2 = input("input a place: ")
print(\n + "Today I went to the zoo.")
print("I saw a(n) " + adjective_1 + " " + noun_1 + " jumping up and down in its tree.")
print("He " + verb_1 + " " + adverb_1 + " through the large tunnel that led to its " + 
adjective_2 + " " + noun_2 + ".")

#############################################

#  "if" with comparison and "return"

def max_num(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else: 
        return num_3

num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
num3 = float(input("Input the third number: "))
Max_num = str(max_num(num1,num2,num3))

print(":" + Max_num)

#############################################

#  Dictionary

WeekDayConvert = {
        "Mon" : "Monday",
        "Tue" : "Tuesday",
        "Wed" : "Wednesday",
        "Thu" : "Thursday",
        "Fri" : "Friday",
        "Sat" : "Saturday",
        "Sun" : "Sunday",
        }

print (WeekDayConvert["Mon"])
print (WeekDayConvert.get("Mon", "Not a valid key"))

#############################################

# while loop

n = int(input("input a number: "))
i = 1
while i <= n:
    print(i)
    i = i + 1
print (n + 1)
print ("finished printing 1 to " + str(n))

#############################################

# while loop and guess game

key_word = "donaldlax"
guess = ""

guess = input("Enter your first guess: ")

while guess != key_word:
    guess = input("Enter another guess: ")#don't make an endless loop
    
    
print("You've guessed it!")

#############################################

# guess game with limit number of guesses

key_word = "Donny"
guess = ""
guess_count = 1
#this could be 0
guess_count_limit = 5
out_of_guesses = False

guess = input("Enter your first guess: ")
guess_count += 1

while guess != key_word and not(out_of_guesses):
    if guess_count <= guess_count_limit:
        #when start from 0, use "<" instead of "<="
        guess = input("Enter another guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("No more guesses, you've failed.")
else:
    print("You win!")

#############################################

# "for" loop examples

# Ex. 01: string
for a_letter in "Donald Lax":
    print(a_letter)
    
# Ex. 02: array
girls = ["Abby", "Becky", "Cathy"]
for index in girls:
    print(index + " loves me!")

# Ex. 03: range
girls = ["Abby", "Becky", "Cathy"]
numbers = len(girls)
for x in range(numbers):
    print(girls[x]+" loves you!")
    
# Ex. 04: try it out
amount = input("Enter an integer: ")
for x in range(int(amount)):
    print(x+1)


# Ex. 04: exponent function

base_num = float(input("Enter a base number: "))
power_num = int(input("Enter a power: "))
def exponent_func(base,power):
    result = 1
    for i in range(power):
        result = result * base
    return result
print(str(base_num)+" to the power of " + str(power_num) + 
" is " + str(exponent_func(base_num,power_num)))

#############################################

# 2D list

num_grid = [
        [1,3,5],
        [2,4,6],
        [3,6,9],
        [0]
        ]
print(num_grid[2][1]) ##index start from 0

#############################################

# nested "for" loops(for loops in for loops)

for row in num_grid:
    for column in row:
        print(column + 1)

#############################################

# Simple replacements

# rules: vowels -> "(^_^)"; e.g. cat -> c(^_^)t, Ant -> [^_^]nt

def replace_func(phrase):
    new_phrase = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                new_phrase = new_phrase + "[^_^]"
            else:
                new_phrase = new_phrase + "(^_^)"
        else:
            new_phrase = new_phrase + letter
    return new_phrase

print(replace_func(input("Enter a new phrase: ")))

#############################################

# try and except

try:
    divisor = float(input("Enter a number: ")) # error: input is a string
    inverse = 1/divisor # error: 1/0
    print("The inverse of " + str(divisor) + " is " + str(inverse) + ".")
    
except ZeroDivisionError as err: # takes care of 1/0
    print(err)
except ValueError as err: #takes care of num/str.
    print(err)

print ("The square of " + str(divisor) + " is " + str(divisor ** 2) + ".")

#############################################

# "read" functions and reading files, better as .txt

sample_read_only = open("sample_data.csv","r")
sample_write_only = open("sample_data.py","w")
sample_read_and_write = open("sample_data.py","r+")
sample_appendix = open("sample_data.py","a")
print(sample_read_only.readable()) #if the file is readable, return True

row = sample_read_only.readlines() #readlines() function show a list.
print(row)

row_1 = sample_read_only.readlines()[1] 
print(row_1)

for rows in sample_read_only.readlines(): #print the list by item
    print(rows)

sample_read_only.close() #pair open with .close()

#############################################

# "read" functions and appending, to the end. Use less.

sample_a = open("sample_data.csv", "a")

sample_a.write("\n5,36,0")

sample_a.close()

#############################################

# "read" functions and writing (create a new file first)

sample_w = open("sample_data_1.csv", "w") #creating new file, with name#

sample_w.write("this is a new file")

sample_w.close()

#############################################

# Modules
import modules as md
import numpy as np
import pandas as pd
import matplotlib as plt

r = np.random
print (r)

#############################################

# Classes and Objects

from Classes import Student

student_1 = Student("Jim", "math", 18, 3.1, True)
student_2 = Student("Sam", "econ", 19, 2.5, False)
#print (student_2.gpa)

student_list = [1,2]
student_list[0] = student_1.age
student_list[1] = student_2.age
print(student_list)

#############################################

# A multiple choice quiz

Question_Prompts = [
    "How many states are in the U.S.?\n(a) 55\n(b) 45 \n(c) 50\n",
    "What is the color of the sky in a sunny day?\n(a) blue\n(b) red\n(c) green\n",
    "The port side of a ship is right.\n(T) True\n(F) False\n"        
        ]# the questions and choices

from Classes import Questions

#class Questions:
#    def __init__(self, question_prompt, answer):
#        self.question_prompt = question_prompt
#        self.answer = answer
    
Quiz1 = [
        Questions(Question_Prompts[0], "c"),
        Questions(Question_Prompts[1], "a"),
        Questions(Question_Prompts[2], "F"),
        ] # an array of Question classes

def start_quiz(quiz):
    score = 0
    is_passed = False
    for question in quiz:
        answer = input(question.question_prompt + "\nAnswer: ")
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + " out of " + str(len(quiz)) + " correct!")
    if score >= 2:
        print("\nYou Passed!")
        is_passed = True
    else:
        print("\nYou failed!")

start_quiz(Quiz1)

#############################################

# Class/Object functions

from Classes import Student

student_1 = Student("Jim", "math", 18, 3.1, True)
student_2 = Student("Sam", "econ", 19, 2.5, False)
student_3 = Student("Tom", "busi", 20, 3.8, True)

List = [
        student_1,
        student_2,
        student_3
        ]

for student in List:
    if student.is_good() == True:
        print(student.name + " is a good student, with a gpa of " 
              + str(student.gpa) + "!")
        print(student.name + " is a " + str(student.year()) + " student.")
    else:
        print(student.name + " is not a good student, with a gpa of only " 
              + str(student.gpa) + "!")
        print(student.name + " is a " + str(student.year()) + " student.")

#############################################

# Inheritance of class

from Classes import Chef, ChineseChef

myChef = Chef()
myChef.make_chicken()
print("\n")
myChineseChef = ChineseChef()
myChineseChef.make_special()

##############################################





