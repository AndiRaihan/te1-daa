import unittest
from sorting_algo import merge_sort


class TestSortingAlgo(unittest.TestCase):

    def test_merge_sort(self):
        # Test case 1
        arr1 = [5, 2, 8, 4, 7, 1, 3]
        expected_output1 = [1, 2, 3, 4, 5, 7, 8]
        merge_sort(arr1)
        self.assertEqual(arr1, expected_output1)

        # Test case 2
        arr2 = [1, 2, 3, 4, 5]
        expected_output2 = [1, 2, 3, 4, 5]
        merge_sort(arr2)
        self.assertEqual((arr2), expected_output2)

        # Test case 3
        arr3 = [5, 4, 3, 2, 1]
        expected_output3 = [1, 2, 3, 4, 5]
        merge_sort(arr3)
        self.assertEqual((arr3), expected_output3)

        # Test case 4
        arr4 = [1]
        expected_output4 = [1]
        merge_sort(arr4)
        self.assertEqual((arr4), expected_output4)

        # Test case 5
        arr5 = []
        expected_output5 = []
        merge_sort(arr5)
        self.assertEqual((arr5), expected_output5)


if __name__ == '__main__':
    unittest.main()
