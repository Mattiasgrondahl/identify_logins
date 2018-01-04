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

#import sys
import argparse
import urllib2
from colorama import Fore, Back, Style, init
init()


#creating lists
forbidden = []
ok = []
access_denied = []
internal_server_error = []
not_found = []
invalid_url = [];
all_lists = [ok, access_denied, forbidden, not_found, internal_server_error]
valid_url = [];

def status():
	print(Back.CYAN + "\nStatus :" + Style.RESET_ALL)
	print(Fore.MAGENTA + "---------------------------------------------------------------" + Style.RESET_ALL)
	for item in ok:
		print("200 OK: " + Fore.GREEN + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in access_denied:
		print("401 Access Denied: " + Fore.GREEN + Fore.GREEN + str(item) + Style.RESET_ALL + Fore.RED + " 		Possible login found!" + Style.RESET_ALL)
	for item in forbidden:
		print("403 Forbidden: " + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in not_found:
		print("404 Not Found: " + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in internal_server_error:
		print("500 Internal Server Error: " + Fore.GREEN + str(item) + Style.RESET_ALL)

def lync(domainname):
	filename = "discover.txt"
	paths = "paths.txt"
	print ("Checking lync avalability for domain: " + Fore.RED + domainname + Style.RESET_ALL)
	print ("\nThis will check the hostnames in: " + Fore.GREEN + filename + Style.RESET_ALL + "\n")
	print ("It will then use the paths from : " + Fore.GREEN + paths + Style.RESET_ALL + "\n")
	with open(filename) as f:
		lyncdiscover = f.readlines()
		for line in lyncdiscover:
			line = line.strip()
			target = str(line) + ('.') + str(domainname)
#			print("\n" + target)
			url_request(target)
	
	status()
#after identifying valid urls
	filename = "paths.txt"
	with open(filename) as f:
		paths = f.readlines()
		for line in paths:
			line = line.strip()
			for valid in valid_url:
				target = str(valid) + '/' + str(line)
			print(target)
			url_request(target)
	status()
	

def url_request(url):
	
	target = "https://" + url
#	print(target)
	request = urllib2.Request(target)
	request.get_method = lambda : 'GET'
	try:
		response = urllib2.urlopen(request)
#		print(response)
		response.info().headers
		header = urllib2.urlopen(target)
#		print(response.info())
#		print(response.geturl() + " - URL")
#		print(Fore.GREEN + str(response.getcode()) + Style.RESET_ALL + " - HTTP response code")
		print (Fore.GREEN + str(response.getcode()) + " - " + Fore.BLUE + str(response.geturl()))
		if response.getcode() == 200:
			ok.append(url)
		return
		pass

	except Exception as e:
		error = str(e)
#		print(Fore.RED + error + Style.RESET_ALL)

		if error != "None":
			print (Fore.YELLOW + error + " - " + Fore.BLUE + target)

		if error == "HTTP Error 403: Forbidden":
#			print("Forbidden try something else")
			forbidden.append(url)
			valid_url.append(url)
#			print (error + " - " + target)

		if error == "HTTP Error 401: Unauthorized":
			access_denied.append(url)
			valid_url.append(url)
#			print (error + " - " + target)

		if error == "HTTP Error 500: Internal Server Error":
			internal_server_error.append(url)
			valid_url.append(url)
#			print (error + " - " + target)

		if error == "<urlopen error [Errno 11001] getaddrinfo failed":
			invalid_url.append(url)
#			print (error + " - " + target)

		if error == "HTTP Error 404: Not Found":
			not_found.append(url)
			valid_url.append(url)
#			print (error + " - " + target)

		else:
#			print("Invalid URL")
			invalid_url.append(url)
#			print (error + " - " + target)
	

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

