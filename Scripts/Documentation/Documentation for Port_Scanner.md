## Port_Scanner.py Documentation

_This class is designed to discover what processes are connecting to what ports on the domain server itself and the computers connected to the domain._

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

### Constructor 
* Initializes a Port_Scanner object which will be used to discover further detail on port activity throughout a specified domain.
* Validates that the Common Name is not null
* Validates that the IP address is in IPv4 format
* Validates that the given domain name is not null
* Validates that the distinguished name for the computer container isn't null

### check_ip method 
* Method that validates the given IP address is in proper format.
* _regex_ - expression which defines a valid IP address that will be used for a search pattern
* Pass the regex variable into a search method to validate the given IP address

### get_hosts method
* Method that uses the pyad package to identify computers that are within the AD domain.

### port_status method
* Method that looks through the AD server and the computers connected to the server domain to identify all processes operating on open ports.
* Goes through all the hosts within the domain (including server itself / all computers connected to it), identifies which ports are open and the processes running in it
* Writes over old status report txt file
* _file_ - txt file report of the full Audit report

### portscan method
* Method executed within the port_status method 
* Collects what information is running from which port, and appending file that is passed in with new content 
* Once function is done, able to retrieve information to txt file, and able to append it 

### threader method
* Takes in inputs for ports for every IP until there are no more ports left
* For a specific target port, puts IP address of specific client and passes in port itself 
* Utilizes daemon mode, allows for running through OS 




