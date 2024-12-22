def perimeter(n):
    def fibonacci_gen(limit):
        a, b = 1, 1
        for _ in range(limit + 1):
            yield a
            a, b = b, a + b

    return 4 * sum(fibonacci_gen(n))
