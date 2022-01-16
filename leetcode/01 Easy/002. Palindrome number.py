# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

def isPalindrome(x):
        st1=str(x)
        st2=str(x)
        st2=st2[::-1]
        return st2==st1

print(isPalindrome(121))
print(isPalindrome(1231))