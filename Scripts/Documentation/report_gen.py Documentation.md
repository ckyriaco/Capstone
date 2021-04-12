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
This method generates a pdf file of the results of the audit.
* This method: 
    * Resets the message 
    * Gives the report a file name
    * Builds a report with a template 
    * Fills the report with data.

### format_text method 
* This method creates a formatted Command Output report with needed headers and empty data.
* Headers included in report:
    * TCP
    * UDP

### format_md method
* This method formats netstat output into organized text prior to the creation of a well-formatted Markdown file.
* This method creates a formatted Command Execution Output report with needed headers and empty data.
* Creates a formatted markdown file 
* Is compatible with netstat ban commands
* Headers included in report:
    * Protocol 
    * Local Address
    * Foreign Address
    * State
    * Owner 


### make_markdown method
* This method creates a markdown file in the form of a large dataframe for netstat commands.
* This method writes the markdown report from active directory.
* Reads raw text file 
* Takes any netstat commands 
* Gathers info 
* Observes report headings 
* Creates dataframe based on how many columns (up to 5)
* Has validation to alert user if no headers are detected 
* Creates needed markdown files 

### bar_graph method 
* This method uses matplotlib to create bar graphs of results.

### autolabel method
* This method automatically labels bar graphs.

