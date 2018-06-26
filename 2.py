from collections import deque
#-------------------------------
#Assignment->2->1,2,3
l=list()
l=list(map(str,input().split()))
l=l+['google','apple','facebook','microsoft','tesla']
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
#-------------------------------
#Assignment->2->4,5
a=[12,10,1,2,15,3,25,8]
a=sorted(a)
b=[15,9,12,30,7]
c=a+b
c=sorted(c)
print('both array joined and sorted:',c)
#-------------------------------
#Assignment->2->6
#list as stack
l=[1,2,3,4]
l.append(5)
l.append(6)
l.append(7)
print(l)
l.pop()
print(l)
l.pop()
print(l)

#list as queue
q=deque(l)
q.append(5)
q.append(6)
q.append(7)
print(q)
q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q)
