# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

def sq_area():
    len = int(input("What is the length? "))
    width = int(input("What is the width? "))
    area = len * width
    return area


def circumf_circle():
    radius = int(input("What is the radius of the circle? "))
    c = 2 * 3.147 * radius
    return c

print(circumf_circle())