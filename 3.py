##Assignment->3->A->1
a=(1,2,'abc',25.3,'xy',45,65)
print('length of tuple:',len(a))
#-------------------------------
#Assignment->3->A->2
t=(10,5,8,15,20,1,9)
print('Largest element:',max(t),' ,smallest element:',min(t))
#-------------------------------
#Assignment->3->A->3
t=(1,2,3,4,5,6,7)
p=1
for x in t:
    p=p*x
print('Product of all element :',p)
#-------------------------------
#Assignment->3->B->1
x={1,2,3,4,5}
y={4,5,6,7}
print('x-y:',(x-y))
if(x==y):
    print('x=y')
elif(x>y):
    print('x>y')
else:
    print('x<y')
print('x intersection y:',x&y)
#-------------------------------
#Assignment->3->C->1,2
d=dict()
for i in range(5):
    a=input('Enter name:')
    b=int(input('Enter marks:'))
    d.update({a:b})
print(d)
d=sorted(d.items(), key=lambda x: x[1])
print('Sorted by value:',d)
#-------------------------------
#Assignment->3->C->3
st="MISSISSIPPI"
l=list(st)
s=set(l)
n=list(s)
d=dict()
y=0
for i in s:
    x=0
    for j in l:
        if(i==j):
            x=x+1
    d.update({n[y]:x})
    y=y+1
print(d)
