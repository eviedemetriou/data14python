def fizzbuzz2(start_default, end_default, step_default):

    start_user_qs = input('Do you want to change the default for start? Y/N\n')
    if start_user_qs.upper() == 'Y' or start_user_qs.upper() == 'YES':
        start = input('Choose your own start point: ')
        while not start.isnumeric():
            print('\'Start point\' has to be numeric!')
            start = input('Choose your own start point: ')
    else:
        start = start_default

    end_user_qs = input('Do you want to change the default for end? Y/N\n')
    if end_user_qs.upper() == 'Y' or end_user_qs.upper() == 'YES':
        end = input('Choose your own end point: ')
        while not end.isnumeric():
            print('\'End point\' has to be numeric!')
            end = input('Choose your own end point: ')
    else:
        end = end_default

    step_user_qs = input('Do you want to change the default for step? Y/N\n')
    if step_user_qs.upper() == 'Y' or step_user_qs.upper() == 'YES':
        step = input('Choose your own increment step: ')
        while not step.isnumeric():
            print('\'Increment step\' has to be numeric!')
            step = input('Choose your own increment step: ')
    else:
        step = step_default

    for num in range(int(start), int(end) + 1, int(step)):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


fizzbuzz2(1, 100, 1)
