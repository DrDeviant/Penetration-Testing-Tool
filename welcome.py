import random
from colorama import Fore, Back, Style
from extras import printcolor
import pyfiglet

def intro1():
    print('\n********************************************************')
  
    print('*                                                      *')
    print('*                                                      *')
    print('********************************************************\n')

def intro2():
result = pyfiglet.figlet_format("Network Pentration Testing")
print(result)
    printcolor('RED', '\n    _____________  _______   ________  ________  ____                 ')                                                         
    
    
                                                                                                                                          

def welcome():
    introList=[intro2]
    random.choice(introList)()
