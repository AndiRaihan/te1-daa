import copy
import random


def generate_data(size:int) -> list[int]:
    """generate list of random numbers ranging from 0 to 10.000
    Args:
        size (int): how many number should be in the array 
    """
    return [random.randint(0, 10000) for _ in range(size)]

if __name__ == "__main__":
    kecil_random = generate_data(2**9)
    sedang_random = generate_data(2**13)
    besar_random = generate_data(2**16)
    
    kecil_sorted_asc = sorted(kecil_random)
    sedang_sorted_asc = sorted(sedang_random)
    besar_sorted_asc = sorted(besar_random)
    
    kecil_sorted_desc = sorted(kecil_random, reverse=True)
    sedang_sorted_desc = sorted(sedang_random, reverse=True)
    besar_sorted_desc = sorted(besar_random, reverse=True)
    
    with open('data/kecil_random.txt', 'w') as f:
        for item in kecil_random:
            f.write("%s\n" % item)
    
    with open('data/sedang_random.txt', 'w') as f:
        for item in sedang_random:
            f.write("%s\n" % item)
    
    with open('data/besar_random.txt', 'w') as f:
        for item in besar_random:
            f.write("%s\n" % item)
    
    with open('data/kecil_sorted_asc.txt', 'w') as f:
        for item in kecil_sorted_asc:
            f.write("%s\n" % item)
    
    with open('data/sedang_sorted_asc.txt', 'w') as f:
        for item in sedang_sorted_asc:
            f.write("%s\n" % item)
    
    with open('data/besar_sorted_asc.txt', 'w') as f:
        for item in besar_sorted_asc:
            f.write("%s\n" % item)
    
    with open('data/kecil_sorted_desc.txt', 'w') as f:
        for item in kecil_sorted_desc:
            f.write("%s\n" % item)
    
    with open('data/sedang_sorted_desc.txt', 'w') as f:
        for item in sedang_sorted_desc:
            f.write("%s\n" % item)
    
    with open('data/besar_sorted_desc.txt', 'w') as f:
        for item in besar_sorted_desc:
            f.write("%s\n" % item)
    
    