from threading import *
#print("current t:",threading.current_thread().getName())
#bydefault main thread all we write are child thread
#3 ways to create a thread

"""creating threads without any class"""
def mfriends():
    for i in range(1,5):
        print("**friend")

t=Thread(target=mfriends) #create thread #assign task
t.start() #start the thread
print("thanks")

for i in range(1,5):
    print("main thread,thankyou")

#print("current exec thread ",threading.current_thread().getName())
#cannot predict the order of thread execution-->depends on cpu scheduler and depends on the vendor


"""#2:creating a thread by extending thread class"""
class ThreadExample(Thread):
    def run(self):
        for i in range(1,5):
            print("child thread")

t=ThreadExample() #creating object of thread class
#3:creating a thread class
"""check this one
thread=Thread(target=t.ThreadExample()) #thread creation"""
t.start()

#run method only inside the thread class
#eye run method overloaded

"""print(current_thread().getName())
current_thread().setname("Abc")
print(current_thread().getName())
"""#doesnt work
#setname not in python 3

#for each thread there is an identification number
def test():
    print("thread")

t=Thread(target=test())
t.start()

#oops



