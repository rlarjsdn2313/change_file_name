import sys
import os
from datetime import datetime

error = ["Too Short Argv"]


def argv_checker(get):
    if len(get) < 1:
        return error[0]
    
    return 0

def file_checker(get):
    no_file_list = []
    final_return = ''
    for file_name in get:
        #if not os.path.isfile(os.getcwd() + '/' + file_name):
        if not os.path.isfile(file_name):
            no_file_list.append(file_name)
        
    if len(no_file_list) != 0:
        for no_file in no_file_list:
            final_return = final_return + no_file + ' '
        return final_return
    return 0

def last_file_check(get):
    already_file_list = []
    final_return = ''
    for file_name in get:
        #if os.path.isfile(os.getcwd() + '/' + file_name):
        if os.path.isfile(file_name):
            already_file_list.append(file_name)

    if len(already_file_list) != 0:
        if len(already_file_list) != 0:
            for no_file in already_file_list:
                final_return = final_return + no_file + ' '
            return final_return
    return 0

def file_changer(get, file_list):
    if len(get) != len(file_list):
        return "Error: file_changer first"

#    file_path = os.getcwd() + '\\'
#    print(file_path)
    for before_name, after_name in zip(get, file_list):
        os.rename(before_name, after_name)
    return 0
def main(get):
    print('\n')
    get = get[1:]
    check = argv_checker(get)
    new_get = []
    for v in get:
        if v not in new_get:
            new_get.append(v)
    get = []
    get = new_get
    if check != 0:
        print("Error In Argv...\nError:" + check)
        return 0
    print('Argv Check : Okay...\n')

    check = file_checker(get)
    if check != 0:
        print("Error In Files...\nNo File Error:\a" + check)
        return 0
    print("File Check : OKay...\n")

    file_name = str(input('Input File Name:'))
    file_form = str(input('Input File Form:'))
    file_list = []
    now_time = str(datetime.today().year) +  str(datetime.today().month).zfill(2) + str(datetime.today().day).zfill(2)
    i = 0

    while len(get) > i:
        file_list.append(now_time + '_' + '10703김건우' + '_' + file_name + '(' + str(i + 1) + ')' + '.' + file_form)
        i = i + 1
    print('\n')
    print(file_list)
    check = last_file_check(file_list)
    if check != 0:
        print("Error In Files...\nAlready File Error :" + check)
        return 0
    print("Already File Check : Okay...\n")

    check = file_changer(get, file_list)


main(sys.argv)