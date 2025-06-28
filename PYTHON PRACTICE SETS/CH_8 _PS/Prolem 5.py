'''
***
**
*
'''

def pettern (n):
    if(n==0):
        return
    print("*"*n)
    pettern(n-1)
    
pettern(500)