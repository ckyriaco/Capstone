## report_gen.py Documentation

_This class is designed to generate an audit report in PDF format._

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
* This method creates a formatted report with empty data.

### format_md method
* This method creates a formatted report with empty data.

### make_markdown method
* This method writes the markdown report from active directory.


