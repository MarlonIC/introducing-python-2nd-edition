import webbrowser
import requests

print('Let\'s find an old website.')
site = input('Type a website URL, like lolcats.com: ')
era = input('Type a year, month, and day, like 20151022: ')
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data['archived_snapshots']['closest']['url']
    print('Found this copy: ', old_site)
    print('It should apper in your browser now.')
    webbrowser.open(old_site)
except:
    print('Sorry, no luck finding', site)
