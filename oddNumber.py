def odd_numbers(n):
    a = 1
    b = 0
    while b < n:
        if a % 2 != 0:
            print(a, end=" ")
            b += 1
        a += 1

n = int(input("Enter the number of odd number: "))
odd_numbers(n)