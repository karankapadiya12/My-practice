"""def p(s):
    temp= s[::-1]
    if s == temp:
        print("Yes is Palindrome ")
    else:
        print("Not palindrome :")
s = "nitin"
p(s)
"""

"""
def p1(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True

s = "nitin"
print(p1(s))

"""
"""
# using while loop

def palindrome(s):
    n = len(s)
    first = 0
    last = 0
    while (first<last):
        if s[first]==s[last]:
            first += 1
            last -= 1
            print("Yes is palindrome")
        else:
            print("No palindrome")
    return True
s = "nitin"
print(palindrome(s))
"""
