
message = input("Type sentence: ")
print("uppercase letters: ", sum(1 for d in message if d.isupper()))
print("lowercase letters: ", sum(1 for c in message if c.islower()))


