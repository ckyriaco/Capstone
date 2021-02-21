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
* re

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
* _admin_last_logon_ - An array of dates when admins last logged on
* _dn_status_ - An array of the statuses of distinguished names
* _dn_set_ - An array of accounts with set distinguished names
* _dn_not_set_ - An array of accounts without set distinguished names
* _validUsernames_ - An array of valid usernames
* _invalidUsernames_ - An array of invalid usernames
* _usersNeedUserNameCorr_ - An array of user accounts that need to reset their usernames 
* _servAccUserNameNeedChange_ - An array of service account users that need to reset their usernames
* _computerNameValid_ - An array of computers with valid names
* _computerNameInValid_ - An array of computers with invalid names
* _computerNeedNameChange_ - An array of computers with names that must be changed
* _pwd_exp_flag_false_ - An array of users with passwords that will never expire 
* _userNamesToBeApproved_ - An array of users with usernames that still need to be approved 
* _approvedUsernamesForChange_ - An array of users with changed usernames that have been approved
* _computerNamesToBeApproved_ - An array of computers with names that still need to be approved
* _approvedComputernamesForChange_ - An array of computers with changed names that have been approved
* _serviceAccountNamesToBeApproved_ - An array of service account users with usernames that still need to be approved
* _approvedServiceAccountNamesForChange_ - An array of service account users with changed usernames that have been approved 

### _init_ Constructor 
* Initializes an ADaudit object and validates pyad's connection to Active Directory by locating a user account via a passed Common Name. 
* With this setup pyad checks the OS and makes sure you are already joined to the domain as a valid administrator user.

### set_CN setter method 
* This method allows the administrator to set a new Common Name and initialize a different user. 
* All set methods are required.
* Has validation to enure the Common Name is not null.

### set_approvedUserNamesForChange method
* This method sets approved usernames for change.
* Updates the current object's approvedUserNamesForChange array.

### set_approvedComputerNamesForChange method
* This method sets approved computer names for change.
* Updates the current object's approvedComputerNamesForChange array.

### set_approvedServiceAccountNamesForChange method
* This method sets approved service account names for change.
* Updates the current object's approvedServiceAccountNamesForChange array.

### get_validUsernames method
* This method returns the current object's list of valid usernames.
* Returns a copy of the current object's validUserNames array.

### get_computerNeedNameChange method 
* This method returns the current object's list of computers with names that need to be changed.
* Returns a copy of the current object's computerNeedNameChange array.

### get_servAccUserNameNeedChange method
* This method returns the current object's list of service account users with usernames that need to be changed.
* Returns a copy of the current object's servAccUserNameNeedChange array.

### get_invalidUsernames method
* This method returns the current object's list of invalid usernames.
* Returns a copy of the current object's invalidUsernames array.

### get_pwd_exp_flag_false method 
* This method returns the current object's list of users with passwords that do not expire.
* Returns a copy of the current object's pwd_exp_flag_false array.

### get_unused_users method 
* This method returns the current object's list of unused users.
* Returns a copy of the current object's unusedUsers array.

### get_unused_computers method 
* This method returns the current object's list of unused computers.
* Returns a copy of the current object's unusedComputers array.

### get_pwdLastSetNDays method 
* This method returns the current object's list of users that haven't set their password in N days.
* Returns a copy of the current object's pwdLastSetNDays array.

### get_userNamesToBeApproved method
* This method returns the current object's list of users with changed usernames that still need to be approved.
* Returns a copy of the current object's userNamesToBeApproved array.

### get_computerNamesToBeApproved method
* This method returns the current object's list of computers with changed names that still need to be approved.
* Returns a copy of the current object's computerNamesToBeApproved array.

### get_serviceAccountNamesToBeApproved method 
* This method returns the current object's list of service account users with changed usernames that still need to be approved.
* Returns a copy of the current object's serviceAccountNamesToBeApproved array.

### get_admin_list method 
* This method returns a list of admin for every admin type.
* Returns a copy of the current object's admin_list array.

### get_serv_man_not_set method
* This method returns a list of service accounts without the manager field set.
* Returns a copy of the current object's serv_man_not_set array.

### get_admin_last_logon method 
* This method returns a list of last login information for each admin.
* Returns a copy of the current object's admin_last_logon array.

### get_dn_status method
* This method returns a list of users/computers and their distinguished name status.
* Returns a copy of the current object's dn_status array.

### get_dn_set method 
* This method returns a list of users with a distinguished name set
* Returns a copy of the current object's dn_set array.

### get_dn_not_set method 
* This method returns a list of users without a distinguished name set
* Returns a copy of the current object's dn_not_set array.

### get_usersNeedUserNameCorr method 
* This method returns a list of usernames who have users, computers, service accounts, etc. that need to be corrected.
* Returns a copy of the current object's usersNeedUserNameCorr array.

### get_last_login_users method 
* This method returns a list of when users last logged in to their accounts.
* Has validation to ensure array parameter is not empty.
* Prints a string of users and last login info.

### set_serve_manager_status method 
* This method discovers all service accounts that do not have a manager attribute set.
* Has validation to ensure distinguished name parameter is not empty.
* Updates the current object's serv_man_not_set array.

### get_last_user_login_list method 
* This method takes in a distinguished name list and looks at the distinguished name that was last looked at. 
* Gets a list of users that are within a container of a specific distinguished name nomenclature, are of a specific object category within that container, and have logged on before (can adjust this to find user accounts that have never been used as well).
* The generated list is designed to be passed into get_login_past_N_days special purpose function.
* The Object category is the group of specific users that the administrator wants to query about. 
* The method makes sure that the user has actually logged on before. 

### get_login_past_N_days method 
* This method finds the users within a provided list that have not logged in N days. 

### get_pwd_last_login_N_days method 
* This method finds out when certain users (within the same distinguished name type, container and object category) have last set their password. 
* After the method gets the specific category, it looks at the specific login. 

### get_All_Admin method
* This method retrieves all administrators of specified administrator types.
 
### get_All_Admin_CN method 
* This method returns a list of the Common Names(CNs) of all admin users

### get_admin_last_logon_info method 
* This method returns a list of last logon times for all admin users of a given type.

### distinguished_name_set method 
* This method checks that a distinguished name is set.

### check_pwd_expire method 
* This method checks that the DONT_EXPIRE_PASSWD flag is set to false.

### set_exp_flag method 
* This method sets the DONT_EXPIRE_PASSWD flag to false.

### check_username method 
* This method checks the usernames of the users with the container, and ensures they are valid.

### check_computer_name method 
* This method checks that the computer name is of a valid naming scheme for ARA standards.

### check_service_account_name method 
* This method checks the service accounts against the proper ARA naming scheme.

### autoChangeServiceAccountName method
* This method creates service account name suggestions.

### changeServiceAccountNames method 
* This method sets an approved service account name.

### findMatch method
* This method finds out if an account name is already in use.

### autoChangeUserName method 
* This method creates username suggestions.

### changeUsernames method 
* This method sets usernames that have just been approved.

### changeComputernames method 
* This method sets computer names that have just been approved.

### force_pwd_change method 
* This method forces a user to change their password.

### autoChangeComputerName method
* This method creates computer name suggestions.

### username_change_needed_report method
* This method generates a report on usernames that need to be changed.

### distinguished_name_report method
* This method generates a report of all distinguished name statuses and displays them for the admin.

### admin_report method
* This method returns a report of the administrator users of each administrator type.
 
### get_unused_report method 
* This method returns a report of the users and computers that have not logged in for the past N days. 
 
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