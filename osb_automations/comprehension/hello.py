import sys
import os
os.mkdir("qw")
argument=sys.argv[0]



def say_hello(argument):
        try:

             print("Hello {} ".format(argument))
        except TypeError:
            raise



say_hello()
list=["hello","fs","gdg"]
tuple=()
set={}
dict={"key:value",""}
for i in list:
    print(i)




