from google.cloud import vision
from google.cloud.vision import types
import requests
from io import BytesIO
from random import *
import twitter

def setCred():
    cons_key = ""
    cons_secret_key = ""
    token = ""
    token_key = ""
    return twitter.Api(cons_key, cons_secret_key, token, token_key)

def returnLabels(url):
    #Initiate Google Vision API client.
    client = vision.ImageAnnotatorClient()
    #Get image byte stream from URL.
    response = requests.get(url)
    content = BytesIO(response.content).read()
    #Create image type
    image = types.Image(content=content)
    #Perform Goggle Vision's label detection.
    response = client.label_detection(image=image)
    labels = response.label_annotations
    #return list of labels
    return labels

def getComp(labels):
    msg_1 = ""
    msg_2 = ""
    msg_3 = ""
    msg_4 = ""
    msg_5 = ""
    msg_6 = ""
    msg_7 = ""
    msg_8 = ""
    msg_9 = ""
    msg_10 = ""
    comps = [msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10]
    if('girl' in labels or 'facial hair' in labels or 'selfie' in labels or 'man' in labels or 'beauty' in labels ):
        x = randint(0, len(comps) - 1)
        return comps[x]
    else: return 'none'

#class for handling previous tweet list
class tweetStorage():

    previous_tweets = ''

    def __init__(self):
        previous_tweets_file = open('stored_tweets.txt', 'r')
        self.previous_tweets = previous_tweets_file.read()
        previous_tweets_file.close()


    def getTweets(self):
        return self.previous_tweets

    #Check is bot has already replied to given tweet
    def checkTweet(self, tweet):
        if(tweet in self.previous_tweets):
            return False
        else: return True

    #Add tweet to list of past tweets
    def addTweet(self, tweet):
        saved_tweet_list = open('stored_tweets.txt', 'a')
        saved_tweet_list.write("\n" + tweet)
        saved_tweet_list.close()
        self.previous_tweets += tweet


