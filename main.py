import random

rnd_num = random.randint(1, 5)
print(rnd_num)
spam = 0
try_count = 1
while spam != rnd_num:
    spam = int(input())
    if spam == rnd_num and try_count < 5:
        print('Число найдено!')
        break
    elif spam != rnd_num and try_count == 4:
        print('Израсходовано количество попыток')
        break
    else:
        try_count += 1
        if spam > rnd_num:
            print('Ваше число больше, чем задумано компьютером. Попробуй еще раз...')
        else:
            print('Ваше число меньше, чем задумано компьютером. Попробуй еще раз...')

