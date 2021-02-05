# Meeting 2 notes
* made class available in Batch file 
* made batch file executable; when coding and passing credentials / attributes that could be sensitive, need to pass it from OS; batch file allows you to pass it from OS
* so far have a class that shows last login in N days (2 days in first example) *
* _CN_ = common name - name of AD user; pyad checks the OS and makes sure that you're already joined to the domain as a valid admin user w privileges to access the info 
* _dn_ = domain name
* _objCat_ = object category - key in exact category of users / groups we want to look at 
* _get_login_past_N_days_ - type = computer or user 
* next class is Active_Directory_ARA
* imported ADQuery class as _ad_ 
* imported _os_ 
* imported _numpy_ 
* bash file 
* exports os variables (_AD_USER_, _CONTAINER_USERS_, etc)
* executes the Active_Directory_ARA script 
* within pythonProject1 directory, made batch file executable to be run in gitbash
