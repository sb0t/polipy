# Printing the first four elements of the Fibonacci sequence
fibonacci = [0, 1]
for i in range(2,6):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
for i in range(0, 4):
    print(f"{i+1}: {fibonacci[i]}")