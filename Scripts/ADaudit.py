#Applied Research Associates
#This class is designed to allow administrators to query information that are vital for cmmc compliance audits of active directory instances.
#Must already be joined to the active directory server's domain to use this class!
#Can set a default domain manually using pyad.set_defaults(ldap_server="dc1.domain.com", username="service_account", password="mypassword").
#Setting the default domain manually is not recommended due to the fact that joining the domain and authenticating through Windows Systems on the end-unit is more secure.
#Can connect to a specific other domain temporarilty instead of the default using user = aduser.ADUser.from_cn("myuser", options=dict(ldap_server="dc1.domain.com"))
#Reusable functions for the previous two notes can be formed to support mass iteration through various domains if requrested. 

from pyad import *
import numpy as np
import pyad.pyadutils as py
from datetime import datetime
from warnings import simplefilter
import re

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

    #Finds the last time a list of users each last logged on to their accounts.
    def get_last_login_users(self, array):
        emptyArray = np.array([])
        if(array == emptyArray or array == ""):
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
            notSet = []
            for i in con.get_children():
                manager = i.get_attribute("manager")
                CN = i.get_attribute("CN")
                if manager == notSet:
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
        emptyArray = np.array([])
        if(array == emptyArray or type not in Allowed_Types):
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
                        self.unusedComputers = np.append(self.unusedComputers, "{} Days Unused: {}".format(i, diff))
                    elif(type == "User"):
                        self.unusedUserCount += 1
                        self.unusedUsers = np.append(self.unusedUsers, "{} Days Unused: {}".format(i, diff))


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
        emptyArray = np.array([])
        if(Admin_Types == emptyArray):
            raise ValueError("The Admin_Types array cannot be empty!")
        else:
            for i in Admin_Types:
                user = aduser.ADUser.from_cn(i)
                l = user.get_attribute("member")
                addition = ("{}: ").format(i)
                for x in l:
                    addition += ("{},").format(x)
                self.admin_list = np.append(self.admin_list, addition)

#Get all the cn's of all admin users
    def get_All_Admin_CN(self, Admin_Types):
        emptyArray = np.array([])
        if (Admin_Types == emptyArray):
            raise ValueError("The Admin_Types array cannot be empty!")
        else:

            for i in Admin_Types:
                user = aduser.ADUser.from_cn(i)
                l = user.get_attribute("member")
                for x in l:
                    c = aduser.ADUser.from_dn(x)
                    c = c.get_attribute("CN")
                    if (c[0] not in emptyArray):
                        emptyArray = np.append(emptyArray, c)
        return emptyArray

#Get the last logon time for all admin of the given types.
    def get_admin_last_logon_info(self, Admin_Types):
        emptyArray = np.array([])
        if(Admin_Types == emptyArray):
            raise ValueError("The admin types cannot be null!")
        else:
            admin = self.get_All_Admin_CN(Admin_Types)
            report = np.array([])
            for i in admin:
                user = aduser.ADUser.from_cn(str(i))
                logon = user.get_last_login()
                message = ("Administrator {} last logon: {}").format(i, logon)
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
                    message = ("{}: Distinguished Name Set: {} | DN = {}").format(cn[0], "Yes", user.get_attribute("distinguishedName"))
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

#This checks the usernames of the users with the container, and ensures they are valid
    def check_username(self, container):
        con = adcontainer.ADContainer.from_dn(container)
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            samAccount = user.get_attribute("samaccountname")
            names = cn[0].split(" ")
            if(len(names) == 3):
                fname = names[0]
                mname = names[1]
                lname = names[2]
                init = fname[0].lower()
                init2 = init
                init2 += mname[0].lower()
                init3 = init
                init3 += fname[1]
                init3 += mname[0]
                regex = "[" + init + "-" + init3 + "]+[a-zA-Z]"
            elif(len(names) == 1):
                fname = names[0]
                init = fname
                regex = "[" + init + "]+[a-zA-Z]"
            else:
                fname = names[0]
                lname = names[1]
                init = fname[0].lower()
                init2 = init
                init2 += lname[0].lower()
                regex = "[" + init + "-" + init2 + "]+[a-zA-Z]"


            if (re.search(regex, samAccount[0])):
                self.validUsernames = np.append(self.validUsernames, samAccount)


            else:
                self.invalidUsernames = np.append(self.invalidUsernames, samAccount)
                self.usersNeedUserNameCorr = np.append(self.usersNeedUserNameCorr, cn[0])

#This checks that the computer name is of a valid naming scheme for ARA standards
    def check_computer_name(self, container):
        con = adcontainer.ADContainer.from_dn(container)
        cn = ""
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])



            regex = "[a-zA-Z]+-+pc"
            regex3 = "[a-zA-Z]+-+lap"
            regex2 = "[a-zA-Z]+-+[a-zA-Z]+-+pc"
            regex4 = "[a-zA-Z]+-+[a-zA-Z]+-+lap"
            # Define a function for
            # validate an Ip address

            # pass the regular expression
            # and the string in search() method

            if (re.search(regex, cn[0]) or re.search(regex2, cn[0]) or re.search(regex3, cn[0]) or re.search(regex4, cn[0])):
                self.computerNameValid = np.append(self.computerNameValid, cn[0])

            else:
                self.computerNameInValid = np.append(self.computerNameInValid, cn[0])
                self.computerNeedNameChange = np.append(self.computerNeedNameChange, cn[0])

#This checks the service accounts against the proper ARA naming scheme
    def check_service_account_name(self, container, OU):

        regex = OU + "+-+[a-zA-Z]"
        con = adcontainer.ADContainer.from_dn(container)
        for i in con.get_children():
            cn = i.get_attribute("CN")
            user = aduser.ADUser.from_cn(cn[0])
            if (re.search(regex, cn[0])):
                self.validUsernames = np.append(self.invalidUsernames, cn[0])

            else:
                self.invalidUsernames = np.append(self.invalidUsernames, cn[0])
                self.servAccUserNameNeedChange = np.append(self.servAccUserNameNeedChange, cn[0])

#Report of usersnames that need to be changed
    def username_change_needed_report(self):
        message = "\n\nUsers that need their username changed:\n"
        message += "Users that need to change username:\n"
        for i in self.usersNeedUserNameCorr:
            message += ("{}, \n").format(str(i))
        message += "Service Accounts that need their names changed:\n"
        for i in self.servAccUserNameNeedChange:
            message += ("{}, \n").format(str(i))
        message += "Computers that need their names changed:\n"
        for i in self.computerNeedNameChange:
            message += ("{}, \n").format(str(i))
        return message

#This generates a report of all distinguished name statuses and displays them for the admin.
    def distinguished_name_report(self):
        message = "\n\nDistinguished Name Report:\n"
        message += "Distinguished Name Status:\n"
        for i in self.dn_status:
            message += ("{}\n").format(str(i))
        message += "\n"
        return message


#Return a report of the admin users of each admin type
    def admin_report(self):
        message = "\n\nAdmin Report:\n"
        for i in self.admin_list:
            message += ("{}\n").format(str(i))
        message += "\n"
        for i in self.admin_last_logon:
            message += ("{}\n").format(str(i))

        return message

#Return a report of the users and computers that have not logged in the last N days.
    def get_unused_report(self):
        message ="\n\nUnused Users:"
        for i in self.unusedUsers:
            message += ("\n{}").format(str(i))
        message += ("\nUnused User Count: {}").format(self.unusedUserCount)
        message += "\n\nUnused Computers:"
        for i in self.unusedComputers:
            message += ("\n{}").format(str(i))
        message += ("\nUnused Computer Count: {}").format(self.unusedComputerCount)
        return message

#Return a report on the users that have not changed their password in N days.
    def get_pwd_report(self):
        message = "\n\nUsers with passwords unchanged past the day limit:\n"
        for i in self.pwdLastSetNDays:
            message += ("{}, ").format(str(i))
        message += "\n\nUsers with password's that don't expire:\n"
        for i in self.pwd_exp_flag_false:
            message += ("{}, ").format(str(i))
        return message

#Report of the service accounts that do not have a manager attribute set.
    def get_serv_man_not_set_report(self):
        message = "\n\nService Accounts without manager set:\n"
        for i in self.serv_man_not_set:
            message += ("{}, ").format(str(i))
        return message

#Print an overall message on information found by querying through Active Directory.
    def toString(self):
        print("Unused Users: ")
        for i in self.unusedUsers:
            print(i, ", ")
        print("\nUnused User Count: ", self.unusedUserCount)
        print("\nUnused Computers: ")
        for i in self.unusedComputers:
            print(i, ", ")
        print("\nUnused Computer Count: ", self.unusedComputerCount)
        print("\nPWD Unchanged Past Day Limit: ")
        for i in self.unusedComputers:
            print(("{}, ").format(str(i)))

# ------------------------------------------------End of Class ADaudit ---------------------------------------------------------------------------------------------














