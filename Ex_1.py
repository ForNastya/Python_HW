a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
exists = a+b > c and a+c > b and b+c > a
if exists:
    print('Triangle exists')
else: print('Triangle can not be')