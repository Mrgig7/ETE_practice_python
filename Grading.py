class SecondDivision(Exception):
    def __init__(self, message):
        self.message = message

class ThirdDivision(Exception):
    def __init__(self, message):
        self.message = message

class Fail(Exception):
    def __init__(self, message):
        self.message = message

try:

    marks = []
    for i in range(5):
        marks.append(int(input("Enter marks in subject {}: ".format(i+1))))

    percentage = sum(marks)/5
    print("Percentage: ", percentage)

    if percentage >= 75:
        print("Eligible record with distinction")
    elif percentage >=60:
        print("Eligible record with first division")
    elif percentage >= 45:
        raise SecondDivision("Exception raised not eligible second division")
    elif percentage >=33:
        raise ThirdDivision("Exception raised not eligible third division")
    else:
        raise Fail("Exception raised not eleigible fail")

except SecondDivision as e:
    print(e.message)
except ThirdDivision as e:
    print(e.message)
except Fail as e:
    print(e.message)



######################################################################################


marks = []
for i in range(5):
    marks.append(int(input("Enter marks in subject {}: ".format(i+1))))

percentage = sum(marks)/5
print("Percentage: ", percentage)

if percentage >= 75:
    print("Eligible record with distinction")
elif percentage >=60:
    print("Eligible record with first division")
elif percentage >= 45:
    print("Exception raised not eligible second division")
elif percentage >=33:
    print("Exception raised not eligible third division")
else:
    print("Exception raised not eligible fail")

#######################################################################################