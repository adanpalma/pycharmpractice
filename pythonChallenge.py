n = int(input("Input Integer"))

if n % 2 != 0:
    print("Weird")
else:
    if n > 20:
        print("Not Weird")
    elif n >= 6:
        print("Weird")
    else:
        print("Not Weird")


