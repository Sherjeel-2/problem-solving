# ================================
# PYTHON LOOPS – FULL PRACTICE FILE
# ================================

print("START OF PROGRAM")
print("-" * 40)

# ----------------
# FOR LOOP BASICS
# ----------------
print("For loop: numbers 1 to 10")
for i in range(1, 11):
    print(i)

print("-" * 40)

# ----------------
# LOOP WITH LIST
# ----------------
fruits = ["apple", "banana", "mango", "orange"]

print("Looping through fruits")
for fruit in fruits:
    print("Fruit:", fruit)

print("-" * 40)

# ----------------
# EVEN & ODD NUMBERS
# ----------------
print("Even numbers from 1 to 20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("-" * 40)

print("Odd numbers from 1 to 20")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

print("-" * 40)

# ----------------
# SUM OF NUMBERS
# ----------------
total = 0
for i in range(1, 11):
    total += i

print("Sum of numbers 1 to 10:", total)

print("-" * 40)

# ----------------
# WHILE LOOP
# ----------------
print("While loop counting")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("-" * 40)

# ----------------
# BREAK EXAMPLE
# ----------------
print("Break example")
for i in range(1, 10):
    if i == 6:
        print("Breaking at", i)
        break
    print(i)

print("-" * 40)

# ----------------
# CONTINUE EXAMPLE
# ----------------
print("Continue example (skip 5)")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("-" * 40)

# ----------------
# NESTED LOOP
# ----------------
print("Nested loop (i, j)")
for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)

print("-" * 40)

# ----------------
# MULTIPLICATION TABLE
# ----------------
print("Multiplication table of 5")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

print("-" * 40)

# ----------------
# REAL LIFE EXAMPLE
# ----------------
marks = [78, 85, 90, 66, 88]
total_marks = 0

for mark in marks:
    total_marks += mark

average = total_marks / len(marks)

print("Marks:", marks)
print("Total Marks:", total_marks)
print("Average:", average)

print("-" * 40)

# ----------------
# FIND LARGEST NUMBER
# ----------------
numbers = [10, 45, 22, 89, 34]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Numbers:", numbers)
print("Largest number:", largest)

print("-" * 40)

# ----------------
# COUNT VOWELS
# ----------------
word = "programming"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("Word:", word)
print("Vowel count:", count)

print("-" * 40)

# ----------------
# STAR PATTERN
# ----------------
print("Star pattern")
for i in range(1, 6):
    print("*" * i)

print("-" * 40)

# ----------------
# REVERSE LOOP
# ----------------
print("Reverse counting")
for i in range(10, 0, -1):
    print(i)

print("-" * 40)

print("END OF PROGRAM")
