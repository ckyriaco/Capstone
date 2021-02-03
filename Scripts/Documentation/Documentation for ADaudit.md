## ADaudit.py Documentation

_This class is designed to allow administrators to query information to test Active Directory instances for CMMC compliance._
_The administrator must already be joined to the Active Directory server's domain to use this class._
_A default domain or an temporary external domain can also be set._

### Import 
* pyad 
* numpy as np
* pyadutils from pyad
* datetime from datetime
* simplefilter from warnings

### Initialize simplefilter
* This filter is set to catch warnings to allow code to continue.

### Class ADaudit created 
* Tracks the number of unused computers and the unused user count. 
**Variables created:**
* _CN_ - The Common Name identifier
    * **CN, or Common Name** is a variable that tracks user and pyad connection to Active Directory and helps the administrator make sure that the connection is actually happening.   
* _user_ - The user object.  
    * A user profile is retrieved using Common Name.  
* _unusedComputerCount_ - A count of the unused computers
* _unusedUserCount_ - A count of the unused users
* _unusedUsers_ - An array of the unused users
* _unusedComputers_ - An array of the unused computers
* _pwdLastSetDays_ - An array of users who haven't set their password in N days
* _admin list_ - An array of the admin for every admin type
* _serv man not set_ - An array of service accounts without the manager field set

### The Constructor 
* Initializes an ADaudit object and validates pyads connection to Active Directory by locating a user account via a passed Common Name. 
* With this setup pyad checks the OS and makes sure you are already joined to the domain as a valid administrator user.

### set_CN setter method 
* This method allows the administrator to set a new Common Name and initialize a different user. 
* All set methods are required.

### get_unused_users method 
* This method returns the current object's list of unused users.

### get_unused_computers method 
* This method returns the current object's list of unused computers.

### get_pwdLastSetNDays method 
* This method returns the current object's list of users that haven't set their password in N days.

### get_admin_list method 
* This method returns a list of admin for every admin type.

### get_serv_man_not_set method
* This method returns a list of service accounts without the manager field set.

### get_last_login_users method 
* This method finds when users last logged in and can feed an array as a parameter.

### set_serve_manager_status method 
* This method discovers all service accounts that do not have a manager attribute set.

### get_last_user_login_list method 
* This method takes in a distinguished name list and looks at the distinguished name that was last looked at. 
* The Object category is the group of specific users that the administrator wants to query about. 
* The method makes sure that the user has actually logged on before. 

### get_login_past_N_days method 
* This method finds the users within a provided list that have not logged in N days. 

### get_pwd_last_login_N_days method 
* This method finds out when certain users (within the same distinguished name type, container and object category) have last set their password. 
* After the method gets the specific category, it looks at the specific login. 

### get_All_Admin method
* This method retrieves all administrators of specified administrator types.
 
### admin_report method
* This method returns a report of the administrator users of each administrator type.
 
### get_unused_report method 
* This method returns a report of the users and computers that have not logged in. 

### get_pwd_report method 
* This method returns a report on the users that have not changed their password in N days.

### get_serv_man_not_set_report method 
* This method returns a report of the service accounts that do not have a manager attribute set.

### toString method 
* This method prints an overall message on information found by querying through Active Directory.
* The toString method prints out the following info:  
    * List of Unused users
    * Count for Unused users
    * List of Unused computers
    * Count for Unused computers
    * List of users who have not changed their passwords in N days 