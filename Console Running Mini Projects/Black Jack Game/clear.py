# this program is used to 
# clear screen

import os
def clear():
   os.system('cls' if os.name == 'nt' else 'clear')
clear()

# use the below code to use the clear screen in your program

# import sys
# sys.path.append("C:\VScode_workspace\python_vscode")
# from clear import clear
# clear()