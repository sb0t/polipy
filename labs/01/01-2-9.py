import random # for the (Extra) below

# Alternating printing
for i in range(4):
    if i%2==0:
        print("abcd", end='')
    else:
        print("1234", end='')

"""
(Extra)
I initially thought we had to
generate it from those given chars,
and that sounds more fun to code so here it is:
"""
chars = ['a', 'b', 'c', 'd', '1', '2', '3', '4']
gen = ""
for i in range(16):
    gen += random.choice(chars)
# print(f"\n{gen}")