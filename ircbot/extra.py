#! /usr/bin/env python
#

#libs
from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr
import irclib
import sys
import re
import time
import datetime
import urllib2, urllib
import random
import config

def main():
	text = "THIS IS TEST"
	title = "this is title"
	mydata=[('post_text', text),('forum_id','2'),('title',title)]
	mydata=urllib.urlencode(mydata)
	path='http://localhost/forum/testpost.php'
	try:
		req=urllib2.Request(path, mydata)
		req.add_header("Content-type", "application/x-www-form-urlencoded")
		page=urllib2.urlopen(req).read()
		print "post success, check forum"
	except urllib2.HTTPError:
		print "Cant post the DATA to forum: Check host server"
	#req=urllib2.Request(path, mydata)

if __name__ == "__main__":
	irc_settings = config.config("irc_config.txt")
	reconnect_interval = irc_settings["reconnect"]
	while True:
		try:
			main()
		except irclib.ServerNotConnectedError:
			print "Server Not Connected! Let's try again!"             
        	time.sleep(float(reconnect_interval))
            
