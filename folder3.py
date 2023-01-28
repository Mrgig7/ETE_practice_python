with open("data.txt", "r") as f:
    data = f.read()
    
option = input("Enter option (1-4): ")

if option == "1":
    print("Number of lines: ", data.count("\n"))
elif option == "2":
    print("Number of words: ", len(data.split()))
elif option == "3":
    print("Number of characters: ", len(data))
elif option == "4":
    data = data.upper()
    with open("data.txt", "w") as f:
        f.write(data)
    print("File converted to uppercase.")
else:
    print("Invalid option.")
