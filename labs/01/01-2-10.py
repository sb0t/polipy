# Checkerboard w/'0's as whites and '1's as blacks
for i in range(5):
    for j in range(5):
        if j%2==0:
            if i%2==0:
                print("0", end='')
            else:
                print("1", end='')
        else:
            if i%2==0:
                print("1", end='')
            else:
                print("0", end='')
    print('\n', end='')