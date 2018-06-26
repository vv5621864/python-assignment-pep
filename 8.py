#----------------------------------------------------------------------------
#Assignment :8->1
class Circle:
    def getArea(self,r):
        a=(22/7)*r*r
        print('Area:',a)
    def getCircumference(self,r):
        p=2*(22/7)*r
        print('Circumference:',p)

r=int(input('Enter radius:'))
c=Circle()
c.getArea(r)
c.getCircumference(r)

#----------------------------------------------------------------------------
#Assignment :8->2
class Student:
    def __init__(self,name,rol):
        self.name=name
        self.rol=rol
    def display(self):
        print('Name:',self.name,'\tRoll No.:',self.rol)
s=Student('vaibhav',24)
s.display()

#----------------------------------------------------------------------------
#Assignment :8->3
class Temprature:
    def convertFahrenheit(self,tc):
        self.tc=tc
        f=tc*1.8+32
        print('In Fahrenhite:',f)
    def convertCelsius(self,tf):
        self.tf=tf
        f=(self.tf-32)/1.8
        print('In Celsius:',f)

t=Temprature()
t.convertFahrenheit(0)
t.convertCelsius(40)        

#----------------------------------------------------------------------------
#Assignment :8->4
class Movie:
    def __init__(self,name='Gadar',artist='Sunny Deol',year=1995,rat=5):
        self.name=name
        self.artist=artist
        self.year=year
        self.rat=rat
    def display(self):
        print('Movie details are:')
        print('Movie name:',self.name,' ,Artist:',self.artist,' ,Year:',self.year,' ,rat:',self.rat)
    def update(self):
        self.name=input('Enter movie name:')
        self.artist=input('Enter artist:')
        self.year=int(input('Enter year:'))
        self.rat=input('Enter rating:')

m=Movie()
m.display()
m.update()
m.display()


#----------------------------------------------------------------------------
#Assignment :8->5
class Expenditure:
    def __init__(self,exp=10000,sav=20000):
        self.exp=exp
        self.sav=sav
    def displayExpSav(self):
        print('Total expenditure is:',self.exp,' ,Total saving is:',self.sav)
    def getSalary(self):
        self.sal=self.exp+self.sav
    def showSal(self):
        print('Total salary is:',self.sal)
e=Expenditure()
e.displayExpSav()
e.getSalary()
e.showSal()
