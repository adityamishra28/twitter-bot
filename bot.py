import tweepy
import time


consumer_key = ''
consumer_secret = ''

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)
#api.update_status('Hi, I am a BOT')

FILE_NAME = 'lastseen.txt'

def read_file(FILE_NAME):
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_lastseen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

def work():
    tweets = api.mentions_timeline(read_file(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(str(tweet.id) + " " + tweet.full_text)
        api.update_status("@" + tweet.user.screen_name+ " everything works fine" , tweet.id)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        store_lastseen(FILE_NAME, tweet.id)

while True:
    work()
    time.sleep(10)
