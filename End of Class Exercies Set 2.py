#1
divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

#2
for letter in 'Ahola':
      print(letter)

#3
num = 0
while num <= 5:
    print(num)
    num +=2

print("Out")
print(num)

#4
num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3:", count)