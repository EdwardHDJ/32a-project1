from pathlib import Path
def N_function(path_list:[Path],s:str)->[Path]:
    new_list = []
    for p in path_list:
        if p.name == s[2:]:
            new_list.append(p)

    return new_list

p1 = Path('C:\Test3\myfile.txt')
pathlist = [p1]
print(N_function(pathlist,'N myfile.txt'))
