my_list = range(3, 5000)
new_list = list()
number = 0

for i in my_list:
    if (i % 5) == 0 or (i % 7) == 0:
        new_list.append(i)

for i in new_list:
    if (i % 5) == 0 and (i % 7) == 0 and (i % 35) == 0:
        new_list.pop(new_list.index(i))

for i in new_list:
    number += i
print(number)