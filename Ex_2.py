a = 2
counter = 0
no_sim = 1
min = 0
max = 100000
while True:
    number = int(input('Enter a number from 1 to 100000: '))
    if min < number < max:
        while a <= number - 1:
            if number % a == 0:
                counter += 1
            a += 1
        if counter >= no_sim:
            print('Composite number')
        else:
            print('Prime number')
        break
    else:
        print('Error:')