# port scanner programm excercise for cyber security course

import socket #library that allows us to connect to machines through the internet
from IPy import IP #library that allows us to define an ip address

def scan(target):
    converted_ip=check_ip(target) #domain to ip conversion
    print('\n'+'[-] scanning target '+str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):#function for converting domains to ip.
    try:
        IP(ip)#using the ipy library IP function gives us the ip format.
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):#function for getting the banner from the ports
    return s.recv(1024)#the number is the number of bytes we want to receive.

def scan_port(ipaddress,port):
    try:
        sock=socket.socket() #the socket object that creates the connection.
        sock.settimeout(0.5) #this defines the time that the scan of the port will take,lower speed -lower accuracy
        sock.connect((ipaddress,port))
        try: # if we get a banner we print the port + the banner otherwise we just print the port
            banner=get_banner(sock)
            print('[+] port '+str(port)+'is open'+':'+str(banner))
        except:
            print ('[+] port '+str(port)+'is open')
    except:
        pass #this is so the program doesnt print all the closed ports.


#this is where the program starts running utilising all the functions above.
targets = input('[+] enter target/s to scan (either domain name or ip) (split multiple trgets with(,) :')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
