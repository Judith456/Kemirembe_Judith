#5! factorial

def factorial(y):
    if(y > 0):
        result = y * factorial(y - 1)
    else:
        result = 1
    return result
print("Factorial of 5:",factorial(5))