# This Source is for 2 years ago
# By Confused Character
# github 

import socket
import sys
import time
from urllib.parse import urlparse
import os
import random
import threading

lists = open("subs.txt",encoding="utf-8").read().splitlines()

guardlists =["104.26.0.120","172.67.71.217","185.143.234.85","185.143.233.85","104.26.1.120","104.16.133.229","185.215.235.21","185.215.234.21","186.2.163.99","185.178.208.176","193.31.15.1","35.227.204.58"]
os.system('cls')
print('''

\033[94m
█▀▀ █▀█ █▄░█ █▀▀ █░█ █▀ █▀▀ █▀▄   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
█▄▄ █▄█ █░▀█ █▀░ █▄█ ▄█ ██▄ █▄▀   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
\033[0m

''')

ms1 = "Enter Website To Start Check Sub Domains : "
for x in list(ms1):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.01)

site = input("")

if "http" in site:
    site = urlparse(site).netloc

ms2=f"\nCurrent {site} IPV4 : {socket.gethostbyname(site)}\n\nPress Enter To Start..."

for x in list(ms2):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.01)

input("")

try:
    os.remove("NoGuard.txt")
except:
    pass
try:
    os.remove("UnderGurad.txt")
except:
    pass

open("NoGuard.txt",'x',encoding='utf-8').write("")
open("UnderGurad.txt",'x',encoding='utf-8').write("")

hitguard=[]
hitnoguard=[]

def bypass(target):
    while lists != []:
        rand = random.choice(lists)
        try:
            gett = socket.gethostbyname(rand+'.'+target)
            if gett not in guardlists:
                hitnoguard.append(f"{rand+'.'+target} ~ {gett}")
                lists.remove(rand)
                try:
                    open("NoGuard.txt",'w+',encoding='utf-8').write("\n".join(set(hitnoguard)))
                except:
                    pass
            else:
                hitguard.append(f"{rand+'.'+target} ~ {gett}")
                lists.remove(rand)
                try:
                    open("UnderGurad.txt",'w+',encoding='utf-8').write("\n".join(set(hitguard)))
                except:
                    pass
        except:
            try:
                lists.remove(rand)
            except:
                pass

def Status():
    print("\n")
    while lists != []:
        num = 135612 - len(lists)
        sys.stdout.write("\r[ + ] Finding "+str(num)+" /135613 ~ %"+str(round(num * 100 / 135613,2))+" NoGuard : "+str(len(set(hitnoguard)))+" , UnderGuard : "+str(len(set(hitguard))))
        sys.stdout.flush()
    else:
        input("\n\nHit File Saved (UnderGurad.txt & NoGuard.txt)\n\nPress Enter To Exit!")

threading.Thread(target=Status).start()
for x in range(1000):
    threading.Thread(target=bypass,args=(site,)).start()