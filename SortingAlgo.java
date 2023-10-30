import java.util.Arrays;

public class SortingAlgo {

    /**
     * Sort a given array of int using merge sort algorithm
     * Source: <a href="https://www.programiz.com/dsa/merge-sort">programiz</a>
     * @param array An array of int that want to be sorted
     */
    public static void mergeSort(int[] array) {
        if (array.length > 1) {
            int mid = array.length / 2;
            int[] leftHalf = Arrays.copyOfRange(array, 0, mid);
            int[] rightHalf = Arrays.copyOfRange(array, mid, array.length);

            mergeSort(leftHalf);
            mergeSort(rightHalf);

            int i = 0, j = 0, k = 0;
            while (i < leftHalf.length && j < rightHalf.length) {
                if (leftHalf[i] < rightHalf[j]) {
                    array[k] = leftHalf[i];
                    i++;
                } else {
                    array[k] = rightHalf[j];
                    j++;
                }
                k++;
            }

            while (i < leftHalf.length) {
                array[k] = leftHalf[i];
                i++;
                k++;
            }

            while (j < rightHalf.length) {
                array[k] = rightHalf[j];
                j++;
                k++;
            }
        }
    }

    /**
     * Partition an array from start to end into three part using two pivots.
     * Uses lomuto with block partitioning method.
     * @param array The array that will be partitioned
     * @param start The start index of the subarray
     * @param end The end index of the subarray
     * @param blockSize The size of the block that will be used
     * @return An array with index 0 as the first pivot and index 1 as the
     * second pivot
     */
    public static int[] twoPivotBlockPartitioning(int[] array, int start, int end, int blockSize) {
        if (end <= start) {
            return new int[]{start, start};
        }

        int pivot1 = array[start];
        int pivot2 = array[end];

        if (pivot1 > pivot2) {
            int temp = pivot1;
            pivot1 = pivot2;
            pivot2 = temp;

            temp = array[start];
            array[start] = array[end];
            array[end] = temp;
        }

        int[] block = new int[blockSize];
        int i = start + 1, j = start + 1, k = start + 1;
        int numP = 0, numQ = 0;

        while (k < end) {
            int t = Math.min(blockSize, end - k);

            for (int c = 0; c < t; c++) {
                block[numQ] = c;
                numQ += (pivot2 >= array[k + c]) ? 1 : 0;
            }

            for (int c = 0; c < numQ; c++) {
                int temp = array[j + c];
                array[j + c] = array[k + block[c]];
                array[k + block[c]] = temp;
            }

            k += t;

            for (int c = 0; c < numQ; c++) {
                block[numP] = c;
                numP += (pivot1 > array[j + c]) ? 1 : 0;
            }

            for (int c = 0; c < numP; c++) {
                int temp = array[i];
                array[i] = array[j + block[c]];
                array[j + block[c]] = temp;
                i++;
            }

            j += numQ;
            numP = 0;
            numQ = 0;
        }

        int temp = array[i - 1];
        array[i - 1] = array[start];
        array[start] = temp;

        temp = array[j];
        array[j] = array[end];
        array[end] = temp;

        return new int[]{i - 1, j};
    }

    public static void twoPivotBlockQuickSort(int[] array, int start, int end) {
        if (array.length == 0) {
            return;
        }

        // Berdasarkan paper rujukan, untuk data ukuran 2^26, block size yang
        // optimal adalah 2^10. saya simpulkan bahwa untuk data ukuran 2^n,
        // block size yang optimal adalah 2^(floor(n/3) + 2)
        int blockSize = (int) Math.pow(2, Math.floor(Math.log(array.length) / Math.log(2) / 3 + 2));
        int[][] stack = new int[array.length][2];
        int top = -1;

        // Quicksort dimodifikasi hingga dalam bentuk iteratif (tapi
        // behaviornya tetap sama seperti recursive call) karena untuk data
        // yang terlalu besar, terjadi stack overflow
        stack[++top] = new int[]{start, end};

        while (top >= 0) {
            int[] range = stack[top--];
            start = range[0];
            end = range[1];

            if (start < end) {
                int[] pivots = twoPivotBlockPartitioning(array, start, end, blockSize);
                stack[++top] = new int[]{start, pivots[0] - 1};
                stack[++top] = new int[]{pivots[0] + 1, pivots[1] - 1};
                stack[++top] = new int[]{pivots[1] + 1, end};
            }
        }
    }

    public static void main(String[] args) {
        int[] array = {5, 7, 3, 1, 6, 9};
        twoPivotBlockQuickSort(array, 0, array.length - 1);
        System.out.println(Arrays.toString(array));

        array = new int[]{1, 2, 3, 4, 5};
        mergeSort(array);
        System.out.println(Arrays.toString(array));
    }
}