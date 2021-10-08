##password generator
import random


def passgen():
  print('####### password generator #######-------------')
  character='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUV'
  print('how many passwords do you want?.(input integer)')
  manypass=int(input())
  list = []
  
  print('do you want the same length for all the passwords? ..Y/N')
  answer=str(input())
  if answer == 'Y':
    print('give password length')
    length=int(input())
    password=''
    for i in range(manypass):
      for i in range(length):
        password += random.choice(character)
      print(password)
      password=''
  elif answer == 'N':
    for i in range(manypass):
      print('give pass'+str(i+1)+' length')
      length=int(input())
      password=''
      for i in range(length):
        password += random.choice(character)
      list.append(password + ',')
      password=''
    print(list)
  else :
    print('you must answer Y or N (case sensitive)')
    answer = str(input())
    if answer == 'Y':
      print('give password length')
      length = int(input())
      password = ''
      for i in range(manypass):
        for i in range(length):
          password += random.choice(character)
        print(password)
        password = ''
    elif answer == 'N':
      for i in range(manypass):
        print('give pass' + str(i + 1) + ' length')
        length = int(input())
        password = ''
        for i in range(length):
          password += random.choice(character)
        list.append(password + ',')
        password = ''
      print(list)
    else :
      print('must answer Y or N. Restarting application. . . .')
    passgen()
passgen()