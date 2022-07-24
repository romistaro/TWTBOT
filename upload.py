import tweepy
import os

all_keys = open('/home/kamui/Documents/PROGRAMMING/TWTBOT/twitterAuth.txt', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)



def send(day, term):
    currentImage = os.listdir('/home/kamui/Documents/PROGRAMMING/TWTBOT/downloads/'+term)[0]

    api.update_status_with_media(
        status=term + '\nBOBLYBOT Upload '+ str(day),
        filename= '/home/kamui/Documents/PROGRAMMING/TWTBOT/downloads/'+term+'/' + currentImage
        )