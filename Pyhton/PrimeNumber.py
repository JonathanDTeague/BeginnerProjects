userinput = int(input("What number do you want to check? "))

factors  = 0 

def prime(x):
    if x <= 1:
        print("This is a number less than or equal to one.")
    for i in range(2, x):
        if x % i == 0:
            print("This is not a prime.")
    print("This is a prime")
prime(userinput)

