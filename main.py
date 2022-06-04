#ignore this file it is a placeholder for the future
import os   
import subprocess
import time
import sys
import docker
import shutil
#imports done
#ask for password
#the password is lopl
password='lopl'
#clear screen
os.system('clear')
#ask for password done
print("enter password")
#get password
password_input=input()
#get password done
#check if password is correct
if password_input==password:
    print("password correct")
    #sys.exit(0)
else:
    #run startup.py
    os.system("cd false-core && python3 startup.py")
    #run startup.py done
    