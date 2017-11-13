#!/usr/bin/python3
#Author: Nahid Sarker
#Date modified: 4/19/2017
#Purpose: Display visible texts in html link given
#Created with python 3.6 and tested on Ubuntu 16.04
import requests
import random
import sys
import html2text
#need to install requests, html2text, and termcolor

title = """/
 __      ___     _ _     _       __          __  _       _____                 
 \ \    / (_)   (_) |   | |      \ \        / / | |     |  __ \                
  \ \  / / _ ___ _| |__ | | ___   \ \  /\  / /__| |__   | |__) |_ _  __ _  ___ 
   \ \/ / | / __| | '_ \| |/ _ \   \ \/  \/ / _ \ '_ \  |  ___/ _` |/ _` |/ _ \
    \  /  | \__ \ | |_) | |  __/    \  /\  /  __/ |_) | | |  | (_| | (_| |  __/
     \/   |_|___/_|_.__/|_|\___|     \/  \/ \___|_.__/  |_|   \__,_|\__, |\___|
                                                                     __/ |     
                                                                    |___/      
"""
if (len(sys.argv) != 2):
	print (title)
	
	print ("NAME")
	print ("\tvisibleWebText.py - displays the visible portion of a webpage (no code)\n")

	print ("SONOPSIS")
	print ("\tpython3 visibleWebText.py [address]\n")
	
	print ("DESCRIPTION")
	print ("\tvisibleWebText.py - displays the visible portion of a webpage and even keeps the structuring of where or how the text was. (Note: This is known to take in links attached to images or somethings like that)\n")
	
	print ("USEAGE:")
	print ("\tvisibleWebTest.py http(s)://<address>\n")	
		
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

if(__name__ == "__main__"):
    # load user agents and set headers
    uas = LoadUserAgents()
    ua = random.choice(uas)  # select a random user agent
    headers = {
        "Connection" : "close",  # another way to cover tracks
        "User-Agent" : ua}

    #webpage in the format of http(s)://<address>
    url = sys.argv[1] 
    #returns the page and randomizes the request
    r = requests.get(url, headers=headers)
    html = r.text

    page = html2text.html2text(html)
    output = open ("visibleHTML.txt", "w+")
    output.write(page)
    output.close()
