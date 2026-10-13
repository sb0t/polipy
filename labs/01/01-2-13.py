# Printing the fourth element of the Fibonacci sequence
fibonacci = [0, 1]
for i in range(2,6):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(f"The 4th element of the Fibonacci sequence is {fibonacci[3]}")