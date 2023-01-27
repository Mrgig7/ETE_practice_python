# with open(r"data.txt", 'r') as fp:
#     x = len(fp.readlines())
#     print('Total lines:', x)

# number_of_words = 0

# with open(r'data.txt','r') as fp:
# 	data = fp.read()
# 	lines = data.split()
# 	number_of_words += len(lines)

# print(number_of_words)

fname = "data.txt"
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
    
print(lines)
print(words)
print(characters)

for line in (list(open("data.txt",'r'))):
    a =(line.rstrip())
    print(a[::-1])
