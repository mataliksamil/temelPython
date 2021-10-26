
#extended control input 
lin = [[1, 2], [3, [4,5,[6,7]]], [8, 9, [10,11,12,[13,14]]]]
#to reverse stag1 list 
lin.reverse()
def revFunc(l):
    for i in l:
#reverse all lists as soon as they detected and iterate untill there is no sublist
        if isinstance(i, list):
            i.reverse()
            revFunc(i)
#no list means we are dealing with single scalar elements that cant be reversed
        else :
            continue
#call function
revFunc(lin)
print(lin)

