## Port_Scanner.py Documentation

_This class is designed to discover what processes are connecting to what ports on the domain server itself and the computers connected to the domain._

### Import
Import Queue, numpy, pyad / pyadutils, re (Regular Expressions package), socket, threading, time, simplefilter

Line 12 
set simplefilter action to 'ignore' and set category to 'FutureWarning'

### Class Port_Scanner created
Tracks the processes connecting to ports on the domain server as well as any computers connected to the domain.

**Variables created:**
* _CN_ - variable that tracks user and pyad connection to active directory
* _Port_Messages_ - array of the port response messages
* _dn_hosts_ - array of the domain name hosts
* _server_ip_ - the IP address of the server
* _server_Domain_name_ - the domain name of the server
* _computerDN_ - distinguished name for the computer container 

### Constructor 
Initializes a Port_Scanner object which will be used to discover further detail on port activity throughout a specified domain.

Lines 24 - 27
Validates that the Common Name is not null

Lines 29 - 33
Validates that the IP address is in IPv4 format

Lines 35 - 38
Validates that the given domain name is not null

Lines 40 - 43 
Validates that the distinguished name for the computer container isn't null

### check_ip method 
Method that validates the given IP address is in proper format.

_regex_ - expression which defines a valid IP address that will be used for a search pattern

Lines 63 - 67 
Pass the regex variable into a search method to validate the given IP address

### get_hosts method
Method that uses the pyad package to identify computers that are within the AD domain.
* 

### port_status method
Method that looks through the AD server and the computers connected to the server domain to identify all processes operating on open ports.

_file_ - 

### portscan method
Method executed within the port_status method 





