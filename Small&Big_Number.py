MaxNumber = int(input("Enter A Number "))
MinNumber = MaxNumber

for i in range (9):
    Number = int(input("Enter A Next Number : "))
    
    if Number > MaxNumber:
        MaxNumber = Number
        
    if Number < MinNumber:
        MinNumber = Number
        
print("The MaxNumber Is : ", MaxNumber)
print("The MinNumber Is : ", MinNumber)