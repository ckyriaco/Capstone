from warnings import simplefilter
import re
from reportlab.pdfgen import canvas
from reportlab import *
from reportlab.rl_config import *
from reportlab.lib.units import cm, inch, mm, pica, toLength
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from mdutils.mdutils import MdUtils
from mdutils import Html
import datetime
import pandas as pd
import csv




simplefilter(action='ignore', category=FutureWarning)


def gen_pdf(file_name, message):
    message = message.replace("#", "")
    pdf_file = file_name


    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rigthMargin=2*cm,leftMargin=2*cm,topMargin=2*cm,bottomMargin=2*cm)
    doc.build([Paragraph(message.replace("\n", "<br />"), getSampleStyleSheet()['Normal']), ])

def formattext(file_name):
	mdFile = MdUtils(file_name=file_name.replace(".txt",""), title= "Command Output")
	tempfile = open(("{}.xxx").format(file_name.replace(".txt","")), "w")
	textfile = open(file_name, "r")
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

def format_md(file_name):
    formattext(file_name)
    mdFile = MdUtils(file_name=file_name.replace(".txt", ""), title='Command Execution Output')
    mdFile.new_line('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), bold_italics_code='bc')
    list_of_strings = ["Protocol", "Local Address", "Foreign Address", "State", "Owner"]
    textfile = open(("{}.xxx").format(file_name.replace(".txt", "")), "r")
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






