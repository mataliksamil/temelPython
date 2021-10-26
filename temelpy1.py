nested_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flat_list=[]

#iterative function which calls itself untill there is no sublist of the current list
def flat_func(nlist): 
     for j in nlist: 
# check if there is a sublist
            if isinstance(j, list):
                flat_func(j)
            else:
#append instances in order if there is no sublist
                flat_list.append(j) 
    
flat_func(nested_list)
print(flat_list)
