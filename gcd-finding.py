def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD of", x, "and", y, "is", find_gcd(x, y))
