
#This script utilizes the ADquery class to audit a variety of users, computers and groups for cmmc compliance
import ADaudit as ad
import os
import numpy as np
import Port_Scanner as ps
from tkinter import *
from tkinter import messagebox
import report_gen as rg
import datetime

from io import *


window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

#Use ADaudit class to audit active directory for users that have not logged on in N days.

def logon_info(containers, objectCategories, types, N, file, doc, AD):
    count = 0
    list = np.array([])
    N = int(N)
    while(count < len(containers)):
        try:
            list = AD.get_last_user_login_list(containers[count], objectCategories[count])
            AD.get_login_past_N_days(N, list, types[count])
        except ValueError as Valer:
            messagebox.showwarning("An Error has occurred: ", Valer)
        else:
            count += 1

    doc = ("{}\n{}").format(doc, AD.get_unused_report())
    #AD.toString()
    f = open(file, "w")
    f.write(doc)
    f.close()
    return AD

#Use ADaudit to locate users that have not changed their password in N days.

def get_dn_status(container, file, AD):
    for i in container:
        try:
            AD.distinguished_name_set(i)
        except ValueError as Valer:
            messagebox.showwarning("An Error has occured: ", Valer)
    doc = AD.distinguished_name_report()
    f = open(file, "a")
    f.write(doc)
    f.close()
    return AD

#Uses ADaudit to check the usernames of different types against the ARA naming scheme rules

def check_usernames(container1, container2, container3, OU2, objCat, file, AD):
    try:
        AD = userAudit(AD, container1, container2, container3, OU2, objCat)
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)

    doc = AD.username_change_needed_report()
    f = open(file, "a")
    f.write(doc)
    f.close()
    return AD

#This checks to see if user, service account, and computer samaccount names/usernames are compliant.
def userAudit(AD, container1, container2, container3, OU2, objCat):
    AD.check_username(container1, objCat)
    AD.check_service_account_name(container2, OU2)
    AD.check_computer_name(container3)
    return AD




#This checks to see that the passwords have been reset at the N required days and that the passwords do expire for all users.
def last_set_pwd(containers, objectCategories, N, file, AD):
    count = 0
    N = int(N)
    for i in containers:
        try:
            AD.get_pwd_last_login_N_days(i, objectCategories[count], N)
            AD.check_pwd_expire(i, objectCategories[count])
        except ValueError as Valer:
            messagebox.showwarning("An Error has occurred: ", Valer)
        else:
            count += 1
    doc = AD.get_pwd_report()
    f = open(file, "a")
    f.write(doc)
    f.close()
    return AD

#Use ADaudit to get all the admin of each admin type in the AD server.
def get_admin(adminTypes, file, AD):
    try:
        AD.get_All_Admin(adminTypes)
        AD.get_admin_last_logon_info(adminTypes)
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)

    doc = AD.admin_report()
    f = open(file, "a")
    f.write(doc)
    f.close()
    return AD

#Use ADaudit to get all the service accounts that don't have the manager attribute set.
def service_account_audit(DN, file, AD):
    try:
        AD.set_serve_manager_status(DN)
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)
    doc = AD.get_serv_man_not_set_report()
    f = open(file, "a")
    f.write(doc)
    f.close()
    return AD

#Uses the Port_Scanner class to identify all processes running on all active ports on the domain server and the computers joined to it.
def port_status(CN, server_ip, file, server_name, container, samAccount, computerName, file_final, commands, add_row):
    message = ""
    try:
        P = ps.Port_Scanner(CN, server_ip, server_name, container, samAccount, computerName, commands)
        P.port_status(file)
        P.command_execute()
        #message = P.command_report()
        outputs = P.get_commandRes()
    except ValueError as Valer:
        messagebox.showwarning("An Error has occured: ", Valer)
    counter = 0
    for i in file_final:
        try:
            f = open(i, "w")
            f.write(outputs[counter])
            f.close()
            rg.make_markdown(i, add_row)
        except ValueError as Valer:
            print("Error has occurred: ", Valer)
        else:
            counter+=1

#This returns if a user would like to make a csv file or not.
def create_csv():
    answer = messagebox.askyesno("CSV File", "Would you like to generate a csv file?")
    return answer

#Main method that takes in os variables from a bash file and passess them into the appropriate functions to audit Active Directory instance within the current admin user's domain

def main():
    file_final = os.getenv('FILE_FINAL')
    CN = os.getenv('AD_USER')
    AD = ad.ADaudit(CN)
    samAccount = os.getenv('SAMACCOUNT')
    computerName = os.getenv('COMPUTER_NAME')
    containerUsers = os.getenv('CONTAINER_USERS')
    containerComputers = os.getenv('CONTAINER_COMPUTERS')
    usersObjectCategory = os.getenv('OBJECT_CATEGORY_USERS')
    computersObjectCategory = os.getenv('OBJECT_CATEGORY_COMPUTERS')
    containers = np.array([containerUsers, containerComputers])
    container3 = np.array([containerComputers])
    servObjectCategory = os.getenv('OBJECT_CATEGORY_SERVICE_ACCOUNT')
    objectCategories = np.array([usersObjectCategory, computersObjectCategory])
    objectCategories2 = np.array([usersObjectCategory, servObjectCategory])
    types = np.array(["User", "Computer"])
    N = os.getenv('DAYS_UNUSED')
    N2 = os.getenv('DAYS_LS')
    adminArray = os.getenv('ADMIN_ARRAY').split(',')
    commandsArray = os.getenv('COMMAND_ARRAY').split(',')
    con_serv = os.getenv('CONTAINER_SERVICE_ACCOUNT')
    containers2 = np.array([containerUsers, con_serv])
    server_name = os.getenv('SERVER_NAME')
    doc = ("# Audit Report for {} #\n\n ## Conducted By {} on {:%Y-%m-%d %H:%M:%S} ##\n").format(server_name, CN, datetime.datetime.now())
    AD = logon_info(containers, objectCategories, types, N, file_final, doc, AD)
    AD = last_set_pwd(containers2, objectCategories2, N2, file_final, AD)
    AD = get_admin(adminArray, file_final, AD)
    AD = service_account_audit(con_serv, file_final, AD)
    file = os.getenv('FILE_NAME')
    ip = os.getenv('SERVER_IP')
    file_final_port = os.getenv('COMMAND_OUTPUT')
    file_final_port_2 = os.getenv('COMMAND_OUTPUT_2')
    file_final_ports = np.array([file_final_port, file_final_port_2])
    AD = get_dn_status(container3, file_final, AD)
    OU = os.getenv("OU_SERV")
    file_xtr_row = os.getenv('FILE_ADD_ROW')
    AD = check_usernames(containerUsers, con_serv, containerComputers, OU, usersObjectCategory, file_final, AD)
    port_status(CN, ip, file, server_name, containerComputers, samAccount, computerName, file_final_ports, commandsArray, file_xtr_row)
    pdf_audit_report = os.getenv('PDF_FILE')
    pdf_command_report = os.getenv('COMMAND_OUTPUT_PDF')
    pdf_port_status = os.getenv('FILE_NAME_PDF')
    f = open(file_final, "r")
    print(f.read())
    f.close()
    labels = np.array(["User Names", "Computer Names", "Service Account Names"])
    values = np.array([int(AD.usernameInvalidCount), int(AD.computerNameInvalidCount), int(AD.servAccNameInvalidCount)])
    y = "Invalid Count"
    title = "Invalid names"
    image = os.getenv('USERNAME_IMAGE')
    answer = create_csv()
    if(answer == 1):
        csv_file = os.getenv('CSV_AUDIT')
        csv = AD.report_to_csv()
        f = open(csv_file, "w")
        f.write(csv)
        f.close()
        f = open(csv_file, "r")
        print(f.read())
        f.close()
    rg.bar_graph(file_final, image, labels, values, y, title)





if __name__ == "__main__":
    main()