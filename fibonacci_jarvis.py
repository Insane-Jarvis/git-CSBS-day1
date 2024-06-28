memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = result
        return result

print(fibonacci(6))
