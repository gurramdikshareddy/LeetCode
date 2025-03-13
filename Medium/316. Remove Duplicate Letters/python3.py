class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = [0] * 26
        pos = 0

        for char in s:
            cnt[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            cnt[ord(s[i]) - ord('a')] -= 1
            if cnt[ord(s[i]) - ord('a')] == 0:
                break

        return "" if len(s) == 0 else s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))
