import math

q1 = int(input("Q1: "))
q2 = int(input("Q2: "))
r = int(input("r: "))
ep = 8.854 * (10^(-12))

force = (q1*q2)/(4*math.pi*ep*(r^2))
print(f"Force: {force} N")