#! /usr/bin/env python
# author = "Andy"
# Date: 2018/7/13

import json
import xlwt
# jsonstr to python dict data
with open('student.txt', 'rb') as f:
    dicts = json.loads(f.read())
# create xls
xls = xlwt.Workbook()
table = xls.add_sheet('student')
# write xls
row = 0
col = 0
for k in sorted(dicts.keys()):
    col = 0
    table.write(row, col, k)
    col += 1
    for v in dicts[k]:
        table.write(row, col, v)
        col += 1
    row += 1
# save to xls
xls.save('student.xls')
