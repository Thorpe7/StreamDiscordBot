import requests
import json
import sys
from dotenv import load_dotenv

# Create Streamer Class:
class Streamer:
    '''Streamer class with url instance'''
    def __init__(self, url):
        self.url = url

    def isLive(self):
        '''Will return string indicating if the streamer is live or not'''
        channel = requests.get(self.url, headers=headers)
        channelData = channel.json()
        return channelData['data']

twitch1 = Streamer("https://www.twitch.tv/originalcyd")
print(twitch1.isLive())

# Set up app on heroku
# Set up storing of information
# get authentification from twitch
# pull streamer data