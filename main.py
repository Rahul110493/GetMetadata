import requests
import json

metadata_url = 'http://MY_URL/latest/'

if __name__ == '__main__':
    metdatapath = ["meta-data/"]
    output = {}
    for item in metdatapath:
        new_url = metadata_url + item
        r = requests.get(new_url)
        text = r.text
        output[item] = json.loads(text)
    print("Metadata is ", + output)
