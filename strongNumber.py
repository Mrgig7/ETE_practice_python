def is_strong_number(num):
    fact_sum = 0
    temp = num
    while temp > 0:
        fact = 1
        i = 1
        r = temp % 10
        while i <= r:
            fact = fact * i
            i = i + 1
        fact_sum += fact
        temp = temp // 10
    return num == fact_sum

def strong_numbers(n):
    strong_nums = []
    for i in range(1, n+1):
        if is_strong_number(i):
            strong_nums.append(i)
    return strong_nums

n = int(input("Enter the number here: "))
(strong_numbers(n))
a=[]
for i in strong_numbers(n):
    a.append(i**2)

print(a)