def print_aa(_list,intend=True,level=0):
        for each_on in _list:

                if isinstance(each_on,list):

                        print_aa(each_on,intend,level+1)
                else:
                        if intend:
                
                                print("\t"*level,end='')
                        
                        print(each_on)
