from pathlib import Path

def E_function(path_list:[Path],s:str)->[Path]:
        new_list = []
        for p in path_list:
            if p.suffix == s or p.suffix == s[1:]:
                new_list.append(p)

        return new_list   

p1 = Path('C:\Test\myfile.py')
p2 = Path('C:\Test2\myfile.py')
p3 = Path('C:\Test3\myfile.py')
list1 = [p1,p2,p3]

s='.py'

print(E_function(list1,s))
