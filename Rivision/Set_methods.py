# Set methods
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Add element
a.add(7)
print("add:", a)  # {1, 2, 3, 4, 7}

# Update with another set or iterable
a.update([8, 9])
print("update:", a)  # {1, 2, 3, 4, 7, 8, 9}

# Remove element (raises error if not found)
a.remove(2)
print("remove 2:", a)  # {1, 3, 4, 7, 8, 9}

# Discard element (does NOT raise error if not found)
a.discard(10)
print("discard 10:", a)  # No error, unchanged set

# Pop (removes and returns a random element)
popped = a.pop()
print("pop:", popped, "| set now:", a)

# Clear all elements
a.clear()
print("clear:", a)  # set()

# Reset sets for set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (a OR b)
print("union:", a.union(b))  # {1, 2, 3, 4, 5, 6}

# Intersection (a AND b)
print("intersection:", a.intersection(b))  # {3, 4}

# Difference (a - b)
print("difference:", a.difference(b))  # {1, 2}

# Symmetric difference (a XOR b)
print("symmetric_difference:", a.symmetric_difference(b))  # {1, 2, 5, 6}

# Check if disjoint (no common elements)
print("isdisjoint:", a.isdisjoint(b))  # False

# Check if subset
print("issubset:", {1, 2}.issubset(a))  # True

# Check if superset
print("issuperset:", a.issuperset({1, 2}))  # True

# In-place operations (modify original set)
a.intersection_update(b)
print("intersection_update:", a)  # {3, 4}

a = {1, 2, 3, 4}
a.difference_update({2, 3})
print("difference_update:", a)  # {1, 4}

a = {1, 2, 3}
a.symmetric_difference_update({3, 4})
print("symmetric_difference_update:", a)  # {1, 2, 4}
