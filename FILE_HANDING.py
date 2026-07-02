
with open ('abcd.txt','r') as f:  # r is used for read
    print(f.read())
with open ('abcd.txt','a') as f: # a is used for append
    print(f.write('this is a test'))
    f.close()

x = open('abcd.txt','r')
print(x.read())
with open ('abcd.txt','a') as f:
    f.write('this is a car ')
    f.close()
x = open('abcd.txt','w')  # w is used for write
print(x.write('this is a car of rich '))
with open ('abcd.txt','r') as f:
    print(f.read())
import os
os.remove('musa.txt')
x = open('musa.txt','w')
print(x.write('this is a car of rich '))