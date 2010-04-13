#! /usr/bin/python

import urllib
import urllib2
import platform
import sys
import ConfigParser
import os
from optparse import OptionParser

def notify_user(user, sender):
    if (config.has_section(user)):
        username = config.get(user, 'username')
        password = config.get(user, 'password')
    else:
        print 'specified section (', user, ') not found in config file'
        exit(1)
    
    url = 'https://boxcar.io/notifications'
    values = {'notification[from_screen_name]' : sender, 'notification[message]' : " ".join(args)}
    
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    
    data = urllib.urlencode( values )
    try:
        response = urllib2.urlopen(url, data)
    except IOError, e:
        if (hasattr(e, 'reason')):
            print 'Error submitting http request: ', e.reason, '\n'
        if (hasattr(e, 'code')):
            print 'Error submitting http request: ',e.code, '\n'
    except Exception, e:
        print 'Unhandled error caught', e.str()


config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.pushrc')])
    
optionParser = OptionParser(usage="%prog [options] <message>", version="%prog 1.0")
optionParser.add_option("-u", "--user", dest="users", action="append", help="A user section of the config file to use. Multiple users may be specified and the notification will be sent to all of them")
optionParser.add_option("-s", "--sender", dest="sender", help="The string to use as the sender of the notification", default=platform.node())
(options, args) = optionParser.parse_args()

if (options.users == None):
    notify_user("user", options.sender)
else:
    for user in options.users:
        notify_user(user, options.sender)
