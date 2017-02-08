"""
Console App for interacting with the locu API from python for Andela Bootcamp15
"""

import urllib2
import json

locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

def main(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for restaurant in data['objects']:
        print restaurant['name'], restaurant['phone']

if __name__ == "__main__":
    main("California")
