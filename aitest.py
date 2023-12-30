import requests
import json
import datetime

#get date
today = datetime.date.today()
date_formatted_today = today.strftime("%d-%m-%Y")
#print("Today's date:", date_formatted_today)

#tomorrow = today + datetime.timedelta(days=1)
#date_formatted_tomorrow = tomorrow.strftime("%d-%m-%Y")
#print("Tomorrow's date:", date_formatted_tomorrow)

#get show data for today's date
url = "https://www.rtp.pt/EPG/json/rtp-channels-page/list-grid/tv/8/" + date_formatted_today

response = requests.get(url)
data = json.loads(response.text)

#trim data down to just shows
data=data['result']
morning = data['morning']
afternoon = data['afternoon']
evening = data['evening']

#print all entries with subtitles and time
for entry in morning:
    
    if 'Teletexto' in json.dumps(entry):
        print(entry["name"] + " : " + entry["date"])

for entry in afternoon:
    
    if 'Teletexto' in json.dumps(entry):
        print(entry["name"] + " : " + entry["date"])

for entry in evening:
    
    if 'Teletexto' in json.dumps(entry):
        print(entry["name"] + " : " + entry["date"])
    
#print(json.dumps(data, indent=4))



