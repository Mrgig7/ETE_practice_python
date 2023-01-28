# with open(r"data.txt", 'r') as fp:
#     x = len(fp.readlines())
#     print('Total lines:', x)

# number_of_words = 0

# with open(r'data.txt','r') as fp:
# 	data = fp.read()
# 	lines = data.split()
# 	number_of_words += len(lines)

# print(number_of_words)
###############################################################33
'''
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
'''
###############################################################

with open("Data.txt", "r") as file:
    option = int(input("Enter an option (1-4): "))

    if option == 1:
        print(len(file.readlines()))
    elif option == 2:
        print(len(file.read().split()))
    elif option == 3:
        print(len(file.read()))
    elif option == 4:
        for line in file.readlines():
            print(line[::-1])
    else:
        print("Invalid")
