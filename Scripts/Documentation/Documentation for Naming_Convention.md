## Naming_Convention.py Documentation

_Example of how the audit will check for the usernames against the ARA's naming convention, regardless of type of user (user, service account, computer)_ 

ARA Naming Conventions include:
* Human Naming
  * First initial of first name followed by the last name - if another user already has that username, include the user's middle initial; if both are taken, use the first name's first and second intitials then the last name.
  
* Service Account Naming
  * Organizational unit followed by a dash and the type of account, for example for the Corp top-level OU would be corp-backup.
  
* Computer Naming
  * Division abbreviation followed by user initials followed by specifying either pc or laptop.

### Import 

* re (Regular Expressions package)

### check_username method 
* This method utilizes the Regular expression package for comparing the username to the acceptible ARA naming conventions.
* takes in username and searches each letter to see if it meets the naming criteria, and returns true if valid and false if invalid.

### check_service_account_name method 
* This method utilizes the Regular expression package for comparing the service account name to the acceptible ARA naming conventions.
* takes in a service account name and searches each letter to see if it meets the naming criteria, and returns true if valid and false if invalid.

### check_computer_name method 
* This method utilizes the Regular expression package for comparing the computer name to the acceptible ARA naming conventions.
* takes in a computer name and searches each letter to see if it meets the naming criteria, and returns true if valid and false if invalid.

### check_dn_Computer method
* This method utilizes the Regular expression package for comparing the  computer domain name to the acceptible ARA naming conventions.
* takes in a  computer domain name and searches each letter to see if it meets the naming criteria, and returns true if valid and false if invalid.

### check_user_dn method
* This method utilizes the Regular expression package for comparing the user domain name to the acceptible ARA naming conventions.
* takes in a user domain name and searches each letter to see if it meets the naming criteria, and returns true if valid and false if invalid.
