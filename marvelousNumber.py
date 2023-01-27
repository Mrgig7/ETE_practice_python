def marvelous(i, j, k):
    count = 0
    for x in range(i, j+1):
        if (x - int(str(x)[::-1])) % k == 0:
            count += 1
    return count
    

print(marvelous(1,10,2))