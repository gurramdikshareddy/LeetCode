class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            current_value = roman_map[s[i]]
            
            if i < length - 1 and current_value < roman_map[s[i + 1]]:
                total -= current_value  # Subtract the current value
            else:
                total += current_value  # Add the current value
        
        return total
