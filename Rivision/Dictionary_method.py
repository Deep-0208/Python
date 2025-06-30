# Dictionary methods
my_dict = {"name": "Alice",
           "age": 25,
           "city": "New York"}

print("get:", my_dict.get("name"))  # Alice

my_dict["age"] = 26
print("update age:", my_dict)  # Updates age

my_dict.update({"city": "Boston", "country": "USA"})
print("update:", my_dict)  # Adds/updates values

print("keys:", list(my_dict.keys()))  # ['name', 'age', 'city', 'country']

print("values:", list(my_dict.values()))  # ['Alice', 26, 'Boston', 'USA']

print("items:", list(my_dict.items()))  # [('name', 'Alice'), ...]

print("pop 'age':", my_dict.pop("age"))  # 26

print("popitem:", my_dict.popitem())  # Last key-value pair

my_dict.clear()
print("clear:", my_dict)  # {}
