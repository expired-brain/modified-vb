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
import socket
import urllib2, urllib
import random
import config


# Configuration

class Logger(irclib.SimpleIRCClient):
	
	def __init__(self, server, port, channel, nick, password, username, ircname, localaddress, localport, ssl, ipv6):

	
		irclib.SimpleIRCClient.__init__(self)
		
		#IRC details
		self.server = server
		self.port = port
		self.target = channel
		self.channel = channel
		self.nick = nick
		self.password = password
		self.username = username
		self.ircname = ircname
		self.localaddress = localaddress
		self.localport = localport
		self.ssl = ssl
		self.ipv6 = ipv6
		
		#Regexes
		self.nick_reg = re.compile("^" + nick + "[:,](?iu)")
		
		#Message Cache
		self.message_cache = []		#messages are stored here before getting pushed to the db
		
		#Disconnect Countdown
		self.disconnect_countdown = 5
	
		self.last_ping = 0
		self.ircobj.delayed_commands.append( (time.time()+5, self._no_ping, [] ) )
		self.connect(self.server, self.port, self.nick, self.password, self.username, self.ircname, self.localaddress, self.localport, self.ssl, self.ipv6)
		#print self.nickname
		
	
	def _no_ping(self):
		if self.last_ping >= 1200:
			raise irclib.ServerNotConnectedError
		else:
			self.last_ping += 10
		self.ircobj.delayed_commands.append( (time.time()+10, self._no_ping, [] ) )

	def strip_non_ascii(self,string):
		''' Returns the string without non ASCII characters'''
		stripped = (c for c in string if 0 < ord(c) < 127)
		return ''.join(stripped)

    #creating title function
	def letterGrade(self,num):
		if(num == '4'):
			file = open('visa.txt', 'r')
			foo = file.readlines()
			mm = random.choice(foo)
			file.close()
		elif (num == '5'):
			file = open('mc.txt', 'r')
			foo = file.readlines()
			mm = random.choice(foo)
			file.close()
		else:
			foo = ['Amex live!!', 'kill it amex', 'hard live card,enjoy', 'Approved high valid amex', 'CC high valid']
			mm = random.choice(foo)
		return mm

	def _dispatcher(self, c, e):
	# This determines how a new event is handled. 
		if(e.eventtype() == "topic" or 
		   e.eventtype() == "part" or
		   e.eventtype() == "join" or
		   e.eventtype() == "action" or
		   e.eventtype() == "quit" or
		   e.eventtype() == "nick" or
		   e.eventtype() == "error" or
		   e.eventtype() == "notregistered" or
		   e.eventtype() == "nochanmodes" or
		   e.eventtype() == "pubnotice" or
		   e.eventtype() == "mode" or
		   e.eventtype() == "pubmsg"):
			try: 
				source = e.source().split("!")[0]

				# Try to parse the channel name
				try:
					channel = e.target()[1:]
				except TypeError:
					channel = "undefined"

			except IndexError:
				source = ""
			try:
				text = e.arguments()[0]
			except IndexError:
				text = ""

			# Print message to stdout
			exp = "\:(.*?)\!!"
			if re.search(exp, text):
				cc = text
				match=re.search(r'(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})(.*?)',cc)
				try:
					ccnum = match.group(0)
					num = ccnum[0]
					title = self.letterGrade (num)
					text = self.strip_non_ascii(text)
					try:
						text = text.split("03",1)[1]
						print "Done From core ==>" + title + "<" + source + "> " + text
					except IndexError:
						print "Cant Split ==>" + title + "<" + source + "> " + text
					with open('crime.txt', 'a') as file:
						file.write(text + '\n')
						file.close
				except AttributeError:
					print "re-search-Error" + "<" + source + "> " + text

			else:
				print "Cant EnteR ANY CONDITION ==== >" + " ("+ e.eventtype() +") [#" + channel + "] <" + source + "> " + text
			if (e.eventtype() == "nochanmodes"):
				self.on_welcome(c,e)

			# Prepare a message for the buffer
			message_dict = {"channel":channel,
							"name": source,
							"message": text,
							"type": e.eventtype(),
							"time": str(datetime.datetime.utcnow()) } 
							
			if e.eventtype() == "nick":
				message_dict["message"] = e.target()
			
			# Most of the events are pushed to the buffer. 
			self.message_cache.append( message_dict )
		
		m = "on_" + e.eventtype()	
		if hasattr(self, m):
			getattr(self, m)(c, e)

	def on_nicknameinuse(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_welcome(self, connection, event):
		connection.join('#unix')

	def on_disconnect(self, connection, event):
		self.on_ping(connection, event)
		connection.disconnect()
		raise irclib.ServerNotConnectedError
			

	def on_pubmsg(self, connection, event):
		text = event.arguments()[0]

		# If you talk to the bot, this is how he responds.
		if self.nick_reg.search(text):
			if text.split(" ")[1] and text.split(" ")[1] == "quit":
				connection.privmsg(self.channel, "Goodbye.")
				self.on_ping( connection, event )
				sys.exit( 0 ) 
				
			if text.split(" ")[1] and text.split(" ")[1] == "ping":
				self.on_ping(connection, event)
				return

def main():
	irc_settings = config.config("irc_config.txt")
	c = Logger(
				irc_settings["server"], 
				int(irc_settings["port"]), 
				irc_settings["channel"],
				irc_settings["nick"],
				irc_settings["password"],
				irc_settings.get("username",None),
				irc_settings.get("ircname",None),
				irc_settings.get("localaddress",""),
				int(irc_settings.get("localport",0)),
				bool(irc_settings.get("ssl",False)),
				bool(irc_settings.get("ipv6",False))) 
	c.start()
	
if __name__ == "__main__":
	irc_settings = config.config("irc_config.txt")
	reconnect_interval = irc_settings["reconnect"]
	while True:
		try:
			main()
		except irclib.ServerNotConnectedError:
			print "Server Not Connected! Let's try again!"             
        	time.sleep(float(reconnect_interval))
            
