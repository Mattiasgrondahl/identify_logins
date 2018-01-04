#!/usr/bin/env python

'''
Author: Mattuas Grondahl
Date: Januari 2018
Filename: ripe.py
Description: OSINT tool

Copyright (c) 2018, Mattias Grondahl All rights reserved.

'''

import sys
import argparse
import urllib2
import requests
import json
from colorama import Fore, Back, Style, init
init()



def ripe(ip):

    url_base='https://stat.ripe.net/data/address-space-usage/data.json?resource='
    url_base= url_base + str(ip)
    print(url_base)

    try:
        r = requests.get(url_base)
        r.json()
        print(r.json())
        pass
    except Exception as e:
        error = str(e)
        print(error)

    r = requests.get(url_base)
    r.json()
#    print(r.json())

def __init__(self,n,a):
     self.full_name = n
     self.age = a

def asn(ip):
    asn_list = []
    url_base='https://stat.ripe.net/data/address-space-usage/data.json?resource='
    url_base= url_base + str(ip)
    
    RIPE = urllib2.urlopen(url_base)
    RJSON = RIPE.read()
    RJDATA = json.loads(RJSON)
    asn_value = RJDATA['data']['assignments'][0]['asn_name']
    return asn_value
    
def main():

    usage = '''usage: %(prog)s [-d http://127.0.0.1] '''
    parser = argparse.ArgumentParser(usage=usage)
    parser = argparse.ArgumentParser(description="This script will lookup domainnames for a given ipaddress")
    parser.add_argument("-ip", action="store", dest="ip", default=None, help="Ipaddress to lookup")
    parser.add_argument('--version', action='version', version='%(prog)s 0.01a')
    args = parser.parse_args()
    ip = args.ip
    
    #Print Help
    if (args.ip == None):
        parser.print_help()
        sys.exit(1)
    asn(ip)

if __name__ == '__main__':
    main()



