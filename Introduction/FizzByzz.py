start = ''
end = ''
step = ''

while not start.isnumeric():
    start = input('Choose a start point: ')
    if not start.isnumeric():
        print('\'Start point\' has to be numeric!')

while not end.isnumeric():
    end = input('Choose an end point: ')
    if not end.isnumeric():
        print(f'\'End point\' has to be numeric!')
    while end.isnumeric() and int(end) <= int(start):
        print(f'\'End point\' has to be bigger than {start}!')
        end = input('Choose an end point: ')

while not step.isnumeric():
    step = input('Choose a step: ')
    if not step.isnumeric():
        print('\'Step\' has to be numeric!')
    while step.isnumeric() and int(step) > (int(end) - int(start)):
        print(f'\'Step\' has to be smaller than {int(end) - int(start) + 1}')
        step = input('Choose a step: ')

for num in range(int(start), int(end)+1, int(step)):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



