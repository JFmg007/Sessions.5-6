# 1. Print multiplication table 1-10 without duplicates
for i in range(1, 11):
    for j in range(i, 11):  # Start from i to avoid duplicates
        print(f"{i} x {j} = {i * j}")
    print()


# 2. Compute a**b using only additions
def power(a, b):
    def multiply(x, y):  # Multiplication using additions
        result = 0
        for _ in range(y):
            result += x
        return result

    result = 1
    for _ in range(b):
        result = multiply(result, a)
    return result


a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
print(f"{a}^{b} = {power(a, b)}")


# 3. Check if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]


num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
