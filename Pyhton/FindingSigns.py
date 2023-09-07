def findingSign(month, day):
    starStuff = {
        "aries": ((3, 21), (4, 19)),
        "taurus": ((4, 20), (5, 20)),
        "gemini": ((5, 21), (6, 21)),
        "cancer": ((6, 22), (7, 22)),
        "leo": ((7, 23), (8, 22)),
        "virgo": ((8, 23), (9, 22)),
        "libra": ((9, 23), (10, 23)),
        "scorpius": ((10, 24), (11, 21)),
        "sagittarius": ((11, 22), (12, 21)),
        "capricornus": ((12, 22), (1, 19)),
        "aquarius": ((1, 20), (2, 18)),
        "pisces": ((2, 19), (3, 20))
    }

    for sign, (startDate, endDate) in starStuff.items():
        if (month, day) >= startDate and (month, day) <= endDate:
            return sign
    return "invalid"


month = input("What is the month of your birthday? ")
day = input("What is the day of your birthday? ")


while not month.isnumeric() or not day.isnumeric():
    print("This program need numbers.")
    month = input("What is the month of your birthday? ")
    day = input("What is the day of your birthday? ")

while not int(month) >= 1 or not int(month) <= 12:
    print("The number you inputed was not in the correct range.")
    month = input("What is the month of your birthday? ")
    day = input("What is the day of your birthday? ")

while not int(day) >= 1 or not int(day) <= 31:
    print("The number you inputed was not in the correct range.")
    month = input("What is the month of your birthday? ")
    day = input("What is the day of your birthday? ")


month = int(month)
day = int(day)

userSign = findingSign(month, day)
print(userSign)