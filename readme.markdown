# push.py
## What is it?

push.py is a quick and (reasonably) dirty python script I knocked together to send [boxcar][1] push notifications to my iPhone. It keeps login details in a config file in your home directory so they don't have to be in the world-readable script, and allows sending the same notification to multiple boxcar accounts in one command. Note that it doesn't send push notifications that other people can subscribe to; it just sends them to known accounts, for which you have the boxcar login details.

## Getting it
1. Make sure you have boxcar active on your phone, and the growl service enabled on your account (growl is currently the only service which allows api access.) You don't actually need to have growl installed on your machine; it doesn't even need to be a Mac. You just need to have the boxcar growl service active, because this script looks like the growl plugin to boxcar's servers.
1. Grab the script from github
1. Put it somewhere in your path
1. create .pushrc in your home directory and put something like this in it:

        [user]
        username=<boxcar-email-address>
        password=<boxcar-account-password>

1. You're done!

## Using it

Sending yourself a notification is as simple as:

    push.py this is a message

By default, the sender name will be the hostname of the machine you're running on, although that can be overridden on the command line (with the `-s` option.)

If you want to support more than one boxcar account, just add more sections to the config file, and then specify them on the command line with the `-u` option. For example, your .pushrc file might look like this:

    [user]
    username=foo@bar.com
    password=xxx

    [support]
    username=support@bar.com
    password=yyy

In which case, you could send notifications to both accounts with:

    push.py -u user -u support Hi guys

Just bear in mind that if you don't specify a user using `-u` then 'user' is the default, so it's a good idea to make sure you always have that one in your config.

If it's more convenient, you can specify the message to push on stdin, rather than the command line, using the `-r` option:

    echo hello | push.py

## Disclaimer

I knocked this script together in my lunch hour, so it's probably pretty buggy and you use it at your own risk. If it ends up burning your house down or shooting your dog, that's not my responsibility. If you notice anything glaring then let me know, or feel free to fork it on github and improve it. If you *do* improve it, please let me know, so I can use your better version.

[1]: http://boxcar.io
