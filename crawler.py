import requests
import json
from datetime import datetime

# pull request from cdc website 
dataset = requests.get("https://data.cdc.gov/resource/9mfq-cb36.json")
print(dataset.status_code)
dataset = dataset.json()

def extract_time(json):
    try:
        dt = datetime.fromisoformat(json['created_at'])
        return dt
    except KeyError:
        return 0

# sort data entries by creation date
dataset.sort(key=extract_time, reverse=True)

# nice printing 
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# write data to file
with open('datas.txt', 'w') as outfile:
    text = json.dumps(dataset, sort_keys=True, indent=4)
    outfile.write(text)
