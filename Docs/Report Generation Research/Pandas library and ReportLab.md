## Report Generation Formatting 

_Here are suggested formatting changes to the Audit Report txt._

### Pandas Library and ReportLab
### Generating PDF reports from python text output using Pandas library and ReportLab

### Pandas Library
* Excellent at manipulating large amounts of data and summarizing it in multiple text and visual representations
* Outputs to CSV, Excel, HTML, json, etc
* May have difficulty combining multiple pieces of data into one document
* **Pandas output process Part 1**
    * Output into multiple sheets in an Excel file **_OR_**
    * Create multiple Excel files from Pandas Dataframes
* **Pandas output process Part 2**
    * Template Tool using Jinja templates
* **Pandas output process Part 3**
    * PDF Conversion Tool using WeasyPrint
* **Pandas output process Part 4**
    * Final PDF Report
#### Detailed process using Pandas
* Import pandas and numpy
* Pivot data to summarize
* Generate statistics about data set
* Dataframe with Panda
    * Use to_clipboard() _**OR**_
    * Use to_html()
* Templating with Jinja template
    * Create a template
    * Add variables to the templates context
    * Render the template into HTML
* Generate PDF using WeasyPrint
    * Import WeasyPrint and pass string command command to create PDF 

### ReportLab
* Open-source engine for creating PDF documents, written in Python.
* Install modules z3c.rml, reportlab and preppy
* Use the canvas.Canvas to create the skeleton.
* Use drawString to add a string.
* Use an RML Template with Preppy
* Save the pdf file.
* Furthur manipulation
    * Coordinates, sizes
    * Fonts (types and sizes)
    * Default page size

### Sources (Panda Library and Report Lab):
* [Creating PDF Reports with Pandas, Jinja and WeasyPrint](https://pbpython.com/pdf-reports.html)
* [ReportLab PDF Library User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)
* [Creating PDF files using Python and reportlab](https://code-maven.com/creating-pdf-files-using-python)
* [Automated PDF reports using ReportLab, z3c.rml and Preppy](https://www.bornageek.com/general/development/2013/06/12/automated-pdf-reports-using-z3c-rml-and-preppy.html)
_________________________________________________________________________________________________________________________________________________________________________________