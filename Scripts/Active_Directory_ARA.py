#Applied Research Associates
#This script utilizes the ADquery class to audit a variety of users, computers and groups for cmmc compliance
import ADaudit as ad
import os
import numpy as np
import Port_Scanner as ps


#Use ADquery class to audit active directory for users that have not logged on in N days.

def logon_info(CN, containers, objectCategories, types, N, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
    except ValueError as Valer:
        print("An Error has occurred: ", Valer)
    count = 0
    list = np.array([])
    N = int(N)
    while(count < len(containers)):
        try:
            list = AD.get_last_user_login_list(containers[count], objectCategories[count])
            AD.get_login_past_N_days(N, list, types[count])
        except ValueError as Valer:
            print("An Error has occurred: ", Valer)
        else:
            count += 1
    doc = AD.get_unused_report()
    f = open(file, "w")
    f.write(doc)
    f.close()

#Use ADquery to locate users that have not changed their password in N days.

def get_dn_status(CN, container, file):
    AD = ""
    for i in container:
        try:
            AD = ad.ADaudit(CN)
            AD.distinguished_name_set(i)
        except ValueError as Valer:
            print("An Error has occured: ", Valer)
    doc = AD.distinguished_name_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Uses ADaudit to check the usernames of different types against the ARA naming scheme rules

def check_usernames(CN, container1, container2, container3, OU2, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
        AD.check_username(container1)
        AD.check_service_account_name(container2, OU2)
        AD.check_computer_name(container3)
    except ValueError as Valer:
        print("An Error has occured: ", Valer)

    doc = AD.username_change_needed_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#This checks to see that the passwords have been reset at the N required days and that the passwords do expire for all users.
def last_set_pwd(CN, containers, objectCategories, N, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
    except ValueError as Valer:
        print("An Error has occured: ", Valer)
    count = 0
    N = int(N)
    for i in containers:
        try:
            AD.get_pwd_last_login_N_days(i, objectCategories[count], N)
            AD.check_pwd_expire(i, objectCategories[count])
        except ValueError as Valer:
            print("An Error has occurred: ", Valer)
        else:
            count += 1
    doc = AD.get_pwd_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Use ADquery to get all the admin of each admin type in the AD server.
def get_admin(CN, adminTypes, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
        AD.get_All_Admin(adminTypes)
        AD.get_admin_last_logon_info(adminTypes)
    except ValueError as Valer:
        print("An Error has occured: ", Valer)

    doc = AD.admin_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Use ADquery to get all the service accounts that don't have the manager attribute set.
def service_account_audit(CN, DN, file):
    AD = ""
    try:
        AD = ad.ADaudit(CN)
        AD.set_serve_manager_status(DN)
    except ValueError as Valer:
        print("An Error has occured: ", Valer)
    doc = AD.get_serv_man_not_set_report()
    f = open(file, "a")
    f.write(doc)
    f.close()

#Uses the Port_Scanner class to identify all processes running on all active ports on the domain server and the computers joined to it.
def port_status(CN, server_ip, file, server_name, container):
    try:
        P = ps.Port_Scanner(CN, server_ip, server_name, container)
        P.port_status(file)
    except ValueError as Valer:
        print("An Error has occured: ", Valer)


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
    logon_info(CN, containers, objectCategories, types, N, file_final)
    last_set_pwd(CN, containers2, objectCategories2, N2, file_final)
    get_admin(CN, adminArray, file_final)
    service_account_audit(CN, con_serv, file_final)
    file = os.getenv('FILE_NAME')
    ip = os.getenv('SERVER_IP')
    server_name = os.getenv('SERVER_NAME')
    port_status(CN, ip, file, server_name, containerComputers)
    get_dn_status(CN, container3, file_final)
    OU = os.getenv("OU_SERV")
    check_usernames(CN, containerUsers, con_serv, containerComputers, OU, file_final)
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