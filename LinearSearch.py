def l_search(data):
    x=int (input("Enter data : "))
    i=0
    while i<len(data):
        if data[i]==x:
            print("Found at position: ",i)
        else:
            print("Not found")
        i+=1
l=[145,98,63,52,0,85,41]
l_search(l)
