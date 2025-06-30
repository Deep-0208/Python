def rem(list, word):
    n = []
    for item in list:
        if not (item == word):
            n.append(item.strip(word))
    return n


list = ["deep", "p"]

print(rem(list, "p"))