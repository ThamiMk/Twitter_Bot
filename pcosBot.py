import pip
import tweepy
import time

consumer_key= 'zx786KyiAdftHwn0MFa1Gl2Jd'
consumer_secret='wDey7vCxK9QI4NUusaYybdwFZSOFTnRVzaZDVNt9tfU4tw7Muh'
access_key='1416024808131895297-oEfZoPCHBLoqP0ftJ6yhDQCZ0XBgsA'
access_secret='Zd9VMECQuEh1FWQYxqvFHtNPEduTHWWMazDyAxHVmBDNp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()
search = 'pcos', 'pcod'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:
        
        tweet.retweet()
        print("Retweet")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break