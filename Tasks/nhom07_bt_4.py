import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import random

def quick_sort_sequential(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_sequential(left) + middle + quick_sort_sequential(right)

def merge_two_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def merge_pair(pair):
    """Helper function to merge a pair of arrays"""
    return merge_two_arrays(pair[0], pair[1])

def parallel_merge(sorted_chunks, num_processes):
    """
    Merge sorted chunks using a binary tree pattern, in parallel.
    """
    while len(sorted_chunks) > 1:
        merged_chunks = []
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            # Prepare merge tasks in pairs
            merge_tasks = []
            i = 0
            while i < len(sorted_chunks):
                if i + 1 < len(sorted_chunks):
                    # Pair (i, i+1)
                    merge_tasks.append((sorted_chunks[i], sorted_chunks[i + 1]))
                    i += 2
                else:
                    # Odd chunk out, keep it for next round
                    merged_chunks.append(sorted_chunks[i])
                    i += 1

            # Run merge tasks in parallel
            results = list(executor.map(merge_pair, merge_tasks))
            merged_chunks.extend(results)

        sorted_chunks = merged_chunks
    return sorted_chunks[0] if sorted_chunks else []

def quick_sort_parallel(arr, num_processes=None):
    if len(arr) <= 1:
        return arr

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    # Split into chunks
    chunk_size = len(arr) // num_processes
    chunks = []
    for i in range(num_processes):
        start = i * chunk_size
        end = len(arr) if i == num_processes - 1 else (i + 1) * chunk_size
        chunks.append(arr[start:end])

    # Sort chunks in parallel
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        sorted_chunks = list(executor.map(quick_sort_sequential, chunks))

    # Merge chunks using binary merge tree (parallel)
    return parallel_merge(sorted_chunks, num_processes)

def MAIN(arr, workers=None):

    if workers is None:
        workers = min(4, multiprocessing.cpu_count())

    result = quick_sort_parallel(arr.copy(), workers)

    
    final = []
    final.append(result[0])
    final.append(result[-1])
    return final

if __name__ == '__main__':
    # Generate random array of 1000 elements with values between 1 and 10000
    my_arr = [random.randint(1, 10000) for _ in range(1000)]
    print(MAIN(my_arr))

    