## ADaudit.py Documentation

_The ADaudit class allows administrators to query information to test active directory instances for CMMC compliance._
_The administrator? must already be joined to the active directory server's domain to use this class._
_A default domain can be set or a temporary external domain can also be set._

### Import
Import pyad, numpy, pyadutil and datetime

### Class ADaudit created - 
Tracks number of unused computers and unused user count  
**Variables created:**
* _unusedComputerCount_ -a count of the unused computers
* _unusedUserCount_ -a count of the unused users
* _unusedUsers_ - an array of the unused users
* _unusedComputers_ - an array of the unused computers
* _pwdLastSetDays_ - an array of users who haven't set their password in N days
* _admin list_ - an array of the admin for every admin type
* _serv man not set_ - an array of service accounts without the manager field set

### The constructor 
* Initializes an ADaudit object and validates pyads connection to Active Directory by locating a user account by a passed common name. 
* With this setup pyad checks the OS and makes sure you are already joined to the domain as a valid administrator user

**CN, or Common Name** is a variable that tracks user and pyad connection to active directory
* A user profile is retrieved using Common Name
* Makes sure that connection is actually happening

### set_CN setter method 
* Allows you to set a new common name and initialize a different user. 
* No getter needed in python
* All set methods are required 

### get_unused_users method 
* Returns the current object's list of unused users

### get_unused_computers method 
* Returns the current object's list of unused computers

### get_pwdLastSetNDays method 
* Returns the current object's list of users that haven't set their password in N days

### get_admin_list method 
* Returns a list of admin for every admin type

### get_serv_man_not_set method
* Returns a list of service accounts without the manager field set

### get_last_login_users method 
* Finds when users last logged in 
* Can feed array as parameter

### set_serve_manager_status method 
* Discovers all service accounts that do not have a manager attribute set

### get_last_user_login_list method 
* Takes in a distinguished name list 
* Looks at the distinguished name that it last looked at 
* Object category is the group of specific users that you want to query about 
* Makes sure that have actually logged on before 

### get_login_past_N_days method 
* Finds the users within a provided list that have not logged in N days 

### get_pwd_last_login_N_days method 
* Finds out when the users within the same distinguished name type, container and object category last set their password. 
* After get specific category, look at the specific login 

### get_All_Admin method
* Retrieves all administrators of specified administrator types
 
### admin_report method
* Returns a report of the administrator users of each administrator type
 
### get_unused_report method 
* Returns a report of the users and computers that have not logged in 

### get_pwd_report method 
* Returns a report on the users that have not changed their password in N days

### get_serv_man_not_set_report method 
* Returns a report of the service accounts that do not have a manager attribute set

### toString method 
* Prints an overall message on information found by querying through Active Directory
* To string method  prints out all info:  
* * List of Unused users
* * Count for Unused users
* * List of Unused computers
* * Count for Unused computers
* * Limit for the number of days allowed passwords must be changed??("PWD Unchanged Past Day Limit")

_End of class so ADaudit_

## Active_Directory_ARA.py Documentation

**Script** 

### Import ADaudit class 
* Allows functions from ADaudit class to be used
* Imported OS to gather variables from bash script 

### Take info from ADquery class
* Generates report based on users that have not logged in N number of days

### Import os variables plug into arrays based on variable types 

### Get number of days since last login 

## Ad_driver.sh Documentation
* Stores OS variables
* Executes active_directory_ARA.py

**Later activities**
* In bash directory made bash file executable 
* So it can be simply run through Gitbash
* (Bash terminal of choice)
