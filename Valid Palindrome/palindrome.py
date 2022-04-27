# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def isPalindrome(s): 
    # Concatenate string removing all spaces and non alpha-numeric characters
    tmp = ''.join(c for c in s if c.isalnum())
    # Convert the whole string to lower case 
    check = tmp.lower()
    #true if the the string equals its reverse else false
    return True if (check[::-1] == check) else False

print(isPalindrome("racecar")) #Should return true
print(isPalindrome("hello")) #Should return False
