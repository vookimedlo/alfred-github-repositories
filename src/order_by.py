#!/opt/homebrew/bin/python3

################################################################
# License: GPLv3
# Author: Michal Duda <github@vookimedlo.cz>
# Home: https://github.com/vookimedlo/alfred-github-repositories
# Project: alfred-github-repositories
#
################################################################

import json
import sys
import tempfile

cache = tempfile.mkstemp()[1]

# Alfred menu items
#
alfreditems = {"items": []}
sortkey = 0;
title = "name"
subtitle = "Order repositories by name."
alfreditems['items'].append({
    "mysortkey": ++sortkey,
    "title": title,
    "subtitle": subtitle,
    "autocomplete": title,
    "arg": "",
    "variables": {
        "orderBy": "^name^^",
        "reversed": 0,
        "autolearn": 1,
        "cache": cache
        },
        "mods": {
            "cmd": {
                "valid": True,
                "arg": "",
                "subtitle": "Do not apply Alfred learning feature on repository list.",
                "variables": {
                    "orderBy": "^name^^",
                    "reversed": 0,
                    "autolearn": 0,
                    "cache": cache

                    }
                }
            }
    })

title = "stars"
subtitle = "Order repositories by stars count."
alfreditems['items'].append({
    "mysortkey": ++sortkey,
    "title": title,
    "subtitle": subtitle,
    "autocomplete": title,
    "arg": "",
    "variables": {
        "orderBy": "^stars^^",
        "reversed": 1,
        "autolearn": 0,
        "cache": cache
        }
    })

title = "forks"
subtitle = "Order repositories by forks count."
alfreditems['items'].append({
    "mysortkey": ++sortkey,
    "title": title,
    "subtitle": subtitle,
    "autocomplete": title,
    "arg": "",
    "variables": {
        "orderBy": "^forks^^",
        "reversed": 1,
        "autolearn": 0,
        "cache": cache
        }
    })

# Sort Repositories
#
lines = sorted(alfreditems['items'], key=lambda k: k['mysortkey'], reverse=False)
dump = json.dumps({'items': lines}, indent=4)

sys.stdout.write(dump)

