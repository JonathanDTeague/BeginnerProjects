from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class account:
    def __init__(self, name, age, gender, SSN) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.SSN = SSN
        self.acccountNumber = random_with_N_digits(8)


    def __str__(self) -> str:
        return f"Name - {self.name}\nAge - {self.age}\nGender - {self.gender}\nSSN - {self.SSN}\nAccount Number - {self.acccountNumber}"

def createAccount():
    a1 = account(input("What is your name? "), input("What is your age? "), input("What is your gender? "), input("What is your SSN? " ))
    print(a1)

createAccount()
    



        


    
    