#integrate logging in your files

import logging

logging.basicConfig(filename="Ciscofile001.log",level=logging.DEBUG)
logging.info("Start:division program")
try:
    x=int(input("enter fno : "))
    y = int(input("enter sno : "))
    logging.info(x)
    logging.info(y)
    print(x/y)
except ZeroDivisionError as msg:
   # print("cannot be divided by zero")
   logging.error("cannot be divided by zero")
   logging.exception(msg)
except ValueError as msg:
   # print("please provide int value only")
    logging.error("not int value")
    logging.exception(msg)
logging.info("end in file")
logging.info("end here")


