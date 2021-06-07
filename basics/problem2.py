a = int(input("type a number: "))
if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print("it's a leap year")
else:
    print ("it's not a leap year")