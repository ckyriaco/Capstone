"""
ou = pyad.adcontainer.ADContainer.from_dn("ou=All_Users, dc=LIFEALIKE, dc=LAB")
new_user = pyad.aduser.ADUser.create("test.02", ou, password="password")
"""

import re

def check_username(samAccount, cn):
    # Python program to validate an Ip address

    # Make a regular expression
    # for validating an Ip-address
    #regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    names = cn.split()
    fname = names[0]
    mname = names[1]
    lname = names[2]
    init = fname[0].lower()
    init2 = init
    init2 += mname[0].lower()
    init3 = init
    init3 += fname[1]
    init3 += mname[0]
    regex = "["+ init + "-"+init3+"]+[a-zA-Z]"
    # Define a function for
    # validate an Ip address

    # pass the regular expression
    # and the string in search() method

    if (re.search(regex, samAccount)):
        return True

    else:
        return False

def check_service_account_name(service_account, OU):
    # Python program to validate an Ip address

    # Make a regular expression
    # for validating an Ip-address
    #regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    regex = OU + "+-+[a-zA-Z]"
    # Define a function for
    # validate an Ip address

    # pass the regular expression
    # and the string in search() method

    if (re.search(regex, service_account)):
        return True

    else:
        return False

def check_computer_name(name):
    # Python program to validate an Ip address

    # Make a regular expression
    # for validating an Ip-address
    #regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    regex = "[a-zA-Z]+-+[pc-lap]"
    regex2 = "[a-zA-Z]+-+[a-zA-Z]+-+[pc-lap]"
    # Define a function for
    # validate an Ip address

    # pass the regular expression
    # and the string in search() method

    if (re.search(regex, name) or re.search(regex, name)):
        return True

    else:
        return False



def check_dn_Computer(dn):
    # Python program to validate an Ip address

    # Make a regular expression
    # for validating an Ip-address
    #regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    regex = "CN=[a-zA-Z]+-+[pc-lap]+,CN=[a-zA-Z]+,DC=[a-zA-Z]+,DC=+[a-zA-Z]"
    regex2 = "CN=[a-zA-Z]+-+[a-zA-Z]+-+[pc-lap]+,CN=[a-zA-Z]+,DC=[a-zA-Z]+,DC=+[a-zA-Z]"
    # Define a function for
    # validate an Ip address

    # pass the regular expression
    # and the string in search() method

    if (re.search(regex, dn) or re.search(regex2, dn)):
        return True

    else:
        return False

def check_user_dn(dn):
    # Python program to validate an Ip address

    # Make a regular expression
    # for validating an Ip-address
    #regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
             #25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    regex = "CN=+[a-zA-Z]+ +[a-zA-Z]+,CN=[a-zA-Z]+,DC=[a-zA-Z]+,DC=[a-zA-Z]"

    # Define a function for
    # validate an Ip address

    # pass the regular expression
    # and the string in search() method

    if (re.search(regex, dn)):
        return True

    else:
        return False


check = check_dn_Computer("CN=nl-nflap-pc,CN=Users,DC=KTG,DC=local")

check2 = check_user_dn("CN=Christopher Kyriacou,CN=Users,DC=KTG,DC=local")

check3 = check_username('chmkyriacou', "Christopher Michael Kyriacou")

check4 = check_service_account_name("corp-backup", "corp")

check5 = check_computer_name('corp-nflap-pc')

print(check)

print(check2)

print(check3)

print(check4)

print(check5)