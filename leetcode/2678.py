# 2678. Number of Senior Citizens


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for detail in details if int(detail[11:13]) > 60)
