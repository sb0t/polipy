import math
import sys

current_pi_calc = 1
pi_calc = 0
x = 0
for i in range(1, 3100000, 2): # running the program 3.1m times to reach precision
    x+=1
    if x%2!=0:
        pi_calc += 1/i
    else:
        pi_calc -= 1/i
    current_pi_calc = pi_calc * 4
    if (
        len(str(current_pi_calc))>7 and # decimal point exists (prevents out of scope)
        str(current_pi_calc)[:8]==str(math.pi)[:8] and  # confirms precision
        int(str(current_pi_calc)[8])!=int(str(math.pi)[8]) # stops running asap precise
    ):
        pi_calc *= 4
        print(str(pi_calc)[:8])
        sys.exit(0)