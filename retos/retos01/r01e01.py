c = 0
for i in range(1, 101):
    c += 1
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz', end=' ')
    elif i % 3 == 0:
        print('fizz', end=' ')
    elif i % 5 == 0:
        print('buzz', end=' ')
    else:
        print(i, end=' ')
    
    if c == 20:
        print()
        c = 0

