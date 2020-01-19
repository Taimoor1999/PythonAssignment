firstNumber = 0
initial = firstNumber
SecondNumber = 1
second = SecondNumber
print("Enter how many times you want to add the number?")
SeriesLastNumber = int(input())
print("Your numbers are")
print(initial)
print(second)
    
for SeriesLastNumber in range (firstNumber, SeriesLastNumber):

    result = SecondNumber + firstNumber

    temp = firstNumber
    firstNumber = SecondNumber
    SecondNumber = result
    
    print(result)