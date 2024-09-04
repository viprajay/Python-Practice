def b_search(data,item):
    frst = 0
    lst = len(data)-1
    fnd = False
    while(frst<=lst and not fnd):
        mid =(frst+lst)//2
        if data[mid]==item:
            fnd = True
            break
        elif(item<data[mid]):
            lst = mid-1
        else:
            frst = mid+1
    return fnd
print(b_search([12,15,9,6,1,4],1))
