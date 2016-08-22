#    ____                                 ____                       
#   / __ \_________ _____  ____ ____     / __ \____ _____ ____  _____
#  / / / / ___/ __ `/ __ \/ __ `/ _ \   / /_/ / __ `/ __ `/ _ \/ ___/
# / /_/ / /  / /_/ / / / / /_/ /  __/  / ____/ /_/ / /_/ /  __(__  ) 
# \____/_/   \__,_/_/ /_/\__, /\___/  /_/    \__,_/\__, /\___/____/  
#                      /____/                    /____/             

# Author: Will Binns (telegram.me/wbinns)
# Description: Get social media accounts associated with an email address.
# GitHub Repository: Orange Pages (github.com/wbinns/orange-pages/)
# License: Unlicense (unlicense.org)

# Load libraries
import requests
import urllib
import os
import json
import yaml
from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Init Flask, Wallet and Payment
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Add 402
@app.route('/whois')
@payment.required(7200)
def lookup_email():
     email = request.args.get('email')
     key = os.environ.get('ORANGE_PAGES_KEY')
     url = requests.get('http://api.fullcontact.com/v2/person.json?email='+email+'&apiKey='+key)
     return url.text

# Add Manifest
@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

# Init Host
if __name__=='__main__':
    app.run(host='0.0.0.0', port='10109')
