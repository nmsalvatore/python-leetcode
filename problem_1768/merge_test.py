import unittest
from merge import Solution

class TestMerge(unittest.TestCase):
    solution = Solution()

    def test_equal_lengths(self):
        self.assertEqual(self.solution.merge_alternately("abc", "pqr"), "apbqcr")

    def test_short_str1(self):
        self.assertEqual(self.solution.merge_alternately("ab", "pqrs"), "apbqrs")

    def test_short_str2(self):
        self.assertEqual(self.solution.merge_alternately("abcd", "pq"), "apbqcd")

    def test_equal_lengths_with_zip(self):
        self.assertEqual(self.solution.merge_alternately_zip("abc", "pqr"), "apbqcr")

    def test_short_str1_with_zip(self):
        self.assertEqual(self.solution.merge_alternately_zip("ab", "pqrs"), "apbqrs")

    def test_short_str2_with_zip(self):
        self.assertEqual(self.solution.merge_alternately_zip("abcd", "pq"), "apbqcd")

if __name__ == "__main__":
    unittest.main()
