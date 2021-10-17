import requests
import json
import sys
import os
from requests import api
from requests.api import post, request
from requests.models import Response

# Create Streamer Class:
class Streamer:
    '''Streamer class with url instance, config json file must be in bots directory'''
    def __init__(self,configParamsJson):
        self.configPath = os.path.join(os.getcwd(),configParamsJson)
        with open(self.configPath) as config_file:
            config = json.load(config_file)
        self.config = config
        self.url = self.config["url"]
        config_file.close()

    def getAccessToken(self):
        '''Retrieves twitch access token and stores in config file,
        token good for 60 days'''
        tokenUrl = "https://id.twitch.tv/oauth2/token"
        response = requests.post(tokenUrl,self.config)
        accessToken = response.json()['access_token']
        self.config.update({"access_token":accessToken})
        with open("config.json", "w") as outfile:
            json.dump(self.config, outfile)
        outfile.close()

    def isLive(self):
        '''Will return string indicating if the streamer is live or not'''
        with open("config.json", "rb") as config_file:
            self.config = json.load(config_file)
        config_file.close()
        params = {
            "login":self.config["user_login"]
        }
        headers = {
            "Authorization": "Bearer {}".format(self.config['access_token']),
            'Client-Id': self.config['client_id']
            }
        response = requests.get(self.url,params=params, headers=headers).json()['data']
        status = response[0]['type']
        return status # returns empty string if not live, otherwise returns 'live'
        

