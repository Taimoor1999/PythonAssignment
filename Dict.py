                    # According to keys


myDict = {}
myDict = {
    "cllo" : 2,
    "borld" : 3,
    "auhammad" : 1,
    "daimoor" : 4   
}
# for key in sorted(myDict.keys()):
#     print (key , "::" , myDict[key])
# print("The reverse answer is")
# for key in sorted(myDict.keys(), reverse=True):
#     print (key , "::" , myDict[key])
    
print()
print()
print("Press 1 for keys ")
print("Press 2 for values ")
Ask = input()
                    # better method to sort values on the basis of keys 
if (Ask ==  "1"):
    for elem in sorted(myDict.items()):
        print (elem[0] , "::" , elem[1])
    print()
    print()
    print("The reverse answer is")

    for elem in sorted(myDict.items() ,reverse=True):
        print (elem[0] , "::" , elem[1])

                    # better method to sort values on the basis of values 
print()
print()
if (Ask== "2"):
    print("on the basis value of values")
    ValuesBased = sorted(myDict.items(), key=lambda x: x[1])

    for elem in ValuesBased:
        print(elem[0] , "::" , elem[1]  ) 
 
 
    print() 
    print()
    print("reverse on the basis of values")
    ValuesBased = sorted(myDict.items(), key=lambda x: x[1] , reverse=True)

    for elem in ValuesBased:
        print(elem[0] , "::" , elem[1]  ) 

