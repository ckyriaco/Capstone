**meeting start 3:08 pm**                                 
**_last meeting_**                                  
ambiguity error                             
pyad has cached credentials                                 
tree set                              
isolating users folders and containers                                  
admin has the ability to isolation                        
but as a result, there is collision                        
chris has a test script that may help                            
```#Testing to ensure that users are not ambiguous by distinguished name
user = aduser.ADUser.from_dn("distinguishedName")
#Testing to ensure that folders are not ambiguous when using distinguished name, Use the user folder for this.
container = adcontainer.ADContainer.from_dn("distinguishedName")
#Test retrieval of information from children within folder.
for i in container.get_children():
            cn = i.get_attribute("CN")
            dn = i.get_attribute("distinguishedName")
            samAccount = i.get_attribute("samaccountname")
            user = aduser.ADUser.from_dn(dn[0])
            objCat = user.get_attribute("objectCategory")```       
based on distinguished name                                    
starting up AD explorer                                      
searching with distinguished name                                     
test with a user container                            
make theres not issue with the folders                        
he should be working in us.ara.com instead of admin.ara.com                                        
he signed into a connection to active directory                                
copy over the value attribute of the distinguished name                                                
copy over the value of the attribute of the distinguished name and its folder                                    
the command worked and it is able to identify a distinguished name                                              
syntax error                        
iterating thru folder and getting common name, distinguished name and making sure it doesnt have any issues                      
its not retrieving the distinguished name                                             
printing dn                                   
printing ```container.getChildren()```                                                    
bring up distinguished name attribute                                    
having quotes in DN could cause problems?                                             
Issue identified                                        
invalid DN syntax                                           
windows is preventing us from querying and giving us the error                                
test fail when testing someone with high privileges, better to test user with simpler privilges                
someone from the HR dept                                 
it worked! no windows errors                                          
returns a list of ADUser objects                                               
by running ```TestAD.py```                                         
a user having a nickname in quotes may interfere with audit                        
AD is magic                                            
checks completed                                     
our group is giving ARA the classes and wanted to make sure the parameters were synonomous with ARAs servers                                      
when running audit there may be errors so need try catch to handle expected errors                                        
pywin takes over and stops things                              
wrap it in a try catch to alert that user has invalid DN                                              
but should investigate in more detail after get error                                                  
Dr ingham is writing it policies and has also been doing physical security for the company                      
make mantraps                                   
facility security officer has to do an assessment for physical security                                       
threat model is different for classified/ unclassified  facilities and security spending should match priority                                        
need to enforce security policy                             
accelerated masters 2nd bachelors                                     
for chris                                  
dr ingham teaches at 2 year school                      
advises get associates so you can show you completed something                                        
start with sym tools when grad with entry level security                               
start low                 
pay - stress balance?                                           
script tests shows that there is potential that ARA can use it                              
chris will do a few last edits                         
we will be adjorning here                            
ownership of script (intellectual property) belong to GMU                                    
not a problem                            
ara doesnt sell scripts like this to others                         
have a license in the github that lays it all out                                
prob in the readme                                        
phd work released it under guno license?                                    
dont want someone taking it and making money off of it                                              
dr asked himself why constantly dealing with bugs only for another to crop up later                          
use the immune system as a model for it security                                                   
immune system works for human body/vertibrates so also for it security                                        
plants, invertibrates immune system is different                                           
quantum tech for photography?                                                  
post quantum algorithm                                                        
we are not going to have the stuff ready in time                                                                                        
encryption is not useful if the data is recorded and then decrypted later when the technology is available                                                             
when quantum tech is widespread                                              
quantum computing exam                                           
dr chris?                                              
dont get phd from the same place as the other degrees because?                                           
phd helps in industry work                                            
other phds will be willing to listen to you because youre a peer                                      
other environments will not matter                                  
academia is no brainer                              
masters is sufficient for what chris wants to do                                                  
classes is easy, research and writeup is hard for phd                                               
dr ingham advisor said stop generating data and explain why you are getting the data                               
he already knew how to do that                                            
six years to get phd going in circles                                        
you can get phd later                                          
changed careers                                          
security is a way, an attitude a process, not a product or checkbox                                  

**meeting end pm**                    