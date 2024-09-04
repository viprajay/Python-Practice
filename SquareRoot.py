def Root(num, tol):
    assume = num
    count = 0
    while True:
        count+=1
        s_root=0.5*(assume+(num/assume))
        z = abs(s_root-assume)
        if(z<tol):
            break
        assume = s_root
    return s_root
print("Square Root : ",Root(25,0.0000001))
