"""
Problem: Valid Anagram (LeetCode #242)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach:
Use a frequency dictionary to count characters in both strings and compare.

Time Complexity: O(n)
Space Complexity: O(1)  (since only 26 lowercase letters)
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True

# Example
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True
