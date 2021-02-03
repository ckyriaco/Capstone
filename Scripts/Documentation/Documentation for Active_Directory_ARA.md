## Active_Directory_ARA.py Documentation

_The Active_Directory_ARA script utilizes the ADquery class to audit a variety of users, computers and groups for CMMC compliance_

### Import packages
* ADaudit class
    * Allows functions from ADaudit class to be used
* os
    * Imported OS to gather variables from bash script 
* numpy
* port scanner

### login_info method
* Uses ADquery class to retrieve info and audit active directory for users that have not logged on in N days.
* Generates report based on users that have not logged in N number of days

### last_set_pwd method 
* Uses ADquery to locate users that have not changed their password in N days.

### get_admin method
* Uses ADquery to get all the admin of each admin type in the AD server.

### service_account_audit method
* Uses ADquery to get all the service accounts that don't have the manager attribute set.

### port_status method
* Uses the Port_Scanner class to identify all processes running on all active ports on the domain server and the computers joined to it.

### main method
* Takes in os variables from a bash file and passes them into the appropriate functions to audit Active Directory instance within the current admin user's domain

### MISC Documentation (unsorted)
* Import os variables plug into arrays based on variable types 
* Get number of days since last login 
* POSSIBLE MISSING FILE?: Ad_driver.sh 
    * Documentation
        * Stores OS variables
        * Executes active_directory_ARA.py
* Later activities
    * In bash directory made bash file executable 
    * So it can be simply run through Gitbash
    * (Bash terminal of choice)