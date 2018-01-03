#!/usr/bin/env python

'''
Author: Mattuas Grondahl
Date: Januari 2018
Filename: noname.py
Description: NTLM brute forcer

Copyright (c) 2018, Mattias Grondahl All rights reserved.

'''

'''
Requirements
pip install colorama
'''

import socket
import argparse
from colorama import Fore, Back, Style, init
init()

def dns(domainname):
	filename = "discover.txt"
	print ("Checking lync avalability for domain: " + Fore.RED + domainname + Style.RESET_ALL)
	print ("\nThis will check the hostnames in: " + Fore.GREEN + filename + Style.RESET_ALL + "\n")
	
	with open(filename) as f:
		lyncdiscover = f.readlines()
		for line in lyncdiscover:
			line = line.strip()
			target = str(line) + ('.') + str(domainname)
			try:
				addr1 = socket.gethostbyname(target)
				pass
			except Exception as e:
				error = str(e)
			print(Fore.GREEN + target + Style.RESET_ALL + "				 " + Fore.RED + addr1 + Style.RESET_ALL)


	print("done")

def main():
	parser = argparse.ArgumentParser(description="Lookup vaild DNS for domainname")
	parser.add_argument("-d", "--domainname", help="the domain name to check")
	args = parser.parse_args()
	domainname = args.domainname
	url = args.url
	dns(domainname)
	#url_request(url)

if __name__ == '__main__':
    main()

