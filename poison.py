import urllib2
import random
import time

# uncomment and add a wordlist
#wordlist =""

f = open(wordlist,'r')
tld = ['.com','.net','.org','.name','.us','.biz','.edu']
for line in f:
        line = line.rstrip()
        ext = random.choice(tld)
        site = line + ext
        print("Getting "+site)
        sleeptime = random.randint(2,300)
        time.sleep(sleeptime)
        try: response = urllib2.urlopen('http://'+site)
        except (urllib2.HTTPError, urllib2.URLError):
                continue
