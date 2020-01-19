import math
height = input("Enter the height = ")
heightInteger = int(height)
volume = input("Enter the volume = ")
volumeInteger = int(volume)
result = heightInteger * volumeInteger * math.pi
resultStr = str(result)
print("Your volume of cylinder is" , result)

