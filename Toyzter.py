# Encoding: UTF-8
# -*- coding: utf-8 -*-

import sys, os
import tweepy
from datetime import *


consumerKey = ''
consumerSecret = ''
accessKey = ''
accessSecret = ''
char = 140
last = ''
printDate = '['+str(datetime.today())+']'
f = open("tweets.txt", 'a')
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

def sendTweets(tuil):
	last = []
	tuits = []
	tweets = [tuil[i:i+char] for i in range(0, len(tuil), char)]
	
	if len(tweets) == 1:
		api.update_status(tuil)
		print "Tweet sent"
		f.write(printDate+'@: '+tuil+'\n')
	else:
		x = 0
		for tuit in tweets:
			if not tuit.endswith(' '):
				split = tuit.split(' ')
				last.append(split[len(split)-1])
				if x == len(tweets):
					split[len(split)-1] = ''
				tuit = split[0]
				for i in range(1, len(split)):
					tuit += ' ' +split[i]
				tuits.append(tuit)
				x+= 1
		last.insert(0,'')
		x = 0
		for tweet in tuits:
			tuit = last[x]+tweet
			print "Tweet modified"
			api.update_status(tuit)
			f.write(printDate+'@: '+tuit+'\n')
			x += 1
	if len(tweets) > 1:
		print "#Toyzter Stats:", len(tweets),'/',len(tuil)
		api.update_status("#Toyzter Stats: "+str(len(tweets))+"/"+str(len(tuil)))

if __name__ == "__main__":
	exit = False
	while not exit:
		val = raw_input("\nDo you want to compose a tweet? ")
		if val == "no":
			exit = True
		else:
			tweet = raw_input("Tweet: ")
			sendTweets(tweet)
f.close()
os.system("pause")

