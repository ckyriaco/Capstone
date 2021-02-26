#!/bin/python3.7

from mdutils.mdutils import MdUtils
from mdutils import Html
import datetime

mdFile = MdUtils(file_name='Port_Details', title='Port Scan Report')
mdFile.new_line('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), bold_italics_code='bc')
textfile = open("Port_Details.txt", "r")

for line in textfile:
    if line.find('-> IPv') == -1:
        (mdFile.new_line(line))
    else:
        (mdFile.new_line(text=line, bold_italics_code='b'))

mdFile.create_md_file()
textfile.close()
