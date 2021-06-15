import json
import time
import sys
import os
import requests
import random

def awal():
	os.system('clear')
awal()

def ketik(w):
	for c in w + '\n':
		
		sys.stdout.write(c)
		sys.stdout.flush()
		
		time.sleep(random.random() * 0.1)
		
ketik('\x1b[0;32m=============================================')
ketik('        Welcom In progress Broken Night')
ketik('=============================================')
ketik('[+] Sc By: Rizal')
ketik('[+] Support Me: Broken Night')
ketik('- - - Warning!!')
ketik('Dilarang Mengakui sc ini!')
ketik('--------------------------')

print "\n"
print "\x1b[1;33m| Verifi |"

user = raw_input("- -Username: ")
	
print "- - - Done! - - - "
print "-- User: ",user
print "\n"
print "---- Value Hex ----"

number = 100

print "Value:",hex (number) + "\n100"

number2 = 250

print "Value:",hex (number2) + "\n250"

number3 = 550

print "Value:",hex (number3) + "\n550"

number4 = 1.5

print "Value:",float.hex (number4) + "\n1.5"

number5 = 10.5

print "Value:",float.hex (number5) + "\n10.5"
print "- - Done! - -"
print "\n"
print "---- Spam Sleep ----"
call = raw_input("Nomor Telepon: ")
spam = input("Jumblah Spam: ")
for i in range(spam):
	time.sleep(0.2)
	print "Spam> " + str(i+1)
print "Nomor Telepon: ",call
print "jumlah spam: ",spam
print "Sukses"