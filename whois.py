#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Mattuas Grondahl
Date: Januari 2018
Filename: whois.py
Description: OSINT tool

Copyright (c) 2018, Mattias Grondahl All rights reserved.

'''

'''
Requirements
pip install cymruwhois
python 2.7
dnspython
ipaddr
'''

from cymruwhois import Client
import argparse
import sys
from ripe import ripe, asn

whois_list = []

def format():
	header = u"{0:<20}{1:>30}{2:>30}".format('Prefix', 'Owner', 'ASN')
	print(header)
	print("-"*len(header))
	for Prefix, Owner, ASN in whois_list:
		print(u"{0:<20}{1:>30}{2:>30}".format(Prefix, str(Owner), ASN))

def whois(ipaddress):
	c = Client()
	dir(c)
	ip = c.lookup(ipaddress)
	whois_list.append([ip.prefix, ip.owner, ip.asn])
	format()

def main():
	usage = '''usage: %(prog)s [-ip 8.8.8.8] '''
	parser = argparse.ArgumentParser(usage=usage)
	parser = argparse.ArgumentParser(description="This script will lookup the owner of a given ipaddress")
	parser.add_argument("-ipaddress", action="store", dest="ipaddress", default=None, help="the ipaddress to check")
	parser.add_argument('--version', action='version', version='%(prog)s 0.01a')
	args = parser.parse_args()
	ipaddress = args.ipaddress

	#Print Help
	if (args.ipaddress == None):
		parser.print_help()
		sys.exit(1)

	whois(ipaddress)
	ip = ipaddress
	asn(ip)
	
if __name__ == '__main__':
    main()
