from re import I, X


x =int(input("Enter a number for x"))
y =int(input("Enter a number for y"))
if x > 0 and y > 0:
    print("Перша чверть")
if x < 0 and y > 0:
    print("Друга чверть")
if x < 0 and y < 0:
    print("Третя чверть")
if x > 0 and y < 0:
    print("Четверта чверть")
if x == 0 and y == 0:
    print("Центр")