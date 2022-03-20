#!/opt/homebrew/bin/python3

################################################################
# License: GPLv3
# Author: Michal Duda <github@vookimedlo.cz>
# Home: https://github.com/vookimedlo/alfred-github-repositories
# Project: alfred-github-repositories
#
################################################################

import queue
import base64
import io
import json
import os
import re
import sys
import urllib.request
from urllib.request import urlopen


# 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗
# ⁰¹²³⁴⁵⁶⁷⁸⁹
def toBetterNumbers(s):
    #    numbers = {'0': "𝟎", '1': "𝟏", '2': "𝟐", '3': "𝟑", '4': "𝟒", '5': "𝟓", '6': "𝟔", '7': "𝟕", '8': "𝟖", '9': "𝟗"}
    numbers = {'0': "⁰", '1': "¹", '2': "²", '3': "³", '4': "⁴", '5': "⁵", '6': "⁶", '7': "⁷", '8': "⁸", '9': "⁹"}

    return ''.join(numbers.get(char, char) for char in s)


query = sys.argv[1]
queryPattern = re.compile(query, re.I)

user = os.getenv('user')
token = os.getenv('personalToken')
cache = os.getenv('cache')

# Just a very simple caching
#
if os.path.isfile(cache) and os.path.getsize(cache) == 0:
    data = []
    url = 'https://api.github.com/user/repos?page=1&per_page=1000'
    auth = {'Authorization': 'Basic ' + (base64.b64encode((user + ':' + token).encode('utf-8',errors = 'strict'))).decode()}

    linkPattern = re.compile('<(https://[^>]+)>\s*;\s*rel="next"')

    queue = queue.Queue()
    queue.put(url)

    while not queue.empty():
        queuedUrl = queue.get()
        response = urlopen(urllib.request.Request(queuedUrl, headers=auth))
        link = response.getheader('Link')
        content = response.read()
        partialData = json.loads(content)

        # Join multiple json data
        #
        for i in range(0, len(partialData)):
            data.append(partialData[i])

        if link:
            result = linkPattern.search(link)
            if result:
                queue.put(result.group(1))

    with io.open(cache, 'w', encoding='utf8') as cacheFile:
        dumpedData = json.dumps(data, ensure_ascii=False)
        cacheFile.write(str(dumpedData))
else:
    with io.open(cache, 'r', encoding='utf8') as cacheFile:
        data = json.loads(cacheFile.read())

# Alfred menu items
#
alfreditems = {"items": []}

for item in data:
    title = item['name']
    description = item['description']
    url = item['html_url']
    urlClone = item['clone_url']
    starsCount = item['stargazers_count']
    forksCount = item['forks_count']

    if query != "" and not queryPattern.search(str(title)):
        continue

    mysortkey = str(title).lower()
    if os.getenv('orderBy') == "^stars^^":
        mysortkey = starsCount
    elif os.getenv('orderBy') == "^forks^^":
        mysortkey = forksCount

    starsCount = toBetterNumbers(str(starsCount))
    forksCount = toBetterNumbers(str(forksCount))

    # Adding star ⭐🎖 and fork 🍴ᛘ
    #
    starPictogram = os.getenv('starPictogram') if os.getenv('starPictogram') else "🎖"
    forkPictogram = os.getenv('forkPictogram') if os.getenv('forkPictogram') else "ᛘ"

    if str(os.getenv('showStarStats')).lower() == 'true' and str(os.getenv('showForkStats')).lower() == 'true':
        title = str(title) + " " + starPictogram + str(starsCount) + " " + forkPictogram + str(forksCount)
    elif str(os.getenv('showStarStats')).lower() == 'true':
        title = str(title) + " " + starPictogram + str(starsCount)
    elif str(os.getenv('showForkStats')).lower() == 'true':
        title = str(title) + " " + forkPictogram + str(forksCount)

    icon = "lock.png" if item["private"] else "icon.png"
    autolearn = "" if os.getenv('autolearn') == "0" else title

    # Alfred menu items
    #
    alfreditems['items'].append({
        "mysortkey": mysortkey,
        "uid": autolearn,
        "title": title,
        "subtitle": description,
        "autocomplete": title,
        "arg": url,
        "icon": {
            "path": icon
        },
        "mods": {
            "cmd": {
                "valid": True,
                "arg": urlClone,
                "subtitle": "Copy a repository clone URL"
            },
            "alt": {
                "valid": True,
                "arg": "git clone " + urlClone,
                "subtitle": "Copy a repository clone command"
            },
            "ctrl": {
                "valid": True,
                "arg": "x-github-client://openRepo/" + url,
                "subtitle": "Open a repository in GitHub client"
            }
        }
    })

# Sort Repositories
#
reversedFlag = False if os.getenv('reversed') == "0" else True
lines = sorted(alfreditems['items'], key=lambda k: k['mysortkey'], reverse=reversedFlag)
dump = json.dumps({'items': lines}, indent=4)

sys.stdout.write(dump)

