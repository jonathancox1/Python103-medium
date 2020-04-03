#calculate how much tip to leave

#prompt user for two items
#bill amount
bill = float(input('Total Bill:  '))

#level of service good, fair or bad
a = str(input('Level of service Good, Fair, or Bad:  '))
service = a.lower()

#amount of ways to split the bill 
split = int(input('Would you like to split the bill, how many ways, or type 0:  '))

#good > 20%
#fair > 15%
#bad > 10%

if service == 'good':
    tip = bill * .20
    total = bill + tip
    if split == 0:
        split = 1
    cut = total / split
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)
    print(f'Amount per person: $''%.2f' % cut)
elif service == 'fair':
    tip = bill * .15
    total = bill + tip
    if split == 0:
        split = 1
    cut = total / split
    cut = total / split
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)
    print(f'Amount per person: $''%.2f' % cut)
elif service == 'bad':
    tip = bill * .10
    total = bill + tip
    if split == 0:
        split = 1
    cut = total / split
    cut = total / split
    print(f'Tip amount: $''%.2f' % tip)
    print(f'Total amount: $''%.2f' % total)
    print(f'Amount per person: $''%.2f' % cut)
