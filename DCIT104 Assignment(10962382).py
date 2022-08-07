minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))
Sum = 0

for Num in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Num//2 + 1)):
        if(Num % i == 0):
            count = count + 1
            break

    if (count == 0 and Num != 1):
        print(" %d" %Num, end = '  ')
        Sum = Sum + Num

print("\n\nSum from %d to %d = %d" %(minimum, maximum, Sum))


