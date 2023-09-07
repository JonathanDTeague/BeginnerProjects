amount = int(input("How many numbers do you want to use? "))
x = 0
list1 = []

while x <= amount:
    num = int(input("What number do you want to add? "))
    list1.append(num)
    x += 1

total = sum(list1) / len(list1)
print(total)