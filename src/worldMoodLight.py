from twython import Twython, TwythonError
from collections import Counter
import sys
import subprocess

CONSUMER_KEY = 'yoYIs8DGdAg1MiPTxI7qsiKSo'
CONSUMER_SECRET = 'L2tx4Iv8FnKazyie9hbmnTRmDe4vgpUJIdjB2jghGmqeLjOABV'
OAUTH_KEY = 'FeGf2BLA3UasN6B11AtC33VPnkl7tTcdSzK9Bvs'
OAUTH_SECRET = 'Q1Es7LVnZzcuNm6IxgNAiRHw1VLIESipHnRi3ZZWCHv1X'

defaultMood = "happy"

happyWords = ["happy", "joy", "excited", "yay", ":)"]
sadWords = ["sad", "depressed", ":("]
angryWords = ["anger", "angry", "upset", ">:/"]
moods = [happyWords, sadWords, angryWords]

def main():
    search_results = []
    if len(sys.argv) > 1:
        openFile = open(sys.argv[1], 'r')
        for line in openFile:
            search_results.append(line)
        openFile.close()

    else:
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
        try:
            tweets = twitter.search(q='world news', count = 10)
            for tweet in tweets['statuses']:
                search_results.append(tweet['text'].encode('utf-8'))

        except TwythonError as e:
            print (e)

    mood = evaluateMood(search_results)
    updateLED(mood)

def evaluateMood(tweets):
    list = []
    currMood = ''
    moodCount = 0

    for tweet in tweets:
        result = evalMoodFromTweet(tweet)
        if result != 'NONE':
            list.append(result)

    if len(list) > 0:
        count = Counter(list)
        for mood in count:
            if count[mood] > moodCount:
                moodCount = count[mood]
                currMood = mood
    else:
        currMood = defaultMood

    return currMood

def evalMoodFromTweet(tweet):
    status = tweet.split()
    for word in status:
        for mood in moods:
            for moodWord in mood:
                if moodWord == word:
                    return mood[0]
    return 'NONE'

# Happy = Green
# Sad   = Blue
# Anger = Red
def updateLED(mood):
    redPort = 7
    greenPort = 5
    bluePort = 3
    maxFreq = 71400 # This gives the max frequency which is 14kHz
    lowFreq = 10000000 # This gives a low frequency

    print mood

    if mood == "sad":
        blue = lowFreq
        red = maxFreq
        green = maxFreq

    elif mood == "happy":
        blue = maxFreq
        red = maxFreq
        green = lowFreq

    elif mood == "anger":
        blue = maxFreq
        red = lowFreq
        green = maxFreq

    else:
        # default mood is happy
        blue = maxFreq
        red = maxFreq
        green = lowFreq

    # export, enable, update period, unexport
    updatePort(redPort, red)
    updatePort(greenPort, green)
    updatePort(bluePort, blue)

def updatePort(port, per):
    exportPort(port)
    enablePort(port, 1)
    updatePeriod(port, per)
    unexportPort(port)

def enablePort(prt, st):
    command = "echo -n '%d' > /sys/class/pwm/pwmchip0/pwm%d/enable" % (st, prt)
    subprocess.call(command, shell=True)

def exportPort(prt):
    command = "echo -n '%d' > /sys/class/pwm/pwmchip0/export" % (prt)
    subprocess.call(command, shell=True)

def unexportPort(prt):
    command = "echo -n '%d' > /sys/class/pwm/pwmchip0/unexport" % (prt)
    subprocess.call(command, shell=True)

def updatePeriod(prt, per):
    command = "echo -n '%d' > /sys/class/pwm/pwmchip0/pwm%d/period" % (per, prt)
    subprocess.call(command, shell=True)

if __name__ == '__main__':
    main()


