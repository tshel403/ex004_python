sum = 0
number = int(input("please enter a 5 digit number->"))
print("you entered the number-> {}".format(number))
numbers = str(number)
print("The digits to the number are->", end=" ")
for i in range (4):
    print(numbers[i], end=", ")
    sum = sum + int(numbers[i])
print(numbers[4])
sum = sum + int(numbers[4])
print("The sum of the digits is-> {}" .format(sum))


