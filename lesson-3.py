n= int(input("Enter a number - "))
if n<10 and n>0:
    if n<5:
        if n<3:
            if n<=1:
                print("Maybe, your num is 1")
            else:
                print("Your num is 2")
        elif n == 3:
            print("Your num is 3")
        else:
            print("Your num is 4")
    elif n == 5:
        print("Your num is 5")
    else:
        print("Your num is between 5 and 10")
elif n == 0 or n == 10:
    print("Your num is 0 or 10")
else:
    print("Your num is less than 0 or higher than 10")
