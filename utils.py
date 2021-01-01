# encoding:utf-8

import json
import os
import pytz
from dateparser import parse
from collections import Counter

def ReadJson(f):
    """
    Read the input JSON file.
    """
    with open(f) as json_file: 
        json_d = json.load(json_file)
    return json_d


def GetNameDict(names_d, name_lst, period):
    """
    Get dictionary of name information.
    """
    for ppl in name_lst:
        name_all = ppl["name"].split('"')
        nickname = name_all[0]
        name = name_all[1]
        names_d[name] = Counter()
        names_d[name]["nickname"] = nickname
        names_d[name]["period"] = period
        names_d[name]["score"] = 0
    return names_d


def CalScore(names_d, daily_d, 
             once_intime=2, once_late=1.5, twice_intime=1, twice_late=0.5):
    """
    Calculate daily score.
    """
    due = daily_d["due"]
    due = parse(due, settings={'TIMEZONE': 'US/Eastern'})

    actions = daily_d["actions"]

    for act in actions:
        if act["type"]=="addAttachmentToCard" or act["type"]=="commentCard":
            name = act["memberCreator"]["fullName"]
            date = act["date"]
            date = parse(date, settings={'TIMEZONE': 'US/Eastern'})
            data = act["data"]
            if "attachment" or "text" in data:
                if name not in names_d:
                    print(name, "not in name board! Please add to the board and rerun the code!")
                    continue
                if names_d[name]["period"]=="once":
                    if date<=due:
                        names_d[name]["score"] += once_intime
                    elif date>due:
                        names_d[name]["score"] += once_late
                elif names_d[name]["period"]=="twice":
                    if date<=due:
                        names_d[name]["score"] += twice_intime
                    elif date>due:
                        names_d[name]["score"] += twice_late
    return names_d

def SaveTxt(names_d, out_path):
    with open(out_path, 'w') as f:
        for ppl in names_d:
            # print(ppl)
            nickname = names_d[ppl]["nickname"]
            score = str(names_d[ppl]["score"])
            f.write("%s,%s\n"%(nickname, score))