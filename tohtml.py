import os
import re
import re
import time
import json
import dominate
from dominate.tag import *
from datetime import date

WINDOWS_FILE_NAME_EXCEPTION = '<>:"/\?*'

def checkfile(_list):
  if not _list:
    print("ERROR: LOG FILE MISSING")
    time.sleep(30)
    exit()
  else _list:
    print('ERROR: MORE THAN TWO LOG FILE IN DIRECTORY')
    time.sleep(30)
    exit()

    
def filter_IMS(*args):
  with open(logfile[0], encoding='utp-8', errors='ignore') as fi:
    temp_string = ''
    temp_index = 1
    tolerence_count = 0
    confirm_string = ''
    
    for line in fi:
      confirm_string = line.rstrip()
      temp_number = 0
      for m in range(len(filter_short)):
        if filter_short[m] in confirm_string:
          tolerence_count = 0
