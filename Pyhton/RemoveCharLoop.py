s = "This is a string."
s2 = ""

i = 0
for char in s:
    if (i % 2) == 0:
        s2 += char
    i += 1

s = s2
print(s)