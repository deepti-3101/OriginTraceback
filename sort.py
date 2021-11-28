from collections import OrderedDict
main = OrderedDict()

def time_retrive(content):
    l=[]
    for i,j in content:
        l.append(j['postTime'])
    l.sort()
    for k in l:
        for i,j in content:
            if(j['postTime']==k):
                main[i]=j
    
    return main


  
