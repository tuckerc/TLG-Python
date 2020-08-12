#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
# open the file for reading
with open("/home/student/TLG-Python/logs/keystone.common.wsgi","r") as keystone_file:
    # loop over the list of lines
    for line in keystone_file:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
print("The number of failed log in attempts is", loginfail)

