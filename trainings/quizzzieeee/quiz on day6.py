"""#q1
try:
    print("try")
except:
    print("except")
finally:
    print("finally")

#output:try finally
#q2
try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")
#output:try except finally

#q3
try:
    print("try")
   # print(10/0)
except NameError: #guy doesnt catch the zero divide error so it wont accept
    print("except")
finally:
    print("finally")

#output:try finally dividebyzero error for th eception

#q4
import os
try:
    print("t b")
    os._exit(0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")

#output: only try block
"""
print("q5")
#q5
try:
    print("try")
    #print(10/0)
except :
    print("except")
else: #only execute when there is no error in try block
    print("else")
finally:
    print("finally")
#output1: when 10/0 error-> no else
#output2: when no 10/0 error else printed
#try->except->else->finally

#q6
"""try:
    print("t")
output:error try and except needed"""
#q7
"""except:
    print("except")
output:error no try block"""

#q8:finally and else works on above
print("q9")
#q9
try:
    print("t b")
finally:
    print("f b")

#q10
try:
    print("t b")
except:
    print("e b")

#q11
try:
    print("t b")
except:
    print("e b")
else:
    print("ee b")

#q12
"""try:
    print("t b")
else:
    print("e b")"""
#else will only work when we have except

#q13
"""try:
    print("t b")
else:
    print("e b")
finally:
    print("f b")"""
#output:not valid no except for try

#q14
"""try:
    print("t b")
except XXX:
    print(xx)
except YYY:
    print("e b")"""
#OUTPUT VALID: try with multi except



#custom exception
class IdCardNotFoundException(Exception):
    def __init__(self,arg):
        self.msg=arg
"""any name to the class init 
func will execute first"""


#swap="Failed"
swap="Success"


if swap=="Failed":
    raise IdCardNotFoundException("please wait we ll bring temp id card for you")
else:
    print("enter in to the campus")
