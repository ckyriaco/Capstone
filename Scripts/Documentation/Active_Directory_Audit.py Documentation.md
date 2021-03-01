## Active_Directory_Audit.py Documentation

_This script is designed to utilize the ADquery class to audit a variety of users, computers and groups for CMMC compliance._

### Import 
* ADaudit class
    * Allows functions from ADaudit class to be used
* os
    * Allows OS to gather variables from bash script
    * Imports os variables to plug into arrays based on variable types  
* numpy
* port scanner
* tkinter
* tkinter messagebox
* report_gen
* datetime
* io

### Initialize window 

### login_info method
* This method uses the ADquery class to retrieve info and audit active directory for users that have not logged on in N days.
* The method also generates a report based on users that have not logged in N days.

### get_dn_status method 
* This method uses ADaudit to locate users that have not changed their password in N days.
* The produdure that follows: `def get_dn_status` does not do that.  It looks like it lists all of the distinguished names. -- Dave Fuller 

### check_usernames method 
* This method uses ADaudit to check the usernames of different types against the ARA naming scheme rules.

### userAudit method 
* This method checks the username, the service account name and the computer name.

### last_set_pwd method 
* This method checks to see that the passwords have been reset at the N required days and that the passwords do expire for all users.

### get_admin method
* This method uses the ADquery class to get all the admin of each admin type in the AD server.

### service_account_audit method
* This method uses the ADquery class to get all the service accounts that don't have the manager attribute set.

### port_status method
* This method uses the Port_Scanner class to identify all processes running on all active ports on the domain server and the computers joined to it.

### main method
* The main method takes in os variables from a bash file and passes them into the appropriate functions to audit an Active Directory instance within the current admin user's domain.