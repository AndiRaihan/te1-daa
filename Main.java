import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {

    static String[] fileNames = {
            "kecil_random", "kecil_sorted_asc", "kecil_sorted_desc",
            "sedang_random", "sedang_sorted_asc", "sedang_sorted_desc",
            "besar_random", "besar_sorted_asc", "besar_sorted_desc"
    };

    public static void main(String[] args) {
        Map<String, int[]> data = loadDataset();
        Map<String, String> memoryAllocationResults = new HashMap<>();
        Map<String, Double> runningTimeResults = new HashMap<>();

        for (int i = 1; i <= 5; i++) {
            try (FileWriter writer = new FileWriter("res/iter" + i + ".txt")) {
                for (String fileName : fileNames) {
                    runningTimeResults.put("merge sort: " + fileName,
                            profileRunningTime(data, fileName, "merge sort"));
                    writer.write("merge sort: " + fileName + " = " + runningTimeResults.get("merge sort: " + fileName) + " ms\n");
                    System.out.println("merge sort: " + fileName + " = " + runningTimeResults.get("merge sort: " + fileName) + " ms");
                }
                writer.write("=".repeat(100) + "\n");
                System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                data = loadDataset();
                for (String fileName : fileNames) {
                    String res = profileMemory(data, fileName, "merge sort");
                    memoryAllocationResults.put("merge sort: " + fileName, res);
                    writer.write("merge sort: " + fileName + " = " + res + "\n");
                    System.out.println("merge sort: " + fileName + " = " + res);
                }
                writer.write("=".repeat(100) + "\n");
                System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                data = loadDataset();
                for (String fileName : fileNames) {
                    runningTimeResults.put("two pivot block quick sort: " + fileName, profileRunningTime(data, fileName, "two pivot block quick sort"));
                    writer.write("two pivot block quick sort: " + fileName + " = " + runningTimeResults.get("two pivot block quick sort: " + fileName) + " ms\n");
                    System.out.println("two pivot block quick sort: " + fileName + " = " + runningTimeResults.get("two pivot block quick sort: " + fileName) + " ms");
                }
                writer.write("=".repeat(100) + "\n");
                System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                data = loadDataset();
                for (String fileName : fileNames) {
                    String res = profileMemory(data, fileName, "two pivot block quick sort");
                    memoryAllocationResults.put("two pivot block quick sort: " + fileName, res);
                    writer.write("two pivot block quick sort: " + fileName + " = " + res + "\n");
                    System.out.println("two pivot block quick sort: " + fileName + " = " + res);
                }
                writer.write("=".repeat(100) + "\n");
                System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static Map<String, int[]> loadDataset() {
        Map<String, int[]> dataSet = new HashMap<>();


        for (String fileName : fileNames) {
            try (BufferedReader reader = new BufferedReader(new FileReader("data/" + fileName + ".txt"))) {
                String line;
                int[] data = new int[0];
                while ((line = reader.readLine()) != null) {
                    data = extendArray(data, Integer.parseInt(line));
                }
                dataSet.put(fileName, data);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return dataSet;
    }

    private static int[] extendArray(int[] arr, int value) {
        int[] newArray = new int[arr.length + 1];
        System.arraycopy(arr, 0, newArray, 0, arr.length);
        newArray[arr.length] = value;
        return newArray;
    }

    private static String profileMemory(Map<String, int[]> data,
                                        String fileName, String functionType) {
        Runtime runtime = Runtime.getRuntime();
        System.gc();
        runSorting(data, fileName, functionType);
        long currentMemory = runtime.totalMemory() - runtime.freeMemory();

        long current = currentMemory / 1024;

        return "current memory usage: " + current + " KB";
    }

    private static void runSorting(Map<String, int[]> data, String fileName, String functionType) {
        switch (functionType) {
            case "merge sort":
                SortingAlgo.mergeSort(data.get(fileName));
                break;
            case "two pivot block quick sort":
                SortingAlgo.twoPivotBlockQuickSort(data.get(fileName), 0,
                        data.get(fileName).length - 1);
                break;
        }
    }

    private static double profileRunningTime(Map<String, int[]> data,
                                             String fileName,
                                             String functionType) {
        long startTime = System.nanoTime();
        runSorting(data, fileName, functionType);
        long endTime = System.nanoTime();
        return (double) (endTime - startTime) / 1000000;
    }
}
