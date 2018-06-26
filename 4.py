#----------------------------------------------
#Assignment: 4->1
a=int(input('Enter an year:'))
if(a%100==0):
    if(a%400==0):
        print(a,'is an leap year')
    else:
        print(a,'is not an leap year')
elif(a%100!=0)&(a%4==0):
    print(a,'is an leap year')
else:
    print(a,'is not an leap year')
#----------------------------------------------
#Assignment: 4->2
l=int(input('Enter length:'))
b=int(input('Enter breadth:'))
if(l==b):
    print('Square')
else:
    print('Rectangle')
#----------------------------------------------
#Assignment: 4->3
a=int(input('Enter age of 1st person:'))
b=int(input('Enter age of 2nd person:'))
c=int(input('Enter age of 3rd person:'))
if(a>b)&(a>c):
    print(a,'is oldest')
elif(b>a)&(b>c):
    print(b,'is oldest')
else:
    print(c,'is oldest')
if(a<b)&(a<c):
    print(a,'is youngest')
elif(b<a)&(b<c):
    print(b,'is youngest')
else:
    print(c,'is youngest')
#----------------------------------------------
#Assignment: 4->4
if(a<0)|(a>200):
    print('Invalid input')
elif(a>=0)&(a<=50):
    print('Sorry! No prize this time')
elif(a>51)&(a<=150):
    print('Wooden Dog')
elif(a>151)&(a<=180):
    print('Book')
elif(a>181)&(a<=200):
    print('Choclates')
#----------------------------------------------
#Assignment: 4->5
a=int(input('Enter purchased quantity:'))
a*=100
if(a>1000):
    print('Amount to be paid:',(a*0.9))
else:
    print('Amount to be paid:',a)
