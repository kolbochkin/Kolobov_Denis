N = 1
for i in range(100):
    if (N % 10 == 1) and (N != 11):
        print(N, 'процент')
    elif (N % 10 == 2 or N % 10 == 3 or N % 10 == 4) and (N != 12) and (N != 13) and (N != 14):
        print(N, 'процента')
    else:
        print(N, 'процентов')
    N += 1