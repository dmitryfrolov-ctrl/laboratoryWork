firstNumber = int(input("Введите первое число:"))
secondNumber = int(input("Введите второе число:"))
responceText = "Большее число:"

if firstNumber < secondNumber:
 print(responceText,secondNumber)
elif firstNumber > secondNumber:
    print(responceText,firstNumber)
else:
    print("Числа равны")
