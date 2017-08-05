# DONT TOUCH ANYTHING FROM HERE
import tweepy

def setup_twitter():
    consumer_key = "DBvGhGxcXrhYdpweTxjXwVBjv"
    consumer_secret = "02nrOHBQOrHulVYq23LBsziAXzj0CrbYItpD8lNr8QSCXk6wIA"
    access_token = "369244189-gSVwKX1huERMlxTuAOazVrQXk7ZmnYycZjYWzldz"
    access_token_secret = "0P7NUGhJkbQtm7EO7ky21Dpi7L1Fr8MuK8ZvzbgHpntR6"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api = tweepy.API(auth)

def print_name(screen_name):
    print(api.get_user(screen_name).name)

def get_friends_screen_name(screen_name):
    res = list()
    for friend in api.friends_ids(screen_name):
        res.append(api.get_user(friend).screen_name)
    return res

setup_twitter()
# TO HERE!
# you can touch stuff below this comment

'''
# Let's find the trumpster
print_screen_name('realDonaldTrump')

# Let's find all of his friends!
for friend in get_friends_screen_name('realDonaldTrump'):
    print(friend)
'''
