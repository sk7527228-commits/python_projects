a =eval(input("enter marks of arabic subject  "))
b = eval(input("enter marks of spanish subject  "))
c= eval(input("enter marks of english subject  "))
d = eval(input("enter marks of french subject  "))
e = eval(input("enter marks of russian subject  "))
obt_marks=a+b+c+d+e
total_marks=500
percent_marks= obt_marks * 100 / total_marks
if percent_marks >= 80:
    print (f"your marks perctage is {percent_marks} and got A+ grade")
elif percent_marks >= 70:
    print (f"your marks perctage is {percent_marks} and got A grade")
elif percent_marks >= 60:
    print(f"your marks perctage is {percent_marks} and got B grade")
elif percent_marks >= 50:
    print(f"your marks perctage is {percent_marks} and got C grade")
else:
    print(f"your marks perctage is {percent_marks}  and sorry you are fail")