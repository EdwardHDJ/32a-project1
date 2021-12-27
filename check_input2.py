def get_input2()->str:
    'check if the input follow the right format'
    s2 = input()
    try:
        if (s2.startswith('A') or s2.startswith('N')or s2.startswith('E')or s2.startswith('T')or s2.startswith('<')or s2.startswith('>'))== False :
            raise TypeError
        if (s2.startswith('A') and len(s2)> 1):
            raise TypeError
        if ((s2.startswith('N')or s2.startswith('E')or s2.startswith('T')) and s2[1:2]==' ' and len(s2)>3)==False:
            raise TypeError
        if ((s2.startswith('<')or s2.startswith('>')) and s2[1:2]==' ')==False:
            if int(s2[2:])<0:
                raise TypeError
    except:
        print('ERROR')
        get_input2()
    else:
        return s2

get_input2()
