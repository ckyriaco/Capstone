**meeting start 3:00pm**           
distinguished name work for ingham's account??                          
seen as two different accounts                                
you query yourself and that is reflected in a notification                         
python test live                      
distinguished names should be unique for each account, even if two accounts are the same person                                        
ingham needs list of imports                       
inghams distinguished name of account   
Writing a line to access a user from their common name as shown (It's recommended you use your admin CN:                                                                       
from Christopher Kyriacou to everyone:    3:05 PM                                 
```user = aduser.ADUser.from_dn(“CN=Kenneth Ingham,OU=IT,OU=Users,OU=Corporate,OU=Sectors,DC=us,DC=ara,DC=com”)```                                            
Ingham's computer is not attached to a AD domain                      
he needs to connect to vpn and login as admin                                     
wordpress bug                                      
switching domains                               
running powershell                           
win32 needs to know you are admin                                      
its working as admin!                                
```from pyad import``` is run                               
the command worked!!!!!                              
```git fetch```                       
Chris is happy that its connecting in!                                   
Ingham usually has multifactor auth with git                             
```git fetch``` is being blocked by multifactor on inghams github account                     
```git pull``` requires signin as admin                     
```git pull``` working on non admin
make note to change something from distinguished name to common name                                    
```bash_script_example_audit.txt``` is well documented!                              
bash needs to be run from the normal account                                 
```export ADMIN_ARRAY=``` looks good                             
we are auditing the different domains                                       
the distinguished names are sensitive because they can point to locations                                  
we can also make info undistinguishable so if info is compromised then it cant be exploited             
looking for admins even if they dont exist                         
how to alter the text file which is a stand in for the bash file                         
which is not visible right now                        
running as user who is running the script would simplify things                                      
not having to specify                              
how it is now was the recommended precautionary step from pyad documentation                          
the common names are not unique                              
the bash file ```bash_script_example_audit.txt``` is a list of user groups you can try to audit for                                 
locate folder                        
distinguished name of that particular folder                            
is needed for search                            
active directory explorer brought up for clarification                                                            
find folder that houses the users                        
and in the properties of the folder you can find the distinguished name  of the folder                       
ingham is in IT corporate group                              
test would prove that you can query a folder and the users therein                                   
may need to look at other query option                           
ingham found himself and his distinguished name                                   
he is in the corporate container                                                          
you also need object category                                    
we want the distinguished name of the computers folder                             
ingham found users that dont belong in the computer folder                                  
they are test accounts that were not removed after use                         
script has ability to detect if managed by field is set                                             
find the DN of the service accounts folder and that goes in the container service account                                       
***Chris will edit the code so when it searches for children it does not search for common names but distinguished names***                                              
skip server ip search                            
you can tell from the name of service accounts that they are service accounts                          
but sometimes you can't                                           
some of the names are horrible                               
its not just one prefix that denotes service accounts                                  
need to be reflected in the script                                  
```COMPUTER_NAME``` is whatever the name of the server is                                     
```SAM_ACCOUNT``` is the account that Ingham is using                                       
```SERVER_NAME``` is the name of the domain controller (could just be extracted out)                           
very happy that it connects                                     
we got the info we need                   
we will meet next Friday                                      
the problem was that common names were ambigious, simple fixes                        
ingham liked what our team did                                                  
chief security for the company is making sure they pass their assessments                                                                                                                    
great meeting!                                       
**meeting end 4:15pm**        