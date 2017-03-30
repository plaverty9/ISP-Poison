import urllib2
import random
import time
import linecache

# Replace this with your own wordlist
wordlist =""

i=0
#Count the number of lines in the wordlist
f = open(wordlist,'r')
for line in f:
        i+=1

tld = ['.com','.net','.org','.name','.us','.biz','.edu']
while True:
        linenum = random.randint(1,i)
        line = linecache.getline(wordlist, linenum)
        line = line.rstrip()
        ext = random.choice(tld)
        site = line + ext
        print("Getting "+site)
        sleeptime = random.randint(2,300)
        print "Sleeping for "+str(sleeptime)+" seconds"
        time.sleep(sleeptime)
        try: response = urllib2.urlopen('http://'+site)
        except (urllib2.HTTPError, urllib2.URLError):
                continue
