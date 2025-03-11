class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char_count = [0] * 3  # array to keep track of character counts for 'a', 'b', and 'c'

        for right in range(len(s)):
            char_count[ord(s[right]) - ord('a')] += 1

            while all(c > 0 for c in char_count):  # check if all 'a', 'b', 'c' are present
                count += len(s) - right
                char_count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return count
