import tweepy
import  time
print("This is my Twitter Bot")
CONSUMER_KEY = 'CyGbuGoot9IBYFDh6fPQWIGcO'
CONSUMER_SECRET = 't4G7Dz7pqq7oqCJNMG3Na1jBzcqlYnJENxGtbLMlN6Mme3rrri'
ACCESS_KEY = '742987171490103296-P2urvJJr9Ekc7wr4DuxnuCC72IVl31V'
ACCESS_SECRET = 'Ns6vs6e17sZYI4yDbsq0IlIxApfaduRNUFM2GDKrLyjmK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
FILE_NAME='last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
# We need to use tweet_mode='extended' below to show
# all full tweets (with full_text). Without it, long tweets would be cut off.
    mentions=api.mentions_timeline(
                      last_seen_id,
                      tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' _ ' + mention.full_text)
        last_Seen_id=mention.id
        store_last_seen_id(last_Seen_id, FILE_NAME)
        if '#myquestion' in mention.full_text.lower():
            print('found #myquestion!')
            print('responding back...')
            api.update_status('@'+ mention.user.screen_name +
                    '#myquestion answer is on the way!', mention.id)
while True:
    reply_to_tweets()
    time.sleep(15)
