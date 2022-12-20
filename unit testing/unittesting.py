def squareIt(x):
    return x*x

assert squareIt(2)==4,"The square of 2 shld be 4"
assert squareIt(3)==9,"The square of 3 shld be 9"
assert squareIt(4)==16,"The square of 4 shld be 16"
#gives error of assertion error
assert squareIt(5)==20,"The square of 5 shld be 20"


print(squareIt(2))
print(squareIt(5))


#tab==>autocomplete
import rlcompleter
my_completer=lcompleter.Completer()
pythonkeywordlist=['co','ass','fin']
for i in pythonkeywordlist:
    print(i+'(TAB',end='')
    try:
        for j in range(50):
            term=my_completer.complete(i,j)
            if term is None:
                break
            print(terms,end='\t')
        print()
    except:
        pass
