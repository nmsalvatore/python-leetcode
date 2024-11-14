from itertools import zip_longest

class Solution:
    def merge_alternately(self, str1: str, str2: str) -> str:
        result = ""
        for i in range(max(len(str1), len(str2))):
            if i < len(str1): result += str1[i]
            if i < len(str2): result += str2[i]
        return result

    def merge_alternately_zip(self, str1: str, str2: str) -> str:
        result = ""
        for a, b in zip_longest(str1, str2, fillvalue=""):
            result += a + b
        return result
