## Active Directory Vulnerabilities 

* #### Weak Domain password policy
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
* #### AD Buffer Overflow Vulnerability 
   * The LDAP service in AD, ADAM, AD LDS, and Active Directory Services allows remote attackers to cause a denial of service (memory consumption and service outage) via a crafted query - Memory Consumption Vulnerability
* #### Not isolating DCs and other critical systems
   * Can resolve by placing DAs and services with privileged access to DAs in Control Zone
* #### Service accounts being members of Domain Admins
   * A service account designates a specific user account with specific set of privileges to run a specific service / application without requiring full admin privileges. If these accounts are assigned extra privileges and / or memberships such as being added to the "Domain Admins" group, there runs a risk that if the service account gets compromised, attackers could have full control over the AD domain, as these service accounts usually have passwords set to never expire, so passwords are rarely if ever changed.

