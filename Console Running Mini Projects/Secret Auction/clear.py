# this program is used to 
# clear screen

import os
def clear():
   os.system('cls' if os.name == 'nt' else 'clear')
clear()