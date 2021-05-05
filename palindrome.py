import math
import re

class Solution(object):
    def isPalindrome(self, s):
        subbed = re.sub('[^A-Za-z0-9]+', '', s).lower()
        mid = math.floor(len(s) / 2)
        for i in range(mid):
            if subbed[i] == subbed[len(subbed) - i - 1]:
                continue
            return False
        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))

