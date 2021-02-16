# Security Vulnerabilities in Active Directory.

## Permission Inheritance in Group Nesting

Active Directory nests groups are based on a parent-child hierarchy. When a group is added as a member of an administrative group, all members of that group will receive administrative privileges. This could potentially mean unauthorized personnel getting access to sensitive data. We should scan groups for admin privileges, from what I heard at the last meeting the number should be near zero, but a audit script should include a check for that. 

-Dave.


