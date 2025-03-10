class Solution:
    vowels = "aeiou"

    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_count = {}
        count = 0
        consonants = 0
        start = 0
        vowel_seen = [0] * 5  # This will track how many of each vowel we have
        temp_i = start
        increment = 0

        # Iterate through each character in the word
        for i in range(len(word)):
            ch = word[i]

            if self.is_vowel(ch):
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                consonants += 1

            # While consonants are more than k, we shrink the window from the start
            while consonants > k:
                ch_removed = word[start]
                start += 1

                if self.is_vowel(ch_removed):
                    left = vowel_count[ch_removed] - 1
                    if left == 0:
                        del vowel_count[ch_removed]
                    else:
                        vowel_count[ch_removed] = left
                else:
                    consonants -= 1

                vowel_seen = [0] * 5
                temp_i = start
                increment = 0

            # Check if we have exactly k consonants and all vowels present
            if consonants == k and len(vowel_count) == 5:
                while True:
                    ch_temp = word[temp_i]
                    ch_index = self.vowels.find(ch_temp)

                    if ch_index == -1:
                        count += 1
                        break

                    increment += 1
                    vowel_seen[ch_index] += 1

                    if vowel_count.get(ch_temp) == vowel_seen[ch_index]:
                        increment -= 1
                        vowel_seen[ch_index] -= 1
                        count += 1
                        break

                    temp_i += 1

                count += increment

        return count

    def is_vowel(self, ch: str) -> bool:
        return ch in self.vowels
