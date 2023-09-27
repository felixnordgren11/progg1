class Smooth:
    
    
    def smooth_a(a, n):
        res = [] #Create empty list
        for i in range(n):  #Add lsit elements at the beginning and end of the list for every iteration
            a.insert(0, a[0]) #Element in 
            a.insert(-1, a[-1])
            res= [sum(a[i-n:i+n+1])/(2*n+1) for i in range(n, len(a)-n)]  #list operation for average value for every i "surrounding" n.
        return res

    def smooth_b(a, n):
        res= [sum(a[:i+n+1])/len(a[:i+n+1]) for i in range(0, len(a)) if i-n<0]             #for values on left side. 
        res+= [sum(a[i-n:i+n+1])/(2*n+1) for i in range(n, len(a)) if i-n>=0 and i+n<len(a)]#for values in the middle not affected by n being outside list.
        res+= [sum(a[i-n:])/len(a[i-n:]) for i in range(0, len(a)) if i+n>=len(a)]          #for values when n is out of list on right side.
        return res

    def round_list(lst, n):
        rounded_lst = [round(i,n) for i in lst]
        return rounded_lst
'''
x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))
'''

