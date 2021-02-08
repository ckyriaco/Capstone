## Active Directory Common Vulnerabilities
* System Vulnerablilities
    * Related to Kerberos Authentication
        * Kerberoasting attacks on service accounts (weak passwords)
        * AS-REP roasting attacks on accounts that do not require Kerboros pre-authentication
    * Related to NTLM Encryption
        * Passwords are stored using depreciated LM hashes
    * Brute Force Attacks
    * Passwords are stored using reversible encryption
    * Policies for creating domain passwords are weak
    * **Having unused domain accounts**
    * **Having privileged accounts with unchanged passwords for a year or more** (Vulnerable to brute force attack)
    * Storing user credentials in Group Policy folders accessible to all authenticated users
* Insider Threats
    * Phishing attacks
    * Social engineering
    * Spear-phishing
* Excessive Permissions
    * Giving users permission to add computers to domain
    * Giving users unnecessarily high privileges with the AdminCount attribute
    * Having an excessively high number of users in certain privileged groups like Domain Admins
    * Having easy-to-compromise service accounts with Domain Admin privileges  
    * Having users with so many Active Directory and Extended Rights that they can be considered shadow Domain Admins
    *  Having users with passwords that never expire
    * Having users with no password requirements at all
    * Having users with weak passwords possibly in spite of strong corporate password policy

### Sources:
* [Active Directory Security Best Practices](https://www.lepide.com/blog/active-directory-security-best-practices/#:~:text=Active%20Directory%20System%20Vulnerabilities%20Active%20Directory%20uses%20Kerberos,actually%20used%20in%20AD%2C%20despite%20security%20being%20subpar.)
* [Top 16 Active Directory Vulnerabilities](https://www.infosecmatter.com/top-16-active-directory-vulnerabilities/)