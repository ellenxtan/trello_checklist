# Trello打卡群自动化算分

## 打卡规则
- 单时段打卡
  - 准时打卡：2分；
  - 迟到打卡：1.5分；
  - 未打卡：0分

- 双时段打卡
  - 准时打卡：1分；
  - 迟到打卡：0.5分；
  - 未打卡：0分

## How to use
1. Installation
```
git clone https://github.com/ellenxtan/trello_checklist.git
cd trello_checklist
```
2. python3 main.py -h
```
usage: main.py [-h] [--folder_path FOLDER_PATH] [--name_path NAME_PATH]
               [--out_path OUT_PATH]

Calculate weekly scores of Trello boards. JSON files of the name board and the
daily boards should be put under the same folder

optional arguments:
  -h, --help            show this help message and exit
  --folder_path FOLDER_PATH
                        the path to the weekly folder
  --name_path NAME_PATH
                        the path to the name board
  --out_path OUT_PATH   the path to the output txt file
```
  - Example:
  ```
  python3 main.py --folder_path week \
                  --name_path names.json \
                  --out_path res.txt \
  ```

# Things to Update
1. Trello has pushed a major update recently, and the JSON export format has changed. Thus, the current main.py and utils.py are in need of an update.
2. Currently, the counting mechanism still counts multiple text and image upload actions. It would be useful to fine tune the counting mechanism in future iterations to avoid repetitive counting of actions of user mistakes.
