import time
import tracemalloc
from sorting_algo import merge_sort, two_pivot_block_quicksort


def load_dataset():
    data_set = {}

    with open('data/kecil_random.txt') as f:
        data_set["kecil_random"] = [int(line.rstrip()) for line in f]
    with open('data/kecil_sorted_asc.txt') as f:
        data_set["kecil_sorted_asc"] = [int(line.rstrip()) for line in f]
    with open('data/kecil_sorted_desc.txt') as f:
        data_set["kecil_sorted_desc"] = [int(line.rstrip()) for line in f]

    with open('data/sedang_random.txt') as f:
        data_set["sedang_random"] = [int(line.rstrip()) for line in f]
    with open('data/sedang_sorted_asc.txt') as f:
        data_set["sedang_sorted_asc"] = [int(line.rstrip()) for line in f]
    with open('data/sedang_sorted_desc.txt') as f:
        data_set["sedang_sorted_desc"] = [int(line.rstrip()) for line in f]

    with open('data/besar_random.txt') as f:
        data_set["besar_random"] = [int(line.rstrip()) for line in f]
    with open('data/besar_sorted_asc.txt') as f:
        data_set["besar_sorted_asc"] = [int(line.rstrip()) for line in f]
    with open('data/besar_sorted_desc.txt') as f:
        data_set["besar_sorted_desc"] = [int(line.rstrip()) for line in f]

    return data_set


def profile_memory(data: dict, file_name: str, sorting_function):
    sorting_function(data[file_name], start = 0, end = len(data[file_name]) - 1)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    current = current/(1024)
    peak = peak/(1024)

    return "current memory usage: " + str(current) + " KB, peak memory usage: " + str(peak) + " KB, " + "peak - current = " + str(peak - current) + " KB"

def profile_running_time(data: dict, file_name: str, sorting_function):
    start_time = time.time()
    sorting_function(data[file_name], start = 0, end = len(data[file_name]) - 1)
    end_time = time.time()
    return (end_time - start_time) * 1000



if __name__ == '__main__':
    data = load_dataset()
    memory_allocation_results = {}
    running_time_results = {}
    tracemalloc.start()
    
    for i in range(5):
        with open(f'res/iter{i}.txt', 'w') as f:
            for file_name in data.keys():
                running_time_results["merge sort" + ": " +
                                        file_name] = profile_running_time(data, file_name, merge_sort)
                f.write(f"merge sort: {file_name} = {running_time_results['merge sort' + ': ' + file_name]} ms")
                print(f"merge sort: {file_name} = {running_time_results['merge sort' + ': ' + file_name]} ms")
            f.write("=" * 100)
            print("=" * 60 + f"iter {i}" + "=" * 60)
            
            data = load_dataset()
            for file_name in data.keys():
                res = profile_memory(data, file_name, merge_sort)
                memory_allocation_results["merge sort" + ": " +
                                        file_name] = res
                f.write(f"merge sort: {file_name} = {res}")
                print(f"merge sort: {file_name} = {res}")
            f.write("=" * 100)
            print("=" * 60 + f"iter {i}" + "=" * 60)
            
            data = load_dataset()
            for file_name in data.keys():
                running_time_results["two pivot block quick sort" + ": " +
                                        file_name] = profile_running_time(data, file_name, two_pivot_block_quicksort)
                f.write(f"two pivot block quick sort: {file_name} = {running_time_results['two pivot block quick sort' + ': ' + file_name]} ms")
                print(f"two pivot block quick sort: {file_name} = {running_time_results['two pivot block quick sort' + ': ' + file_name]} ms")
            f.write("=" * 100)
            print("=" * 60 + f"iter {i}" + "=" * 60)
            
            data = load_dataset()
            for file_name in data.keys():
                res = profile_memory(data, file_name, two_pivot_block_quicksort)
                memory_allocation_results["two pivot block quick sort: " + file_name] = res
                f.write(f"two pivot block quick sort: {file_name} = {res}")
                print(f"two pivot block quick sort: {file_name} = {res}")
            f.write("=" * 100)
            print("=" * 60 + f"iter {i}" + "=" * 60)
    