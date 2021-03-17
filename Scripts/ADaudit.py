
#This class is designed to allow administrators to query information that are vital for cmmc compliance audits of active directory instances.
#Must already be joined to the active directory server's domain to use this class!
#Can set a default domain manually using pyad.set_defaults(ldap_server="dc1.domain.com", username="service_account", password="mypassword").
#Setting the default domain manually is not recommended due to the fact that joining the domain and authenticating through Windows Operating Systems on the end-unit is more secure.
#Can connect to a specific other domain temporarilty instead of the default using user = aduser.ADUser.from_cn("myuser", options=dict(ldap_server="dc1.domain.com"))
#Reusable functions for the previous two notes can be formed to support mass iteration through various domains if requrested. 


from pyad import *
import numpy as np
import pyad.pyadutils as py
from datetime import datetime
from warnings import simplefilter
import re
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.rl_config import *
from io import StringIO

simplefilter(action='ignore', category=FutureWarning)

class ADaudit:
    CN = ""
    user = ""
    unusedComputerCount = 0
    unusedUserCount = 0
    unusedUsers = np.array([])
    unusedComputers = np.array([])
    pwdLastSetNDays = np.array([])
    admin_list = np.array([])
    serv_man_not_set = np.array([])
    admin_last_logon = np.array([])
    dn_status = np.array([])
    dn_set = np.array([])
    dn_not_set = np.array([])
    validUsernames = np.array([])
    invalidUsernames = np.array([])
    usersNeedUserNameCorr = np.array([])
    servAccUserNameNeedChange = np.array([])
    computerNameValid = np.array([])
    computerNameInValid = np.array([])
    computerNeedNameChange = np.array([])
    pwd_exp_flag_false = np.array([])
    userNamesToBeApproved = np.array([])
    approvedUsernamesForChange = np.array([])
    computerNamesToBeApproved = np.array([])
    approvedComputernamesForChange = np.array([])
    serviceAccountNamesToBeApproved = np.array([])
    approvedServiceAccountNamesForChange = np.array([])
    userDaysUnused = np.array([])
    computerDaysUnused = np.array([])
    df_user_username = ""
    df_serv_username = ""
    df_computer_username = ""
    df_dn_status = ""
    df_admin_list = ""
    df_admin_last_logon = ""
    df_unusedUsers = ""
    df_unusedComputers = ""
    df_pwdLastSetNDays = ""
    df_pwd_exp_flag_false = ""
    df_serv_man_not_set = ""

    #This constructor initialzes an ADquery object and validates pyad's connection to AD by locating a user account by a passed common name.
#Will add extra validation to this constructor for final product.
    def __init__(self, CN):
        if(CN != ""):
            self.CN = CN
            self.user = aduser.ADUser.from_cn(CN)
        else:
            raise ValueError("The Common Name cannot be null!")

#Allows you to set a new cn and initialize a different user.
    def set_CN(self, CN):
        if (CN != ""):
            self.CN = CN
            self.user = aduser.ADUser.from_cn(CN)
        else:
            raise ValueError("The Common Name cannot be null!")

#Set approved usernames for change
    def set_approvedUserNamesForChange(self, array):
        self.approvedUsernamesForChange = array

    # Set approved computer names for change
    def set_approvedComputerNamesForChange(self, array):
        self.approvedComputernamesForChange = array

    # Set approved service account names for change
    def set_approvedServiceAccountNamesForChange(self, array):
        self.approvedServiceAccountNamesForChange = array


#Returns the array of valid usernames
    def get_validUsernames(self):
        array = np.array([])
        for i in self.validUsernames:
            array = np.append(array, i)
        return array

#Returns array of users that have a computer names that need to be changed
    def get_computerNeedNameChange(self):
        array = np.array([])
        for i in self.computerNeedNameChange:
            array = np.append(array, i)
        return array

#Returns array of service accounts that need their usernames changed
    def get_servAccUserNameNeedChange(self):
        array = np.array([])
        for i in self.servAccUserNameNeedChange:
            array = np.append(array, i)
        return array

#Returns array of invalid usernames
    def get_invalidUsernames(self):
        array = np.array([])
        for i in self.invalidUsernames:
            array = np.append(array, i)
        return array

#Returns the users that have accounts that do not expire.
    def get_pwd_exp_flag_false(self):
        array = np.array([])
        for i in self.pwd_exp_flag_false:
            array = np.append(array, i)
        return array

#Return the current object's list of unused users
    def get_unused_users(self):
        array = np.array([])
        for i in self.unusedUsers:
            array = np.append(array, i)
        return array

#Return the current object's list of unused computers
    def get_unused_computers(self):
        array = np.array([])
        for i in self.unusedComputers:
            array = np.append(array, i)
        return array

#Return the current object's list of users that haven't set their password in N days
    def get_pwdLastSetNDays(self):
        array = np.array([])
        for i in self.pwdLastSetNDays:
            array = np.append(array, i)
        return array

#Returns array of usernames that need approval
    def get_userNamesToBeApproved(self):
        array = np.array([])
        for i in self.userNamesToBeApproved:
            array = np.append(array, i)
        return array

#Returns array of computer names that need approval
    def get_computerNamesToBeApproved(self):
        array = np.array([])
        for i in self.computerNamesToBeApproved:
            array = np.append(array, i)
        return array

#Returns an array of service account names that need approval
    def get_serviceAccountNamesToBeApproved(self):
        array = np.array([])
        for i in self.serviceAccountNamesToBeApproved:
            array = np.append(array, i)
        return array

    #Return the list of admin for every admin type
    def get_admin_list(self):
        array = np.array([])
        for i in self.admin_list:
            array = np.append(array, i)
        return array

    #Return the list of service accounts without the manager field set.
    def get_serv_man_not_set(self):
        array = np.array([])
        for i in self.serv_man_not_set:
            array = np.append(array, i)
        return array

    #Return the list of admin last logon information.
    def get_admin_last_logon(self):
        array = np.array([])
        for i in self.admin_last_logon:
            array = np.append(array, i)
        return array

    #Return the list of users/computers and their dn status
    def get_dn_status(self):
        array = np.array([])
        for i in self.dn_status:
            array = np.append(array, i)
        return array

    #Returns those with a dn set
    def get_dn_set(self):
        array = np.array([])
        for i in self.dn_set:
            array = np.append(array, i)
        return array

    #Return those without a dn set
    def get_dn_not_set(self):
        array = np.array([])
        for i in self.dn_not_set:
            array = np.append(array, i)
        return array

#Returns array of usernames that need correction for users, computers, service accounts, etc.
    def get_usersNeedUserNameCorr(self):
        array = np.array([])
        for i in self.usersNeedUserNameCorr:
            array = np.append(array, i)
        return array



    #Finds the last time a list of users each last logged on to their accounts.
    def get_last_login_users(self, array):
        emptyArray = np.array([])
        if(len(array) == 0 or array == ""):
            raise ValueError("The array cannot be empty!")
        for i in array:
            x = aduser.ADUser.from_cn(i)
            print(i, x.get_last_login())

#Discover all service accounts that do not have a manager attribute set.
    def set_serve_manager_status(self, dn):
        if(dn == ""):
            raise ValueError("The distinguished name cannot be null!")
        else:
            con = pyad.adcontainer.ADContainer.from_dn(dn)

            for i in con.get_children():
                manager = i.get_attribute("manager")
                CN = i.get_attribute("CN")
                if len(manager) == 0:
                    self.serv_man_not_set = np.append(self.serv_man_not_set, CN)



#Get a list of users that are within a container of a specific distinguished name nomenclature, are of a specific object category within that container, and have logged on before (can adjust this to find user accounts that have never been used as well).
#The generated list is designed to be passed into get_login_past_N_days special purpose function.

    def get_last_user_login_list(self, dn, objCat):
        if(dn == "" or objCat == ""):
            raise ValueError("The distinguished name and object category cannot be null!")
        else:
            con = pyad.adcontainer.ADContainer.from_dn(dn)
            array = np.array([])
            for obj in con.get_children():
                c = obj.get_attribute("CN")
                d = obj.get_attribute("objectCategory")
                c = str(c[0])
                d = str(d[0])
                if (d == objCat):
                    array = np.append(array, c)
            array2 = np.array([])
            for i in array:

                u = aduser.ADUser.from_cn(i)
                e = u.get_attribute("CN")
                e = str(e[0])

                b = u.get_allowed_attributes()
                if ('logonCount' in b):
                    v = u.get_attribute("logonCount")
                    g = v[0]
                    if (v[0] > 0):
                        str(i)
                        array2 = np.append(array2, e)
            return array2

#Find the users, within a provided list, that have not logged on in N days.
    def get_login_past_N_days(self, N, array, type):
        Allowed_Types = np.array(["Computer", "User"])
        if(len(array) == 0 or type not in Allowed_Types):
            raise ValueError("The array cannot be empty and the type must be either 'Computer' or 'User'")
        else:
            now = datetime.now()
            dt = now.strftime("%Y-%m-%d %H:%M:%S")
            currentDate = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
            array2 = np.array([])
            for i in array:
                x = aduser.ADUser.from_cn(i)
                z = x.get_last_login()
                z = str(z)
                y = datetime.strptime(z, "%Y-%m-%d %H:%M:%S")
                diff = abs((currentDate - y).days)
                if(diff >= N):
                    array2 = np.append(array2, [i, diff])
                    if(type == "Computer"):
                        self.unusedComputerCount += 1
                        self.unusedComputers = np.append(self.unusedComputers, i)
                        self.computerDaysUnused = np.append(self.computerDaysUnused, diff)
                    elif(type == "User"):
                        self.unusedUserCount += 1
                        self.unusedUsers = np.append(self.unusedUsers, i)
                        self.userDaysUnused = np.append(self.userDaysUnused, diff)


#Find out when all users of a specific object category, within a container under a specific distinguished name type, last set their #password.
    def get_pwd_last_login_N_days(self, dn, objectCategory, N):
        if(dn == "" or objectCategory == "" or N == "" or N < 1):
            raise ValueError("The distinguished, object category and number of days cannot be null!"
                             "\nThe number of days cannot be less than one!")
        else:
            container = adcontainer.ADContainer.from_dn(dn)
            for obj in container.get_children():
                now = datetime.now()
                dt = now.strftime("%Y-%m-%d %H:%M:%S")
                currentDate = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                c = obj.get_attribute("CN")
                d = obj.get_attribute("objectCategory")
                c = str(c[0])
                d = str(d[0])
                e = aduser.ADUser.from_cn(c)
                if (d == objectCategory):
                    f = e.get_password_last_set()
                    f = str(f)
                    y = datetime.strptime(f, "%Y-%m-%d %H:%M:%S")
                    diff = abs((currentDate - y).days)
                    if (diff >= N):
                        self.pwdLastSetNDays = np.append(self.pwdLastSetNDays, c)

#Retrieve all admin of specified admin types
    def get_All_Admin(self, Admin_Types):
        if(len(Admin_Types) == 0):
            raise ValueError("The Admin_Types array cannot be empty!")
        else:
            for i in Admin_Types:
                user = aduser.ADUser.from_cn(i)
                l = user.get_attribute("member")
                addition = ("{}| ").format(i)
                for x in l:
                    addition += ("{}-").format(x)
                    addition = addition.replace("[", "")
                    addition = addition.replace("]", "")
                    addition = addition.replace("'", "")
                    print(addition)
                self.admin_list = np.append(self.admin_list, addition)

#Get all the cn's of all admin users
    def get_All_Admin_CN(self, Admin_Types):
        array = np.array([])
        if (len(Admin_Types) == 0):
            raise ValueError("The Admin_Types array cannot be empty!")
        else:

            for i in Admin_Types:
                user = aduser.ADUser.from_cn(i)
                l = user.get_attribute("member")
                for x in l:
                    c = aduser.ADUser.from_dn(x)
                    c = c.get_attribute("CN")
                    if (c[0] not in array):
                        array = np.append(array, c)
        return array

#Get the last logon time for all admin of the given types.
    def get_admin_last_logon_info(self, Admin_Types):
        if(len(Admin_Types) == 0):
            raise ValueError("The admin types cannot be null!")
        else:
            admin = self.get_All_Admin_CN(Admin_Types)
            report = np.array([])
            now = datetime.now()
            dt = now.strftime("%Y-%m-%d %H:%M:%S")
            currentDate = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
            for i in admin:
                user = aduser.ADUser.from_cn(str(i))
                logon = user.get_last_login()
                f = str(logon)
                y = datetime.strptime(f, "%Y-%m-%d %H:%M:%S")
                diff = abs((currentDate - y).days)
                message = ("{},{},{} ").format(i, logon, diff)
                self.admin_last_logon = np.append(self.admin_last_logon, message)

#Check that a dn name is set
    def distinguished_name_set(self, dn):
        if(dn == ""):
            raise ValueError("The distinguished name cannot be null!")
        else:
            con = adcontainer.ADContainer.from_dn(dn)
            for i in con.get_children():
                cn = i.get_attribute("CN")
                print(cn[0])
                user = aduser.ADUser.from_cn(cn[0])
                c = user.get_allowed_attributes()
                message = ""
                if ("distinguishedName" in c):
                    x = user.get_attribute("distinguishedName")
                    message = ("{} | {} | {}").format(cn[0], "Yes", x[0])
                    self.dn_status = np.append(self.dn_status, message)
                    self.dn_set = np.append(self.dn_set, cn[0])
                else:
                    message = ("{}: Distinguished Name Set: {}").format(cn[0], "No")
                    self.dn_status = np.append(self.dn_status, message)
                    self.dn_not_set = np.append(self.dn_not_set, cn[0])

#Check that the DONT_EXPIRE_PASSWD flag is set to false
    def check_pwd_expire(self, con, cat):
        container = adcontainer.ADContainer.from_dn(con)
        for i in container.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            a = user.get_attribute("objectCategory")
            if (a[0] == cat):
                account_control = user.get_user_account_control_settings()
                message = str(account_control)
                c = "'DONT_EXPIRE_PASSWD': False"
                d = c in message
                if (d == False):
                    self.pwd_exp_flag_false = np.append(self.pwd_exp_flag_false, cn[0])

#Sets the don't expire password flag to false
    def set_exp_flag(self):
        for i in self.pwd_exp_flag_false:
            user = aduser.ADUser.from_cn(i)
            user.set_user_account_control_setting("DONT_EXPIRE_PASSWD", False)
            print("New password policy successfully set.")
            self.pwd_exp_flag_false = np.delete(self.pwd_exp_flag_false, np.where(self.pwd_exp_flag_false == i))


#This checks the usernames of the users with the container, and ensures they are valid
    def check_username(self, container, objCategory):
        con = adcontainer.ADContainer.from_dn(container)
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            objCat = user.get_attribute("objectCategory")
            objCat = objCat[0]
            samAccount = user.get_attribute("samaccountname")
            names = cn[0].split(" ")
            if(objCat == objCategory):
                if(len(names) == 3):
                    fname = names[0]
                    mname = names[1]
                    lname = names[2].lower()
                    init = fname[0].lower()
                    init2 = init
                    init2 += mname[0].lower()
                    init3 = init
                    init3 += fname[1]
                    init3 += mname[0]
                    regex = "[" + init + "-" + init3 + "]+"+lname
                elif(len(names) == 1):
                    fname = names[0]
                    init = fname
                    regex = "[" + init + "]+[a-zA-Z]"
                else:
                    fname = names[0]
                    lname = names[1].lower()
                    init = fname[0].lower()
                    init2 = init
                    init2 += lname[0].lower()
                    regex = "[" + init + "-" + init2 + "]+"+lname


                if (re.search(regex, samAccount[0])):
                    self.validUsernames = np.append(self.validUsernames, samAccount)


                else:
                    self.invalidUsernames = np.append(self.invalidUsernames, samAccount)
                    self.usersNeedUserNameCorr = np.append(self.usersNeedUserNameCorr, cn[0])

#This checks that the computer name is of a valid naming scheme for ARA standards
    def check_computer_name(self, container):
        con = adcontainer.ADContainer.from_dn(container)
        sam = ""
        for i in con.get_children():
            cn = i.get_attribute("cn")
            user = aduser.ADUser.from_cn(cn[0])
            sam = user.get_attribute("samaccountname")



            regex = "[a-zA-Z]+-+pc"
            regex3 = "[a-zA-Z0-9]+-+lap"
            regex2 = "[a-zA-Z0-9]+-+[a-zA-Z0-9]+-+pc"
            regex4 = "[a-zA-Z0-9]+-+[a-zA-Z0-9]+-+lap"
            # Define a function for
            # validate an Ip address

            # pass the regular expression
            # and the string in search() method

            if (re.search(regex, sam[0]) or re.search(regex2, sam[0]) or re.search(regex3, sam[0]) or re.search(regex4, sam[0])):
                self.computerNameValid = np.append(self.computerNameValid, sam[0])

            else:
                self.computerNameInValid = np.append(self.computerNameInValid, sam[0])
                self.computerNeedNameChange = np.append(self.computerNeedNameChange, cn[0])

#This checks the service accounts against the proper ARA naming scheme
    def check_service_account_name(self, container, OU):

        regex = OU + "+-+[a-zA-Z]"
        con = adcontainer.ADContainer.from_dn(container)
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            sam = user.get_attribute("samaccountname")
            if (re.search(regex, sam[0])):
                self.validUsernames = np.append(self.invalidUsernames, sam[0])

            else:
                self.invalidUsernames = np.append(self.invalidUsernames, sam[0])
                self.servAccUserNameNeedChange = np.append(self.servAccUserNameNeedChange, cn[0])

#Creates recommended usernames for service accounts
    def autoChangeServiceAccountName(self, invalid, container, OU):
        con = adcontainer.ADContainer.from_dn(container)
        newSam = ""
        for i in invalid:
            user = aduser.ADUser.from_cn(i)
            sam = user.get_attribute("samaccountname")
            newSam += str(OU) + "-" + str(sam[0])
            valid = self.findMatch(newSam, container)
            if(valid == True):
                input = i + "_" + newSam
                self.serviceAccountNamesToBeApproved = np.append(self.serviceAccountNamesToBeApproved, input)

#Sets approved names for service accounts
    def changeServiceAccountNames(self):
        if(len(self.approvedServiceAccountNamesForChange) > 0):
            for i in self.approvedServiceAccountNamesForChange:
                names = i.split("_")
                sam = names[1]
                user = aduser.ADUser.from_cn(names[0])
                pyad.adobject.ADObject.update_attribute(user, "samaccountname", str(sam))
                print(user.get_attribute("samaccountname"), " has been set!")
                user.rename(str(sam))
                self.servAccUserNameNeedChange = np.delete(self.servAccUserNameNeedChange, np.where(self.servAccUserNameNeedChange == names[0]))
        else:
            print("No names to be changed!")

#Finds out if a samAccount name is already in use.
    def findMatch(self, samAccount, container):
        con = adcontainer.ADContainer.from_dn(container)
        valid = True
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            sam = user.get_attribute("samaccountname")
            sam = sam[0]
            if (sam == samAccount):
                valid = False
                break

        return valid

#Sets suggested usernames for accounts that need to be changed.
    def autoChangeUserName(self, invalid, container):
        con = adcontainer.ADContainer.from_dn(container)
        array = np.array([])
        newsam = ""
        for i in invalid:
            names = i.split(" ")
            if (len(names) == 3):
                fname = names[0].lower()
                mname = names[1].lower()
                lname = names[2].lower()
                init = fname[0].lower()
                init2 = init
                init2 += mname[0].lower()
                init3 = init
                init3 += fname[1].lower()
                init3 += mname[0]
                newsam = init + lname
                found = self.findMatch(newsam, container)
                input = i + "-" + newsam
                if (found == False):
                    newsam = init2 + lname
                    found = self.findMatch(newsam, container)
                    if (found == False):
                        newsam = init3 + lname
                        input = i + "-" + newsam
                        array = np.append(array, input)
                    else:
                        input = i + "-" + newsam
                        array = np.append(array, input)
                else:
                    array = np.append(array, input)
            elif (len(names) == 1):
                fname = names[0]
                init = fname
                newsam = init
                input = i + "-" + newsam
                array = np.append(array, input)
            else:
                fname = names[0].lower()
                lname = names[1].lower()
                init = fname[0].lower()
                init2 = init
                init2 += lname[0].lower()
                newsam = init + lname
                print(newsam)
                found = self.findMatch(newsam, container)
                input = i + "-" + newsam
                if (found == False):
                    newsam = init2 + lname
                    input = i + "-" + newsam
                    array = np.append(array, input)
                else:
                    array = np.append(array, input)

        self.userNamesToBeApproved = array

#Sets newly approved usernames
    def changeUsernames(self):
        if(self.approvedUsernamesForChange.size > 0):
            for i in self.approvedUsernamesForChange:
                names = i.split("-")
                sam = names[1]
                user = aduser.ADUser.from_cn(names[0])
                pyad.adobject.ADObject.update_attribute(user, "samaccountname", str(sam))
                print(user.get_attribute("samaccountname"), " has been set!")
                self.usersNeedUserNameCorr = np.delete(self.usersNeedUserNameCorr, np.where(self.get_usersNeedUserNameCorr() == names[0]))
        else:
            print("No names to be changed!")

#Sets newly approved computernames
    def changeComputernames(self):
        if(self.approvedComputernamesForChange.size > 0):
            for i in self.approvedComputernamesForChange:
                names = i.split("_")
                newName = names[1]
                user = aduser.ADUser.from_cn(names[0])
                pyad.adobject.ADObject.update_attribute(user, "samaccountname", newName)
                print(user.get_attribute("samaccountname"), " has been set!")
                user.rename(newName)
                self.computerNeedNameChange = np.delete(self.computerNeedNameChange, np.where(self.computerNeedNameChange == names[0]))
        else:
            print("No names to be changed!")

    def force_pwd_change(self):
        if(self.pwdLastSetNDays.size > 0):
            for i in self.pwdLastSetNDays:
                user = aduser.ADUser.from_cn(i)
                user.force_pwd_change_on_login()
                print("The Password change has been forced for ", i, "\n")
                self.pwdLastSetNDays = np.delete(self.pwdLastSetNDays, np.where(self.pwdLastSetNDays == i))


#Creates suggestion for computer names
    def autoChangeComputerName(self, invalid, container):
        con = adcontainer.ADContainer.from_dn(container)
        newName = ""
        input = ""
        for i in invalid:
            computer = adcomputer.ADComputer.from_cn(i)
            name = i.split("-")
            desc = computer.get_attribute("description")
            desc = desc[0]
            if(len(name) == 2):
                if("laptop" in desc):
                    newName = name[0].lower() + "-" + name[1].lower() + "-lap"
                    valid = self.findMatch(newName, container)
                    if(valid == True):
                        input = str(i) + "_" + newName
                        self.computerNamesToBeApproved = np.append(self.computerNamesToBeApproved, input)
                    else:
                        raise ValueError("The pc already exists in the system!")
                elif("pc" in desc):
                    newName = name[0].lower() + "-" + name[1].lower() + "-pc"
                    valid = self.findMatch(newName, container)
                    if (valid == True):
                        input = str(i) + "_" + newName
                        self.computerNamesToBeApproved = np.append(self.computerNamesToBeApproved, input)
                    else:
                        raise ValueError("The pc already exists in the system!")
                else:
                    raise ValueError("Must be a laptop or pc!")
            elif(len(name) == 1):
                if ("laptop" in desc):
                    newName = name[0].lower() + "-lap"
                    valid = self.findMatch(newName, container)
                    if (valid == True):
                        input = str(i) + "_" + newName
                        self.computerNamesToBeApproved = np.append(self.computerNamesToBeApproved, input)
                    else:
                        raise ValueError("The pc already exists in the system!")
                elif ("pc" in desc):
                    newName = name[0].lower() + "-pc"
                    valid = self.findMatch(newName, container)
                    if (valid == True):
                        input = str(i) + "_" + newName
                        self.computerNamesToBeApproved = np.append(self.computerNamesToBeApproved, input)
                    else:
                        raise ValueError("The pc already exists in the system!")
                else:
                    raise ValueError("Must be a laptop or pc!")
            else:
                raise ValueError("The name is too long!")


    #Report of usersnames that need to be changed
    def username_change_needed_report(self):
        message = ""
        message += "\n\n## Users that need to change username: ##\n\n"
        df = pd.DataFrame([], columns=['User', 'Username'])
        if (self.usersNeedUserNameCorr.size > 0):
            for i in self.usersNeedUserNameCorr:
                #message += ("## {}, ##\n").format(str(i))
                user = pyad.aduser.ADUser.from_cn(str(i))
                sam = user.get_attribute('samaccountname')
                newRow = {'User':i, 'Username':str(sam[0])}
                df = df.append(newRow, ignore_index=True)
            self.df_user_username = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No users need username correction."
            self.df_user_username = "N/A"
            message+= str(df)
        message += "\n\n## Service Accounts that need their names changed: ##\n"
        df = pd.DataFrame([], columns=['Service Account', 'Username'])
        if (self.servAccUserNameNeedChange.size > 0):
            for i in self.servAccUserNameNeedChange:
                #message += ("## {}, ##\n").format(str(i))
                user = pyad.aduser.ADUser.from_cn(str(i))
                sam = user.get_attribute('samaccountname')
                newRow = {'Service Account': i, 'Username': str(sam[0])}
                df = df.append(newRow, ignore_index=True)
            self.df_serv_username = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "\nNo service accounts need username correction. \n"
            self.df_serv_username = "N/A"
            message += str(df)
        message += "\n\n## Computers that need their names changed: ##\n\n"
        df = pd.DataFrame([], columns=['Computer', 'Username'])
        if (self.computerNeedNameChange.size > 0):
            for i in self.computerNeedNameChange:
                #message += ("## {}, ##\n").format(str(i))
                user = pyad.aduser.ADUser.from_cn(str(i))
                sam = user.get_attribute('samaccountname')
                newRow = {'Computer': i, 'Username': str(sam[0])}
                df = df.append(newRow, ignore_index=True)
            self.df_computer_username = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No computers need their names changed."
            self.df_computer_username = "N/A"
            message += str(df)
        return message

#This generates a report of all distinguished name statuses and displays them for the admin.
    def distinguished_name_report(self):
        message = ""
        message += "## Distinguished Name Status: ##\n"
        df = pd.DataFrame([], columns=['Computer', 'DN Set', 'DN'])
        if(self.dn_status.size > 0):
            for i in self.dn_status:
                #message += ("## {} ##\n").format(str(i))
                x = i.split(" | ")
                if(x[1] == "Yes"):
                    newRow = {'Computer':x[0],'DN Set':x[1],'DN':x[2]}
                else:
                    newRow = {'Computer': x[0], 'DN Set': x[1], 'DN': '[Unknown]'}
                df = df.append(newRow, ignore_index=True)
            self.df_dn_status = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No distinguished name audit has been conducted"
            self.df_dn_status = "N/A"
            message += str(df)
        return message


#Return a report of the admin users of each admin type
    def admin_report(self):
        message = "\n\n## Admin Report: ##\n"
        df = pd.DataFrame([], columns=['Admin Group', 'Members'])
        if(self.admin_list.size > 0):
            for i in self.admin_list:
                #message += ("## {} ##\n").format(str(i))
                x = i.split("| ")
                x2 = x[1].split("-")
                x3 = np.array([])
                counter = 0
                for i in x2:
                    xtemp = i.split(",")
                    xtemp[0] = xtemp[0].replace("CN=", "")
                    if(counter < len(x2) - 2):
                        xtemp[0] += ", "
                        counter+=1
                    x3 = np.append(x3, xtemp[0])
                x3 = str(x3)
                x3 = x3.replace("[", "")
                x3 = x3.replace("]", "")
                x3 = x3.replace("'", "")
                newRow = {'Admin Group':x[0], 'Members':x3}
                df = df.append(newRow, ignore_index=True)
            self.df_admin_list = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No admin audit has been conducted."
            self.df_admin_list = "N/A"
            message += str(df)
        message += "\n"
        message += "\n## Administrator Last Logon ##\n\n"
        df = pd.DataFrame([], columns=['Admin Name', 'Last Logon', 'Days Since'])
        if(self.admin_last_logon.size > 0):
            for i in self.admin_last_logon:
                #message += ("## {} ##\n").format(str(i))
                x = i.split(",")
                newRow = {'Admin Name':x[0],'Last Logon':x[1], 'Days Since':x[2]}
                df = df.append(newRow, ignore_index=True)
            self.df_admin_last_logon = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No admin last logon audit has been conducted."
            self.df_admin_last_logon = "N/A"
            message += str(df)
        return message

#Return a report of the users and computers that have not logged in the last N days.
    def get_unused_report(self):
        message ="\n\n## Unused Users: ##\n\n"
        df = pd.DataFrame([], columns=['User', 'Days Unused'])
        counter = 0
        if(self.unusedUsers.size > 0):
            for i in self.unusedUsers:
                #message += ("\n## {} ##").format(str(i))
                newRow = {'User':i, 'Days Unused':self.userDaysUnused[counter]}
                df = df.append(newRow, ignore_index=True)
                counter += 1
            self.df_unusedUsers = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "There are no unused users past the day limit."
            self.df_unusedUsers = "N/A"
            message += str(df)
        message += ("\n## Unused User Count: {} ##\n\n").format(self.unusedUserCount)
        message += "\n\n## Unused Computers: ##\n\n"
        df = pd.DataFrame([], columns=['Computer', 'Days Unused'])
        counter = 0

        if(self.unusedComputers.size > 0):
            for i in self.unusedComputers:
                #message += ("\n## {} ##").format(str(i))
                newRow = {'Computer':i, 'Days Unused':self.computerDaysUnused[counter]}
                df = df.append(newRow, ignore_index=True)
                counter += 1
            self.df_unusedComputers = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "There are no unused computers past the day limit."
            self.df_unusedComputers = "N/A"
            message += str(df)
        message += ("\n## Unused Computer Count: {} ##").format(self.unusedComputerCount)
        return message

#Return a report on the users that have not changed their password in N days.
    def get_pwd_report(self):
        message = "\n\n## Users with passwords unchanged past the day limit: ##\n\n"

        df = pd.DataFrame([], columns=['User', 'Username'])
        if(self.pwdLastSetNDays.size > 0):
            for i in self.pwdLastSetNDays:
                user = pyad.aduser.ADUser.from_cn(str(i))
                u = user.get_attribute("samaccountname")
                #message += "## "
                #message += ("{}, ").format(str(i))
                #message += " ##"
                newRow = {'User':str(i), 'Username':str(u[0])}
                df = df.append(newRow, ignore_index=True)
            self.df_pwdLastSetNDays = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No passwords that are older than the day limit."
            self.df_pwdLastSetNDays = "N/A"
            message += str(df)
        message += "\n\n## Users with password's that don't expire: ##\n\n"
        df = pd.DataFrame([], columns=['User', 'Username'])
        if(self.pwd_exp_flag_false.size > 0):
            for i in self.pwd_exp_flag_false:
                #message += ("{}, ").format(str(i))
                user = pyad.aduser.ADUser.from_cn(str(i))
                u = user.get_attribute("samaccountname")
                newRow = {'User': str(i), 'Username': str(u[0])}
                df = df.append(newRow, ignore_index=True)
            self.df_pwd_exp_flag_false = df.to_csv(index=False)
            message += df.to_markdown()
        else:
            df = "No accounts are set to have passwords that don't expire."
            self.df_pwd_exp_flag_false = "N/A"
            message += str(df)
        return message

#Report of the service accounts that do not have a manager attribute set.
    def get_serv_man_not_set_report(self):
        message = "\n\n## Service Accounts without manager set: ##\n\n"
        df = pd.DataFrame([], columns=['Service Account'])
        if(self.serv_man_not_set.size > 0):
            for i in self.serv_man_not_set:
                #message += "## "
                #message += ("{}, ").format(str(i))
                #message += " ##"
                newRow = {'Service Account':i}
                df = df.append(newRow, ignore_index=True)
            self.df_serv_man_not_set = df.to_csv(index=False)
            message += df.to_markdown()
            message += "\n\n"
        else:
            df = "No service accounts without their password set.\n\n"
            self.df_serv_man_not_set = "N/A"
            message += str(df)
        return message

#Full Report in csv format.
    def report_to_csv(self):
        info = "Users with invalid Usernames:\n"
        info += str(self.df_user_username)
        info += "\n"
        info += "Service Accounts with invalid Usernames:\n"
        info += str(self.df_serv_username)
        info += "\n"
        info += "Computers with invalid Usernames:\n"
        info += str(self.df_computer_username)
        info += "\n"
        info += "Distinguished Name set?:\n"
        info += str(self.df_dn_status)
        info += "\n"
        info += "Admin List:\n"
        info += str(self.df_admin_list)
        info += "\n"
        info += "Admin Last Logon:\n"
        info += str(self.df_admin_last_logon)
        info += "\n"
        info += "Unused Users:\n"
        info += str(self.df_unusedUsers)
        info += "\n"
        info += "Unused Computers:\n"
        info += str(self.df_unusedComputers)
        info += "\n"
        info += "Users with passwords past the day limit:\n"
        info += str(self.df_pwdLastSetNDays)
        info += "\n"
        info += "Users with password flag set to false:\n"
        info += str(self.df_pwd_exp_flag_false)
        info += "\n"
        info += "Service Accounts without a manager:\n"
        info += str(self.df_serv_man_not_set)
        info += "\n"
        return info
#Print an overall message on information found by querying through Active Directory.
    def toString(self):
        df = pd.DataFrame([], columns=['User', 'Days Unused'])
        print("Unused Users: ")
        counter = 0
        for i in self.unusedUsers:
            newRow = {'User': i, 'Days Unused': self.userDaysUnused[counter]}
            df = df.append(newRow, ignore_index=True)
            # message += str(df)
            counter += 1
        print(df)
        print("\nUnused User Count: ", self.unusedUserCount)
        print("\nUnused Computers: ")
        for i in self.unusedComputers:
            print(i, ", ")
        print("\nUnused Computer Count: ", self.unusedComputerCount)
        print("\nPWD Unchanged Past Day Limit: ")
        for i in self.unusedComputers:
            print(("{}, ").format(str(i)))

# ------------------------------------------------End of Class ADaudit ---------------------------------------------------------------------------------------------
#obj = adobject.ADObject.from_cn("Christopher Kyriacou")
#user = aduser.ADUser.from_cn("Jamie Sutton")
#user.set_user_account_control_setting("DONT_EXPIRE_PASSWD", True)
#user.rename("Jamie Sutton")
#print(user)
#print(user.get_last_login())
#admin = aduser.ADUser.from_cn("Christopher Kyriacou")
#pyad.adobject.ADObject.update_attribute(user, "samaccountname", "CLIENT")
#print(user.get_attribute("samaccountname"))

#user.set_user_account_control_setting("DONT_EXPIRE_PASSWD", True)
#print(user.get_user_account_control_settings())
#ad = adcomputer.ADComputer.from_cn("DESKTOP-A67G0P2")
#ad.update_attribute("samaccountname", "DESKTOP-A67G0P2$")
#print(ad.get_attribute("samaccountname"))
#ad = adcomputer.ADComputer.from_cn("CLIENT")
#ad.update_attribute("samaccountname", "CLIENT")
#print(ad.get_attribute("samaccountname"))

#user = aduser.ADUser.from_cn("Updates")
#user.update_attribute("samaccountname", "Updates")
#print(user.get_attribute("manager"))
#user2 = aduser.ADUser.from_cn("Jamie Sutton")
#user2.force_pwd_change_on_login()
#user.update_attribute("manager", "Christopher M Kyriacou")
#obj = pyad.adobject.ADObject.from_cn("Updates")
#obj.set_managedby(obj)