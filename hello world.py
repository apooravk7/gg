a = 100
b = 450
c = 90
"""
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
"""
if a>b and a>c:
    print("a is biggest")
if b>a and b>c:
    print("b is biggest")
else:
    print("c is bigger")
