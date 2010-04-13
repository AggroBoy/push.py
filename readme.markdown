# push.py
## What is it?

push.py is a quick and (reasonably) dirty python script I knocked together to send [boxcar][1] push notifications to my iPhone. It keeps login details in a config file in your home directory so they don't have to be in the world-readable script, and allows sending the same notification to multiple boxcar accounts in one command. Note that it doesn't send push notifications that other people can subscribe to; it just sends them to known accounts, for which you have the boxcar login details.

## Getting it
1. Make sure you have boxcar active on your phone, and the growl service enabled on your account (growl is currently the only service which allows api access.)
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

Just bear in mind that if you don't specify a user using `-u` then 'user' is the default, so it's a good idea to make sure you always have that on in your config.

[1]: http://boxcar.io
