try:
    date=eval(input("enter the date"))
except SyntaxError:
    print("date not correctly formated")
else:
    print("you entered :",date)


try:
    name=input("enter filesname")
    f=open(name,"r")
except IOError:
    print("file not found",name)
else:
    n=len(f.readlines())
    print(name,"has ",n,"lines.")
    f.close()