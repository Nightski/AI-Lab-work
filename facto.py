def fact(n):
    if n < 0:
        return "Null"
    if n == 0 or n == 1:
        return 1
    return  n * fact(n - 1)

n = int(input("Enter number: "))
print(f"The factorial of {n} is:",fact(n))