# function and function call
# Function is a block of code that to use again and agin to use at.
# Function is just call at to use run at.

def ali (Sname , Fname  ):
    print(f'my name {Sname} and my father name is {Fname}')
ali("musa", "khan")
# PARAMETER
# A parameter is a variable defined in a function when it is created. It is used to accept input values.
#  ARGUMENT
#An argument is the actual value passed to a function when it is called.
# SCOPE
#Scope defines where a variable can be accessed in a program.
#. Local Scope
#A variable created inside a function can only be used inside that function.
def king (name , age):
    print(f'my name {name} and my age is {age}')
king("musa", "khan")
# Python Module
# A module in Python is a file that contains Python code (functions, variables, or classes) which you can reuse in other programs.
def ali(Sname, Fname, age):
    print(f"my name {Sname} {Fname} and my age is {age}")
ali("musa", "khan", 20)
import datetime
x = datetime.datetime.now()
print(x)
import datetime
y = datetime.datetime.now()
print(y.year)
print(y.month)
print(y.day)
ali = {'name': 'musa', 'age': 20}
print(type(ali))
import json
print(json.dumps(ali))
print(json.dumps(ali, sort_keys=True, indent=4))
# 