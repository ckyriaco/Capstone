## Report Generation Formatting 

_Here are suggested formatting changes to the Audit Report txt._

### Title (ARA Audit Report Findings)

**Vulnerabilites** (For each label a level of severity - Critical, High, Medium, Low)
* Users with passwords unchanged past the day limit:

* Users with passwords that don't expire:

* Unused Users:

* Unused Computers:

**Remediation Report**
* Users that need their username changed:

* Computers that need their names changed:

* Service Accounts that need their names changed:

**Admin Report** 
* Domain Admins:
* Enterprise Admins:
* Key Admins:
* Schema Admins:

* Administrator __ last logon:

* Service Accounts without manager set:

**Distinguished Name Report**
* Distinguished Name Status:

**Port Status**

_________________________________________________________________________________________________________________________________________________________________________________

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

### Sources (Panda Library and Report Lab):
* [Creating PDF Reports with Pandas, Jinja and WeasyPrint](https://pbpython.com/pdf-reports.html)

_________________________________________________________________________________________________________________________________________________________________________________
