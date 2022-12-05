print("hello")
#int datatype
a=10
print(type(a)) #<class 'int'> keyword:int
print(a)
#float datatype
b=10.45
print(type(b)) #<class 'float'> keyword:float
print(b)
#complex datatype
x=10+80j
print(type(x)) #<class 'float'> keyword:float
#print(x+iy)
#string datatype:array of characters keyword:str
myName="Mini"
print(type(myName)) #<class 'str'>
print(myName)
#**********************#
myage="3.14"
print(type(myage))
#concatenation
fn="mini"
ln="jain"
fullname=fn+" "+ln
print(fullname)
initialname='mr'
print(type(initialname))
#single and double quotes==>string why both in " " & ' '

#Homework--> convert all the above code into single quote and verify output
fn='mini'
ln='jain'
fln=fn+' '+ln
print(fln)

#all these datatypes can hold only single value
#************************************#

#to hold multiple value-->multiple item in single variables
#list datatype
countryList=["ind","pak","uk","us"]
print(type(countryList)) #<class 'list'>
print(countryList) #output:['ind', 'pak', 'uk', 'us']
# (given in double quotes got ouput in single quotes whyy?
# string denoted in " " & ' ' python will convert
# )


mixedList=[2,"3","mini"]
print(mixedList)

#dictionary keyword:dist
#keyword:unique value:may duplicate values

anydict={101:"mini",102:"jay"}
print(type(anydict))
print(anydict)


#tuples keyword:tup:multiple value can stored,order cannot be changed
names=("ads","jays","ankkits")
print(type(names))
print(names)
#int type tuple:
inttup=(1,2,3,456)
print(type(inttup))
print(inttup)


#set
books={"java","C++","python","html"} #setofstrings
print(type(books))
print(books)
numbersets={254,876,98,345}
print(numbersets)


#[]=list,{:}=dict,()=tuple,{}=set

#boolean
istrue=10>20
print(type(istrue))
print(istrue)


print(4,"Data",123)
