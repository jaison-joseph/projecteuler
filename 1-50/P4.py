#pallindrome

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def pall(num): #if num is pallindrome, 1
    num_in_str = str(num)
    if num_in_str == num_in_str[::-1]:
        return True
    else:
        return False

print(pall(121))

largest = 1
n1 = 1
n2 = 1
for i in range (1, 1000):
    for j in range (1, 1000):
        if pall(i*j) and i*j > largest:
            largest  = i*j
            n1 = i
            n2 = j

print(largest)
print(n1)
print(n2)

