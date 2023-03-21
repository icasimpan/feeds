## to improve:
##    * json_conf - add attribute to real domain as like TheHackerNews, it's rssfeed comes from feedburner
##                  at current implementation, it feedburner is shown as source instead of TheHackerNews
##    * check duplication - in crypto json, cointelegraph has a lot of feeds that sometimes, same news are
##                  in different feeds
##    * add top cves? for different sofwares (e.g. python, golang, rust etc)

import os
import json
import feedparser
import tldextract
from datetime import datetime

def pubdate_dateonly(full_pubdate):
   return ' '.join(list(full_pubdate.split(" "))[1:4])

def today_dateonly(output_format='%d %b %Y'):
   str_today = ''.join(list(str(datetime.utcnow()).split(" "))[0])
   date = datetime.strptime(str_today, "%Y-%m-%d")

   return datetime.strftime(date, output_format)

def get_source(domain):
    ext=tldextract.extract(domain)
    return ext.domain + '.' + ext.suffix

def is_published_today(full_pubdate):
    retval=False

    if today_dateonly() == pubdate_dateonly(full_pubdate):
        retval=True

    return retval

## returns a dict()
## https://stackoverflow.com/questions/15789059/python-json-only-get-keys-in-first-level
##
def getInputKeys(conf):
    with open(conf) as jsonFile:
        data = json.load(jsonFile)
        jsonData = data.keys()

    return jsonData

## https://dev.to/bluepaperbirds/get-all-keys-and-values-from-json-object-in-python-1b2d
##
def getInputValuesFromKey(conf, key):
    with open(conf) as jsonFile:
        data = json.load(jsonFile)
        jsonData = data[key]

    return jsonData


today_only = True

def header():
    print('---')
    print('title: "Web3 Feed"')
    print('date: ' + today_dateonly(output_format="%Y-%m-%d") + 'T00:00:00+08:00')
    print('tags: [crypto, blockchain]')
    print('draft: false')
    print('---')

header()
current_source=""
next_source=""

config_file=os.path.dirname(__file__) + "/conf/feed-input.json"
jsonKeys = getInputKeys(config_file)

for i in jsonKeys:
    feedlist_from_key = getInputValuesFromKey(config_file, i)
    print("\n# " + i)
    for each_feedsource in feedlist_from_key:
        d = feedparser.parse(each_feedsource)
        for n in range(0, len(d.entries)):

            ## ----------------------------
            ## Only show today's news (UTC)
            ## ----------------------------
            if today_only == True and is_published_today(d.entries[n].published):

                if current_source == "":
                    current_source=get_source(each_feedsource)
                    print('## ' + current_source)
                else:
                    next_source=get_source(each_feedsource)
                    if current_source != next_source:
                        print('## ' + next_source)
                        current_source=next_source

                print('* [' + d.entries[n].title + '](' + d.entries[n].link + ') - ' +  d.entries[n].description)

            elif today_only == False:
                if current_source == "":
                    current_source=get_source(each_feedsource)
                    print('## ' + current_source)
                else:
                    next_source=get_source(each_feedsource)
                    if current_source != next_source:
                        print('## ' + next_source)
                        current_source=next_source

                print('* [' + d.entries[n].title + '](' + d.entries[n].link + ') - ' +  d.entries[n].description)
