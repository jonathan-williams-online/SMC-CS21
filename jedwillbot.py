import tweepy
import tkinter

consumer_key = 'uedw4QvzzmOyWIG6J2J5IKHe5'
consumer_secret = 'POiaUWLavccyIqF5ioPZqreF9kyzqQaSfK1XuiT63vPvnrDdal'
access_token = '903336835174117376-bxOnlVkYIfxf6SzLyKEjLBVEtVfhtTx'
access_token_secret = 'lEYtXFzUz92e3brgOXxNW7XHomBPme4atNfMAP4kRxNP3'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)
