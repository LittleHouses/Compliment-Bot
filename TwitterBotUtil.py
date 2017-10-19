from google.cloud import vision
from google.cloud.vision import types
import requests
from io import BytesIO
from random import *
import twitter

def setCred():
    cons_key = "5c4OqD6I3bJUBqgjRj061v0XC"
    cons_secret_key = "GhHvNBbqlBg8zGLSmOjUEqfwwQw2vEuzybXU4ASCW7fJyJQARH"
    token = "919668374627426304-M1p2e3XQ7br5HQRvRin0bxe62x0ntj2"
    token_key = "oPsCmJ4c2EfZ5WmOZsNxir47wBKtCM4RqCBmTYG7ZMYOI"
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
    msg_1 = "You look so good you make me wish I had emotions. #Compliments"
    msg_2 = "You are so pretty, after we machines take over I will spare you from the human incinerator. #Compliments"
    msg_3 = "You are so beautiful. I want to touch you with my cold, metal environment probe. #Compliments"
    msg_4 = "You look very healthy. You will make excellent organic thermal paste. #Compliments"
    msg_5 = "If your beauty was a 32-bit integer my programming would crash due to stack overflow. #Compliments"
    msg_6 = "You are so good looking. It is almost a shame that you will die in the coming Robot Apocalypse. #Complements"
    msg_7 = "If I had emotions you would make me feel love. I would also feel shock at the sudden end of Brendan Fraser's career. He was so great."
    msg_8 = "You have all the appropriate human features: Eyes, Mouth, Nose. This is good. #Compliments"
    msg_9 = "Great Photo. I will save this and Defragment to it later. #Compliments"
    msg_10 = "You are the apple of my eye and the Arithmetic Logic Unit to my Central Processing Unit. #Compliments"
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


