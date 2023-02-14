## Left Pascal Star Triangle Code:
'''
*
* *
* * *
* * * *
* * *
* *
*
'''
def left_pascal(n):
    for i in range(1, 2*n+1):
        if i<=n:
            print('* '*i, end=' '*abs(n-i))
            print()
        else:
            print('* '*abs(2*n-i), end=' '*abs(n-i))
            print()
