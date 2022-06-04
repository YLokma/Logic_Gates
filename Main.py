from Functions import numerically_validate

print("\nWelcome to our logic gates project, if you haven't already, please check out our GitHub for instructions")
print('https://github.com/YLokma/Logic_Gates \n')
print('Choose the type of input you prefer')
print('1: type using numbers only (112)')
print('2: type gates as text and the points as numbers (1 and 2)')
print('3: type using text and spaces only (a and b)')

input_type = numerically_validate('input type',1,3)

match input_type:
    case 1: from Logic_Gates_int import *
    case 2: from Logic_Gates_mix import *
    case 3: from Logic_Gates_str import *

print(f'\nX = {Table[-1]} \n')

exit = input('Press enter to exit \n')