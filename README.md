# Capstone
Active Directory Auditing for Cybersecurity Maturity Model Certification (CMMC) Compliance

Main Goal:

The goal of this project is to create an auditing system that allows authorized security admin at the Applied Research Associates (ARA) 
to audit their active directory servers to ensure CMMC compliance. This process should be easily automated by being initiated as a task within any automation pipeline
that ARA prefers.


Functionality list to reach our main goal:
1. Using AD to identify computers, verify that the computer has a distinct name, the name follows the convention, and it requires the user to log in.
2. List the users and computers in AD who have not logged in in N days.
3. Produce a list of users who have not changed their password in N days.
4. Produce a list of users in a given AD section (i.e., restrict.ara.com) who have administrative privileges
5. For service accounts, ensure that the “manager” field is filled out.  A question is how to identify service accounts.  There is a naming convention, but we do not know if it is followed (another audit requirement).
6. For all accounts, the “password expire” flag is set.  More specifically, which accounts do not have this set?
7. Write a script that uses Windows Sysinternals tool(s) on a remote system to monitor for what process is communicating with a given IP and/or port.  As much detail about the process as can be found should be reported.  Install sysinternals on the remote computer if needed.  Using psexec is OK.  This is probably the top priority.

Audit Process (End-Goal)

1. Automation environment of choice initiates a bash script to pass credentials and variables, requried by the procedural python script, then executes the python script.
2. Domain Admin User establishes connection with an Active Directory Domain Controller.(Must be on end-unit that is joined with the Active Directory Server Domain of interest)
3. The python script attempts to retrieves all information requested using the customized class that utilizes the pyad 0.6.0 package.
4. If the audit succeeded, it will be indicated if the Domain(s) are compliant or not. If it is unsuccessful because of an error, a restart will be triggered up to 3 times before indicating a ticket for an Admin to take a look into the error. 

![](Diagrams/Audit_Process_1.png)
