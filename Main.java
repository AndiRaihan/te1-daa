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

        for (int i = 1; i <= 5; i++) {
            try (FileWriter writer = new FileWriter("res/iter" + i + ".txt")) {
                try (FileWriter writerPureData = new FileWriter("res/iter_pure_data" + i + ".txt")){
                    for (String fileName : fileNames) {
                        double res = (profileRunningTime(data, fileName, "merge sort"));
                        writer.write("merge sort: " + fileName + " = " + res + " ms\n");
                        writerPureData.write(res + "\n");
                        System.out.println("merge sort: " + fileName + " = " + res + " ms");
                    }
                    writer.write("=".repeat(100) + "\n");
                    writerPureData.write("=".repeat(100) + "\n");
                    System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                    data = loadDataset();
                    for (String fileName : fileNames) {
                        double res = profileMemory(data, fileName, "merge sort");
                        writer.write("merge sort: " + fileName + " = " + "current memory usage: " + res + " KB" + "\n");
                        writerPureData.write(res + "\n");
                        System.out.println("merge sort: " + fileName + " = " + "current memory usage: " + res + " KB");
                    }
                    writer.write("=".repeat(100) + "\n");
                    writerPureData.write("=".repeat(100) + "\n");
                    System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                    data = loadDataset();
                    for (String fileName : fileNames) {
                        double res = (profileRunningTime(data, fileName, "two pivot block quick sort"));
                        writer.write("two pivot block quick sort: " + fileName + " = " + res + " ms\n");
                        writerPureData.write(res + "\n");
                        System.out.println("two pivot block quick sort: " + fileName + " = " + res + " ms");
                    }
                    writer.write("=".repeat(100) + "\n");
                    writerPureData.write("=".repeat(100) + "\n");
                    System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));

                    data = loadDataset();
                    for (String fileName : fileNames) {
                        double res = profileMemory(data, fileName, "two pivot block quick sort");
                        writer.write("two pivot block quick sort: " + fileName + " = " + "current memory usage: " + res + " KB" + "\n");
                        writerPureData.write(res + "\n");
                        System.out.println("two pivot block quick sort: " + fileName + " = " + "current memory usage: " + res + " KB");
                    }
                    writer.write("=".repeat(100) + "\n");
                    writerPureData.write("=".repeat(100) + "\n");
                    System.out.println("=".repeat(60) + "iter " + i + "=".repeat(60));
                } catch (IOException e) {
                    e.printStackTrace();
                }

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

    private static double profileMemory(Map<String, int[]> data,
                                        String fileName, String functionType) {
        Runtime runtime = Runtime.getRuntime();
        for (int i = 0; i < 3; i++) {
            runtime.gc();
        }
        long initialMemory = runtime.totalMemory() - runtime.freeMemory();
        runSorting(data, fileName, functionType);
        long currentMemory = runtime.totalMemory() - runtime.freeMemory();

        return (double) (currentMemory - initialMemory) / 1024;
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
