import math
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def div(x,y):
    return x / y
a=input('operation::')
b=int(input('No1::'))
c=int(input('No2::'))
if a=='add':
    print(b,'+',c,'=',add(b,c))
elif a=='sub':
    print(b,'-',c,'=',sub(b,c))
elif a=='div':
    print(b,'/',c,'=',div(b,c))
else:
    print('use keywords "add","sub","div"')

  
