meeting start 2:00pm    
scripts running   
github   
run through it    
chris present scripts   
using pycharm   
scan on limited resources on    
takes 5 to 10 seconds    
runs through clients    
limited resources   
ara will be able to bring it up on a VM and give it whatever resources are needed   
script is quicker than pycharm boot up   
vm servers have a lot of resources to play with   
dr ingham has invitation to github   
pyad is a tool that is used industry wide   
less invasive to implement   
programming platform to run through VM    
nature of python makes auditing easier to work with   
simple class ADaudit   
5 of the 7 are covered    
naming convention    
distinguished names distinct to ara??   
users and computers    
convention    
will send to chris    
pass into through bash script as a driver   
passing variables    
ip of server is sensitive info     
constructor    
joined to domain   
domain admin has rights to query the info   
validating     
not passing credentials so more secure    
pyad    
initiate pyad is working correctly   
common name of admin and retrieve info   
user and computer are authorized    
get variables    
copy array not pass array    
get last login users    
which users have not changed their passwords in N days    
get login past N days    
finding all admin on a specified domain    
methods for generating reports    
port scanner   
this number one priority    
ports open and what is running on those ports   
formating reports will be improved   
currently whatever users have not changed passwords within 2 days    
admin report    
distinguish diff kind of admins  
manager flag set?   
KTG local   
local domain   
ports open asking from inside    
not scanning from outside?    
not nmap scan    
its looking at what is actively running on the ports    
port and service    
from the os initiate daemen mode       
its good   daemon mode go into os and retrieve from there   
pretty common method to check ipv4    
extent of where we have gotten so far    
naming conventions   
is it good info???    
yes!    
prettier reports      
getting good info!    
accurate as possible    
operating on a single domain    
run server on laptop is struggle    
windows 10 pro    
easily scalable good to think about that     
admin was worried about running scripts     
stress security   on this script   
windows run as    
the admins never log in as administrator    
ara two accounts normal everyday no special privileeges     
higher privilieges admin acccoumnt full blown admin   
run as admin     
one process run as admin   
principle of least privilege     
we dont want to put account info into script    
you can sign into your own domain    
dont want    
ara uses 2 factor authentication     
dr ingham present how    
run as administrator   
windows authenication     
for powershell    
rsa authentication and passrord    
2 factor    
powersheel running as administratior    
vs  regular user powershelll     
almost every need admin     
windows    
everything has run as administrtator      
sign in with credentialls    
same as join in with domain account     
sudu on linux    
precursor to windows run as feature    
chris prefers linux    
chris has an admin and regular account    
dont want login as root    
you want to login as user and become root     
only if system is too broken do we login as root   
automation languages like ansible    
changes will be made to run as administrator    
ansible will allow ARA to reach out and touch stuff that they need to audit    
run it within powershell    
linux system     
cant use linux networking     
we are on track    
getting experience is good    
getting info    
naming conventions sent to chris   
use regular expression to check computer names     
regex import in python     
to check computer names    
sounds quite reasonable    
we got a lot of snow getting more     
chris prather not able to attend   
safee ask about text report    
getting data is far more important    
approach is good      
personal suggestions for report format???    
not really       
one functionality    
send email how you manaually check if user has to login    
has someone    
ara has login log outside capability of active directory    
dont worry about that     
active directory does store when admin or user has last logged in    
ara would want to see privileges that are used    
verify that admins are using run as administrator     
dr ingham last logged in as admin several months ago     
hawaii login attempt didnt work   
local administrator info stored    
one example of valid reason to actually login as administrator    
we would contact the user and ask why they needed to login as an administrator      
standard computers if users had to login    
manually look at    
computer audit login record    
normal and expected logins    
log system     
did kenneth ever log in   
ara wants to monitor people who just do work while logged in as administrator     
flag for login required    
set to true     
auto login    
ara would want to know if there is false flag for login required (default setting)    
needs to be set to true    
nist alludes to this phenomenon   
bypassing login would be a violation    
would be very useful to know if login reguired flag    
UTC - 10    
3 hours      
this time is still fine    
meeting early in the morning is no good    
meeting end 3:52 pm   

meeting start 3:55 pm
went really well    
the other admin    
dr ingham liked the code   
report format    
html or printout    
dont want report to be in markdown or viewable to anyone other than admin     
qualis    
PDQ    
run as administrator    
go in as   
admin login is easier to debug    
system is not connected to internet no vulnerability   
not our thing about how their going to authenticate   
template to do with as they want    
csv    
create   
plugin to pdq    
biggest issue was retrieving info   
and the script is able to handle that    
dr ingham is happy   
does not need remediation   
or auto remediation     
stage 3 CMMC not needed?    
remediation is more stage 4    
next steps next week    
documentation for common vulnerabilities for login not required flag     
dr ingham didnt seem to be aware of account controls for active directory   
compile report on common vulnerabilities    
if an admin has logged on in active directory   
pyad has a way to check    
blockchain report due on 17th   
picking sections for report   
mine is original business practices     
first one   
chatting about pandemic
research more vulnerabilities
meeting end 4:34 pm