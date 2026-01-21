#sum the list using range loop method
list = [1,2,6,7,8,33,12,54,67]
sum = 0
print(len(list))
for i in range (0,len(list)):
    sum = sum + list[i]

print(f"The sum is {sum}")

#sum the list using while loop
listTwo = [1,2,6,7,8,33,12,54,67]

j = 0
sum2 = 0
while j < len(listTwo):
    print(j)
    sum2 = sum2 + listTwo[j]
    j = j+1

print(f"The sum 2 is {sum2}")

#Nested Loops in Python 

listA = ["red", "yellow", "blue"]
listB = ["apple", "mango", "cherry"]

# We can use in to iterate list
for i in listA:
    for j in listB:
        print(i,j)

for k in listTwo:
    print(k)