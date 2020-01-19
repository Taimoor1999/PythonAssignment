myList = []

print("Do you want to enter something")
answer = input()
while (answer == "yes"):
    enter = input()
    myList.append(enter)
    print("Do you want to enter something")
    answer = input()
    if (answer == "no"): 
        break
print(myList , "original list")
myList.reverse()
print(myList , "Reverse list")
