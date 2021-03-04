# Report Generation 

We could generate our reports in a number of formats, markdown, comma separated value (for creating MS Excel readable spreadsheets), MS Word, or PDF. 

## markdown

​	Python has easy to use built in module (`mdutils`) for formating output into .md, we could code headings, tables, or even generate a checklist of fixes or known issues. 

link: https://pypi.org/project/mdutils/#overview

## .csv

​	Using a basic bash script we can insert headers and commas into the report and saving it to *.csv to be opened by MS Excel or LibreOffice Calc in an easy to read spreadsheet. 

## MS Excel

​	Using the `pyxll` library is another (and better) way to format an output file into a spreadsheet.

Link: https://www.pyxll.com/features.html

## MS Word

​	There is a python module python-docx, that can create Word documents. 

link: https://medium.com/arriendoasegurado/generating-microsoft-word-documents-with-python-62dd0b21615d

## .pdf

​	Another python module is `fpdf`, we can use this to save the reports as a pdf.  We could either convert another of the formatted styles in a pdf, or create a pdf on the fly with this utility.

link: https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/

I looked at the coding for each of these and I would recommend the **markdown** (`mdutils`) due to ease of coding and since it is the preferred ARA document format.

-Dave F.