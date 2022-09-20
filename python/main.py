#!/usr/bin/python

import re

#1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland,FALSE
pattern = re.compile(r'^([\d]{4,4})\-\d{2,2}\-\d{2,2}\,(.+)\,(.+)\,(\d+)\,(\d+)\,.*$')

f = open('./dataRegex.csv', 'r')

for line in f:
  res = re.match(pattern, line)
  if res:
    total = int(res.group(4)) + int(res.group(5))
    if total > 10:
      print(f'{res.group(1)} | {res.group(2)}: {res.group(4)} - {res.group(3)}: {res.group(5)}')

f.close()