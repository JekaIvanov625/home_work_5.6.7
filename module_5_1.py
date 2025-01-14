def caching_fibonacci():
    # створюємо кеш
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Check if result is already in cache
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
# результат
fib = caching_fibonacci()
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610