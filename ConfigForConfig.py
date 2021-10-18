import json
import os
from dotenv import load_dotenv
load_dotenv()


# Load and configure the config json by loading the env vars
def configureJson():
    configPath = os.getcwd()
    with open(os.path.join(configPath,"config.json"))as config_file:
        config = json.load(config_file)

    config['user_login'] = os.environ.get('user_login')
    config['client_id'] = os.environ.get('client_id')
    config['client_secret'] = os.environ.get('client_secret')
    config['access_token'] = os.environ.get('access_token')

    with open("config.json", "w") as outfile:
        json.dump(config, outfile)
    outfile.close()