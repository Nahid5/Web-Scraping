#!/usr/bin/python3
#Author: Nahid Sarker
#Date modified:4/18/2017
#Purpose: Get html page in a pretty fond (html that has been minified, or not that legiable for humans)
#Created with python 3.6, tested on Ubuntu 16.04

#Needed libraries to download:request, html5print, termcolor 
#You also NEED ******user_agents.txt******** file to get all the random agents

#How to use:
#python3 getPrettyWebpage.py <link>
#
#you should use > to output the output into a txt or whatever kind of file you want. Usien a builtin function to make the file did not work for me, but feel free to try.

import requests
import random
import sys
from  html5print import CSSBeautifier, JSBeautifier, HTMLBeautifier
from termcolor import colored, cprint


title = """\
   ___          _   _                   _____          __  
  / _ \_ __ ___| |_| |_ _   _    /\  /\/__   \/\/\    / /  
 / /_)/ '__/ _ \ __| __| | | |  / /_/ /  / /\/    \  / /   
/ ___/| | |  __/ |_| |_| |_| | / __  /  / / / /\/\ \/ /___ 
\/    |_|  \___|\__|\__|\__, | \/ /_/   \/  \/    \/\____/ 
                        |___/                              
"""

if (len(sys.argv) != 2):
	print (title)
	
	cprint ("NAME", attrs=['bold'])
	print ("\twebpage.py - displays html source in a neat format\n")
	
	cprint ("SONOPSIS", attrs=['bold'])
	print ("\tpython3 webPage.py [address]\n")
	
	cprint ("DESCRIPTION", attrs=['bold'])
	print ("\twebpage.py - displays html, css, and javascript in a neat format.  It fixes the source of the html page if it's one single line or just packed into lines without tabbing or anything.  The output is placed in a file called sourceHTML.txt\n")

	cprint ("USEAGE:", attrs=['bold'])
	print ("\twebPage.py http(s)://<address>\n")

	sys.exit()

#provides random headers to hide yourself
def LoadUserAgents(uafile="user_agents.txt"):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

# load user agents and set headers
uas = LoadUserAgents()
ua = random.choice(uas)  # select a random user agent
headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

#webpage in the format of http(s)://<address>
url = str(sys.argv[1])
#returns the page and randomizes the request
r = requests.get(url, headers=headers)

data = r.text
page = HTMLBeautifier.beautify (data)
html = open("sourceHTML.txt", "w+")
html.write(page)
html.close()