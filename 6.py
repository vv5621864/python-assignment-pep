#--------------------------------------------
#Assignment: 6->1
def areaCircle():
    r=int(input('Radius:'))
    a=(22/7)*r*r
    print('Area of circle:',a)
#--------------------------------------------
#Assignment: 6->1
def perfect():
    a=int(input('Enter range of perfect number:'))
    n=int(a/2)+1
    ans=list()
    for x in range(1,a+1):
        sum=0
        for i in range(1,n):
            if(x%i==0):
                sum=sum+i
        if(sum==x):
        ans.append(x)
    print(ans)
