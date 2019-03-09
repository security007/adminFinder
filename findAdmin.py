#!/usr/bin/python
import os
import sys
class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	TUTUP = '\033[00m'
usage ="""
Usage : python %s <target> <wordlist>
"""%sys.argv[0]	
hanyaJudul = """
+------------------------------------+
|            Admin Finder            |
|   Version  : 1.2                   |
|   Author   : Security007           |
|   Pesan    : Jangan mengganti      |
|              Author!!              |
|           Copyright 2018           |
+------------------------------------+"""
if (len(sys.argv)!=3):
	print hanyaJudul+"\n"
	print usage
	sys.exit()
print warna.KUNING+hanyaJudul+warna.TUTUP
#print os.getcwd()
import urllib, time

site = sys.argv[1]
daftar = sys.argv[2]
url = site
list = daftar
try:
	buka = open(list,"rb")
	c = buka.readlines()
	p = len(c)
	print "="*50
	print "Total ada ",p," directory pada wordlist"
	print "="*50
	time.sleep(3)
	print "Start to find admin page..."
	time.sleep(2)
	print "Wait until scanning done..."
except:
	print warna.MERAH+"[-]List tidak ketemu/directory salah"+warna.TUTUP
	sys.exit()
try:
	for file in range(p):
		b = c[file]
		req = urllib.urlopen(url+"/"+b)	
		hasil=url+"/"+b
		if (req.code == 200):
			print "\n"+hasil,warna.HIJAU+"[+]Ketemu > 200 ok\r\n\r"+warna.TUTUP
		elif (req.code == 403):
			print "\n"+hasil,warna.KUNING+"[+]Ketemu > 403 Forbidden\r\n\r"+warna.TUTUP
		else:
			a = "--> "+b
			cc = "Progress ["+str(file)+"/"+str(p)+"]"
			sys.stdout.write("\r%s"%cc)
			sys.stdout.flush()
except IOError:
	print "\nConnection refuse by host"
print "[+] Scan Complete..."
