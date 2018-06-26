#----------------------------------------------
#Assignment: 5->1
##l=list()
##for x in range(10):
##    a=int(input())
##    l.append(a)
##print(l)
#----------------------------------------------
#Assignment: 4->2
#while(True):
#    print('infinite loop')
#----------------------------------------------
#Assignment: 4->3
a=list(map(int,input().split()))
b=list([x*x] for x in a)
print(b)
#----------------------------------------------
#Assignment: 4->4
x=[1,'a',25.3]
for a in x:
    print(a,':',type(a))
#----------------------------------------------
#Assignment: 4->5
le=list()
lo=list()
for x in range(1,101):
    if(x%2==0):
        le.append(x)
    else:
        lo.append(x)
print('Even:',le)
print('Odd:',lo)

#----------------------------------------------
#Assignment: 4->6
n=int(input('No of row for pattern'))
for i in range(1,n+1):
    print('*'*i)
#----------------------------------------------
#Assignment: 4->7
d={'a':1,'b':2,'c':3,'d':4,'e':5}
for x in ()

#----------------------------------------------
#Assignment: 4->8
a=list(map(int,input().split()))
b=int(input('Enter value to search'))
for x in a:
    if(x==a):
        a.remove(x)
print(a)
