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

**Active Connections**

_________________________________________________________________________________________________________________________________________________________________________________

_We have several options for formatting the text file._

* The Pandas library is great for manipulating large amounts of data and summarizing it into multiple text and visual representations - it supports output to CSV, Excel, HTML, JSON, and more
* We can can utilize the Pandas library along with ReportLab to output the text file into PDF format
  * ReportLab creates a canvas object using the data provided to it to generate a PDF document which we can customize the output of
* Alongside ReportLab we can utilize PollyReports, which is intended to generate reports from databases using Python
  * Able to play around with how the output will look to better improve readability 

