
# identify_logins
Identify possible login paths

Discover.py is an OSINT tool that helps you identify valid dns namnes and if there are any possible logins.



This tool is run with:
discover.py -d domain.com

1. It will do a quick limited bruteforce for valid dnsnames
2. It will lookup the owner of the ipaddresses associated with the domain.
3. It will do limited path bruteforce each valid hostname
4. It will output hostnames and paths where a possible login bruteforce can be done.

Installation:
git clone https://github.com/Mattiasgrondahl/identify_logins.git
cd identify_logins
pip install -r requirements.txt

Example:

sudo python discover.py -d yourdomainname.com

