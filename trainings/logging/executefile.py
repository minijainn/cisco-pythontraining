"""import logging

logging.basicConfig(filename="Ciscofile001.log",level=logging.WARNING)
#logging.basicConfig(filename="Ciscofile001.log",level=logging.NOTSET)
logging.basicConfig(filename="log.txt",level=logging.DEBUG)
try:
    x=int(input("enter fno : "))
    y = int(input("enter sno : "))
    print(x/y)
except ZeroDivisionError as e:
    print("cannot be divided by zero")
    logging.exception(e)
except ValueError as msg:
    print("please provide int value only")
    logging.exception(msg)



#level:decide till where you need to print the data
logging.info("i am info msg 1")
logging.debug("i am debug msg ")
logging.error("i am info msg 2")
logging.error("i am warning msg 1")
logging.critical("i am error msg1")
logging.warning("i am critical msg 1")


"""
import logging



def main():
    logging.basicConfig(filename="trymain.txt",level=logging.INFO)
    logging.info("its started")
    gotofun()
    logging.info("its done")



if __name__=='__main__':
    main()
    #mylib.py
    import logging

def gotofun():
    logging.info("im from second function")

