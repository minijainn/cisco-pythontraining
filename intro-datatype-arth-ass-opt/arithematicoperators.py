
#arithematic operator(+)
a=10
b=4
c=a+b
print(type(c))
print(c)

a=10.5
b=4.9
c=a+b
print(type(c))
print(c)

a=20
b=30.5
c=a+b    #int+float==>float
print(type(c))
print(c)

#arithematic operator(-)

a=10
b=5
c=a-b
print(type(c))
print(c)

myage=70
kidsage=10
diff=myage-kidsage
print(type(diff))
print(diff)

val1=30
val2=40
addme=(val1)+(-val2)
print(type(addme))
print(addme)

myfbalance=-990
mysbalance=-90
mygbalance=myfbalance-mysbalance
print(type(mygbalance))
print(mygbalance)

#arithematic operator(*):multiplication
x=2
y=3
z=5*6
print(type(z))
print(z)

z1=x*y
print(type(z1))
print(z1)

x1=-10
y1=10
m1=x1*y1
print(type(m1))
print(m1)

#arithematic operator(/):division
x=10
y=2
z=x/y
print(type(z))
print(z)

x=11
y=2
z=x/y
print(type(z))
print(z)

#arithematic operator(%):modulus
m=21
n=2
v=m%n
print(type(v))
print(v)


x=99
y=2
z=x%y
print(type(z))
print(z)

#arithematic operator(**):exponential
a=2
b=2
c=a**b
print(type(c))
print(c)

a=2
b=3
c=a**b
print(type(c))
print(c)

x1=5
y1=0
z1=x1**y1
print(type(z1))
print(z1)

x1=5
y1=0
z2=y1**x1
print(type(z2))
print(z2)

#arithematic operator(//):floor division
#diff between floor devision and normal division

#case1:if m & n tends to + infinity /-infinity & r=0 then it returns q
x=10
y=2
z=x//y
print(type(z))
print(z)

m=4
n=2
mn=m//n
print(type(mn))
print(mn)


m=20
n=10
mn=m//n
print(type(mn))
print(mn)


x1=20.0
y1=10
z1=x1//y1
print(type(z1))
print(z1)

#case2:if m or n tends to infinity & r=0 then it returns -q
a1=-4
b1=2
c1=a1//b1
print(type(c1))
print(c1)

a2=6
b2=-3
c2=a2//b2
print(type(c2))
print(c2)


a3=11
b3=-1
c3=a3//b3
print(type(c3))
print(c3)

#case3:if m or n tends to -infinity & r!=0 then it returns -(q+1)
a4=11
b4=-2
c4=a4//b4
print(type(c4))
print(c4)


a4=-90
b4=4
c4=a4//b4
print(type(c4))
print(c4)



