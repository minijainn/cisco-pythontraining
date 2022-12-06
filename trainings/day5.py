#tuple
#tuple with elements
tuplee=("asia","africa","australia")
print(tuplee)
print(type(tuplee))
#tuple with one element
tuplee=("asia",)
print(tuplee)
print(type(tuplee))
#tuple without brackets
tuplee="asia","africa","australia"
print(tuplee)
print(type(tuplee))
#empty tuple
t=()
print(type(t))

#tuple function
#convert a list to tuple
mydata=[10,20,30,40]
t=tuple(mydata)
print(t)
print(type(t))

#tuple using range function
rt=tuple(range(0,10,2))
print(rt)
print(type(rt))

#tuple index representation
t=(10,20,30,40,50)
print(t[2])
#print(t[100])#index out of range
#tuple and slicing
print(t[2:5])
print(t[2:100])
print(t[:4])
print(t[-2:-5])#doesnt work
print(t[-5:-2]) #works
print(t[::2])#double colons intervals

#check for immutablity
print(t[1])
#t[1]=70 #tuples don't support item assignment


#tuple with while loop
wt=(2,3,4,5,6,7,7,6,7,8)
i=0
while i < len(wt):
    print(wt[i])
    i+=1

for i in range(0,len(wt)):
    print(wt[i])


import sys
print("count")
print(wt.count(7))
print("Size of Tuple1: " + str(sys.getsizeof(wt)) + "bytes")
wts=sorted(wt)
print(wts)
print(wt.count(7))
print(wt.index(7))
print(min(wt))
#concatetaion of 2 tupless
#repetition of tuple
#cmp() to compare 2 tuples
t1=(2,3,4)
t2=(2,3,4)
#print (cmp(t1, t2))#not in python 3 only in python2


#set
countryName={"india","japan","uk","usa","india"}

print(countryName)
print(type(countryName))

rollno=[1,2,3,4,5,6]
s=set(rollno)
print(s)
print(type(s))

myset=set(range(5))
print(myset)
print(type(myset))
#empty set
"""myemptyset={}<class 'dict'>
print(type(myemptyset))"""
#have to define set
myemptyset=set()
print(type(myemptyset))
myemptyset.add("australia")
print(myemptyset)

#write a code to traverse the set element using 1.while 2.for

"""i=0
while i < len(countryName):
    print(countryName[i])
    i+=1
    """
"""for i in range(1,len(countryName)):
    print(countryName[i])"""

#we cannot traverse through a set without converting it into a list



myset={2,3,4,45}
myset.add(40)
myset.add(0)
myset.add(1)
#ordered
print(myset)
countryName.update(myset)
print(countryName)

dupl=myset.copy()
print(dupl)
print(myset.pop())
print(myset)
print(myset.remove(3)) #key not found get error
print(myset)
#myset.clear(10)
print(myset)
print("discarding")
print(myset.discard(2))
print(myset)

#mathematical operations
#union
x={1,2,3,4,5}
y={5,6,7,8,9}
print(x.union(y))
print(x|y)
#intersection
x={1,2,3,4,5}
y={5,6,7,8,9}
print(x.intersection(y))
print(x&y)
#difference
x={1,2,3,4,5}
y={5,6,7,8,9}
print(x.difference(y))
print(x-y)
#symmetric-difference
x={1,2,3,4,5}
y={5,6,7,8,9}
print(x.symmetric_difference(y))
print(x^y)


#dictionary

print("dictionaryyyyyy")
d={1:"one",2:"two",3:"three"}
print(type(d))
d[4]="four"
print(d)
d[2]="second"
print(d)
if 1 in d:
    del d[1]
else:
    print("key not exits")
print(d)



"""d.clear()
print(d)"""

dictvalue=d.get(2)
print(dictvalue)


"""del d
print(d) # name 'd' is not defined."""
"""item=d.popitem()
print(item)"""

#for loop in dictionary
print("dictionary using for loop")
for i in d:
    print(d[i])

#print("dictionary using while loop")
#cant happen cause there is no index in dict
"""i=0
while i<len(d):
    print(d[i])
"""



#functions
def myfun():
    print("im here")

myfun()
myfun()

#can call the function as many no of times you want
#dont forget calling the function

#variable and pass the function
def addtwo(a,b):
    c=a+b
    return c

ans=addtwo(15,14)
print(ans)

#function with argument
def addtwo(a,b):
    c=a+b
    print(c)

addtwo(5,9)

#dynamically calling the functions at timers
def welcomemsg(name,timeofday):
    print("hi " +name+","+timeofday)


import datetime
currentTime = datetime.datetime.now()
loginname="mini"
print(currentTime)
if currentTime.hour < 12 :
    welcomemsg(loginname,"good morning")
if currentTime.hour > 6 :
    welcomemsg(loginname,"good evening")

def getsum(a,b):
    print("fno",a)
    print("sno",b)
    return a+b
    print("doesnt print this")

res=getsum(9,4)
print(res)

def findoddeven(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

findoddeven(20)

#return 2 / 3 things together
def sumsub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub

s=sumsub(12,5)
ss=sumsub(12,9)
print(s,ss)

#do a calculator
def calsi(a,b):
    sum=a+b
    diff=a-b
    mul=a*b
    div=a/b
    return sum,diff,div,mul

s,d,m,dd=calsi(12,4)
print(s,d,m,dd)


def wish(name="p"):
    print("hello",name)

user="mini"
wish(user)