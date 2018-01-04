#!/usr/bin/env python

'''
Author: Mattuas Grondahl
Date: Januari 2018
Filename: dns.py
Description: OSINT tool

Copyright (c) 2018, Mattias Grondahl All rights reserved.

'''

'''
Requirements
pip install colorama cymruwhois numpy ripe
'''
import sys
import socket
import argparse
from colorama import Fore, Back, Style, init
from cymruwhois import Client
import numpy as np
import ripe


init()

#Create list
valid_dns = []
whois_list = []

def format():
	header = u"{0:<30}{1:>18}{2:>20}{3:>40}{4:>30}".format('Hostname', 'IpAddress', 'Prefix', 'Owner', 'ASN')
	print(header)
	print("-"*len(header))
	for Hostname, IpAddress, Prefix, Owner, ASN in whois_list:
		print(u"{0:<30}{1:>18}{2:>20}{3:>40}{4:>30}".format(Hostname, str(IpAddress), str(Prefix), str(Owner), str(ASN)))

def whois(target, addr1, asn_value):
	c = Client()
	dir(c)
	ip = c.lookup(addr1)
	whois_list.append([target, addr1, ip.prefix, ip.owner, asn_value])

def dns(domainname):

	filename = "discover.txt"
	ip_list = []
	valid_targets = []		
	with open(filename) as f:
		discover = f.readlines()
		for line in discover:
			line = line.strip()
			target = str(line) + ('.') + str(domainname)
			try:
				addr1 = socket.gethostbyname(target)
				valid_dns.append([target, addr1])
				valid_targets.append(target)
				ip = addr1
				if str(ip) in ip_list:
					print(target + " - " + addr1)
				else:
					#ripe.asn(ip)
					asn_value = ripe.asn(ip)
					print(target + " - " + addr1 + " - " + asn_value)
					ip_list.append(ip)
				whois(target, addr1, asn_value)
				pass
			except Exception as e:
				error = str(e)
	format()
	#print(valid_targets)
	return valid_targets

def main():
	usage = '''usage: %(prog)s [-d http://127.0.0.1] '''
	parser = argparse.ArgumentParser(usage=usage)
	parser = argparse.ArgumentParser(description="This script will lookup domain names for a given domain")
	parser.add_argument("-d", action="store", dest="domainname", default=None, help="the domain name to check")
	parser.add_argument('--version', action='version', version='%(prog)s 0.01a')
	args = parser.parse_args()
	domainname = args.domainname

	#Print Help
	if (args.domainname == None):
		parser.print_help()
		sys.exit(1)

	dns(domainname)
	
if __name__ == '__main__':
    main()

