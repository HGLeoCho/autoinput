import os

start_num = 1
end_num = 200
_dir = os.path.abspath(__file__)

with open('file.txt.', 'r') as fr:
  for value in fr:
    os.rename(os.path.join(_dir,value),os.path.join(_dir,f'{start_num}_{start_num+4}.value[-3:]'))
    start_num += 5
