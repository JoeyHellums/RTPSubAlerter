import requests
import json
import datetime
from plyer import notification

def make_notification(show, datetime):
    title = show + "está legendada em RTP2"
    message = show + "está a iniciar em RTP2 agora"
    send_notification(title,message,datetime)

def send_notification(title, message, datetime_str):
    # Convert the date and time strings to datetime objects
    datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    # Calculate the delay in seconds from the current time to the notification time
    delay = (datetime_obj - datetime.datetime.now()).total_seconds()

    # Schedule the notification to be sent after the delay
    notification.schedule(title,message,delay)


def get_formatted_date(date):
    #Return a formatted date string.
    return date.strftime("%d-%m-%Y")


def get_show_data(date):
    #Return show data for a given date.
    url = f"https://www.rtp.pt/EPG/json/rtp-channels-page/list-grid/tv/8/{get_formatted_date(date)}"
    response = requests.get(url)
    return response.json()["result"]


def print_subtitled_shows(shows):
    #Print the names and dates of shows with subtitles.
    subtitle_shows = filter(lambda show: "Teletexto" in json.dumps(show), shows)
    for show in subtitle_shows:
        print(f"{show['name']} : {show['date']}")
        #make_notification(show['name'],show['date'])
    


# Get today's date
today = datetime.date.today()

# Get show data for today's date
show_data = get_show_data(today)

# Print all entries with subtitles and time
print_subtitled_shows(show_data["morning"])
print_subtitled_shows(show_data["afternoon"])
print_subtitled_shows(show_data["evening"])
