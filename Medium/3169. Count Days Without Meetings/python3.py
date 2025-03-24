from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        total_meeting_days = 0
        for start, end in merged:
            total_meeting_days += end - start + 1
        
        return days - total_meeting_days
