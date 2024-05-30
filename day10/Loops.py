#For loop:Iterates over a sequence (like list)
print("For loop:")
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
    
    
 #While loop: Repeats as long as a conditionis true
print("\nWhile loop:")
count = 1 
while count <= 5:
    print(count)
    count += 1
    
    
#Nested loop: A loop inside another loop
print("\nNested loops:")
for i in range(1,4): #Outer loop
   for j in range(1,4): #Inner loop
       print(f"i={i} j={j}")