list = [1,2,6,7,8,33,12,54,67]
sum = 0
print(len(list))
for i in range (0,len(list)):
    print(i)
    sum = sum + list[i]

print(f"The sum is {sum}")