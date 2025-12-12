def sortm(l):
    newlist = []

    while (len(l)>0):

        mini = l[0]
        for i in range ( len(l)):
            
            if mini > l[i]:
                mini = l[i]
        newlist.append(mini)
        l.remove (mini)
    return newlist  


a = [1 , 4, 2, 17, 10, 15]
print (sortm(a))

