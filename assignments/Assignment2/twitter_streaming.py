import sys
sys.path.append("/python/lib/site-packages")

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "826452717447086080-CbB2AGFfEjkaWpGwT0nnMoR9eFt5KEH"
access_token_secret = "3arHhTJzUaNKG1mA2axLHir1lGr0uyTLKMsMZfaye9tPU"
consumer_key = "TJByr8RB7hBK56QZ72tdElwiU"
consumer_secret = "8cRgcjNVwvabOvlXQaoqtnhDnD1Xd13vmzBntZ9pw7gvFpIaJD"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])