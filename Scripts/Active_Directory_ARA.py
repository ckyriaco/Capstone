#Applied Research Associates
#This script utilizes the ADquery class to audit a variety of users, computers and groups for cmmc compliance
import ADquery as ad
import os
import numpy as np



#Use ADquery class to audit active directory for users that have not logged on in N days.

def logon_info(CN, containers, objectCategories, types, N):
    AD = ad.ADquery(CN)
    count = 0
    list = np.array([])
    N = int(N)
    while(count < len(containers)):
        list = AD.get_last_user_login_list(containers[count], objectCategories[count])
        AD.get_login_past_N_days(N, list, types[count])
        count += 1
    AD.toString()
    doc = AD.get_unused_report()
    f = open(("Logon_in_{}_days.txt").format(N), "w")
    f.write(doc)
    f = open(("Logon_in_{}_days.txt").format(N), "r")
    print(f.read())
    f.close()

#Use ADquery to locate users that have not changed their password in N days.

def last_set_pwd(CN, containers, objectCategories, N):
    AD = ad.ADquery(CN)
    count = 0
    N = int(N)
    while(count < len(containers)):
        AD.get_pwd_last_login_N_days(containers[count], objectCategories[count], N)
        count += 1
    doc = AD.get_pwd_report()
    f = open(("PWD_Last_Set_Past_{}_days.txt").format(N), "w")
    f.write(doc)
    f = open(("PWD_Last_Set_Past_{}_days.txt").format(N), "r")
    print(f.read())
    f.close()

#Use ADquery to identify all admin of the specified admin types of interest
    
def get_admin(CN, adminTypes):
    AD = ad.ADquery(CN)
    AD.get_All_Admin(adminTypes)
    doc = AD.admin_report()
    f = open("Admin_Report.txt", "w")
    f.write(doc)
    f = open("Admin_Report.txt", "r")
    print(f.read())
    f.close()


#Main method that takes in os variables from a bash file and passess them into the appropriate functions to audit Active Directory instance within the current admin user's domain

def main():
    CN = os.getenv('AD_USER')
    containerUsers = os.getenv('CONTAINER_USERS')
    containerComputers = os.getenv('CONTAINER_COMPUTERS')
    usersObjectCategory = os.getenv('OBJECT_CATEGORY_USERS')
    computersObjectCategory = os.getenv('OBJECT_CATEGORY_COMPUTERS')
    adminType1 = os.getenv('ADMIN_TYPE1')
    adminType2 = os.getenv('ADMIN_TYPE2')
    adminType3 = os.getenv('ADMIN_TYPE3')
    adminType4 = os.getenv('ADMIN_TYPE4')
    adminTypes = np.array([adminType1, adminType2, adminType3, adminType4])
    containers = np.array([containerUsers, containerComputers])
    containers2 = np.array([containerUsers])
    objectCategories = np.array([usersObjectCategory, computersObjectCategory])
    objectCategories2 = np.array([usersObjectCategory])
    types = np.array(["User", "Computer"])
    N = os.getenv('DAYS_UNUSED')
    N2 = os.getenv('DAYS_LS')
    logon_info(CN, containers, objectCategories, types, N)
    last_set_pwd(CN, containers2, objectCategories2, N2)
    get_admin(CN, adminTypes)


if __name__ == "__main__":
    main()



