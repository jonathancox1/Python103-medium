#create multiplication table

stop = 1
power = 1
while power <= 10:
    while stop <= 10:
        num = (power * stop)
        print(f'{power} X {stop} = {num}')
        stop += 1
    power += 1



