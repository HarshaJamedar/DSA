# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

def gcdOfStrings(str1, str2):
        
        if str1 + str2 != str2 + str1:
            return ""
        else:
            len1 = len(str1)
            len2 = len(str2)
            while len2:
                len1, len2 = len2, len1%len2
            
        
        return str1[:len1]

str1 = "ABCABC"
str2 = "ABC"

print(gcdOfStrings(str1, str2))