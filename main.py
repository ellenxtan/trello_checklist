# encoding:utf-8

from utils import *

import json
import os
import sys
import argparse
import pytz
from dateparser import parse
from collections import Counter


my_parser = argparse.ArgumentParser(description="Calculate weekly scores of Trello boards. JSON files of the name board and the daily boards should be put under the same folder")
my_parser.add_argument("--folder_path", type=str, help="the path to the weekly folder")
my_parser.add_argument("--name_path", type=str, help="the path to the name board")
my_parser.add_argument("--out_path", type=str, help="the path to the output txt file")

args = my_parser.parse_args()
path = args.folder_path  # "week"
name_path = args.name_path  # "names.json"
out_path = args.out_path  # res.txt


## name board
names_json = ReadJson(os.path.join(path, name_path))
names_json = names_json["checklists"]

lst1 = names_json[0]['checkItems']
lst2 = names_json[1]['checkItems']

names_d = Counter()
names_d = GetNameDict(names_d, lst1, "once")
names_d = GetNameDict(names_d, lst2, "twice")


## daily board
files = os.listdir(path)
for f in files:
    print(f)
    if f == name_path:
        continue
    daily_d = ReadJson(os.path.join(path, f))  # f = path + "exported2.json"
    names_d = CalScore(names_d, daily_d)


## save results
SaveTxt(names_d, out_path)

print("Finished!")
