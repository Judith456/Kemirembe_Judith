while True:
    try:
      firstNumber = int(input("Enter first number: "))
      secondNumber = int(input("Enter second number: "))
      result = firstNumber / secondNumber
      
    except ZeroDivisionError:
        print("Error: Division by zero. Input a nn zero number")   
     
    if secondNumber > 0: 
        print(result)
        break
    else:
          print("Invalid input")
      