# # ✅ 1. lambda – Anonymous function (1-line)

# square = lambda x: x ** 2
# print(square(4))  # ➜ 16

# '''
# same as
# def square(x):
#     return x ** 2

# '''

# # ✅ 2. map() – Apply function to each item

# nums = [1, 2, 3, 4]
# # squared = list(map(lambda x: x ** 2, nums)) We can also write as below->

# squared = list(map(square, nums))

# print(squared)  # ➜ [1, 4, 9, 16]

# # ✅ 3. filter() – Keep only items that match condition

# nums = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)  # ➜ [2, 4, 6]


# 🧪 Practice Questions (Try These)
# ✅ Square all numbers in list: [2, 4, 6]

# lst = [2,4,6]
# sqr = list(map(lambda x : x*x , lst))
# print(sqr)

# ✅ Keep only names with more than 4 letters: ['Jay', 'Pooja', 'Ravi', 'Krishna']


# names =  ['Jay', 'Pooja', 'Ravi', 'Krishna']
# filt = list(filter(lambda name:len(name)>4  , names ))
# print(filt)

# ✅ Convert string numbers to integers: ['1', '2', '3']
# str = ['1', '2', '3']

# integers = list(map(int, str))
# print(integers)


# # ✅ Add 2 lists element-wise using map(): [1, 2, 3] + [4, 5, 6]
# l1 = [1, 2, 3]
# l2 = [4, 5, 6,]

# summs = list(map(lambda x,y: x+y , l1,l2))
# print(summs)

# # ✅ From list[1-20], get square of all even numbers
# l = list(range(1,21))
# sqr = list(map(lambda y : y**2 ,filter(lambda x,: x % 2 == 0 , l)))
# print(sqr)

# 🧪 Practice Questions (Solve with List/Dict Comprehension)

# # 🔹 List Comp:
# # ✅ Make a list of squares from 1 to 10
# sqr = [x*x for x in range (1,21)]
# print(sqr)

# # ✅ Extract all vowels from a string
# str = "aeiouDeepAeiou"
# str = [vowel for vowel in str if vowel in "aeiouAEIOU" ]
# print(str)

# # ✅ Make a list of words with more than 3 letters from: ['hi', 'hello', 'yes', 'no', 'python']

# words = ['hi', 'hello', 'yes', 'no', 'python']
# filtered = [word for word in words if len(word)>3]
# print(filtered)


# # ✅ Convert a list of words to lowercase
# words = ['hi', 'hello', 'yes', 'no', 'python']
# upperCase = [word.upper() for word in words ]
# print(upperCase)

# # 🔹 Dict Comp:
# # ✅ Create a dict: numbers and their cubes from 1 to 5
# cubes = {x : x**3 for x in range(1,6) }
# print(cubes)

# # ✅ Count each letter in "banana" using comprehension
# words = "banana"
# letter_count = {ch: words.count(ch) for ch in words}
# print(letter_count)

# # ✅ Map numbers to "even"/"odd" label from list: [1,2,3,4,5]

# l = [1, 2, 3, 4, 5]

# conver = {x : "even" if x % 2 == 0 else "odd" for x in l}
# print(conver)

# 🧪 Practice Questions For Json
# # Convert this JSON string to Python and print name:
# # {"name": "Amit", "role": "Developer", "salary": 45000}

# import json

# data = '{"name": "Amit", "role": "Developer", "salary": 45000}'
# person = json.loads(data)

# print(person['name'])  # ➜ Amit

# # Create a Python dict of 3 students and save it to students.json.
# import json

# students = {
#     "students": [
#         {"name": "Ravi", "age": 20},
#         {"name": "Pooja", "age": 22},
#         {"name": "Amit", "age": 21}
#     ]
# }

# with open ("students.json" , "w") as f:
#     json.dump(students , f , indent=2)

# print("✅ Saved to students.json")

# # Read a JSON file students.json and print names only.
# import json

# with open ("students.json", 'r') as f:
#     info = json.load(f)

# for student in info['students']:
#     print(student['name'])   

# # Modify a Python dictionary, convert it to JSON, and print.

# import json

# profile = {
#     "name": "Sneha",
#     "city": "Rajkot"
# }

# jsdata = json.dumps(profile , indent=2)
# print(jsdata)
