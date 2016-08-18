a = input("enter a sentence: ")

i = 0
j = 0
for b in a:
    if b.isupper():
        i += 1
    elif b.islower():
        j += 1

print("uppercase alphabet count: %d" % (i))
print("lowercase alphabet count: %d" % (j))