import sys import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__)+'/src'))) 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__) + '/tests' )))



#from care import get_answer from core import main
from core import main
if__name__=='__main__':
  f = open("packets/tcp.txt","r") 
  B = open('packets/udp.txt','r')
  main(f)
