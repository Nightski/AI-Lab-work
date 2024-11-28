def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

n = int(input("Enter the limit of fibonacci series: "))
for i in range(1, n + 1):
    print(fibo(i))