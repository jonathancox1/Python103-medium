width = int(input('Width?  '))
height = int(input('Height?  '))

#prints top border
print('*' * width)

#creates new value for squares that are larger than 2x2
adjusted_height = height - 2

#loops through the print sequence to add spaces between outside boarder while hieght is more than 2
while height > 2:
    spaces = ' '
    print('*' + (adjusted_height * spaces) + '*')
    height -= 1
    
    
#prints bottom border
print('*' * width)