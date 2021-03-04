## report_gen.py Documentation

_This class utilizes pandas 1.2.3, mdutils 1.3.0, and reportlab 3.5.62 to clean and output results as either a markdown file or a PDF._

### Import 
* simplefilter
* re
* canvas
* reportlab
    * config
    * units
    * pagesizes
    * platypus
    * lib.styles
* Mdutils
* Html
* datetime
* pandas
* csv

### Initialize simplefilter

### gen_pdf method
* This method resets the message, gives the report a file name, builds a report with a template, and fills the report with data.

### format_text method 
* This method creates a formatted Command Output report with needed headers and empty data.
* Headers included:
    * TCP
    * UDP

### format_md method
* This method creates a formatted Command Execution Output report with needed headers empty data.
formatted markdown file 
* Compatible with netstat ban commands
* Headers included:
    * Protocol 
    * Local Address
    * Foreign Address
    * State
    * Owner 


### make_markdown method
* This method writes the markdown report from active directory.
* Reads raw text file 
* Takes any netstat commands 
* Gathers info 
* Look at headings 
* Creates dataframe based on how many columns (up to 5)
* Has validation to alert user if no headers are detected 
* Creates needed markdown files 



