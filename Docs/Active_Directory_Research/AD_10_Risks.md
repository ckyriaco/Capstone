# AD_10_Risks #

- 1. ## Too many Administrators: ## If you have a long list of AD admin, then you most likely have given out execissive levels of privileges to accounts.
  - ## Solution: ## Only give admin privileges to those who absolutely need them.
- 2. ## Delegating Too Many Tasks in Active Directory: ## Delegating too many tasks to non-administrators, without proper evaluation and tracking, is a big risk!
  - ## Solution: ## Be very selective with who a task is delegated to.
- 3. ## Short and Simple Passwords: ## They are easy to remember, but they are also easy to guess.
  - ## Solution: ## Use stringent password policies and force users to adopt them. Force password changes every 90-180 days.
- 4. ## Leaving Inactive Accounts: ## Having inactive accounts increases the risk of a breach and information being compromised; especially those with administrative privileges.
  - ## Solution: ## Deactivate inactive accounts
- 5.## Increasing Open Access: ## It's good if Open Access is given to vetted users that need it, but make sure guests and anonymous accounts don't have the same freedom!
  - ## Solution: ## Make sure only authorized users have Open Access privileges.
- 6.## Not Knowing Who's Logging in to Your Domain Controllers: ##If you don't keep track of who is logging into the Domain Controllers, it's difficult to protect privileged identities and vital information. It also creates a blind spot that isn't accounted for.
  - ## Solution: ## A continuous and proactive way of keeping track of logins to the domain controller, so that the anomalies can be caught quickly.
- 7.## Relaxed Password Policies:## Password policies should not be compromised on, otherwise your server and the network it is running and/or runs on is at risk of being compromised.
  - ## Solution: ## Ensure that password policies are stringent and that users are educated on why the passwords must be stringent in the first place.
- 8.## Not Knowing the Members of Sensitive Security Groups: ##The members of these groups have the highest levels of privileges. If the credentials to an account with these privileges are stolen, it can be very damaging for your organization's security.
  - ## Solution: ## Note all that have are part of security groups, only grant membership to those accounts that need it and withdraw group membership the minute they are no longer required.
- 9. ## Unaware of Permission Inheritance in Group Nesting: ##When a group is added as a member of an admin group, all members of that group will receive admin priveleges. This is because AD nested groups are based on parent-child hierarchy.
  - ## Solution: ## Track all group nesting and what privileges are passed to who.
- 10.## Not Implementing Least Privilege Policy Models: ##Users should only have the absolute minimum permissions required for their job. If they have more than they require, it causes an unnecessary risk.
  - ## Solution: ## Consistently track changes to privileges to ensure that the right users have the right levels of access to the right data.

- For more information: [Top 10 Risks to Active Directory Servers](https://www.lepide.com/blog/top-10-risks-to-active-directory-security/)
