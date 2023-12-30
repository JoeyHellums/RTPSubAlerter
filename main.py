import re #regex
import urllib.request #grabs urls
from urllib.parse import unquote
#import urllib.parse #urllib acts up if links arent put through this
from bs4 import BeautifulSoup #html scraper
from plyer import notification #ability to show system notifications 
import json #json

def get_page(quote_page):
    page = urllib.request.urlopen(quote_page)
    return page

def notifyshowstart(starttime,endtime):
    notifytitle = 'Uma programa legendada está a iniciar agora em RTP2!'
    notifymessage = 'Tempo de iniciar: ' + starttime + 'h \nTempo de fim: ' + endtime 
    notification.notify(
        title = notifytitle,
        message = notifymessage,
        app_icon = '',
        timeout = 15,
    )

def notifyshowstart(nexttime):
    notifytitle = 'Uma programa legendada acabei fim em RTP2'
    notifymessage = 'Proxima programa legendada ás: ' + nexttime
    notification.notify(
        title = notifytitle,
        message = notifymessage,
        app_icon = '',
        timeout = 15,
    )

#page = get_page('https://www.rtp.pt/rtp2/')
page = get_page('https://www.rtp.pt/EPG/json/rtp-channels-page/list-grid/tv/8/27-02-2023')
#print(page)
soup = BeautifulSoup(page, 'html5lib') #convert page to text
#print(soup.body.get_text)
pagedata = str(soup.body.text) #convert page text to string
#print(pagedata)
data = json.dumps(pagedata, indent=4)
print(data)

