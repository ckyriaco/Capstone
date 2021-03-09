# Prototype Status #

## Original functions Checklist: [7/7] ##

- [X] Using AD to identify computers, verify that the computer has a distinct name, the name follows the convention, and it requires the user to log in. 
- [X] List the users and computers in AD who have not logged in in N days. 
- [X] Produce a list of users who have not changed their password in N days. 
- [X] Produce a list of users in a given AD section (i.e., restrict.ara.com) who have administrative privileges. 
- [X] For service accounts, ensure that the “manager” field is filled out. A question is how to identify service accounts. There is a naming convention, but we do not know if it is followed (another audit requirement). 
- [X] For all accounts, the “password expire” flag is set. More specifically, which accounts do not have this set? 
- [X] Write a script that uses Windows Sysinternals tool(s) on a remote system to monitor for what process is communicating with a given IP and/or port. As much detail about the process as can be found should be reported. Install sysinternals on the remote computer if needed. Using psexec is OK. This is probably the top priority.

## Additions to functions [3/3] ## 
- [X] Add the time it's been since an admin has signed on to the reporting of the last time an admin signed on.
- [X] Add Markdown report generation.
- [X] Add imporvements to Markdown report.
