code1 = str(input("First Student Number: "))
code2 = str(input("Second Student Number: "))
for i in range(
    (min(int(code1[1:]),int(code2[1:]))),
    (max(int(code1[1:]),int(code2[1:])))+1
    ):
    print(i)