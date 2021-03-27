#!/bin/bash/



export ADMIN_ARRAY='Domain Admins,Enterprise Admins,Key Admins,Schema Admins'
export COMMAND_ARRAY='/c netstat -ban,/c netstat -an'
export COMMAND_OUTPUT='Netstat-ban.txt'
export COMMAND_OUTPUT_2='Netstat-an.txt'
export COMMAND_OUTPUT_PDF='Command_Output.pdf'
export AD_USER='Christopher M Kyriacou'
export CONTAINER_USERS='CN=Users, DC=KTG, DC=local'
export OBJECT_CATEGORY_USERS='CN=Person,CN=Schema,CN=Configuration,DC=KTG,DC=local'
export Container_COMPUTERS='CN=Computers, DC=KTG, DC=local'
export OBJECT_CATEGORY_COMPUTERS='CN=Computer,CN=Schema,CN=Configuration,DC=KTG,DC=local'
export CONTAINER_SERVICE_ACCOUNT='CN=Managed Service Accounts, DC=KTG, DC=local'
export OBJECT_CATEGORY_SERVICE_ACCOUNT='CN=Person,CN=Schema,CN=Configuration,DC=KTG,DC=local'
export SERVER_IP='192.168.1.101'
export FILE_NAME='Port_Details.md'
export FILE_NAME_PDF='Port_Details.pdf'
export FILE_FINAL='Audit_Report.md'
export PDF_FILE='Audit_Report.pdf'
export OU_SERV='Corp'
export FILE_ADD_ROW='Netstat-ban.txt'
export CSV_AUDIT='Audit_Report.csv'
export COMPUTER_NAME='WIN-PNHM2JDCCEV'
export SAMACCOUNT='ckyriacou'
export SERVER_NAME='KTG.local'
export USERNAME_IMAGE='Username_Report.PNG'
export DAYS_UNUSED=2
export DAYS_LS=2
exec python Active_Directory_Audit.py
