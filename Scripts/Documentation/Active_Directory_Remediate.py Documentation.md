# Active_Directory_Remediate.py Documentation

*Utilizes the ADaudit class to audit a variety of users, computers and groups for CMMC compliance.*

### Import

- ADaudit class
  - Allows functions from ADaudit class to be used
- OS (Operating System)
  - Allows OS to gather variables from bash script
  - Imports OS variables to plug into arrays based on variable types
- imports numpy
- tkinter is Python's standard GUI
- messagebox from tkinter
- datetime
- Active_Directory_Audit


### Initialize window

### check-usernames method

- This method compares username types, (server, user, computer), against ARA's naming convention.
- The method also generates a report of which usernames need changed.

### servRemediate method

- This method calls ADaudit and remediates service account usernames if requested.
- If there is a need for remediation, an option is given to view the service accounts that need remediation, first.

### userRemediate method

- This method uses ADaudit to remediate invalid usernames.
- If there is a need for remediation, an option is given to view the users that need remediation, first.

### computerRemediate method

- This method uses ADaudit to remediate invalid computer names.
- If there is a need for remediation, an option is given to view the computer names the need remediation, first.

### last_set_pwd method

- This method checks to see that passwords are reset at N required days.
- This method also ensures that passwords do expire for all users.

### Force_Password_Change method

- This method forces users to change their password if not changed in N days at their next login.

### PWD_EXP_Remediate method

- This method uses ADaudit to remediate accounts that have passwords that do not expire, and sets them to N days before expiring.

### main method

- The main method takes in OS variables from a bash file and passes them into the appropriate functions to audit an Active Directory instance within the current admin user's domain.