a = int(input("enter the number:"))
#sum of digit
temp = a
sum = 0
digit = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10
print(sum)

    