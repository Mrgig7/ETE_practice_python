def count_lines():
    with open("Primary.txt", "r") as file:
        lines = file.readlines()
        return len(lines)

def move_cursor(position):
    with open("Primary.txt", "r") as file:
        file.seek(position)
        rest_of_content = file.read()
        return rest_of_content

def copy_and_read():
    with open("Primary.txt", "r") as primary_file, open("secondary.txt", "w") as secondary_file:
        secondary_file.write(primary_file.read())

    with open("secondary.txt", "r") as secondary_file:
        data = secondary_file.read()
        return data

def main():
    option = input("Enter an option (1, 2, 3): ")

    if option == "1":
        print("Number of lines:", count_lines())
    elif option == "2":
        position = int(input("Enter a position: "))
        print(move_cursor(position))
    elif option == "3":
        print(copy_and_read())
    else:
        print("Invalid")

main()
