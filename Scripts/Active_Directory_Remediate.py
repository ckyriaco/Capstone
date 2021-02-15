
#Applied Research Associates
#This script utilizes the ADquery class to audit a variety of users, computers and groups for cmmc compliance
import ADaudit as ad
import os
import numpy as np
from tkinter import *
from tkinter import messagebox
import Active_Directory_Audit as audit

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()


#Uses ADaudit to check the usernames of different types against the ARA naming scheme rules

def check_usernames(CN, container1, container2, container3, OU2, objCat, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
        audit.userAudit(AD, container1, container2, container3, OU2, objCat)
        userRemediate(AD, container1)
        servRemediate(AD, container2, OU2)
        computerRemediate(AD, container3)
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)

    doc = AD.username_change_needed_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Calls ADaudit and remediates service account usernames if requested.
def servRemediate(AD, container2, OU):
    a = AD.get_servAccUserNameNeedChange()

    if(a.size == 0):
        messagebox.showwarning("All Clear", "No service accounts to remediate")

    else:
        try:
            action = messagebox.askyesno("Username Remediation",
                                         "Would you like to see if you would like to remediate usersnames for the incompliant service account names found?")
            # action = ""
            #while(action != 1 and action != 2):
            #action = int(input("Press 1 to view invalid serverAccounts or 2 to continue with audit"))
                #if (action != 1 and action != 2):
                    #print("You must select 1 for remediate and 2 to skip!")
            if (action == 1):
                array = AD.get_servAccUserNameNeedChange()
                message = ""
                for i in array:
                    #print(i, "\n")
                    message += i
                    message += "\n"
                #action = int(input("Press 1 to remediate or 2 to move forward"))
                action = messagebox.askyesno("Username Remediation", ("Would you like to remediate any of these service accounts?\n {}").format(message))
                if (action == 1):
                    AD.autoChangeServiceAccountName(array, container2, OU)
                    array3 = AD.get_serviceAccountNamesToBeApproved()
                    array4 = np.array([])
                    for i in array3:
                        #print(i)
                        message = i
                        action = messagebox.askyesno("Username Remediation",
                                                     ("Would you like to remediate this user?\n {}").format(
                                                         message))

                        #action = int(input("Press 1 to add for remediation and 2 to skip"))
                        if (action == 1):
                            array4 = np.append(array4, i)
                    AD.set_approvedServiceAccountNamesForChange(array4)
                    AD.changeServiceAccountNames()
        except ValueError as Valer:
            messagebox.showwarning("An Error has occurred", Valer)

#Use ADaudit to remediate invalid usernames
def userRemediate(AD, container1):
    a = AD.get_usersNeedUserNameCorr()

    if(a.size == 0):
        messagebox.showwarning("All Clear", "No usernames to remediate")

    else:
        try:
            action = messagebox.askyesno("Username Remediation", "Would you like to see if you would like to remediate usersnames for the incompliant users found?")
            #action = ""
            #while(action != 1 and action != 2):
                #action = int(input("Press 1 to view invalid userAccounts or 2 to continue with audit"))
                #if (action != 1 and action != 2):
                    #print("You must select 1 for remediate and 2 to skip!")
            if (action == 1):
                array = AD.get_usersNeedUserNameCorr()
                message = ""
                for i in array:
                    #print(i, "\n")
                    message += i
                    message += "\n"
                #action = int(input("Press 1 to remediate or 2 to move forward"))
                action = messagebox.askyesno("Username Remediation", ("Would you like to remediate any of these user?\n {}").format(message))
                if (action == 1):
                    AD.autoChangeUserName(array, container1)
                    array3 = AD.get_userNamesToBeApproved()
                    array4 = np.array([])
                    for i in array3:
                        #action = int(input("Press 1 to add for remediation and 2 to skip"))
                        action = messagebox.askyesno("Username Remediation", ("Would you like to remediate {}?").format(i))
                        if (action == 1):
                            array4 = np.append(array4, i)
                    AD.set_approvedUserNamesForChange(array4)
                    AD.changeUsernames()
        except ValueError as Valer:
            messagebox.showwarning("An error has occurred", Valer)

#Uses ADaudit to remediate invalid computer names.
def computerRemediate(AD, container3):
    a = AD.get_computerNeedNameChange()

    if (a.size == 0):
        messagebox.showwarning("All Clear", "No computer names to remediate")

    else:
        try:
            #action = ""
            #while(action != 1 and action != 2):
                #action = int(input("Press 1 to view invalid Computer Accounts or 2 to continue with audit"))
                #if (action != 1 and action != 2):
                    #print("You must select 1 for remediate and 2 to skip!")
            action = messagebox.askyesno("Computer Remediation",
                                         "Would you like to see if you would like to remediate computer names for the incompliant computers found?")
            # action = ""
            if (action == 1):
                array = AD.get_computerNeedNameChange()
                message = ""
                for i in array:
                    #print(i, "\n")
                    message += i
                    message += "\n"
                #action = int(input("Press 1 to remediate or 2 to move forward"))
                action = messagebox.askyesno("Computer Remediation", ("Would you like to remediate any of these computer names?\n {}").format(message))

                if (action == 1):
                    AD.autoChangeComputerName(array, container3)
                    array3 = AD.get_computerNamesToBeApproved()
                    array4 = np.array([])
                    for i in array3:
                        #print(i)
                        message = i
                        #action = int(input("Press 1 to add for remediation and 2 to skip"))
                        action = messagebox.askyesno("Computer Remediation",
                                                     ("Would you like to remediate this computer?\n {}").format(
                                                         message))
                        if (action == 1):
                            array4 = np.append(array4, i)
                    AD.set_approvedComputerNamesForChange(array4)
                    AD.changeComputernames()
        except ValueError as Valer:
            messagebox.showwarning("An error has occurred", Valer)

#This checks to see that the passwords have been reset at the N required days and that the passwords do expire for all users.
def last_set_pwd(CN, containers, objectCategories, N, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)
    count = 0
    N = int(N)
    for i in containers:
        try:
            AD.get_pwd_last_login_N_days(i, objectCategories[count], N)
            AD.check_pwd_expire(i, objectCategories[count])
            Force_Password_Change(AD)
            PWD_EXP_Remediate(AD)
        except ValueError as Valer:
            messagebox.showwarning("An Error has occurred: ", Valer)
        else:
            count += 1
    doc = AD.get_pwd_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Forces a password change for users that have not changed their password in N days.
def Force_Password_Change(AD):
    if(AD.get_pwdLastSetNDays().size == 0):
        messagebox.showwarning("All Clear", "No accounts need a forced password change")

    else:
        action = ""
        try:
            #while(action != 1 and action != 2):
                #action = int(input("Would you like to force all users that haven't changed their password in time to change it? 1 for yes and 2 for no."))
                #if(action !=1 and action != 2):
                    #print("You must select 1 for remediate and 2 to skip!")
            action = messagebox.askyesno("Password Remediation",
                                         "Would you like to force all incompliant users to change their passwords at next logon?")
            if (action == 1):
                    AD.force_pwd_change()
        except ValueError as Valer:
            messagebox.showwarning("An Error has occurred ", Valer)

#Uses ADaudit to remediate accounts that have passwords that do not expire.
def PWD_EXP_Remediate(AD):
    if(AD.get_pwd_exp_flag_false().size == 0):
        messagebox.showwarning("Password Remediation", "No users with passwords that don't expire")
    else:
        answer = ""
        try:
            #while(answer != 1 and answer != 2):
            message = ""
            for i in AD.get_pwd_exp_flag_false():
                #print(i, "\n")
                message += i
                message += "\n"
                #answer = int(input("Would you like to set these account's passwords to expire? Press 1 for yes and 2 for no."))
                answer = messagebox.askyesno("Password Remediation","Would you like to set these account's passwords to expire? Press 1 for yes and 2 for no.")
                if(answer == 1):
                    AD.set_exp_flag()
        except ValueError as Valer:
            messagebox.showwarning("An Error has occured", Valer)



#Main method that takes in os variables from a bash file and passess them into the appropriate functions to audit Active Directory instance within the current admin user's domain

def main():
    file_final = os.getenv('FILE_FINAL')
    CN = os.getenv('AD_USER')
    containerUsers = os.getenv('CONTAINER_USERS')
    containerComputers = os.getenv('CONTAINER_COMPUTERS')
    usersObjectCategory = os.getenv('OBJECT_CATEGORY_USERS')
    computersObjectCategory = os.getenv('OBJECT_CATEGORY_COMPUTERS')
    containers = np.array([containerUsers, containerComputers])
    containers2 = np.array([containerUsers])
    container3 = np.array([containerComputers])
    objectCategories = np.array([usersObjectCategory, computersObjectCategory])
    objectCategories2 = np.array([usersObjectCategory])
    types = np.array(["User", "Computer"])
    N = os.getenv('DAYS_UNUSED')
    N2 = os.getenv('DAYS_LS')
    adminArray = os.getenv('ADMIN_ARRAY').split(',')
    con_serv = os.getenv('CONTAINER_SERVICE_ACCOUNT')
    audit.logon_info(CN, containers, objectCategories, types, N, file_final)
    last_set_pwd(CN, containers2, objectCategories2, N2, file_final)
    audit.get_admin(CN, adminArray, file_final)
    audit.service_account_audit(CN, con_serv, file_final)
    file = os.getenv('FILE_NAME')
    ip = os.getenv('SERVER_IP')
    server_name = os.getenv('SERVER_NAME')
    audit.port_status(CN, ip, file, server_name, containerComputers)
    audit.get_dn_status(CN, container3, file_final)
    OU = os.getenv("OU_SERV")
    check_usernames(CN, containerUsers, con_serv, containerComputers, OU, usersObjectCategory, file_final)
    f = open(file, "r")
    doc = f.read()
    f.close()
    f = open(file_final, "a")
    f.write(doc)
    f.close()
    f = open(file_final, "r")
    print(f.read())
    f.close()

if __name__ == "__main__":
    main()