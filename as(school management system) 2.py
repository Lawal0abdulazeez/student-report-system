# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:12:00 2022

@author: user
"""

ans='y'
storage={'seun':['pry1','08105812632','male','77'],
        'lawali':['pry2','0810138304','female','43']}
acceptable=['1','2','3','4','q','Q']
sexi=['m','f']
classess=['pry1','pry2','pry3','pry4','pry5']
deletey=['y','Y','n','N']
def adder():
    name= input('enter student name ')
    level=input('enter student class ')
    while level not in classess:
        print('invalid class ')
        print('try again ')
        level=input('')
    gender=input('press m for male and f for female ')
    while gender not in sexi:
        print('invalid input')
        print('enter  valid option')
        gender=input(' ')
    age= int(input('enter student age '))
    while age not in range(1,100):
        print('enter valid age')
        age=int(input(' '))
    guardian_number = int(input('enter  number '))
    while len(str(guardian_number))>11:
        print('invalid option')
        print('enter valid option')
        guardian_number=input(' ')
    print('student name is ', name)
    print('student class is ', level)
    print('student gender is ', gender)
    print('student age is ', age)
    print('student guardian contact is ', guardian_number)
    std_profile={name:[level,gender,age,guardian_number]}
    return std_profile
while ans=='y':
    print('''
          ###################################
          ########### welcome ###############
          ###########    to   ###############
          ###########    our  ###############
          ########### student ###############
          ########### record  ###############
          ######## management system ########''')
    print('''
          ########################################################
          ########## press 1 to add new student ##################
          ########## press 2 to search for student ###############
          ########## press 3 to edit stident details #############
          ########## press 4 to delete student details ###########
          ########## press Q to exit       #######################
          ''') 
    
    
    res = input('enter your response')
    while res not in acceptable:
        print('wrong input')
        print('try again')
        print('''
          ########################################################
          ########## press 1 to add new student ##################
          ########## press 2 to search for student ###############
          ########## press 3 to edit stident details #############
          ########## press 4 to delete student details ###########
          ########## press Q to exit       #######################
          ''') 
        res = input('enter your response')
    if res == '1':
        addun=adder()
        storage.update(addun)
        print('you successfully added a student')
    elif res=='2':
        print('enter student name to search')
        srch=input('')
        while not srch in storage.keys():
            print('student not found try again')
            srch=input('')
        if srch in storage.keys():
            print(storage.get(srch))
    elif res=='3':
        print('enter student name to edit')
        edity=input('')
        while not edity in storage.keys():
            print('student not found try again')
            edity=input('')
        if edity in storage.keys():
            print(storage.get(edity))
            print('''
                  enter new details
                  ''')
            print('enter new name ')
            namee=input('')
            level=input('enter student class ')
            while level not in classess:
                print('invalid class')
                print('try again')
                level=input(' ')
            gender=input('press m for male and f for female ')
            while gender not in sexi:
                print('invalid input')
                print('enter  valid option')
                gender=input(' ')
            age= int(input('enter student age '))
            
            guardian_number = int(input('enter  number '))
            while len(str(guardian_number))>11:
                print('invalid option')
                print('enter valid option')
                guardian_number=input(' ')
            std_profild={namee:[level,gender,age,guardian_number]}
            storage.pop(edity)
            storage.update(std_profild)
            print(std_profild)
            print('you succesfully added',namee)
    
    elif res=='4':
        print('enter student name to delete')
        deleter=input(' ')
        while not deleter in storage.keys():
            print('student not found try again')
            deleter=input(' ')
        if deleter in storage.keys():
            storage.pop(deleter)
    elif res == 'q' or 'Q':
        print('Good bye')
        break
    print('do you wish to try again')
    ans = input('y/n')
print('''
         ################################################
         ############## thanks for choosing us ##########
         ##############     @ team D-prince    ###########
          ''')
            
print(storage)
          
          
