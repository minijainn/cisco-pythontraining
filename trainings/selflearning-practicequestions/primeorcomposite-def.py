def primeOrComposite(num):
    x=1
    for i in range(2,num):
        if num%i==0:
            x=0
            break;
        else:
            x=1
    return x


num=int(input("enter the number"))
res=primeOrComposite(num)
if res==0:
    print("composite")
else:
    print("prime no")