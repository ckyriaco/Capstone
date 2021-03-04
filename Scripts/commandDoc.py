#!/bin/python3.7

from mdutils.mdutils import MdUtils
from mdutils import Html
import datetime

def formattext():
	mdFile = MdUtils(file_name='command', title='Command Execution Output')
	tempfile = open("Command_Output.xxx", "w")
	textfile = open("Command_Output.txt", "r")
	for line in textfile:
		line = line.strip()
		if line.startswith("["):
			tempfile.write("  ")
			tempfile.write(line)
		if line.startswith("TCP"):
			tempfile.write("\n")
			tempfile.write(line)
		if line.startswith("UDP"):
			tempfile.write("\n")
			tempfile.write(line)
	tempfile.close()
	textfile.close()

formattext()
mdFile = MdUtils(file_name='command', title='Command Execution Output')
mdFile.new_line('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), bold_italics_code='bc')
list_of_strings = ["Protocol", "Local Address", "Foreign Address", "State", "Owner"]
textfile = open("Command_Output.xxx", "r")
mdFile.new_line(text="Active Connections", bold_italics_code='b')
count = 0
textfile.readline()
for line in textfile:
    columnR = line.split()
    column = ["test0", "test1", "text2", "text3", "text4"]
    for x in range(0, len(columnR)):
        if columnR[x] == "[Microsoft.ActiveDirectory.WebServices.exe]":
            columnR[x] = "[MS WebServices.exe]"
        column[x] = columnR[x].strip()
    list_of_strings.extend(column)
#    print(column)  # this line was used for troubleshooting
    count = count+1

# print(count) 	# this line was used for troubleshooting
mdFile.new_line()
mdFile.new_table(columns=5, rows=(count+1), text=list_of_strings, text_align='center')


mdFile.create_md_file()
textfile.close()
