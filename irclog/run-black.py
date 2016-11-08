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
	
	def _no_ping(self):
		if self.last_ping >= 1200:
			raise irclib.ServerNotConnectedError
		else:
			self.last_ping += 10
		self.ircobj.delayed_commands.append( (time.time()+10, self._no_ping, [] ) )

    #creating title function
    	def strip_non_ascii(self,string):
		''' Returns the string without non ASCII characters'''
		stripped = (c for c in string if 0 < ord(c) < 127)
		return ''.join(stripped)

	def colourstrip(self,data):
		find = data.find('\x03')
		while find > -1:
		    done = False
		    data = data[0:find] + data[find+1:]
		    if len(data) <= find+1:
		        done = True
		    try:
		        assert int(data[find])
		        data = data[0:find] + data[find+1:]
		    except:
		        done = True
		    try:
		        assert not done
		        assert int(data[find])
		        data = data[0:find] + data[find+1:]
		    except:
		        if not done and (data[find] != ','):
		            done = True
		    if (len(data) > find+1) and (data[find] == ','):
		        try:
		            assert not done
		            assert int(data[find+1])
		            data = data[0:find] + data[find+1:]
		            data = data[0:find] + data[find+1:]
		        except:
		            done = True
		        try:
		            assert not done
		            assert int(data[find])
		            data = data[0:find] + data[find+1:]
		        except: pass

		    find = data.find('\x03')
		data = data.replace('\x02','')
		data = data.replace('\x1d','')
		data = data.replace('\x1f','')
		data = data.replace('\x16','')
		data = data.replace('\x0f','')
		return data

	def letterGrade(self,num):
		if(num == '4'):
			file = open('visa.txt', 'r')
			foo = file.readlines()
			mm = random.choice(foo)
			file.close()
		elif (num == 'W'):
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
			text = self.colourstrip(text)
			exp = "APPROVED"
			if re.search(exp, text):
				cc = text
				match=re.search(r'(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})(.*?)',cc)
				try:
					ccnum = match.group(0)
					num = ccnum[0]
					title = self.letterGrade(num)
					text = self.strip_non_ascii(text)
					text = text.strip()
					try:
						if (source=='Tr0ll'):
							text = text.split(' ',1)[1]
							print "Done From core ==>" + title + "<" + source + "> " + text
							with open('cc.txt', 'a') as file:
								file.write(text + '\n')
								file.close
					except IndexError:
						print "Cant Split ==>" + title + "<" + source + "> " + text
						with open('black.txt', 'a') as file:
							file.write(text + '\n')
							file.close
				except AttributeError:
					print "re-search-Error" + "<" + source + "> " + text

			else:
				print "Cant EnteR ANY CONDITION ==== >" + " ("+ e.eventtype() +") [#" + channel + "] <" + source + "> " + text
			#text = text.split(",", 1)[1]
			#first = text[0]
			#title = self.letterGrade(text[0])
			#if 1st word == 5 
			    #foo = ['high valid live master card', 'master card high valid', 'live master enjoy!!', 'master card live', 'live master kill it']
			#else:
			    #foo = ['high valid live visa card', 'visa card high valid', 'live visa enjoy!!', 'visa card live', 'live visa kill it']
			#foo = ['high valid live master card', 'visa card high valid', 'live visa enjoy!!', 'master card live', 'live visa kill it']
			# file = open('myFile.txt', 'r')
			# foo = file.readlines()
			# file.close()
			#title = random.choice(foo)
			#print "("+ e.eventtype() +") [#" + channel + "] <" + source + "> " + text
				# mydata=[('post_text', text),('forum_id','2'),('title','title from python..mm')] 
				# mydata=urllib.urlencode(mydata)
				# path='http://localhost/forum/testpost.php'
				# req=urllib2.Request(path, mydata)
				# req.add_header("Content-type", "application/x-www-form-urlencoded")
				# page=urllib2.urlopen(req).read()
				# print page
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
		if irclib.is_channel(self.target):
			connection.join(self.target)

	def on_disconnect(self, connection, event):
		try:
			self.on_ping(connection, event)
			connection.disconnect()
			raise irclib.ServerNotConnectedError
		except AttributeError:
			print "some error on ping"


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
				irc_settings["server3"],
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
	server = 'irc.blackirc.net'
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
            
