#redirect to docker container to capture user login
#imports
from pydoc import cli
import sys
import random
import re
import os
import docker
import shutil
import subprocess

from psutil import users


#imports done
#variables
dockerusername = "editme"
dockerpassword = "editme"
docker_image = "ubuntu:latest"  #placeholder for main
#variables done
client = docker.from_env()
#make docker function
def docker_make():
    try:
        client = docker.from_env()
        client.containers.run("ubuntu:latest", "sleep infinity", detach=True, name="faker", user=dockerusername)
        dkr_id = client.containers.list()[0].id
        client.containers.get(dkr_id).exec_run("/bin/bash")
        return dkr_id
    except Exception as e:
        print("[!] Error: " + str(e))
        sys.exit(1)
def getid():
    #get docker container id
    client = docker.from_env()
    client.containers.list()
    return client.containers.list()[0].id
#make docker function done
#make docker function
#make docker function done
#make docker function
def docker_cleanup(docker_iddel):
    try:
        #cleanup docker 
        client = docker.from_env()
        #stop docker container
        client.containers.get(docker_iddel).stop()
        client.containers.get(docker_iddel).remove()
        return 'done'
    except Exception as e:
        print("[!] Error: " + str(e))
        sys.exit(1)
#make docker function done
#make docker function
#make docker function done
#make docker function
def ssh_startdocker(docker_container_id):
    try:
        #ssh into docker container
        
        client = docker.from_env()
        client.containers.get(docker_container_id).exec_run("/bin/bash")
        #apt update
        client.containers.get(docker_container_id).exec_run("apt update")
        #apt install openssh-server
        client.containers.get(docker_container_id).exec_run("apt install openssh-server")
        return docker_container_id
    except Exception as e:
        print("[!] Error: " + str(e))
        sys.exit(1)
#make docker function done

#connect to docker container done
def main():
    #ask user if they want to clean up container or start it
    print("[*] Do you want to clean up the container or start it?")
    print("[*] 1. Clean up")
    print("[*] 2. Start")
    choice = input("[*] Enter choice: ")
    if choice == "1":
        #clean up docker container
        docker_id = getid()
        print("[*] Cleaning up docker container")
        #read AUTO_DOCKER_CONTAINER_ID file
        with open("AUTO_DOCKER_ID", "r") as f:
            docker_iddel = f.read()
        #delete AUTO_DOCKER_CONTAINER_ID file
        os.remove("AUTO_DOCKER_ID")
        #clean up docker container
        docker_cleanup(docker_iddel)
    elif choice == "2":
        #start docker container
        print("[*] Starting docker container")
        docker_make()
        docker_id = getid()
        print("[*] Connecting to docker container")
        print("[*] Starting ssh session")
        ssh_startdocker(docker_id)
        print("[*] Done")
        #execute commands on docker container dont use ssh
        print("[*] Executing commands on docker container")
        client.containers.get(docker_id).exec_run("/bin/bash")
        print("[*] Script complete")
        #save docker id to file called AUTO_DOCKER_ID
        with open("AUTO_DOCKER_ID", "w") as f:
            f.write(docker_id)
        print("[*] Saved docker id to file called AUTO_DOCKER_ID")
        #get ip address of docker container, username and password
        print("[*] Getting details of docker container")
        client.containers.get(docker_id).exec_run("/bin/bash")
        print("[*] Getting ip address of docker container")
        #save to variables
        ip = client.containers.get(docker_id).attrs['NetworkSettings']['IPAddress']
        print("[*] Getting username of docker container")
        username =  dockerusername
        print("[*] Getting password of docker container")
        password = client.containers.get(docker_id).attrs['Config']['Env'][0].split("=")[1]
        print("[*] Script complete")
        #save details to file called AUTO_DOCKER_DETAILS
        with open("AUTO_DOCKER_DETAILS", "w") as f:
            f.write(ip + "\n" + username + "\n" + password)

            
        print("[*] Saved details to file called AUTO_DOCKER_DETAILS")
        #print details to screen
        print("[*] Printing details to screen")
        print("[*] IP address: " + ip)
        print("[*] Username: " + username)
        print("[*] Password: " + password)
        print("[*] FINISHED")



    else:
        print("[!] Error: Invalid choice")
        sys.exit(1)



#main function
main()





#idk if this script works i just wrote a bunch of random stuff lol
#also pls gimme credit if you use this script 


#https://kofi.com/hmmlopl