import tracemalloc
from sorting_algo import merge_sort


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

def profile_memory(data:dict, file_name:str, sorting_function):
    sorting_function(data[file_name])

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    current = current/(1024)
    peak = peak/(1024)

    return "current memory usage: " + str(current) + " KB, peak memory usage: " + str(peak) + " KB, " + "peak - current = " + str(peak - current) + " KB"

if __name__ == '__main__':
    data = load_dataset()
    
    
    memory_allocation_result = {}
    tracemalloc.start()
    for file_name in data.keys():
        memory_allocation_result["merge sort" + ": " + file_name] = profile_memory(data, file_name, merge_sort)
    
    for key, val in memory_allocation_result.items():
        print(key + "= ", val)