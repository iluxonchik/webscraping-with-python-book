import tokens
from twitter import *

t = Twitter(auth=OAuth(tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET, tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET))
# status_update = t.statuses.update(status='API test')
python_tweets = t.search.tweets(q = "#python")
print(python_tweets)