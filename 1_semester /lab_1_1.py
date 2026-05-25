numbers = int(input("Введите число:"))

if numbers < 1:
 print("Введите положительно число")
else:
    for i in range(numbers + 1): print(i)
