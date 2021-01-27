#!/bin/bash/



export ADMIN_ARRAY='Domain Admins,Enterprise Admins,Key Admins,Schema Admins'
export AD_USER='Christopher Kyriacou'
export CONTAINER_USERS='CN=Users, DC=KTG, DC=local'
export OBJECT_CATEGORY_USERS='CN=Person,CN=Schema,CN=Configuration,DC=KTG,DC=local'
export Container_COMPUTERS='CN=Computers, DC=KTG, DC=local'
export OBJECT_CATEGORY_COMPUTERS='CN=Computer,CN=Schema,CN=Configuration,DC=KTG,DC=local'
export DAYS_UNUSED=2
export DAYS_LS=2
exec python Active_Directory_ARA.py
