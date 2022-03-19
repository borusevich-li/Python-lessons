n = int(input("Enter a number - "))
if n < 10:
    print("n is less than 10")
    if n > 0:
        print("n is bigger than 0")
        if n < 5:
            if n < 3:
                if n <= 1:
                    print("Maybe,your num is 1")
                else:
                    print("Your num is 2")
            else:
                print("Your num is 4")
        else:
            print("Your num is 5 or higher")
    else:
        print("Seems, your num is 0 or less")
else:
    print("Your num is 10 or highe")
