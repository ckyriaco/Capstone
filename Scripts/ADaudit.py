#Applied Research Associates
#This class is designed to allow administrators to query information that are vital for cmmc compliance audits of active directory instances.
#Must already be joined to the active directory server's domain to use this class!
#Can set a default domain manually using pyad.set_defaults(ldap_server="dc1.domain.com", username="service_account", password="mypassword").
#Setting the default domain manually is not recommended due to the fact that joining the domain and authenticating through Windows Systems on the end-unit is more secure.
#Can connect to a specific other domain temporarilty instead of the default using user = aduser.ADUser.from_cn("myuser", options=dict(ldap_server="dc1.domain.com"))
#Reusable functions for the previous two notes can be formed to support mass iteration through various domains if requrested. 

from pyad import *
import numpy as np
import pyad.pyadutils
from datetime import datetime
from warnings import simplefilter

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

#Return a report of the admin users of each admin type
    def admin_report(self):
        message = "\n\nAdmin Report:\n"
        for i in self.admin_list:
            message += ("{}\n").format(str(i))
        return message

#Return a report of the users and computers that have not logged in the last N days.
    def get_unused_report(self):
        message ="\n\nUnused Users:"
        for i in self.unusedUsers:
            message += ("\n{}, ").format(str(i))
        message += ("\nUnused User Count: {}").format(self.unusedUserCount)
        message += "\n\nUnused Computers:\n"
        for i in self.unusedComputers:
            message += ("{}, ").format(str(i))
        message += ("\nUnused Computer Count: {}").format(self.unusedComputerCount)
        return message

#Return a report on the users that have not changed their password in N days.
    def get_pwd_report(self):
        message = "\n\nPWD Unchanged Past Day Limit:\n"
        for i in self.pwdLastSetNDays:
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


