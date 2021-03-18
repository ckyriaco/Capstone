## Port_Scanner.py Documentation

_This class is designed to discover what processes are connecting to what ports on the domain server itself and the computers connected to the domain._       
_This class is also designed to allow you to use psexec to run commands on the designated server's command prompt. This is mainly used to run nestat commands, but can be used to run any command._        
_Bennefits of psexec is that it is not disruptive to other users like an ssh. It briefly connects in using a temporary encrypted tunnel to the server._        
_This class utilizes socket and threading to discover what processes are running on a socket level on an Active Directory instance, and pypsexec 0.2.0 to execute commands on an Active Directory instance's command prompt from a remote host._        

### Import
* Import Queue, numpy, pyad / pyadutils, re (Regular Expressions package), socket, threading, time, simplefilter
* A filter is set to catch warnings to allow code to continue

### Class Port_Scanner created
* Tracks the processes connecting to ports on the domain server as well as any computers connected to the domain.

**Variables created:**
* _CN_ - variable that tracks user and pyad connection to active directory
* _Port_Messages_ - array of the port response messages
* _dn_hosts_ - array of the domain name hosts
* _server_ip_ - the IP address of the server
* _server_Domain_name_ - the domain name of the server
* _computerDN_ - distinguished name for the computer container 
* _samAccount_ - the samAccount name for the user 
* _computerName_ - the name of the computer
* _commands_ - array of commands
* _commandRes_ - array of command results

### Constructor 
* Initializes a Port_Scanner object which will be used to discover further detail on port activity throughout a specified domain.
* Validates that the Common Name is not null
* Validates that the IP address is in IPv4 format
* Validates that the given domain name is not null
* Validates that the distinguished name for the computer container isn't null

### get_commandRes method
* This method returns an array of command responses.

### check_ip method 
* This method validates the given IP address is in proper format.
* _regex_ - expression which defines a valid IP address that will be used for a search pattern
* Pass the regex variable into a search method to validate the given IP address

### get_hosts method
* This method uses the pyad package to identify computers that are within the AD domain.

### port_status method
* This method looks through the AD server and the computers connected to the server domain to identify all processes operating on open ports.
* Goes through all the hosts within the domain (including server itself / all computers connected to it), identifies which ports are open and the processes running in it
* Writes over old status report txt file
* _file_ - txt file report of the full audit

### portscan method
* This method executes within the port_status method 
* Collects what information is running from which port, and appending file that is passed in with new content 
* Once function is done, able to retrieve information to txt file and append to it 

### threader method
* Takes in inputs for ports for every IP until there are no more ports left
* For a specific target port, puts IP address of specific client and passes in port itself 
* Utilizes daemon mode, allows for running through OS 

### command_execute method
* This method utilizes the pypsexec module to connec to a remote computer or server, execute specified commands on that computer / server, and collect the returned information into an overall message.
* Using cache credentials, which only get cached during sign in as an admin

### command_report method
* This method builds the output message for the information collected from the command_execute method
* This is the report of commands that have been executed in raw format.

### toString method
* This method prints an overall report based on the output message created from the command_report method
* Generic toString method that shows all command results.

