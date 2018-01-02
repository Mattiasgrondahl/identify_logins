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

import sys
import argparse
import urllib2
from colorama import Fore, Back, Style, init
init()


#creating lists
forbidden = []
ok = []
access_denied= []
valid_url = [];
invalid_url = [];
valid_path = [];

def lync(domainname):
	filename = "lyncdiscover.txt"
	print ("Checking lync avalability for domain: " + Fore.RED + domainname + Style.RESET_ALL)
	print ("\nThis will check the hostnames defined in: " + Fore.GREEN + filename + Style.RESET_ALL + "\n")
	with open(filename) as f:
		lyncdiscover = f.readlines()
		for line in lyncdiscover:
			line = line.strip()
			target = str(line) + ('.') + str(domainname)
			print("\n" + target)
			url_request(target)

	print("These are the identified 200 OK: " + Fore.GREEN + str(ok) + Style.RESET_ALL)
	print("These are the identified 401 Access Denied: " + Fore.GREEN + Fore.GREEN + str(access_denied) + Style.RESET_ALL)
	print("These are the identified 403 Forbidden: " + Fore.GREEN + str(forbidden) + Style.RESET_ALL)
#after identifying valid urls
	filename = "paths.txt"
	with open(filename) as f:
		paths = f.readlines()
		for line in paths:
			line = line.strip()
			target = str(forbidden[0]) + '/' + str(line)
			print("\n" + target)
			url_request(target)
	print("These are the identified 200 OK: " + Fore.GREEN + str(ok) + Style.RESET_ALL)
	print("These are the identified 401 Access Denied: " + Fore.GREEN + Fore.GREEN + str(access_denied) + Style.RESET_ALL)
	print("These are the identified 403 Forbidden: " + Fore.GREEN + str(forbidden) + Style.RESET_ALL)
	


def url_request(url):
	
	target = "https://" + url
	print(target)
	request = urllib2.Request(target)
	request.get_method = lambda : 'GET'
	try:
		response = urllib2.urlopen(request)
		response = urllib2.urlopen(request)
		print(response)

		response.info().headers
		header = urllib2.urlopen(target)
#		print(response.info())
		print(response.geturl() + " - URL")
		print(Fore.GREEN + str(response.getcode()) + Style.RESET_ALL + " - HTTP response code")
		if response.getcode() == 200:
			ok.append(url)
		return
		pass

	except Exception as e:
		error = str(e)
		print(Fore.RED + error + Style.RESET_ALL)
		if error == "HTTP Error 403: Forbidden":
#			print("Forbidden try something else")
			forbidden.append(url)
			print (forbidden)

		if error == "HTTP Error 401: Unauthorized":
			print("Unauthorized NTLM")
			access_denied.append(url)
			print (access_denied)


		else:
#			print("Invalid URL")
			invalid_url.append(url)
	

def main():

	parser = argparse.ArgumentParser(description="Lync test for NTLM")
	parser.add_argument("-d", "--domainname", help="the domain name to check")
	parser.add_argument("-u", "--url", help="the url to check")
	args = parser.parse_args()

	domainname = args.domainname
	url = args.url
	lync(domainname)
	#url_request(url)


if __name__ == '__main__':
    main()

