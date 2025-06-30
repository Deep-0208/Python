words = ["fucking", "badboy", "donkey"]

# Open and read the content of the file
with open("donkey.txt", "r") as f:
    data = f.read()

# Replace the words in the list with hashtags
newData = data
for word in words:
    newData = newData.replace(word, "#" * len(word))

# Write the modified content back to the file
with open("donkey.txt", "w") as f:
    f.write(newData)
