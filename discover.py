#!/usr/bin/env python

'''
Author: Mattuas Grondahl
Date: Januari 2018
Filename: discover.py
Description: OSINT tool

Copyright (c) 2018, Mattias Grondahl All rights reserved.

'''

#import sys
import argparse
import urllib2
import sys
from colorama import Fore, Back, Style, init
import dns
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

def format():
	header = u"{0:<30}{1:>18}{2:>20}{3:>40}{4:>30}".format('HTTP', 'Hostname')
	print(header)
	print("-"*len(header))
	for HTTP, Hostname in whois_list:
		print(u"{0:<30}{1:>18}{2:>20}{3:>40}{4:>30}".format(Hostname, str(IpAddress), str(Prefix), str(Owner), str(ASN)))

def status():
	print(Back.CYAN + "\nStatus :" + Style.RESET_ALL)
	print(Fore.MAGENTA + "---------------------------------------------------------------" + Style.RESET_ALL)
	status = []
	for item in ok:
		print("200 OK: " + Fore.GREEN + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in access_denied:
		print("401 Access Denied: " + Fore.GREEN + Fore.GREEN + str(item) + Style.RESET_ALL + Fore.RED + " 		Possible login found!" + Style.RESET_ALL)
		#status.append([401, item])
	for item in forbidden:
		print("403 Forbidden: " + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in not_found:
		#print("404 Not Found: " + Fore.GREEN + str(item) + Style.RESET_ALL)
	for item in internal_server_error:
		print("500 Internal Server Error: " + Fore.GREEN + str(item) + Style.RESET_ALL)

def lync(domainname):
	#ripe.asn(ip)
	filename = "discover.txt"
	paths = "paths.txt"
	print ("Starting discovery for domain: " + Fore.RED + domainname + Style.RESET_ALL)
	print ("\nThis will check the hostnames in: " + Fore.GREEN + filename + Style.RESET_ALL + "\n")
	print ("It will then use the paths from : " + Fore.GREEN + paths + Style.RESET_ALL + "\n")
# 	with open(filename) as f:
# 		lyncdiscover = f.readlines()
# 		for line in lyncdiscover:
# 			line = line.strip()
# 			target = str(line) + ('.') + str(domainname)
# #			print("\n" + target)
# 			url_request(target)
	
# 	status()

	filename = "paths.txt"
	with open(filename) as f:
		paths = f.readlines()
		for line in paths:
			line = line.strip()
			target = str(domainname) + '/' + str(line)
			print(target)
			url_request(target)
	status()

		

def url_request(url):
	
	target = "https://" + url
	request = urllib2.Request(target)
	request.get_method = lambda : 'GET'
	try:
		response = urllib2.urlopen(request)
		response.info().headers
		header = urllib2.urlopen(target)
		print (Fore.GREEN + str(response.getcode()) + " - " + Fore.BLUE + str(response.geturl()))
		if response.getcode() == 200:
			ok.append(url)
		return
		pass

	except Exception as e:
		error = str(e)

		if error != "None":
			print (Fore.YELLOW + error + " - " + Fore.BLUE + target)

		if error == "HTTP Error 403: Forbidden":
			forbidden.append(url)
			valid_url.append(url)

		if error == "HTTP Error 401: Unauthorized":
			access_denied.append(url)
			valid_url.append(url)

		if error == "HTTP Error 500: Internal Server Error":
			internal_server_error.append(url)
			valid_url.append(url)

		if error == "<urlopen error [Errno 11001] getaddrinfo failed":
			invalid_url.append(url)

		if error == "HTTP Error 404: Not Found":
			not_found.append(url)
			valid_url.append(url)

		else:
			invalid_url.append(url)
	

def main():

	parser = argparse.ArgumentParser(description="Discovery tool")
	parser.add_argument("-d", "--domainname", help="the domainname to check")
	parser.add_argument("-u", "--url", help="the url to check")
	args = parser.parse_args()
	domainname = args.domainname
	url = args.url
	

		#Print Help
	if (args.domainname == None):
		parser.print_help()
		sys.exit(1)

	#dns.dns(domainname)	
	valid_targets = dns.dns(domainname)
	for i in valid_targets:
		lync(i)
	#print(valid_targets)
	#lync(domainname)

if __name__ == '__main__':
    main()

