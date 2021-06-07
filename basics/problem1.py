
# a = int(input("type first number: "))
# b = int(input("type second number: "))
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("=="


import random
a = random.randint(0,100)
print(a)

for i in range(10):
    b = int(input(f"{i} guess the number: "))
    if a == b:
        print("correct")
        break
    elif a > b:
        print("too small")
    else:
        print("too big")
    
else:
    print("HEY LAD YOU RAN OUT OF ROUNDS LOOSEEER")