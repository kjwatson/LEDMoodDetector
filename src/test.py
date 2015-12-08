# try following the directions at the Twython github account

from twython import Twython, TwythonError

CONSUMER_KEY = 'yoYIs8DGdAg1MiPTxI7qsiKSo'
CONSUMER_SECRET = 'L2tx4Iv8FnKazyie9hbmnTRmDe4vgpUJIdjB2jghGmqeLjOABV'
OAUTH_KEY = 'FeGf2BLA3UasN6B11AtC33VPnkl7tTcdSzK9Bvs'
OAUTH_SECRET = 'Q1Es7LVnZzcuNm6IxgNAiRHw1VLIESipHnRi3ZZWCHv1X'

#twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_KEY, OAUTH_SECRET)

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
# auth = twitter.get_authentication_tokens()

try:
    search_results = twitter.search(q='news', count = 50)

    for tweet in search_results['statuses']:
        print(tweet['text'].encode('utf-8'), '\n')

except TwythonError as e:
    print (e)



