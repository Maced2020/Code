# this does not work yet. because the Public key does not let the user SSH in. 
# I am sure i am doing something wrong but i dont know what it is. 

import os
import time

username = input("Give me a user name: ")
currenthostname = input("Old host name; give me everything after the @: ")
hostname = input("give me new host name: ")
publicssh = input(" paste in your public ssh key: ")


usercommand = 'sudo adduser ' + username
hostnamecommand = 'sudo sed -i s/' + currenthostname + '/' + hostname + '/ /etc/hostname'


os.system(hostnamecommand)
print("hostname changed")

time.sleep(2)

os.system(usercommand)
print("User ",  username, " added successfully!")

time.sleep(2)

os.system('sudo mkdir /home/' + username + '/.ssh')

print ("ssh directory created ")

time.sleep(2)

os.system('sudo chmod 700 /home/' + username + '/.ssh')

print("folder permisson changed")

time.sleep(2)

os.system('echo ' + publicssh + '>> /home/' + username + '/.ssh/authorized_keys')

print("ssh key added, please restart and log in with new user.")
