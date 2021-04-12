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
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import csv




simplefilter(action='ignore', category=FutureWarning)

#This generates a pdf file of the results of an audit
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

#This functions formats netstat output into organized text prior to the creation of a well formatted markdown file.
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

#This function creates a markdown file in the form of a large dataframe for netstat commands.
def make_markdown(filename, add_row):
    formattext(filename)
    f = open(filename, 'r')
    list = []
    counter = 0
    for line in f:
        x = line.split()
        if counter == 6:
            list = x
            print(x)
            break
        else:
            counter+=1
    list = np.array(list)
    f.close()
    f = open(filename.replace(".txt", ".xxx"), 'r')
    list = np.delete(list, np.where(list == "Address"))
    if(filename == add_row or add_row in filename):
        list = np.append(list, "Owner")
    if(list.size == 0):
        raise ValueError("No Headers Found!")
    elif(list.size == 5):
        df = pd.DataFrame([], columns=[str(list[0]), str(list[1]), str(list[2]), str(list[3]), str(list[4])], index=None)
    elif(list.size == 4):
        df = pd.DataFrame([], columns=[str(list[0]), str(list[1]), str(list[2]), str(list[3])], index=None)
    elif(list.size == 3):
        df = pd.DataFrame([], columns=[str(list[0]), str(list[1]), str(list[2])], index=None)
    elif(list.size == 2):
        df = pd.DataFrame([], columns=[str(list[0]), str(list[1])], index=None)
    else:
        df = pd.DataFrame([], columns=[str(list[0])], index=None)
    for line in f:
        x = line.split()
        if(list.size == 5):
            if(len(x) == 5):
                if(x[3] == "[Microsoft.ActiveDirectory.WebServices.exe]"):
                    x[3] = "[Microsoft.ActiveDirectory\n.WebServices.exe]"
                if (x[4] == "[Microsoft.ActiveDirectory.WebServices.exe]"):
                    x[4] = "[Microsoft.ActiveDirectory\n.WebServices.exe]"
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: x[3], list[4]: x[4]}
            elif (len(x) == 4):
                if (x[3] == "[Microsoft.ActiveDirectory.WebServices.exe]"):
                    x[3] = "[Microsoft.ActiveDirectory\n.WebServices.exe]"
                temp = x[3]
                if (temp[0] == "[" and temp[len(temp) - 1] == "]"):
                    newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: 'N/A', list[4]: x[3]}
                else:
                    newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: x[3], list[4]: 'N/A'}
            elif (len(x) == 3):
                temp = x[2].split()
                print(temp)
                if(temp[0] == "[" and temp[len(temp) - 1] == "]"):
                    newLine = {list[0]: x[0], list[1]: x[1], list[2]: 'N/A', list[3]: x[2], list[4]: 'N/A'}
                else:
                    newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: 'N/A', list[4]: 'N/A'}
            elif (len(x) == 2):
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: 'N/A', list[3]: 'N/A', list[4]: 'N/A'}
            elif (len(x) == 1):
                newLine = {list[0]: x[0], list[1]: 'N/A', list[2]: 'N/A', list[3]: 'N/A', list[4]: 'N/A'}
            else:
                newLine = "N/A"
        elif(list.size == 4):
            if (len(x) == 4):
                if (x[3] == "[Microsoft.ActiveDirectory.WebServices.exe]"):
                    x[3] = "[Microsoft.ActiveDirectory\n.WebServices.exe]"
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: x[3]}
            elif (len(x) == 3):
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2], list[3]: 'N/A'}
            elif (len(x) == 2):
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: 'N/A', list[3]: 'N/A'}
            elif (len(x) == 1):
                newLine = {list[0]: x[0], list[1]: 'N/A', list[2]: 'N/A', list[3]: 'N/A'}
            else:
                newLine = "N/A"
        elif(list.size == 3):
            if (len(x) == 3):
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: x[2]}
            elif (len(x) == 2):
                newLine = {list[0]: x[0], list[1]: x[1], list[2]: 'N/A'}
            elif (len(x) == 1):
                newLine = {list[0]: x[0], list[1]: 'N/A', list[2]: 'N/A'}
            else:
                newLine = "N/A"
        elif(list.size == 2):
            if (len(x) == 2):
                newLine = {list[0]: x[0], list[1]: x[1]}
            elif (len(x) == 1):
                newLine = {list[0]: x[0], list[1]: 'N/A'}
            else:
                newLine = "N/A"
        else:
            if (len(x) == 1):
                newLine = {list[0]: x[0]}
            else:
                newLine = "N/A"
        if(newLine != "N/A"):
            df = df.append(newLine, ignore_index= True)
    numRows = len(df.axes[0])
    numColumns = len(df.axes[1])
    df = df.to_markdown()
    print(df)
    f.close()
    f = open(filename.replace(".txt", ".md"), "w")
    title = "# Active Connection Results #"
    time = datetime.datetime.now()
    timestamp = ("## Timestamp: {:%Y-%m-%d %H:%M:%S} ##").format(time)
    df = str(df)
    doc = ("{}\n\n{}\n\n{}").format(title, timestamp, df)
    f.write(doc)
    f.close()

#This function uses matplotlib to create bar graphs of results
def bar_graph(file, image, labels, values, y, title):
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x-width/2, values, label="Quantity")

    ax.set_ylabel(str(y))
    ax.set_title(str(title))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()



    def autolabel(rects,):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')




    autolabel(rects1)
    fig.tight_layout()
    plt.savefig(str(image))
    f = open(file.replace(".txt", ".md"), "a")
    f.write(("\n\n![]({})").format(str(image)))
    f.close()
    #plt.show()





