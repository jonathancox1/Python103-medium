#a = int(input('How wide would you like the base of the triangle to be?  '))

a = 4
b = (a - 1) / 2
ast = 1
while a > 0:
    spaces = ' '
    trict = '*'
    while b > 0:
        print((int(b) * spaces) + (ast * trict) + (int(b) * spaces))
        a -= 1
        b -= 1
        ast += 1
    print(ast * trict)
    a -= 1
    ast += 1
    






# while a > 0:
#     while a > b:
#         spaces = ' '
#         print(spaces * int(b) + '*')
#         b -= 1
#     a -= 1