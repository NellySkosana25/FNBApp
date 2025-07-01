#Loop Control Statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break #Exits the loop if cherry is found
    print(fruit)
    
    for fruit in fruits:
        if fruit == "cherry":
            continue #Skips cherry and moves to the interation
        print(fruit)
        
        
#Why Loop

count = 0 

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #exits loop when the count is -3
    