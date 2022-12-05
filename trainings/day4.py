#iterate the string using "in" keyword
#dynamically pass the values in the variables
learner1="mini jain"
if "mini" in learner1:
    print("true")

#formatting a string==>web development
print("%(t)d is completed courses"%{"t":1000})

print("%(edtech)s is %(rank)d %(course)s learning platform in %(country)s"%{"edtech":"simplilearn","country":"india","course":"python","rank":1})

#omly if there is one value
simplilear_tag="{}+ hiring partners"
hp=200
print(simplilear_tag.format(hp))
#multiple values
heading="{edtech} is {review}"
print(heading.format(edtech="simplilearn",review="good"))


#slicing a string
mystr="abcd"
print(mystr[0])
print(mystr[1])
print(mystr[-1])
print(mystr[1:3])
print(mystr[0:6]) #anygreater no it will ignore and print how much is the string
print(mystr[0:])
#print(mystr[80]) #index out of range
print("********************")
print(mystr[-1:0]) #no ouput
print(mystr[-1:-1]) #no ouput -(1-1)==>0








#Lists
countrylist=["india","argentina","china"]
print(countrylist)

#dynamiclist=eval(input("enter the list: "))
#print(dynamiclist)
#print(type(dynamiclist))

x=list(("mini","darsh","jai"))
print(x)

x=list(range(0,10,2))
print(x)
x=list(range(0,15,3))
print(x)

#using split function on strings to make them into lists
str="dont kn from tommoroow you are gonna concentrate on these concepts"
str_list=str.rsplit(" ")
print(str_list)


#lists-->mutable
n=[10,20,30,80,60,40,90]
print(n)
n[1]=50
print(n)

print("this is while loop printing a list")
i=0
while i<len(n):
    print(n[i],end=",")
    i+=1

print("\nthis is for loop printing a list")
for n1 in n:
    print(n1,end=";")

#write a program to print only even numbers
print("\nwrite a program to print only even numbers")
mylist=[1,2,3,4,5,6,7,8,9,0,2,2,3]
for n in mylist:
    #print(mylist[n],end="|")
    if mylist[n]%2==0:
        print(mylist[n],end=",")



print("\nlist operations")
for i in range(0,len(mylist)):
    print(mylist[i])




print("len command")
print(len(mylist))
print(mylist.count(2))
print(mylist.index(3))
mylist.append(10)
print(mylist)
mylist.insert(4,80)
print(mylist)
newlist=[7,8,9,0,6,4,3,2,4]
mylist.extend(newlist)
print(mylist)
mylist.remove(2,)
print(mylist)
mylist.pop()
print(mylist)
ele=mylist.pop(15)
print(ele)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
#contactenation,repetition,in and not in
#nested lists
nl=[1,2,3,4,[1,2,3,4,5,6],[0,9,6,[5,7,4,3]]]
print(nl[4])
print(nl[4][4])
print(nl[5][3][1])
