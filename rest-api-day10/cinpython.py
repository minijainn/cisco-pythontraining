import subprocess
import os

def executec():
    s=subprocess.check_call("gcc helloWorld.c -o out1;./out1",shell=True)
    print(",return code",s)



def executeCPP():
    data,temp=os.pipe()
    os.write(temp,bytes("5 , 10 \n""utf-8"))
    os.close(temp)
    s = subprocess.check_call("g++ helloWorld.c -o out1;./out1", shell=True)
    print(s.decode("utf-8"))
    print("returncode",s)


def executeJava():
    s=subprocess.check_output("javac helloWorld.java;java HelloWorld",shell=True)
    print(s.decode('utf-8'))

# if __name__=="main":
#



executec()
executeCPP()
executeJava()


