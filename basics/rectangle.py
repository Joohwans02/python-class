import random
a = random.randint(1, 100)
b = random.randint(1, 100)

for counter in range(1,101):
    if counter%15 == 0:
        print("fizzbuzz")
    elif counter%3 == 0:
        print("fizz")
    elif counter%5 == 0:
        print("buzz")
    else: 
        print(counter)


