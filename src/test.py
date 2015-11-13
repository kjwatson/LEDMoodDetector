from twython import Twython

CONSUMER_KEY = 'yoYIs8DGdAg1MiPTxI7qsiKSo'
CONSUMER_SECRET = 'L2tx4Iv8FnKazyie9hbmnTRmDe4vgpUJIdjB2jghGmqeLjOABV'
ACCESS_KEY = 'FeGf2BLA3UasN6B11AtC33VPnkl7tTcdSzK9Bvs'
ACCESS_SECRET = 'Q1Es7LVnZzcuNm6IxgNAiRHw1VLIESipHnRi3ZZWCHv1X'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, oauth_version=2)

token = twitter.obtain_access_token()

twitter = Twython(CONSUMER_KEY, access_token = token)

try:
    results = twitter.search(q='news', count = 100)

    for tweet in results:
        print(tweet)

except:
    print "error happened"



