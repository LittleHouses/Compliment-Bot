import twitter
import time
from random import *
from TwitterBotUtil import returnLabels
from TwitterBotUtil import getComp
from TwitterBotUtil import tweetStorage
from TwitterBotUtil import setCred

#Initiate python wrapper for Twitter API
api = setCred()

#Aquire previous tweet list
storage = tweetStorage()

tweet_key = [#list of search terms]
tweet_count = 0
no_limit = True


while(no_limit):

    # Search a random term and acquire tweet list
    term = randint(0, len(tweet_key) - 1)
    search_term = tweet_key[term]
    search = api.GetSearch(search_term, include_entities=True, count=100, result_type="recent")

    tweeted = False

    #Search tweets acquired
    for status in search:
    #Check if retweet and if the bot has already responded to this tweet
        if(status.text[0:2] != 'RT' and storage.checkTweet(status.id_str)):
            descriptions = []
            #Check if tweet has media attached and that media is a photo
            if (status.media != None):
                if(status.media[0].type == 'photo'):
                    print(status.text)
                    #Send pic to google vision and acquire labels
                    labels = returnLabels(status.media[0].media_url)
                    #Creat list of descriptions from labels
                    for label in labels:
                        descriptions.append(label.description)
                    #Get compliment
                    compliment = getComp(descriptions)
                    print(compliment)
                    #send compliment and update counter and previous tweet list
                    if (compliment != 'none'):
                        api.PostUpdate(status=compliment, auto_populate_reply_metadata=True, in_reply_to_status_id=status.id)
                        storage.addTweet(status.id_str)
                        tweeted = True
                        tweet_count += 1
                        break
    #wait to tweet again
    if(tweeted): time.sleep(60*60)
    else: time.sleep(2*60)
