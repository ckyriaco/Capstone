## Active Directory Vulnerabilities 

* #### Weak domain password policy
   * Passwords in AD must be enforced with long and complex passwords, following criteria such as:
      * Minimum password length: 14
      * Enforce password history: 24
      * Maximum password age: 60 or fewer days
      * Minimum password age: 1 or more
* #### Users being able to add computers to the domain
    * In a default installation of AD, any domain user can add workstations to the domain - any low privileged domain user can join up to 10 computers to the domain. This brings up the issue that any user is allowed to join their own, unmanaged computer to access the corporate domain with advantages like
      * No antivirus will be pushed into their machine
      * No GPO settings or policies will be applied to their system
      * Allows them having Administrative rights on their system
    * Can be resolved by ensuring that normal domain users do not have the privilege of adding other computers to the domain
* #### AD Buffer Overflow Vulnerability 
   * The LDAP service in AD, ADAM, AD LDS, and Active Directory Services allows remote attackers to cause a denial of service (memory consumption and service outage) via a crafted query - Memory Consumption Vulnerability
   * Can be resolved via Microsoft update
* #### Service accounts being members of Domain Admins
   * A service account designates a specific user account with specific set of privileges to run a specific service / application without requiring full admin privileges. If these accounts are assigned extra privileges and / or memberships such as being added to the "Domain Admins" group, there runs a risk that if the service account gets compromised, attackers could have full control over the AD domain, as these service accounts usually have passwords set to never expire, so passwords are rarely if ever changed.
* #### Service accounts that are vulnerable to Kerberoasting
  * Kerberoasting is a pervasive attack technique that targets AD service account credentials. It is a post-exploitation attack that extracts service account credential hashes from AD for offline cracking. It is effective because the attacker doesn't require domain administrator credentials to successfully attack and can extract service account credential hashes without sending packets to the target.
  * Can defend against this attack by setting trap accounts in the AD environment known as "honey accounts" that act as dummy service accounts which when compromised trigger an alert if they are used to login or generate a service ticket request
  * Can utilize monitoring tools for telltale signs of Kerberoasting attacks
* #### Inactive domain accounts
  * Having unused domain accounts in the domain increases attack surface of the organization, as it provides the opportunity to compromise these accounts
  * Can be resolved by establishing a policy to disable or delete these accounts based on periodic checks, such as 30 days of inactivity.
* #### Storing passwords using LM hashes
  * LM hash is an old, deprecated method of storing passwords with the following weaknesses:
    * Password length is limited to 14 characters
    * Passwords longer than 7 characters are split in two, and each half is hashed separately
    * All lower-case characters are converted to upper-case before hashing
  * These weaknesses cause LM hashes to be extremely easy to crack, and any privileged insiders, such as domain administrators, can crack them and obtain plaintext passwords
  * Can be resolved by utilizing stronger hashes, such as NTLM.
* #### Service accounts vulnerable to AS-REP roasting
  * This vulnerability is similar to Kerberoasting, but here the attack abuses user accounts that do not require Kerberos pre-authentication, specifically affecting domain users with the DONT_REQ_PREAUTH flag set. Without this preauthentication, hackers can easily request a piece of encrypted information for these accounts and efficiently crack the material offline, revealing the user's password.
  * Can be resolved by ensuring DONT_REQ_PREAUTH is not set for the AD builds with the option available.
