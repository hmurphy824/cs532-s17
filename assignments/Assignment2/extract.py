import re
import sys

urls_data_path = '/Users/Heather/Documents/School/432/A2/urls.txt'

urls_file = open(urls_data_path, "r")
for line in urls_file:
    try:
        #print (re.findall(r"^(http\S+)", file))
        #print ("curl -IL --silent "+ line + " | egrep -i \"(HTTP/1.1|^location:)\"")
        print ("curl -IL --silent "+ line)
    
        except ValueError as err:
        #print(err)
        continue