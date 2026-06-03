A = 88
B = 99
if A > B:
    print('first number is greator')
else:
    print('second number is greater')
a = int(input('enter first number   '))
b = int(input('enter second number  '))
c = int(input('enter third number   '))
d = int(input('enter fourth number  '))
if a > b and a > c and a > d:
    print('first number is greater',a)
elif b > a and b > c and b > d:
    print('second number is greater',b)
elif c > a and c > b and c > d:
    print('third number is greater',c)
else :
    print('fourth number is greater',d)
a = 5
b = 6
print("a")if a > b else print("b")