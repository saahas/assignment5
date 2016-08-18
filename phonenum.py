x = [int(x) for x in input("enter the phone numbers: ").split()]

y = sorted(x)

for i in y:
    print("+ 91 %d" % (i))