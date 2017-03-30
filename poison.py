import urllib
import urllib2
import random
import time
import linecache

# Use your own wordlist here
wordlist =""

i=0
#Count the number of lines in the wordlist
f = open(wordlist,'r')
for line in f:
        i+=1

#Choose a random line to read
linenum = random.randint(1,i)
line = linecache.getline(wordlist, linenum)

tld = ['.com','.net','.org','.name','.us','.biz','.edu']

# never stop, keep poisoning
while True:
        line = line.rstrip()
        ext = random.choice(tld)
        site = line + ext
        print("Getting "+site)
        # Sleeps for a random time between 2 seconds and 5 minutes for the next request
        sleeptime = random.randint(2,300)
        print "Sleeping for "+str(sleeptime)+" seconds"
        time.sleep(sleeptime)
        try: response = urllib2.urlopen('http://'+site)
        except (urllib2.HTTPError, urllib2.URLError):
                continue
