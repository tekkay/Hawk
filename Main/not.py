import  tweepy

consumer_key = "RMaqFhcVupsxQUDTDcc0d7rvn"
consumer_secret = "VPLVy3To01PFAFZSPCY5hLckswBZw33y8bRp5wLzJycw5t4kz6"
access_token = "Q893620754289487872-WHV0al62u8tKlkX76XEMn1kOBB3G90"
access_token_secret = "KXHehu3dJyMG7x3hKNTt1TT0OoBNbZVeGV1xfG2HXGa0S"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

text_query = 'USA Election 2020'
count = 2000# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                            .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]# Creation of dataframe from tweets list
tweets_df = pd.DataFrame(text_tweets)