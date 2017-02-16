import pprint
import json

tweets_data_path = '/Users/Heather/Documents/School/432/A2/2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    
    except ValueError as err:
        #print(err)
        continue

#for one_tweet in tweets_data:
#    pprint.pprint (one_tweet)
#    break
#for one_tweet in tweets_data:
    #print (one_tweet.id)
	#for one_urlblob in one_tweet.entities.urls:
			#print (one_urlblob.url)

for one_tweet in tweets_data:
	for one_urlblob in one_tweet["entities"]["urls"]:
		print (one_urlblob["url"])