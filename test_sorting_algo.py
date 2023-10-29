import unittest
from sorting_algo import merge_sort, two_pivot_block_partitioning, two_pivot_block_quicksort


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
    
    def test_two_pivot_block_partitioning(self):
            # Test case 1
        arr1 = [5, 2, 8, 4, 7, 1, 3]
        expected_output1 = (2, 4)
        output1 = two_pivot_block_partitioning(arr1, 0, len(arr1) - 1)
        self.assertEqual(output1, expected_output1)

        # Test case 2
        arr2 = [1, 2, 3, 4, 5]
        expected_output2 = (0, 4)
        output2 = two_pivot_block_partitioning(arr2, 0, len(arr2) - 1)
        self.assertEqual(output2, expected_output2)

        # Test case 3
        arr3 = [5, 4, 3, 2, 1]
        expected_output3 = (0, 4)
        output3 = two_pivot_block_partitioning(arr3, 0, len(arr3) - 1)
        self.assertEqual(output3, expected_output3)

        # Test case 4
        arr4 = [1]
        expected_output4 = (0, 0)
        output4 = two_pivot_block_partitioning(arr4, 0, len(arr4) - 1)
        self.assertEqual(output4, expected_output4)

        # Test case 5
        arr5 = []
        expected_output5 = (0, 0)
        output5 = two_pivot_block_partitioning(arr5, 0, len(arr5) - 1)
        self.assertEqual(output5, expected_output5)
        
    def test_two_pivot_quicksort(self):
        # Test case 1
        arr1 = [5, 2, 8, 4, 7, 1, 3]
        expected_output1 = [1, 2, 3, 4, 5, 7, 8]
        two_pivot_block_quicksort(arr1, 0, len(arr1) - 1)
        self.assertEqual(arr1, expected_output1)

        # Test case 2
        arr2 = [1, 2, 3, 4, 5]
        expected_output2 = [1, 2, 3, 4, 5]
        two_pivot_block_quicksort(arr2, 0, len(arr2) - 1)
        self.assertEqual((arr2), expected_output2)

        # Test case 3
        arr3 = [5, 4, 3, 2, 1]
        expected_output3 = [1, 2, 3, 4, 5]
        two_pivot_block_quicksort(arr3, 0, len(arr3) - 1)
        self.assertEqual((arr3), expected_output3)

        # Test case 4
        arr4 = [1]
        expected_output4 = [1]
        two_pivot_block_quicksort(arr4, 0, len(arr4) - 1)
        self.assertEqual((arr4), expected_output4)

        # Test case 5
        arr5 = []
        expected_output5 = []
        two_pivot_block_quicksort(arr5, 0, len(arr5) - 1)
        self.assertEqual((arr5), expected_output5)
if __name__ == '__main__':
    unittest.main()
