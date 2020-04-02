#calculate how much tip to leave

#prompt user for two items
#bill amount
bill = float(input('Total Bill: '))

#level of service good, fair or bad
a = str(input('Level of service Good, Fair, or Bad '))
service = a.lower()

#good > 20%
#fair > 15%
#bad > 10%

if service == 'good':
    tip = bill * .20
    total = bill + tip
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)
elif service == 'fair':
    tip = bill * .15
    total = bill + tip
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)

elif service == 'bad':
    tip = bill * .10
    total = bill + tip
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)

