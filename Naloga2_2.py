print("Welcome to the fizzbuzz game!")
guess = int(input("Please enter a number between 1 and 100: "))

for x in range (1, guess+1):
    if x % 3 == 0 and x % 5 == 0:
        print("FIZZBUZZ")
    elif x % 3 == 0:
        print ("FIZZ")
    elif x % 5 == 0:
        print("BUZZ")

    else:
        print(x)
