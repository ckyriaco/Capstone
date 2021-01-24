# Capstone
Active Directory Auditing for Cybersecurity Maturity Model Certification (CMMC) Compliance

Main Goal:

The goal of this project is to create an auditing system that allows authorized Security Admin at the Applied Research Associates (ARA) 
to audit their active directory servers to ensure CMMC compliance.


Functionality list to reach our main goal:
1. Using AD to identify computers, verify that the computer has a distinct name, the name follows the convention, and it requires the user to log in.
2. List the users and computers in AD who have not logged in in N days.
3. Produce a list of users who have not changed their password in N days.
4. Produce a list of users in a given AD section (i.e., restrict.ara.com) who have administrative privileges
5. For service accounts, ensure that the “manager” field is filled out.  A question is how to identify service accounts.  There is a naming convention, but we do not know if it is followed (another audit requirement).
6. For all accounts, the “password expire” flag is set.  More specifically, which accounts do not have this set?
7. Write a script that uses Windows Sysinternals tool(s) on a remote system to monitor for what process is communicating with a given IP and/or port.  As much detail about the process as can be found should be reported.  Install sysinternals on the remote computer if needed.  Using psexec is OK.  This is probably the top priority.

Audit_Process

[Audit_Process_1.png](Diagrams/Audit_Process_1.png)
