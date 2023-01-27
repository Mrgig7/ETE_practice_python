n = int(input("Enter the number: "))
a =[]
for num in range (0, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            a.append(num)
          
print(a)

