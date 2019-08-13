import logging
##logging.basicConfig(filename='log.txt',level=logging.WARNING,format='%(asctime)s-%(message)s')
##print("python logging demo")
##logging.debug("debug message")
##logging.info("info message")
##logging.warning("warning message")
##logging.error("error message")
##logging.critical("critical message")




logging.basicConfig(filename='jaya.log',format='%(asctime)s:::%(name)s--%(message)s',level=logging.INFO)

logging.info("A new request come")
try:
    x=int(input("Enter first value: "))
    y=int(input("Enter second value: "))
    print(x/y)

except ZeroDivisionError as msg:
    print("can not divided by zero")
    logging.exception(msg)

except ValueError as msg:
    print("can not divided by text")
    logging.exception(msg)


logging.info("Request process compleated")
