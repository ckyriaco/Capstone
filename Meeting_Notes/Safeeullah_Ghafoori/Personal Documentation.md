## Personal Documentation of code so far

### ADAudit.py 
* This class lets admins query info in order to test AD instances for CMMC Level 3 compliance
* Admin must already be joined to the AD server's domain to use this class
* Importing various utilities / packages including pyad, the main package used to automate AD auditing 
* The class creates an initial ADaudit object, with variables to retrieve audit information
* The class contains methods to query info which will ultimately be be printed in an overall message

### Active_Directory_Audit.py
* This class actually audits a variety of users, computers, and groups for CMMC Level 3 compliance, utilizing the ADquery class
* Class allows the OS to gather variables from bash script to be plugged into arrays based on variable types for auditing
* Contains a method to get info and audit AD users that haven't logged on in a specific number of days
* Contains a method to get all service accounts without the manager attribute set
* Contains a method calling the Port_Scanner class to identify all processes running on active ports within the domain server and computers joined to it
* Main method takes in OS variables from a bash file and passes them into the appropriate functions to audit an AD instance with the current admin user's domain

### Active_Directory_Remediate.py
* This script actually performs the remediations based on the audit from the Active_Directory_Audit.py script
* Checks for naming convention violations
* Provides a GUI for the admin to select specific user(s) to remediate

### Port_Scanner.py
* This class finds which processes are connecting to which active ports on the domain server itself as well as computers connected to the domain
* Method to check for valid IP address
* Method to identify computers within the AD domain
* Port_Status method which looks through the AD server and the computers connected to the server domain and identifies all processes running on active ports
* Writes over prior status report txt file with each new scan and is able to append to it


