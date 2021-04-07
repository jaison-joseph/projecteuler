n1=1
n2 = 1
ct = 2
while (len(str(n2))<1000):
    t=n2
    n2 += n1
    n1 = t
    ct += 1
    
print(ct, ": ", n2)