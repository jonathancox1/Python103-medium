width = int(input('Width?  '))
height = int(input('Height?  '))

#prints top border
print('*' * width)



#loops through the print sequence to add spaces between outside boarder while height is more than 2
while height > 2:
    spaces = ' '
    print('*' + ((width -2) * spaces) + '*') #addes spaces into the center of box not border (width -2)
    height -= 1
    
    
#prints bottom border
print('*' * width)