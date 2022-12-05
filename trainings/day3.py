#comments
#single line:use #
#this is a comment
#multiline comment:use ''' /"""
'''this is a multiline comment
whts up wht are you doing
hope all ar good'''
"""this is a multiline comment
whts up wht are you doing 
hope all ar good"""

#if else
x=9
if(x>5):
    print("i am bigger")
    print("i am wrt if")
print("i am outside") #out of scope of if

if(x<5):
    print("im less")
else:
    print("im greater")
print("end statement")
#short hand
x=7
#if(x>6): else:print("study this")

x=10
if(x>2):
    print("t")#<--- it prints
elif(x>5):
    print("th")
elif(x>6):
    print("thi")
else:
    print("this")

#for loop
#for lists

mpl=["java","html","react","js"]
for any in mpl:
    print(any)

#for tuple
mpl2=("java","html","react","js")
for any in mpl2:
    print(any)

#for set
mpl3={"java","html","react","js"}
for any in mpl3:
    print(any)


#for dictionary
sr={1:"ads",2:"ass",3:"mini"}
#get the keys
for any in sr:
    print(any)
# get the values
for any in sr:
    print(sr[any])
# get the key against the values
for key, value in sr.items():
    print(key, value)

# in strings
str1="abcd"
for s1 in str1:
    print(s1)


#while loop
i=0
while(i<5):
    print("inside ",i)
    i+=1


#Strings
str="abcd"
k=0
lengthofstr=len(str)
print(lengthofstr)
while(k<lengthofstr):
    print("st 1")
    if(str[k]=="c"):
        print("required str found at ",k)
        break
    #print("st 1")
    k+=1


mystr="    "
print(len(mystr))


#represent multi strings
multilinestring="""this is 
can you see this bullshit 
a multiline comment"""



#SELF LEARNING
#string operators:
a="mini mini mini"
b="jain"
print(a+b)#concatenation
print(a*2)#repetition
print(a[1])#slice
print(a[1:4])#slice range
print("m" in a) #check in if a character is present in a string
print("hello %s" %(a))
print(a.count("mini"))
print(a.capitalize())
print(len(a))
print(a.find("m"))
print(b.index("j"))
print(a.isalpha())
print(a.islower())
print(a.split(" "))
print(a.rsplit(";"))
print(a.max)
print(a.index(a,start=3,end=len(a)))




#conditional statements
"""if-else
if-elif-else
"""

