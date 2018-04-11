#Pre-set functions
def new_line():
    print()

def three_line():
    new_line()
    new_line()
    new_line()

#Nesting the three_lines function into the nine_line function
def nine_lines():
    three_line()
    three_line()
    three_line()

#Nesting all previous functions to get the number 25 lines
def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()
    three_line()
    new_line()

#Calling the clear_screen and nine_lines functions
print("Printing 9 lines:")#Placeholders for better visualization
nine_lines()
print("Printing 25 lines now:")#Placeholders for better visualization
clear_screen()





