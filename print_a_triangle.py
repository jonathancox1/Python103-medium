#draw a silly little triangle with a base width of 5 '*'
a = 5
b = (a + 1) / 2
ast = 1
while a > 1:
    spaces = ' '
    trict = '*'
    while b > 0:
        print((int(b) * spaces) + (ast * trict) + (int(b) * spaces))
        a -= 1
        b -= 1
        ast += 2
    print(ast * trict)
    a -= 1
    ast += 2
    
