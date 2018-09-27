#!/usr/bin/python

class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	TUTUP = '\033[00m'
	
hanyaJudul = """
+------------------------------------+
|            Admin Finder            |
|   Version  : 1.2                   |
|   Author   : Security007           |
|   Pesan    : Jangan mengganti      |
|              Author!!              |
|           Copyright 2018           |
+------------------------------------+"""
print warna.KUNING+hanyaJudul+warna.TUTUP
print ""
import urllib, sys, time

site = raw_input("Ip/Host [http://victim.com/<path>] >>> ")
daftar = raw_input("List Of Admin Page [list.txt] >>> ")
url = site
list = daftar
try:
	buka = open(list,"rb")
	c = buka.readlines()
	p = len(c)
except:
	print warna.MERAH+"[-]List tidak ketemu/directory salah"+warna.TUTUP
	sys.exit()
try:
	for file in range(p):
		b = c[file]
		req = urllib.urlopen(url+"/"+b)	
		hasil=url+"/"+b
		if (req.code == 200):
			print hasil,warna.HIJAU+"[+]Ketemu > 200 ok\r\n\r"+warna.TUTUP
		elif (req.code == 403):
			print hasil,warna.KUNING+"[+]Ketemu > 403 Forbidden\r\n\r"+warna.TUTUP
		else:
			print hasil,warna.MERAH+"[-]Tidak Ketemu > 404 not found\r\n\r"+warna.TUTUP
except:
	print warna.HIJAU+"Rebuild url to http://"+site+"/"+warna.TUTUP
	time.sleep(3)
	for file in range(p):
		b = c[file]
		req = urllib.urlopen("http://"+url+"/"+b)	
		hasil=url+"/"+b
		if (req.code == 200):
			print hasil,warna.HIJAU+"[+]Ketemu > 200 ok\r\n\r"+warna.TUTUP
		elif (req.code == 403):
			print hasil,warna.KUNING+"[+]Ketemu > 403 Forbidden\r\n\r"+warna.TUTUP
		else:
			print hasil,warna.MERAH+"[-]Tidak Ketemu > 404 not found\r\n\r"+warna.TUTUP