# started on 22nd May 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

## DAY -- 1

print("Hello world!")

print("dont print hello world")

print('This is the first worksheet')
print('this is what has to be printed:')
print("print('my first code')")

#printing a new line within same print function (\n)
print('Hello World!\nI\'m Anuraag!')

#String Concatenation
print('Hello' + ' ' + "Anuraag")

#input function
input("What is your name?")

print("Hello! " + input('What\'s your name?') + "!")

#python variables
name = input('What\'s your name?')
print(name)
print(len(name))

#excercise on input functions
a = input("a:")
b = input("b:")
c=a
a=b
b=c
print(a)
print(b)

#variables and input functions project -- for the cursor to show up on the next line

city = input('What\'s the name of the city you grew up in?\n')
pet = input('What\'s your favourite pet animal?\n')
print('You can name your band as ' + city + " "+ pet)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

## DAY -- 2 

# Data types - integers, floats, strings and booleans
# Using underscore helps in visualizing 
123_254 + 143_324

# during string concatenation only strings can be concatenated
num_char = len(input('What\'s your name?'))
print("your name has " + str(num_char) + " letters")
type(num_char)

# coding excercise
number = input('Type a two digit number: ')
first_digit = number[0]
second_digit = number[1]
total = int(first_digit) + int(second_digit)
total = str(total)
print("required output is equal to: " + total)

# different mathematical operations -- +,-,*,/,**(exponent)

# coding exercise
weight = float(input('What\'s your weight in kgs?'))
height = float(input('What\'s your height in meters squared?'))
bmi = weight/(height**2)
print('your bmi is ' + str(bmi))

print(round(8/3))
print(8//3) # floor division

# using an f string
height = 1.4
winning = True
score = 12
print(f"The score is {score}, the height is {height}, the team is winning {winning}")

# coding exericse 
current_age = int(input('What is your current age?'))
days_left = 90*365 - current_age*365
weeks_left = 90*52 - current_age*52
years_left = 90 - current_age

print(f"You have {days_left} days left, {weeks_left} weeks left, {years_left} years left!")

# 2nd day coding project
total_bill = float(input("What was the total bill?"))
total_bill = round(total_bill,2)
percentage = float(input('What is the tip percentage (10/12/15)?'))
people = float(input('How many people should the bill be split in?'))
bill_with_tip = total_bill * ((100+percentage)/100)
per_person = bill_with_tip/people

print(f'The bill per person is: {per_person}')


#--------------------------------------------------------------------------------------------------------------------------------------------------------

# DAY -- 3 

# Conditionals - if and else statements

print('welcome to the rollercoaster ride')
height = int(input('What is your height in cms?'))

if height>120:
    print('You can\'t ride the rollercoaster')
else:
    print('You can ride the rollercoaster')

# one (=) sign is for assigning , two (==) sign is for checking the equality

# coding assignment (modulus operator)

x = float(input('Type the number you want to check'))
x_modulus = x%2

if x_modulus == 0:
    print('The number is even')
else:
    print('The number is odd')

# Nested if else statements

print('welcome to the rollercoaster ride')
height = int(input('What is your height in cms?'))
age = int(input('Type your age'))

if height>120:
    print('You can ride the rollercoaster')
    if age <12:
        print('You have to pay 12 dollars')
    elif age>12 and age<18:
        print('You have to pay 15 dollars')
    else:
        print('You have to pay 25 dollars')
else:
    print('You can\'t ride the rollercoaster')

# coding excercise

weight = float(input('Type your weight in kgs'))
height = float(input('Type your height in ms'))

bmi = weight / (height**2)

if bmi<18:
    print('You are underweight')
elif bmi>18 and bmi<25:
    print('You have a normal weight')
elif bmi>25 and bmi<30:
    print('You are overweight')
else:
    print('You are obese')

# Coding assignment

year = int(input('Type the year you want to check whether its leap or not\n'))


if year%4 == 0:
    if year%100 == 0 and year%400 == 0:
        print('This is a leap year')
    elif year%100 == 0 and year%400 !=0:
        print('This is not a leap year')
    else:
        print('This is a leap year')
else:
    print('This is not a leap year')


# if statements in succession

print('Welcome to the roller coaster ride')
height = int(input('Type your height in cms'))
age = int(input('type your age'))
wants_photo = input('Do you want a photo [Yes/No]')
bill = 0

if height>120:
    if age<10:
        print('Sorry you cannot get onto the rollercoaster because of your age')
    elif age>10 and age<20:
        bill = bill+10 # 10 dollars
        print('Your rollercoaster ride costs 10 dollars')
    elif age>20 and age<30:
        bill = bill+20 # 20 dollars
        print('Your rollercoaster ride costs 20 dollars')
    else:
        bill = bill+30 # 30 dollars
        print('Your rollercoaster ride costs 30 dollars')
    if wants_photo == "Yes":
        bill = bill + 20 # 20 dollars for photo
        print('Your photo costs 20 dollars')
    else:
        print('You have not opted for photo')
else:
    print('You cannot get onto the rollercoaster because of your height')

print(f"Your total bill is {bill}")


# coding assignment

pizza_type = input('What type of pizza do you want? [S/M/L]')
pepperoni = input('Do you want pepperoni? [Yes/No]')
extra_cheese = input('Do you want extra cheese? [Yes/No]')
bill = 0

if pizza_type == 'S':
    print('You have ordered a small pizza')
    bill = bill + 15
    if pepperoni == "Yes":
        print('you have ordered for pepperoni along with pizza')
        bill = bill+2
    elif pepperoni == 'No':
        print('Your pizza does not contain pepperoni')
    if extra_cheese == 'Yes':
        print('Your pizza has extra cheese')
        bill = bill+1
elif pizza_type == 'M':
    print('You have ordered a medium type pizza')
    bill = bill + 20 
    if pepperoni == "Yes":
        print('you have ordered for pepperoni along with pizza')
        bill = bill+3
    elif pepperoni == 'No':
        print('Your pizza does not contain pepperoni')
    if extra_cheese == 'Yes':
        print('Your pizza has extra cheese')
        bill = bill+1
elif pizza_type == 'L':
    print('You have ordered a large type pizza')
    bill = bill + 25 
    if pepperoni == "Yes":
        print('you have ordered for pepperoni along with pizza')
        bill = bill+3
    elif pepperoni == 'No':
        print('Your pizza does not contain pepperoni')
    if extra_cheese == 'Yes':
        print('Your pizza has extra cheese')
        bill = bill+1
else:
    print('you have not placed your order correctly')

print(f'Your total bill is {bill}')


# coding assignment 

print('welcome to the love calculator!')
name1 = input(str('Write down the first name'))
name2 = input(str('Write down the second name'))
lname1 = name1.lower()
lname2 = name2.lower()
final_name = lname1 + lname2
t_count = final_name.count('t')
r_count = final_name.count('r')
u_count = final_name.count('u')
e__count = final_name.count('e')
l_count = final_name.count('l')
o_count = final_name.count('o')
v_count = final_name.count('v')
e_count = final_name.count('e')

sum1 = t_count + r_count + u_count + e_count
sum2 = l_count + o_count + v_count + e_count

sum1_str = str(sum1)
sum2_str = str(sum2)
final_sum = sum1_str + sum2_str

final_sum_int = int(final_sum)

if final_sum_int<10 or final_sum_int>90:
    print(f'You go together like Coke and Mentos, your score is {final_sum_int}')
elif final_sum_int>40 and final_sum_int<50:
    print(f'You are alright together, your score is {final_sum_int}')
else:
    print(f'You both are useless together, your score is {final_sum_int}')


# coding assignment 

print("welcome to treasure island")

lorr = input('Where do you want to go first [L/R]')
if lorr == "L":
    sorw = input('Do you want to swim or wait [S/W]')
    if sorw == "W":
        door = input('Which door you want to go through [R/Y/B]')
        if door == "Y":
                print('You won the game')
        else:
                print("Game over")
    else:
        print('Game Over')            
else:
    print('Game over')


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# DAY - 4 

# Randomization - degree of unpredictability - most useful in games - MERSENEE TWISTER - Algo behind this 
# Random - its a python module - what is a module - it helps in splitting the different functionalities of your program for easier coding and understanding. 

from lib2to3.pygram import Symbols
import numbers
from posixpath import split
import random
from re import L
from tkinter import N
c = random.randint(100,200) # gives random integer - inclusive of both. 
d = random.random() # gives a number between 0 and 1. 

# if you need random numbers from 0 to 5 then use the multiplication
e = random.random()*5
e # e will always be equal to or greater than 0 and less than 5.

# Coding excercise

print('Welcome to heads or tails')
c = random.randint(0,1)
if c == 0:
    print('The toss is heads')
else:
    print ('The toss is tails')

# Simple variables store only 1 peice of data. 
# Python Lists - Data Structure - These store grouped peices of data  
# They can have mixed data types - syntax matters [] - items are separated by a comma 
# They have an order - the order is determined by the order in the list
# List starts from 0 - because the first item has no offset and the second item has 1 offset from the beginning 

states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey']
print(states_of_america[2])
states_of_america[2] = 'Arizona'
states_of_america
states_of_america.append('Alaska')  # adds the next item at the end of the list
states_of_america.extend(['Hawaii', 'California'])  # adds a new list of items at the end of the list
states_of_america 

# Coding excercise - randomly assign best state in America
best = random.choice(states_of_america)
best 

print(len(states_of_america))
# Index error usually occurs with lists 

# Nested lists  - list within a list

fruits_and_veggies = [['Strawberries','Apples','Banana'],['Spinach','Tomato','Potato']]
fruits_and_veggies[0][1]

# Coding assignment

row1 = [' ', ' ',' ']
row2 = [' ', ' ',' ']
row3 = [' ', ' ',' ']

map = [row1,row2,row3]
print(f"{row1}\n {row2}\n {row3}")

c = random.randint(1,3)
d = random.randint(1,3)

print(f"c is {c} and d is {d}")

map[c][d] = 'X'
print(f"{row1}\n {row2}\n {row3}")


# Coding Assignment - rock paper scissors game

c = int(input('Rock - 0, Paper - 1, Scissors - 2'))
d = int(random.randint(0,2))
c
d

if c == d:
    print('Its a tie')
elif c==0 and d== 1:
    print('You have won')
elif c==0 and d== 2:
    print('You have won')
elif c == 1 and d == 0:
    print('You have lost')
elif c == 1 and d == 2:
    print('You have lost')
elif c == 2 and d == 0:
    print('You have lost')
elif c == 2 and d == 1:
    print('You have won')
else:
    print('Your code is wrong')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# DAY 5 - Python Loops

# Loops - things that have to happen over again
# for loop - in combination with lists

fruits = ['Apple', 'Bananna', 'Orange']

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
fruit # the last fruit will become the value assigned to the variable fruit

# Coding excercise

# Giving an input of student heights
stud_heights = input('Input a list of student heights').split()
stud_heights
for n in range(0,len(stud_heights)):
    stud_heights[n] = int(stud_heights[n])
print(stud_heights)

total = 0
for n in stud_heights:
    total += n 
average_height = total / len(stud_heights)
print(f"the average height of the students is {average_height}")


# Code assignment - get the highest score as output without using max min functions

scores = input('Type the scores obtained by the students').split()
for a in range(0, len(scores)):
    scores[a] = int(scores[a])
print(f'these are the final scores: {scores}')

highest_score = 0
for a in scores:
    if a > highest_score:
        highest_score = a

print(f'the Highest score is {highest_score} ')

# Using for loops with the range function

for number in range(10,200):       # does not include 200 
    print(number)

for number in range(10,200,4):       # step by 4 
    print(number)

total = 0 
for number in range(10,20,3):
    total += number
total

# coding assignment 
total = 0
for number in range(0,101,2):
    total += number
total


# coding assignment - Fizz buzz challenge -- usually asked in interviews

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# random password generator


list_of_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_of_letters.extend(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
list_of_numbers = [str(i) for i in range(10)]
list_of_symbols = ("!","@", "$", "%", "^", "&", "*", "(", ")", "_", "+" )

letters = int(input('How many letters do you want in your password'))
symbols = int(input('How many symbols do you want in your password'))
numbers_ = int(input('How many numbers do you want in your password'))

import random

letters_total = ''
random_letters = random.choices(list_of_letters,k=letters)

for a in random_letters:
    letters_total +=a 

numbers_total = ""
random_numbers = random.choices(list_of_numbers,k=numbers_)

for b in random_numbers:
    numbers_total +=b 

symbols_total = ""
random_symbols = random.choices(list_of_symbols,k=symbols)

for c in random_symbols:
    symbols_total +=c 

final_password = letters_total+symbols_total+numbers_total

list_1 = []
for a in final_password:
    list_1[:0] = a

shuffled_final_password = ""
random.shuffle(list_1)

for a in list_1:
    shuffled_final_password += a

print(f'your shuffled final password is {shuffled_final_password}')


# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# DAY - 6 - Python Kernel, Code blocks, While Loops and Functions

# Making our own function

def my_func():
    print('Hello')
    print('Bye')
my_func()

# While loops - loop that continues when a particular condition is True
# Sometimes while loops become endless and the program crashes.  - infinite loop 

## USED REBORG WORLD FOR LEARNING LOOPS

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# DAY - 7 - HANGMAN PROJECT

# Breaking down a long program into parts - FLOW CHART PROGRAMMING 

# Steps according to me
# input for the letter
# input the word
# if letter not in the word, then give a new hangman output
# if the letter is in the word, replace the blank with the letter

# making a list of random words

words = ['Audi', 'Mercedes', 'Porsche']

import random
random_word = random.choice(words)
random_word

l=0
h = ""
while l<len(random_word):
    guess = str.lower(input('Guess the letter:'))
    for letter in random_word:
        if letter == guess:
            h = 'Right Answer'
            print('Right answer')
        else:
            print('wrong answer')  # Letters might repeat.. therefore, else is inside the loop
    display_list = ["_"]*len(random_word)
    n = 0 # if answer is right
    if h == 'Right Answer':
        while n<len(random_word):
            for a in random_word:
                if random_word[n] == guess:
                    display_list[n] = guess
                else:
                    n += 1
    print(display_list)


guess = str.lower(input('Guess the letter:'))
for letter in random_word:
    if letter == guess:
        h = 'Right Answer'
        print('Right answer')
    else:
        print('wrong answer')  # Letters might repeat.. therefore, else is inside the loop
display_list = ["_"]*len(random_word)
n = 0 # if answer is right

if h == 'Right Answer':
    while n<len(random_word):
        for a in random_word:
            if random_word[n] == guess:
                display_list[n] = guess
            else:
                n += 1
print(display_list)
n














