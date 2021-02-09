# Meeting Feb 04 #

## Demo of Current Prototype ##
- Demonstration was a success.
- Wants additional information on administrators and when their last logon was.
- Wants names of Users, Admin, and computers as follows:

  - Human naming:
    - Standard format of first initial, last name should be used for the username.  If someone already has that username, include the user's middle initial.  If both are taken, use first initial and second initial and then last name.  And so on.  So, for example Jason P. Doe.  If jdoe and jpdoe are taken we are to go with jadoe and then jasdoe, etc.


  - Service account naming:
    - Use proper naming convention when creating the account. For example, a backup account for the Corp top-level OU would be called corp-backup. An Anti-virus account for the RMD top-level OU would be called RMD-AntiVirus.  Put the word "service" (case-insensitive) in the Description field.  Use the Manager field on the Organization tab to denote the person responsible for the service account.   'Password does not expire' flag should NOT be set.


  - Computer naming:
    - Since each computer object in AD must be unique, it is important to follow good naming convention when creating computer accounts. Computer names should be prefixed with the name of the top-level OU (or Division name) at the minimum. This prevents a computer with the same name from being joined to the domain and causing a collision. We also recommend using either "pc" or "lap" as a suffix to distinguish between a desktop PC and a laptop. 
    - A good overall convention is:  division abbreviation - user initials - pc/lap. For example, my laptop is named hq-nflap. hq-nf-lap, corp-nflap, or corp-nf-lap are all also acceptable. Keeping good naming convention can ease management of co

![](../CMMC_Lvl1_Req.png)
