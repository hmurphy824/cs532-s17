import re
import fileinput
for line in fileinput.input(r'/Users/Heather/Documents/School/432/A2/almost.txt', inplace = True):
   if not re.search(r'\btinyurl\b',line):
      print (line),