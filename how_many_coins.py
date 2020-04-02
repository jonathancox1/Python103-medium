coins = 0

# print(f'You have {coins} coins.')
# a = str(input('Would you like another coin? Yes/No  '))
# response = a.lower()

while coins >= 0:
    print(f'You have {coins} coins.')
    a = str(input('Would you like another coin? Yes/No  '))
    coins += 1
    if a == 'no':
        print('Bye!')
        break




