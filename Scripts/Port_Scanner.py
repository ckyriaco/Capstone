from queue import Queue
import numpy as np
from pyad import *
import pyad.pyadutils
import re
import socket
import threading
import time
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

class Port_Scanner:
    CN = ""
    Port_Messages = np.array([])
    dn_hosts = np.array([])
    server_ip = ""


    def __init__(self, CN, server_ip):
        if(CN == ""):
            raise ValueError("The Domain name cannot be null!")
        else:
            self.CN = CN

        if(self.check_ip(server_ip) == False):
            raise ValueError("The IP address must be in proper IPv4 format!")
        else:
            self.server_ip = server_ip
            self.dn_hosts = np.append(self.dn_hosts, self.server_ip)



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

    def get_hosts(self):
        hosts = adcontainer.ADContainer.from_dn('CN=Computers, DC=KTG, DC=local')
        for i in hosts.get_children():
            n = i.get_attribute("CN")
            self.dn_hosts = np.append(self.dn_hosts, str(n[0]))

    def port_status(self, file):
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()
        self.get_hosts()
        for i in self.dn_hosts:
            target = i
            t_IP = socket.gethostbyname(target)
            message = ('\nHost: {} -> {}').format(t_IP, i)
            #message = ("\n{} ({}):\n").format(t_IP, i)
            f = open(file, "a")
            f.write(message)
            f.close()
            message = ""
            def portscan(port, target, i, file, message):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((t_IP, port))
                    with print_lock:
                        #print(port, 'is open')
                        message += ("\n{} is open\n").format(port)
                        protocolname = 'tcp'
                        #print("Port: %s => service name: %s" % (port, socket.getservbyport(port, protocolname)))
                        message += ("Port: {} => service name: {}\n").format(port, socket.getservbyport(port, protocolname))
                        f = open(file, "a")
                        f.write(message)
                        f.close()
                    con.close()
                except:
                    pass

                #f = open(file, "a")
                #f.write(message)
                #f.close()


            def threader():
                while True:
                    worker = q.get()
                    portscan(worker, target, i, file, message)
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


