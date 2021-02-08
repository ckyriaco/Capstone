## Active Directory Common Vulnerabilities
* System Vulnerablilities
    * Related to Kerberos Authentication
        * Kerberoasting attack on service accounts (weak passwords)
    * Related to NTLM Encryption
    * Brute Force Attacks
    * Passwords  are store using reversible encryption
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
    * 

_In Progress_

### Sources:
* [Active Directory Security Best Practices](https://www.lepide.com/blog/active-directory-security-best-practices/#:~:text=Active%20Directory%20System%20Vulnerabilities%20Active%20Directory%20uses%20Kerberos,actually%20used%20in%20AD%2C%20despite%20security%20being%20subpar.)
* [Top 16 Active Directory Vulnerabilities](https://www.infosecmatter.com/top-16-active-directory-vulnerabilities/)