class Basic:
    def oor(x,y):
        if x==1:
            return 1
        elif y==1:
            return 1
        else:
            return 0
    def aand(x,y):
        if x==1:
            if y==1:
                return 1
            else:
                return 0
        else:
            return 0
    def nnot(x):
        if x==1:
            return 0
        else:
            return 1
    def nnand(x,y):
        m=aand(x,y)
        if m==1:
            return 0
        else:
            return 1
    def nnor(x,y):
        v=oor(x,y)
        if v==1:
            return 0
        else:
            return 1        
x=1    
while x==1:    
    a=int(input('::'))
    b=int(input('::'))
    s=input('Select gate (and,or,not,nand,nor) ::')
    if s=='or':
        print (Basic.oor(a,b))
    elif s=='and':
        print(Basic.aand(a,b))
    elif s=='nand':
        print(Basic.nnand(a,b))
    elif s=='nor':
        print(Basic.nnor(a,b))
    elif s=='not':
        print(Basic.nnot(a))
    else:
        print('Invalid') 
    x=int(input('continue(1/0)::'))  
