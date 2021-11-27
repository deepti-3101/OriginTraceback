from collections import OrderedDict
main = OrderedDict()

def sort(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for i in sorted_keys:
        data=a_dictionary[i]
        main[i]=data
    return main

main=sort({1:3,22:4,5:3})


    

