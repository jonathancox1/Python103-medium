#create multiplication table
count = 1
stop = 1
power = 1
while count <= 100:
    while power <= 10:
        while stop <= 10:
            num = (power * stop)
            print(f'{power} X {stop} = {num}')
            stop += 1
        power += 1
        stop -= 9
    count += 1


