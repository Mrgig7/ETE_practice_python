n = int(input())
words = []
for i in range(n):
    words.append(input().lower()) 

count = 0
for word in words:
    if word == word[::-1]: 
        count += 1

print(count)
