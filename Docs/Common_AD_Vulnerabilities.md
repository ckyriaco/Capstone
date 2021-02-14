**Common Vulnerabilities within AD: Is there a preventative method?**

It seems a lot of vulnerabilities stem from how well AD is managed, such as:

If there are too many Domain Admins or signing in as admin for daily tasks when they should be signed in as users. Tasks should be performed with least privilege.

Do not use default settings such as default groups since some may have more access rights than needed.

Not monitoring and documenting access rights and group memberships.

Not removing inactive accounts.

Unpatched systems, such as workstations and servers.

Not running the most recent Windows OS version.

Domain Controllers not promptly patched.

[Most Common Active Directory Security Issues](https://adsecurity.org/?p=1684) 

Use GMSAs (Group Managed Service Accounts) wherever possible instead of regular user accounts because the passwords will automatically rotate.

[AD GMSAs](https://adsecurity.org/?p=4367 )

Old accounts with no expiration.

Use of legacy systems are vulnerable due to unpatched critical vulnerabilities.

Weak passwords such as plaintext and reused passwords.

[Seven Common Microsoft Active Directory Misconfigurations](https://www.ehackingnews.com/2021/02/seven-common-microsoft-active-directory.html)
