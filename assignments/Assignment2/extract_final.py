f = open("/Users/Heather/Documents/School/432/A2/curl.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "location:" in line: 
        for l in searchlines[i:i+1]: print (l),
        print