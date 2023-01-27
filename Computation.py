class Computation:
    def fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
            print(a, end=" ")

    def factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        print(result)

c = Computation()
n = int(input("Enter a number: "))

c.fibonacci(n)
print()
c.factorial(n)
