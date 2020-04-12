# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 02:36:24 2020

@author: sayantan
"""

import urllib # Python URL functions
import urllib.parse
import urllib.request # Python URL functions

authkey = "YOUR_AUTHKEY" # Your authentication key.

mobiles = "YOUR_NUMBER"
#open("SMSmobileNumber.txt", "r") # Multiple mobiles numbers separated by comma.

message = open("SMSfile1.txt", "r")
#message1 = open("SMSfile2.txt", "r")
#print (message1.readlines()); # Your message to send.

#print (mobiles.readlines());

sender = "NewUsr" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message.readlines(),
          #'message2' : message1.readlines(),
          'sender' : sender,
          'route' : route
          }

#values1 = {
 #         'authkey' : authkey,
  #        'mobiles' : mobiles,
   #       'message' : message1.readlines(),
    #      #'message2' : message1.readlines(),
     #     'sender' : sender,
      #    'route' : route
       #   }

url = "http://api.msg91.com/api/sendhttp.php" # API URL

postdata = urllib.parse.urlencode(values).encode("utf-8") # URL encoding the data here.
#postdata2 = urllib.parse.urlencode(values1).encode("utf-8")
req = urllib.request.Request(url, postdata)
#req2 = urllib.request.Request(url, postdata)
response = urllib.request.urlopen(req)
#response2 = urllib.request.urlopen(req)
output = response.read() # Get Response
#output2 = response.read()
print (output);
#print (output2) ; # Print Response
