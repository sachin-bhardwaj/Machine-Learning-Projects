#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
  
class Twitterclient(): 
   
    def __init__(self): 
        ''' 
        
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = '7bV3zxiL9cwHgfEmZ7rYdnB4H'
        consumer_secret = 't24Zca5nJI4axEwJ8Hn88niaTNhpjXm2PBobeg5JyjIZXkLlt3'
        access_token = '857588081809137664-ZRb0HHfeyUpPGniHqKd1ofqvjrPrzWo'
        access_token_secret = 'MT3xo8KkLDroE8SGCkS762jwiLdQRPHn1qURlTuxcjnkL'
        try:
            
        # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        
        except:
            
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
         
        
        
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        
        # empty list to store parsed tweets 
        tweets = []

                               
        try:

            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count>0:
                     
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets 
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
  
 
def main():
    
    
    # creating object of TwitterClient Class 
    api = Twitterclient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query ='@INCIndia', count = 20) 

    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
  #  print("Neutral tweets percentage: {} %\".format(100*len(tweets - ntweets - ptweets)/len(tweets))) 

    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 

    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 

        
if __name__ == "__main__":
    main() 
  


# In[ ]:




