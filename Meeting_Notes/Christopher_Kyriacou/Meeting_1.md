# Meeting 1 #

### Regulation to comply with: CMMC Certification ###
	- NIST 800-171 and a few extra extensive. 
	- ARA configurations do not line up 100% with things provided with 
	- We use Tenable security center
	- Qualys maybe the next system used

Current system: Manual

 ### Desired System: Automated OO script or other possible tool ###

AD is set up where we have users in 1 of 2 major areas, 1 is us.ara.com, 2 is restrict.ara.com (where restricted people go) , admin.ara.com (corporate IT/sysadmin)
RBAC through AD groups, then that group has access to the disc center. 
Proposed procedures that are to be automated:
Use RSA as a multifactor authentication
The current tokens are expiring. 
Alarms go off when servers use stuff from Russia and China. Be able to reach out to a running system and say who is communicating. 
Using kerberos

# Task List: #
	- Using AD to identify computers, verify that the computer has a distinct name, the name follows the convention, and it requires the user to log in.
	- List the users and computers in AD who have not logged in in N days.
	- Produce a list of users who have not changed their password in N days.
	- Produce a list of users in a given AD section (i.e., restrict.ara.com) who have administrative privileges
	- For service accounts, ensure that the “manager” field is filled out.  A question is how to identify service accounts.  There is a naming convention, but we do not know if it is followed (another audit requirement).
	- For all accounts, the “password expire” flag is set.  More specifically, which accounts do not have this set?
	- Write a PowerShell script that uses Windows Sysinternals tool(s) on a remote system to monitor for what process is communicating with a given IP and/or port.  As much detail about the process as can be found should be reported.  Install sysinternals on the remote computer if needed.  Using psexec is OK.  This is probably the top priority.
