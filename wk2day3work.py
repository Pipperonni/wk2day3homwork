# Exercises
# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

shopping_list = []

def shopping_cart(items):
    shopping_list.append(items)

def main_function():
    while True:
        itm = input('What item would like to add or delet (del)? ')
        if itm != 'del' or itm != '':
            shopping_cart(itm)
        if itm == "del":
            item_del = input('What item would you like to remove? ')
            shopping_list.remove(item_del)
        next1 = input('Would you like to quit (y/n)')    
        if next1 == 'y':
            break
        print(shopping_list)
    print(shopping_list)
            

main_function()

