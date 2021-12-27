from pathlib import Path
import os
import time
import shutil 

def get_input1()->str:
    'get an input from the user and check if the line is in the right format. If the format is right return its value. If format is wrong,ask for a input again'

    while True:
        s1 = input()
        try:
            p1 = Path(s1[2:])
            if ((s1.startswith('D') or s1.startswith('R'))and s1[1:2]==' ' and p1.exists()and p1.is_dir()):
                break
            print('ERROR')
        except:
            print('ERROR')
    return s1
def get_filelist1()->[Path]:
    'spilt the first input to a letter and a path,then put them on variables and decide to call which function.return the result of function'
    input_string = get_input1()
    path_string = input_string[2:]
    intput_path = Path(path_string)

    if input_string.startswith('D'):
        path_list = D1_function(intput_path)    
    elif input_string.startswith('R'):
        path_list = R_function(intput_path)

    for path in path_list:
        print(path)
    return path_list

def get_filelist2()->[Path]:
    'store the second input to a variable and decide to call which function, return the result of function'
    sec_input_string = get_input2()
    if sec_input_string.startswith('A'):
        sec_path_list = A_function(path_list)

    elif sec_input_string.startswith('N'):
        sec_path_list = N_function(path_list,sec_input_string)

    elif sec_input_string.startswith('E'):
        sec_path_list = E_function(path_list, sec_input_string)

    elif sec_input_string.startswith('T'):
        sec_path_list = T_function(path_list,sec_input_string)

    elif sec_input_string.startswith('<'):
        sec_path_list = small_function(path_list,int(sec_input_string[2:]))

    elif sec_input_string.startswith('>'):
        sec_path_list = large_function(path_list,int(sec_input_string[2:]))
    
    for path in sec_path_list:
        print(path)
    return sec_path_list

def get_filelist3()->None:
    'store the third input to a variable and decide to call which function'
    action_string = get_input3()
    for path in sec_path_list:
        if action_string.startswith('F'):
            F_function(path)
        if action_string.startswith('D'):
            D2_function(path)
        if action_string.startswith('T'):
            T2_function(path)

    
def D1_function(p:Path)->[Path]:
    'get a path list from the parameter and get all the file in that directory(not including subdirectory)'
    list1 = list(p.iterdir())
    for x in list1:
        if x.is_file() == False:
            list1.remove(x)
    list1.sort()
    return list1


def R_function(p:Path)->[Path]:
    'get a path from parameter and return all file in directory (including in subdirectory)'
    new_list = []
    list1 = list(p.iterdir())
    for path in list1:
        if path.is_file():
            new_list.append(path)
    new_list.sort()
    for path1 in list1:
        if path1.is_dir():
            new_list.extend(R_function(path1))
    return new_list

def get_input2()->str:
    'get the second input from the user and check if the line is in the right format. If the format is right return its value. If format is wrong,ask for a input again'
    
    while True:
        s2 = input()
        try:
            if (s2.startswith('A') and len(s2)== 1):
                break
            elif (s2.startswith('N')or s2.startswith('E')or s2.startswith('T')) and s2[1:2]==' ' and len(s2)>3:
                break
            elif (s2.startswith('<')or s2.startswith('>')) and s2[1:2]==' ' and int(s2[2:])>0 :
                break
            print('ERROR')
        except:
            print('ERROR')
    return s2

def A_function(path_list: [Path])->[Path]:
    'return the path of all the files in the path(a directory)'
    return path_list

def N_function(path_list:[Path],s:str)->[Path]:
    'get a string from parameter,then search a file match a particular name,  including extension'
    new_list = []
    for p in path_list:
        if p.name == s[2:]:
            new_list.append(p)

    return new_list

def E_function(path_list:[Path],s:str)->[Path]:
    'get a pathlist and string from parameter and search file with a particular extension(py and .py are included)'
    new_list = []
    for p in path_list:
        if p.suffix == s[2:] or p.suffix == '.'+s[2:]:
            new_list.append(p)

    return new_list   

def T_function(list2:[Path],s:str)->[Path]:
    'get a pathlist and string from parameter, then return the list of path of the file containing the string'
    new_list = []
    for p in list2:
        the_file = open(p,'r')
        text_list = the_file.readlines()
        for text in text_list:
            if text.find(s[2:])!= -1:
                new_list.append(p)
                break

    return new_list


def small_function(list1:[Path],i:int)->[Path]:
    'get a pathlist and int from parameter and return the list of path of files whose size is less than the int'
    new_list = []
    for p in list1:
        if os.path.getsize(p) < i :
            new_list.append(p)
    return new_list

def large_function(list1:[Path],i:int)->[Path]:
    'get a pathlist and int from parameter and return the list of path of files whose size is larger than the int'
    new_list = []
    for p in list1:
        if os.path.getsize(p) > i :
            new_list.append(p)
    return new_list

def F_function(p:Path)->None:
    'print the first line of the txt file'
    try:
        the_file = open(p,'r')
        print(the_file.readline(),end = '')
    except:
        print('NOT TEXT')
    finally:
        if the_file != None:
            the_file.close()

def D2_function(p:Path)->None:
    'make a duplicate file put it on the same directory'
    shutil.copyfile(p,Path(str(p)+'.dup'))

def T2_function(p:Path)->None:
    'modify the timestamp to the current time'
    timestamp = (0,int(time.time()))
    os.utime(p,timestamp)

def get_input3()->str:
    'get the third input from the user and check if the line is in the right format. If the format is right return its value. If format is wrong,ask for a input again'
    while True:
        s = input()
        try:
            
            if (s.startswith('F')or s.startswith('D')or s.startswith('T'))and len(s)==1:
                return s
            else:
                raise TypeError
        except:
            print('ERROR')

if __name__ == '__main__':
    path_list = get_filelist1()
    sec_path_list =  get_filelist2()

    if len(sec_path_list)>0:
        get_filelist3()
