keys = input("Enter the keys for the dictionary, separated by commas: ").split(',')
values = input("Enter the values for the dictionary, separated by commas: ").split(',')
my_dict = dict(zip(keys, values))
print(my_dict)


while True:
    try:
        key = input("Enter key to be searched: ")
        print(my_dict[key])
        break
    except KeyError:
        print("Key not found. Exception raised as key is not available in the dictionary.")
