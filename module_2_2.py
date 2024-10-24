# Teplova // Create three variables, transfer entered data to a number, use a method int
first = int(input("Input the first figure: "))
second = int(input("Input the second figure: "))
third = int(input("Input the third figure: "))
# Create a condition: if three numbers equal, output 3, if two out of three numbers equal, output 2, if it's not, output 0
# Use if for the first condition, use elif for the second condition and else in the end
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
