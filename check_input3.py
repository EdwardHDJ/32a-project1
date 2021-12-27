def get_input3()->bool:
    try:
        s = input()
        if (s.startswith('F')or s.startswith('D')or s.startswith('T'))and len(s)==1:
            pass
        else:
            open(1)
    except:
        print('ERROR')
        get_input3()
        

get_input3()
