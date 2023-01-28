class Parent:
    def number(self, n):
        if n > 0:
            status = "positive"
        else:
            status = "negative"
        if (n ** (1/5)) % 1 == 0:
            status += " and perfect 5th power"
        else:
            status += " and non-perfect 5th power"
        return status

class Child(Parent):
    def number(self, n):
        if (n ** (1/5)) % 1 == 0:
            status = "positive and perfect 5th power" if n > 0 else "negative and perfect 5th power"
        else:
            status = super().number(n)
        return status

n = int(input("Enter an integer number: "))

parent_obj = Parent()
print("Parent class: ", parent_obj.number(n))

child_obj = Child()
print("Child class: ", child_obj.number(n))
