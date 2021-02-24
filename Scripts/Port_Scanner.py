#This class is designed to discover what processes are connecting to what ports on the domain server itself and the computers connected to the domain. 
from queue import Queue
import numpy as np
from pyad import *
import pyad.pyadutils
import re
import socket
import threading
import time
import logging
import numpy as np
from pypsexec.client import Client
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

class Port_Scanner:
    CN = ""
    Port_Messages = np.array([])
    dn_hosts = np.array([])
    server_ip = ""
    server_Domain_name = ""
    computerDN = ""
    samAccount = ""
    computerName = ""
    commands = np.array([])
    commandRes = np.array([])

#Initializes a Port_Scanner object that will be used to discover futher detail on port activity throughout a specified domain.
    def __init__(self, CN, server_ip, server_Domain_name, computerDN, samAccount, computerName, commands):
        if(CN == ""):
            raise ValueError("The common name cannot be null!")
        else:
            self.CN = CN

        if(self.check_ip(server_ip) == False):
            raise ValueError("The IP address must be in proper IPv4 format!")
        else:
            self.server_ip = server_ip
            self.dn_hosts = np.append(self.dn_hosts, self.server_ip)

        if(server_Domain_name == ""):
            raise ValueError("The Domain name cannot be null!")
        else:
            self.server_Domain_name = server_Domain_name

        if (computerDN == ""):
            raise ValueError("The distinguished name for the computer container cannot be null!")
        else:
            self.computerDN = computerDN

        if (samAccount == ""):
            raise ValueError("The samAccount name for the user cannot be null!")
        else:
            self.samAccount = samAccount

        if (computerName == ""):
            raise ValueError("The computer name cannot be null!")
        else:
            self.computerName = computerName

        self.commands = commands


    #This ensures that the ip address is of a valid format.
    def check_ip(self, ip):
        # Python program to validate an Ip address

        # Make a regular expression
        # for validating an Ip-address
        regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        # Define a function for
        # validate an Ip addess

            # pass the regular expression
            # and the string in search() method

        if (re.search(regex, ip)):
            return True

        else:
            return False

#This uses pyad to identify the computers that are within the domain. 
    def get_hosts(self):
        if(self.computerDN == ""):
            self.dn_hosts = np.append(self.dn_hosts, "No Hosts")
        else:
            hosts = adcontainer.ADContainer.from_dn(self.computerDN)
            for i in hosts.get_children():
                n = i.get_attribute("CN")
                self.dn_hosts = np.append(self.dn_hosts, str(n[0]))

#This method looks through the server and the computers connected to the server domain to identify all processes operating on open ports.
    def port_status(self, file):
        f = open(file, "w")
        f.write("")
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()
        self.get_hosts()
        #for i in self.dn_hosts:
        #target = i
        array = np.array([])
        for i in self.dn_hosts:
            target = i
            t_IP = socket.gethostbyname(target)
            array = np.append(array, t_IP)
        #message = ('\nHost: {} -> {}').format(t_IP, i)
        #message = ("\n{} ({}):\n").format(t_IP, i)
        #f = open(file, "a")
        #f.write(message)
        #f.close()
        message = ""
        def portscan(port, target, file, message):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((target, port))
                #print(i)
                with print_lock:
                    #print(target)
                    #print(port, 'is open')
                    message += ("\n## {} is open ##\n").format(port)
                    protocolname = 'tcp'
                    #print("Port: %s => service name: %s" % (port, socket.getservbyport(port, protocolname)))
                    message += ("## Port: {} => service name: {} ##\n").format(port, socket.getservbyport(port, protocolname))
                    f = open(file, "a")
                    f.write(message)
                    f.close()
                con.close()
            except:
                pass

            #f = open(file, "a")
            #f.write(message)
            #f.close()


        counter = 0
        for i in array:
            if(counter == 0):
                message = ("\n\n# Port Status:\n\n#{} -> IPv4: {} #\n").format(self.server_Domain_name, i)
            else:
                message = ("\n# {} -> IPv4: {} #\n").format(self.dn_hosts[counter], i)
            f = open(file, "a")
            f.write(message)
            f.close()
            counter += 1
            def threader():
                message = ""
                while True:
                    worker = q.get()
                    portscan(worker, i, file, message)
                    q.task_done()

            q = Queue()
            startTime = time.time()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(1, 500):
                q.put(worker)

            q.join()

            #print('Time taken:', time.time() - startTime)

#This uses pypsexec module to connect to a remote computer/server, execute specified commands on that computer/server and collect the returned information.
    def command_execute(self):

        import os
        import pytest
        import sys
        import time
        import logging
        import numpy as np
        from pypsexec.client import Client
        #Note this sign in setup is utilizing securely cached credentials within the OS rather than risking the exposure of the password.
        #User must be within an admin group with unrestricted privileges to use this!
        #Computer must be joined to the domain and you must be signed in as an admin with proper privileges.
        #The connection is encrypted.
        if (len(self.commands) == 0):
            print("There are no commands to execute!")
        else:
            for i in self.commands:

                username = ("{}@{}").format(self.samAccount, self.server_Domain_name)

                c = Client(str(self.computerName), username=str(username), encrypt=True)

                c.connect()
                try:
                    c.create_service()
                    stdout, stderr, rc = c.run_executable("cmd.exe", arguments=str(i))
                    stdout = stdout.decode("utf-8")
                    logger = logging.getLogger("pypsexec")
                    logger.setLevel(logging.INFO)
                    ch = logging.StreamHandler()
                    ch.setLevel(logging.INFO)
                    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    ch.setFormatter(formatter)
                    logger.addHandler(ch)
                    self.commandRes = np.append(self.commandRes, stdout)
                finally:
                    c.remove_service()
                    c.disconnect()

    def command_report(self):
        message = "# Command Execution Output #\n\n"
        x = 0
        for i in self.commandRes:
            message += ("# Command Result: #\n## {} ##\n## {} ##\n").format(self.commands[x], i)
            x += 1
        return message

    def toString(self):
        for i in self.commandRes:
            print("Command Result:\n", i, "\n")

