import logging
logging.basicConfig(filename='aaa.txt',level=logging.ERROR)
try:
 a=10/0
except Exception as e:
 logging.exception(e);