import sys 

num = int(input("num: "))
if num > 10000 and num < 99999:
    # Each line for a digit of the number
    for i in range(5):
        print(int(str(num)[i]))
else:
    print("Please enter a number between 10000 and 99999.")
    sys.exit(0)