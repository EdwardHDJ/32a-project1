from pathlib import Path
import shutil

def D2_function(p:Path)->None:
    shutil.copyfile(p,p.parent[0])

p1 = PureWindowsPath('C:\Test\myfile.py')
D2_function(p1)
