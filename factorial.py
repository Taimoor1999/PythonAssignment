# print("hello World")
print("Enter the number")
a = int(input()) 

i = a - 1
result = a * i
loopStart = i-1
for i in range(loopStart, 1, -1):
        result = result * i
StringResult = str(result)        
print("Your answer is " + StringResult)