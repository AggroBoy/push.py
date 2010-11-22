#! /usr/bin/env python

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import platform
import sys
import configparser
import os
from optparse import OptionParser
from time import time

def notify(username, password, sender, message):
    url = 'https://boxcar.io/notifications'
    values = {
            'notification[from_screen_name]' : sender,
            'notification[message]' : message,
            'notification[from_remote_service_id]' : int(time()*100)
            }
    
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)
    
    data = urllib.parse.urlencode( values )
    try:
        response = urllib.request.urlopen(url, data)
    except IOError as e:
        if (hasattr(e, 'reason')):
            print('Error submitting http request: ', e.reason, '\n')
            return 1
        if (hasattr(e, 'code')):
            print('Error submitting http request: ',e.code, '\n')
            return 1
    except Exception as e:
        print('Unhandled error caught', e.str())
        return 1
    return 0

def notify_user(user, sender, message):
    if (config.has_section(user)):
        username = config.get(user, 'username')
        password = config.get(user, 'password')
    else:
        print('specified section (', user, ') not found in config file')
        return 1
	
    return notify(username, password, sender, message)


config = configparser.ConfigParser()
config.read([os.path.expanduser('~/.pushrc')])
    
optionParser = OptionParser(usage="%prog [options] [<message>]", version="%prog 1.0")
optionParser.add_option("-u", "--user", dest="users", action="append", help="A user section of the config file to use. Multiple users may be specified and the notification will be sent to all of them")
optionParser.add_option("-s", "--sender", dest="sender", help="The string to use as the sender of the notification", default=platform.node())
optionParser.add_option("-r", "--read-stdin", "--stdin", action="store_true", dest="stdin", default=False, help="Read the message to send from the standard input, rather than from the command line.")
(options, args) = optionParser.parse_args()

if (options.stdin):
    message = sys.stdin.read()
else:
    message = " ".join(args)

status = 0
if (options.users is None):
    status = notify_user("user", options.sender, message)
else:
    for user in options.users:
        if (notify_user(user, options.sender, message) == 1):
            status = 1

sys.exit(status)
