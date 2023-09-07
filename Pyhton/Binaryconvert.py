# Takes user input and assigns it to the var userin
userVal = input("What is the binary value you want to convert? ")

# Assigning a variable that takes a string value and convets it to a int with a base 2 format
intVal = int(userVal, 2)

# This assigns a varaible doing the samething as above but adds the step of conveting the base 2 number to a hex value
hexVal = hex(intVal)

# Prints the value of var intval and hexval
print("Base 10:", intVal, "Hex:", hexVal)
