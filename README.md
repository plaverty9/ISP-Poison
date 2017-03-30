# ISP-Poison
ISPs want to collect data on the sites you visit. So poison their tracking with random web requests.

Supply your own wordlist, one word per line. 

Words need to only have characters that are acceptable for web site domains. 

Script chooses a random line from the wordlist, appends a random valid TLD, makes a request for that site. 
Sleeps a random amount of time between 2 seconds and 5 minutes. 
Lather, rinse, repeat. 
