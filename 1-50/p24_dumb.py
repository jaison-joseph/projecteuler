nos = '0123456789'

#def isnoice(x):
#    start_ind = str(x)[0]
#    for ch in str(x):
        
def chk():
    for i in range (len(nos)):
        s1 = nos[i:] + nos[0:i]
        s2 = s1[::-1]
        print(s1, s2)
 
chk()
nos = '0'+nos
print(nos)
chk()