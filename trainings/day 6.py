
#exception handling-
#have the requirnment to read the file /database
# and while running find the file doesnt exists


#error- shown by red
#compile
#two types==>1.syntax error & 2.runtime error
#syntax error: at compile time ex:print "hi" (observe no brackets)
#runtime error: at runtime no red lines ex:10/0 (divide by zero error)

#print "hi" #syntax missing==>compile time
#print(10/0) #ZeroDivisionError: division by zero==>logic problem
#logical error causes runtime error

#Exception:
print("st1") #1
try:
    print(10/0) #it will throw the error always risky code #2
    print("st2")#3
except ZeroDivisionError as msg:
    print("i got the error ",msg)
    print(10/2) #temproray code/code tht can execute #4
    print("st3")#5
print("st4")#6

"""1 passes to 2 it passes to 4 and then 5 and 6 but skips 3-->why
if any line is getting exception then below all the code will not get executed at any cost"""
#in try block below exception will not get executed
#how to believe the line is throwing the error?-->know wht is the error==>how?
#line 20 is accepting error so when you get  print the msg
#exception handling is how to print the error





print("st1") #1
try:
    x=int(input("enter the fno: ")) #invalid literal for int() with base 10: '9.2'==>error
    y=int(input("enter the sno: "))
    print(x/y)
except ZeroDivisionError:
    print("my own msg--> cannot divide with zero")
except ValueError:
    print("please provide int value only")

#clean codes and handle the error mesgs
#now handle the error in one lines

try:
    x=int(input("enter the fno: ")) #invalid literal for int() with base 10: '9.2'==>error
    y=int(input("enter the sno: "))
    print(x/y)
except (ZeroDivisionError,ValueError):
    print("my own msg--> cannot divide with zero or please provide int value only")
finally:
    print("i finally")

#finally==>terminate the jvm/end the program/close a file
#import means to include external library


"""i m done here"""

import os
try:
    print("this is try block")
    os._exit(0)
except NameError:
    print("i am in except")
finally:
    print("i am finally")


#finally block-->? always get executed because os isnt there

"""#custom exception
class IdCardNotFoundException(Exception):
    def __init__(self,arg):
        self.msg=arg

swap="entry gate swapping success"

if swap=="entry gate swapping success":
    raise IdCardNotFoundException("please wait we ll bring temp id card for you")
"""
#check in quizeeiieeee

#in project -->please check the log
#Logging level
"""few things to mention while writing alog
    1:critical :50-->some serious problem in code
    2:error: 40-->runntime error in production
    3:warning:30-->
    4:info:20
    5:debug:10
    6:noset:0"""

#logging
#threads-->

