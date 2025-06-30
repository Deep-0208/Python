# from datetime import datetime
# import datetime
# import math

# # Q1. Add single-line and multi-line comments to explain the purpose of this code block:

# name = "Alice"  # this is for name
# age = 25  # this is for age
# height = 5.6  # this is for height
# is_student = True  # this is for true of false

# # Q2. Define variables with these data types:

# Integer = int(10)

# Float = float(40.44)

# Boolean = True

# String = "hey"

# NoneType = None

# # Q3. Write a program that takes a user's name and prints:
# '''
# Name in uppercase
# Number of characters in name
# First 3 letters'''

# name = input("enter your name : ")
# print(name.capitalize())
# print(len(name))
# print(name[0], name[1], name[2])

# # Q4. Combine two strings "Python" and "Programming" with a space in between.

# str1 = "Python"
# str2 = "Programming"

# print(str1 + " " + str2)

# # Q5. Create a list of your 5 favorite fruits. Then:
# '''
# Add one fruit
# Remove the third fruit
# Print the length of the list'''

# list = ["Apple",
#         "Banana",
#         "Mango",
#         "Orange",
#         "Grapes"
#         ]
# list.append("KIWII")
# list.remove(list[2])
# print(len(list), list)

# # Q6. Create a tuple of 3 cities you want to visit. Try to change one city – what happens? Explain.

# # Q7. Create a dictionary of student info:
# '''student = {
#     "name": "John",
#     "age": 20,
#     "course": "Python"
# }'''

# '''Print only the values
# Add a new key "grade" with value "A"
# Remove "age" from the dictionary'''

# student = {
#     "name": "John",
#     "age": 20,
#     "course": "Python"
# }

# print(student.values())
# student["grade"] = "A"
# # del student["age"]
# student.pop("age")
# print(student)

# # Q9. Use the math module to:
# '''
# Print the square root of 16
# Find the value of π (pi)'''


# print(math.sqrt(16))

# # BONUS: Mini Project
# '''
# Write a small Python script that:

# Asks the user for their name, age, and favorite color.

# Stores this in a dictionary.

# Adds the current year using the datetime module.

# Prints a sentence like:
# Hello Alice, you are 25 years old and your favorite color is Blue. Year: 2025.
# '''

# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age : "))
# favColor = input("Enter Your Favorite Colour : ")
# now = datetime.now()
# year = now.year

# person = {
#     "Name": name,
#     "Age": age,
#     "Favorite Colour": favColor
# }

# print(f"Hello {name}, you are {age} years old and your favorite color is {favColor}. Year: {year}.")


# # Q10. Write a program to check if a number is:
# '''
# Positive, Negative, or Zero
# Even or Odd
# '''

# n = int(input("Enter Numbr :"))
# if (n > 0):
#     print(f"Number {n} is Positive")
#     if (n % 2 == 0):
#         print(f"Number {n} is even number  ")
#     else:
#         print(f"Number {n} is odd number  ")
# elif (n < 0):
#     print(f"Number {n} is Negative")
# elif (n == 0):
#     print("It is zero")


# # Q11. Print a pattern like this using loops (take input from user):
# '''
# *
# **
# ***
# ****
# '''
# n = int(input("Enter Numbr :"))

# for i in range(1, n + 1):
#     print("*"*i)
#     i += 1

# # Q12. Write a program to find the factorial of a number using:
# '''
# a loop

# recursion
# '''
# # using loop --->>

# # 3 =  3 x 2 x 1
# n = int(input("Enter Numbr :"))

# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
#     '''
#     1 = 1 * 1 = 1
#     1 = 1 * 2 = 2
#     2 = 2 * 3 = 6
#     '''
# print(fact)

# # using recursion  -- >>


# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return n*factorial(n-1)


# print(factorial(3))

# # Q13. Create a function that:
# ''''
# Takes a list of numbers

# Returns the sum and average

# Call this function with different inputs
# '''


# def sun_and_avg(n):
#     if (n == 0):
#         return 0, 0

#     total = sum(n)
#     print(f"sum is {total}")
#     avg = sum(n)/len(n)
#     print(f"avg is {avg}")

#     return sum, avg


# sun_and_avg([10, 10, 10, 10])

# # Q.14 Write a recursive function to calculate the n-th Fibonacci number


# def fibonacci(n):
#     if (n <= 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input("Enter Numbr :"))
# print(f"The fibonacci of {n}th is {fibonacci(n)}")

# # Q15. Create a text file named info.txt and write 3 lines:

# '''
# Name, age, and hobby
# Now, write a program to:

# Read the file and print its contents

# Count how many lines are in the file
# '''

# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))
# hobby = input("Enter Your Hobby :")

# with open("info.txt", "w+") as f:
#     f.write(f"Name: {name}\n")
#     f.write(f"Age: {age}\n")
#     f.write(f"Hobby: {hobby}\n")


# with open("info.txt") as f:
#     content = f.read()
#     print(content)
#     f.seek(0)
#     lines = f.readlines()
#     print("Number of lines in file:", len(lines))

# # Q16. Write a program that:
# '''
# Takes user input (name and feedback)

# Appends it to a file called feedback.txt

# Reads and displays all feedbacks
# '''

# name = input("Enter Your Name: ")
# feedback = input("Enter a feedback: ")

# with open("feedback.txt", "a") as f:
#     f.write(f"Name : {name}\n")
#     f.write(f"feedback : {feedback}\n")
#     f.write("-"*30 + "\n")

# with open("feedback.txt", "r") as f:
#     data = f.read()
#     print(data)

# # Q17. Student Marksheet Generator (Full Program)
# '''
# Build a Python program that:
# - Takes input for 3 subjects and their marks
# - Stores them in a dictionary
# - Calculates total, average, and grade using conditionals
# - Writes the result to a file report.txt
# - Reads and displays the saved report
# '''


# def total_avg_grade(physicsMark, mathMark, chemistryMark):
#     totalMark = physicsMark + mathMark + chemistryMark
#     avg = totalMark / 3
#     grade = ""
#     if totalMark >= 85:
#         grade = "A"
#     elif totalMark >= 60:
#         grade = "B"
#     else:
#         grade = "C"
#     return totalMark, avg, grade


# # User inputs
# name = input("Enter Student Name: ")
# physicsMark = int(input("Enter Physics mark: "))
# mathMark = int(input("Enter Math mark: "))
# chemistryMark = int(input("Enter Chemistry mark: "))

# # Creating dictionary
# subject_marks = {
#     "Physics": physicsMark,
#     "Chemistry": chemistryMark,
#     "Math": mathMark
# }

# # Calculating total, average, and grade
# totalMark, avg, grade = total_avg_grade(physicsMark, mathMark, chemistryMark)

# # Writing results to the file
# with open("report.txt", "a") as f:
#     f.write(f"\nStudent Name: {name}\n")
#     f.write(str(subject_marks) + "\n")
#     f.write(f"Total Marks: {totalMark}, Average: {avg:.2f}, Grade: {grade}\n")

# # Reading and displaying the saved report
# print("\nSaved Report:\n")
# with open("report.txt", "r") as f:
#     print(f.read())

# # ✅ OOP Practice Problems

# # 🔸 Q1. Create a Student class
# '''Attributes: name, age, grade

# Method: display_info() - prints all attributes'''


# class Student:
#     def __init__(self, name, age, grade):  # Constructor method
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def show_info(self):
#         print(f"Student Name is {self.name}")
#         print(f"Student age is {self.age}")
#         print(f"Student grade is {self.grade}")


# std = Student("deep", 18, "A")
# std.show_info()

# # 🔸 Q2. Use Constructor (__init__)
# '''
# Modify Student class to accept data via constructor

# Create two student objects and display their data
# '''


# class Student:
#     def __init__(self, name, age, grade):  # Constructor method
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def show_info(self):
#         print(f"Student Name is {self.name}")
#         print(f"Student age is {self.age}")
#         print(f"Student grade is {self.grade}")
#         print(f"-"*20)


# studen1 = Student("Deep", 18, "A")
# studen2 = Student("Komal", 19, "A+")

# studen1.show_info()
# studen2.show_info()

# #  Q3. Class vs Instance Attribute
# '''
# Add a class attribute: school = "ABC School"

# Print it from object and class
# '''


# class Student:
#     school = "ABC School"

#     def __init__(self, name, age, grade):  # Constructor method
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def show_info(self):
#         print(f"Student Name is {self.name}")
#         print(f"Student age is {self.age}")
#         print(f"Student grade is {self.grade}")
#         print(f"Student is From  {Student.school}")


# std = Student("deep", 18, "A")
# std.show_info()

# # for Instance
# studen1 = Student("Komal", 19, "A+")
# # accsing from new object
# print(studen1.school)

# # 🔸 Q4. Encapsulation Example
# '''
# Make the grade attribute private (__grade)

# Create get_grade() and set_grade() methods to access it
# '''


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grade = "A"

#     def get_grade(self):
#         print(f"grade is {self.grade}")

#     def set_grade(self, grade):
#         self.grade = grade

#     def show_info(self):
#         print(f"Student Name is {self.name}")
#         print(f"Student age is {self.age}")
#         print(f"Student grade is {self.grade}")


# std = Student("deep", 18)
# std.get_grade()
# std.set_grade("A++")
# std.get_grade()

# # 🔸 Q5. Inheritance
# '''
# Create class Employee with name, salary

# Create class Manager that inherits from Employee, adds department

# Add method to show full details
# '''


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Department : {self.department}")


# emp1 = Employee("Alice", 50000)
# print("Employee Details:")
# emp1.show_details()

# print("\nManager Details:")
# mgr1 = Manager("Bob", 80000, "Sales")
# mgr1.show_details()


# # 🔸 Q6. Polymorphism
# '''
# Create classes Circle and Square
# Both have a method .area(), return respective area

# Create a function print_area(shape) that works for both
# '''

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square:
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2


# def print_area(shape):
#     print(f"The area is: {shape.area()}")

# # 🔸 Q7. Abstraction (Using ABC)
# '''
# Create an abstract class Vehicle with abstract method move()

# Create Car and Bike classes that implement move()
# '''

# from abc import ABC , abstractmethod

# class Vehicle(ABC) :

#     @abstractmethod
#     def move(self):
#         pass

# class Car(Vehicle):

#     def move(self):
#         print("Car has 4 - wheels")

# class Bike(Vehicle):

#     def move(self):
#         print("Bike has 2 - wheels")


# car = Car()
# car.move()

# bike = Bike()
# bike.move()

# # 🏗️ Mini Project: Bank Account Management System (OOP-Based)
# '''
# 🎯 Features:
# Create account (name, number, balance)

# Deposit amount

# Withdraw amount

# Check balance
# '''

# class Account :
#     def __init__(self,name,number,balance):
#         self.name = name
#         self.number = number
#         self.balance = balance

#     def Deposite(self,amount):
#         self.amount = amount
#         self.balance = self.balance + self.amount
#         print(f"{self.amount} is added and total balance is {self.balance}")

#     def Withdraw(self,amount):
#         self.amount = amount
#         self.balance = self.balance - self.amount
#         print(f"{self.amount}RS. Withdarw Successfull and total balance is {self.balance}")

#     def CheckBalance(self):
#         print(f"Current Balance is {self.balance}")

# a = Account("deep" , 3636 , 10000)
# a.CheckBalance()
# a.Deposite(10000)
# a.Withdraw(10000)

# ✅ LEVEL 1: Logic & Flow Practice

# # 1. Write a program that reverses a number (e.g. 123 → 321)

# num = int(input("Enter number"))
# rev = 0

# while (num > 0):
#     digit = num % 10 #FOR ACCESSING LAST DIGIT OF THE NUMBER
#     rev = rev*10 + digit # ADDING LAST NUMBER TO REV VAR
#     num //= 10  #REMOVE LAST NUMBER TO VAR NUM

# print(f"Reverse number is ", rev)

# # 2 . Count the digits, sum of digits of a number
# num = int(input("Enter number"))
# count = 0
# sum_of_digits = 0
# temp = num

# while (temp > 0):
#     digit = temp % 10
#     sum_of_digits += digit
#     count += 1
#     temp //= 10

# # Check if a number is palindrome (e.g. 121 → yes)
# num = int(input("Enter numberc : "))
# original = num
# rev = 0

# while (num > 0):
#     digit = num % 10
#     rev = rev*10 + digit
#     num //= 10

# if (rev == original):
#     print("Number is palindrome ")
# else:
#     print("Number is no  palindrome ")


# # 3 . Print all Armstrong numbers between 1 and 1000
# '''🔍 What’s the goal?
# A number is Armstrong if sum of cube of digits = number itself
# e.g., 153 = 1³ + 5³ + 3³ = 153'''


# num = int(input("Enter number : "))

# for num in range(1, 1001):
#     total = 0
#     temp = num

#     while (temp > 0):
#         digit = temp % 10
#         total = total + digit ** 3
#         temp = temp // 10

#     if total == num:
#         print(f"{num} is armstrong")

# #4. Convert a decimal number to binary (without using bin())
# num = int(input("Enter a decimal number: "))
# binary = ''

# if num == 0:
#     binary = '0'
# else:
#     while num > 0:
#         binary = str(num % 2) + binary
#         num //= 2

# print("Binary:", binary)


# # ✅ LEVEL 2: String Mastery
# # 1. Remove all vowels from a string

# def removeVowels(s):
#     vowels = "aeiouAEIOU"
#     result = ""

#     for char in s:
#         if (char not in vowels):
#             result += char
#     print(result)
#     return result


# removeVowels("aeiouDeep")


# # 2 .Count uppercase, lowercase, digits, and special characters

# def char_count(s):
#     upper = lower = digit = special_char = 0
#     for char in s:
#         if (char.isupper()):
#             upper += 1

#         elif (char.islower()):
#             lower += 1

#         elif (char.isdigit()):
#             digit += 1

#         else:
#             special_char += 1
#     print(f"{s} contain")
#     print("Total Upper Char is", upper)
#     print("Total Lower Char is", lower)
#     print("Total Digits  is", digit)
#     print("Total Special Char is", special_char)


# char_count("HeeloLL@@13390")

# 3. Check if two strings are anagrams (e.g. listen and silent)

# using sort method
# def anagrams(str1 , str2 ):
#     str1 = str1.replace(" " , "").lower()
#     str1 = str2.replace(" " , "").lower()

#     return sorted(str1) == sorted(str2)

# print(anagrams("listen","selint"))

# using collection lib

# from collections import Counter

# def anagrams(str1 , str2 ):
#     return Counter(str1.replace(" " , "").lower()) == Counter(str2.replace(" " , "").lower())

# print(anagrams("listen","selint"))

# #4. Replace spaces with hyphens
# def exchange(str):
#     str = str.replace(" " , "-")
#     print(str)

# exchange("f f f ")

# # Capitalize first letter of every word (like a title)
# def capitalize(str):
#     str = str.capitalize()
#     print(str)

# capitalize("deep")

# # ✅ LEVEL 3: Lists, Tuples, Sets, Dicts Deep Practice
# # 1 .Find the second largest number in a list

# def second_large(number):
#     unique_num = list(set(number))
#     unique_num.sort(reverse=True)
#     print(unique_num)
#     print(f"Second Largest Number is {unique_num[1]}")


# second_large([12, 2, 3, 4, 5, 6, 7])

# # 2. Remove duplicates from a list (using sets)


# def remove_Duplicates(number):
#     removed_num = list(set(number))
# #     print(removed_num)


# remove_Duplicates([12, 12, 20, 3424, 324324, 434, 434, 432, 133, 432])
# # 3. Merge two dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# merged = {**dict1 , **dict2}
# print(merged)


# 4. Sort a list of tuples based on second value
# data = [(1, 4), (2, 1), (3, 5), (4, 2)]

# Sort by second value in each tuple
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # Output: [(2, 1), (4, 2), (1, 4), (3, 5)]


# 5. Count frequency of each element in a list (use dict)
# def count_freq(lst):
#     freq = {}
#     for item in lst :
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     return

# def count_frequency(lst):
#     freq = {}
#     for item in lst:
#         freq[item] = freq.get(item, 0) + 1
#     return freq

# print(count_frequency(['a', 'b', 'a', 'c', 'b', 'a']))


# print(count_freq(['a', 'b', 'a', 'c', 'b', 'a']))


# ✅ LEVEL 4: Functions + File I/O + Modules

# # Write a function that accepts a list and returns only even numbers
# def evenFunc(lst):
#     newlst = []
#     for num in lst :
#         if (num % 2 == 0):
#             newlst.append(num)
#     print(newlst)

# evenFunc([1,2,3,4,5,6,7,8,9,10,12,14,45,46])

# # Write a function to read a file and count words and lines
# def count_words_lines(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)

#             print(f"Total Lines: {line_count}")
#             print(f"Total Words: {word_count}")
#     except FileNotFoundError:
#         print("File not found. Please check the file name or path.")


# count_words_lines("read.txt")

# Create a module mymath.py with add, subtract, multiply, divide functions
# import mymath
# import mymath

# add = mymath.add(5, 7)
# print(add)

# # Import that module and build a calculator using it


# def calculator():
#     print("THIS IS A SIMPLE ARITH MATIC CALCULATOR ")
#     print("Select Operation")
#     print("1. add")
#     print("2. subtract")
#     print("3. multiply")
#     print("4. divide")

#     choice = input("Choose number for calculation(1/2/3/4) : ")
#     if choice in ['1', '2', '3', '4']:
#         a = float(input("Enter first number : "))
#         b = float(input("Enter second number : "))

#         if choice == '1':
#             print("sum of both number is", mymath.add(a,b))
            
#         elif choice == '2':
#             print("subtaction of both number is", mymath.subtract(a,b))
            
#         elif choice == '3':
#             print("multiply of both number is", mymath.multiply(a,b))
            
#         elif choice == '4':
#             print("divide of both number is", mymath.divide(a,b))

#         else:
#             print("Invaild Operation")

# calculator()

# 1 Convert ['1','2','3'] to integers	['1','2','3']	[1, 2, 3]

# l = ['1','2','3']
# o = map(int, l)

# print(list(o))

