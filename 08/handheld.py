
boot_code = {i[0]: tuple(i[1].split()) for i in enumerate(open('08/input.txt').read().splitlines())}
open('08/input.txt').close()

position, accumulator = 0, 0
exit = None 
log = []

while exit != 1:
    while position <= max(list(boot_code.keys())) and position not in log:
        if boot_code[position][0] == 'nop':
            log.append(position)
            position += 1
            print('pos is ' + str(position))

        elif boot_code[position][0] == 'acc':
            log.append(position)
            accumulator += int(boot_code[position][1])
            position += 1
            print('pos is ' + str(position))
            print('accumulator is ' + str(accumulator))
        else:
            log.append(position)
            position += int(boot_code[position][1])
            print('pos is ' + str(position))

    if position > max(list(boot_code.keys())):
        print(f'A2 accumulator: {accumulator}')
        exit = 1