my_list = list()
new_list = list()
for i in range(1,5050505,23):
     my_list.append(i)

for i in my_list[0::2]:
     new_list.append(i)

print(sum(new_list))