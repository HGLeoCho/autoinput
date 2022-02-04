'''
Text file to HTML
by : Leo HoGyeong Cho
last modified : 2022/01/12
'''


import os
import re
import time
import sys
import json
import dominate
from dominate.tags import *
from datetime import date

WINDOWS_FILE_NAME_EXCEPTION = '<>:"/\|?*'

def checkfile(_list):
  if not _list:
    print("ERROR: LOG FILE MISSING\nPlease put log file into the folder")
    time.sleep(30)
    exit()
  if len(_list) > 1:
    print("ERROR: MORE THAN TWO LOG FILE DETECTED\nPlease make sure there is only one log file")
    time.sleep(30)
    exit()

def filter_IMS(*args):
  with open(logfile[0], encoding='utf-8', error='ignore') as fi:
    temp_string = ''
    temp_index = -1
    tolerence_count = 0
    
    for line in fi:
      confirm_string = line.rstrip()
      temp_number = 0
      for m in range(len(filter_short)):
        # if re.match(rf'^.*{filter_short[m]}', confirm_string):
        if filter_short[m] in confirm_string:
          tolerence_count = 0
          if temp_index == m:
            temp_string += '\n' + confirm_string
          elif temp_string == '':
            temp_string = confirm_string
            temp_index = m
          else:
            result[temp_index].append(temp_string)
            temp_string = confirm_string
            temp_index = m
          else:
            temp_nubmer += 1
      if temp_number == len(filter_short):
        tolerence_count += 1
      if tolerence_count == 2 and temp_string != '':
        result[temp_index].append(temp_string)
        temp_string = ''
        temp_index = -1
        tolerence_count = 0
      if tolderence_count == 2:
        tolerence_count = 0
              
            
     
    
