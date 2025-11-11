import multiprocessing as mp
from multiprocessing import Array
import time

def compute_prefix_sum_chunk(chunk_data):
    """Process a chunk of the array and compute its prefix sum."""
    start_idx, end_idx, arr_chunk, offset = chunk_data
    result_size = end_idx - start_idx
    result = Array('i', result_size)

    # Compute local prefix sum
    for i in range(len(arr_chunk)):
        if i == 0:
            result[i] = arr_chunk[i] + offset
        else:
            result[i] = result[i - 1] + arr_chunk[i]

    return start_idx, list(result)


def parallel_prefix_sum(arr, num_processes=None):
    """Compute prefix sum using all available CPUs."""
    if len(arr) == 0:
        return []

    # Use all available CPUs if not specified
    if num_processes is None:
        num_processes = mp.cpu_count()

    # For very small arrays, computing directly is faster
    if len(arr) <= 1000:
        result = [0] * len(arr)
        result[0] = arr[0]
        for i in range(1, len(arr)):
            result[i] = result[i - 1] + arr[i]
        return result

    # Limit processes to array size or available CPUs
    num_processes = min(num_processes, len(arr), mp.cpu_count())

    # Divide the array into chunks
    chunk_size = len(arr) // num_processes
    chunks = []

    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < num_processes - 1 else len(arr)
        chunks.append((start_idx, end_idx, arr[start_idx:end_idx], 0))

    # First pass: compute local prefix sums for each chunk
    with mp.Pool(processes=num_processes) as pool:
        local_results = pool.map(compute_prefix_sum_chunk, chunks)

    # Extract the final value from each chunk's prefix sum
    chunk_sums = [result[1][-1] for result in local_results]

    # Compute offsets for each chunk
    offsets = [0] * num_processes
    for i in range(1, num_processes):
        offsets[i] = offsets[i - 1] + chunk_sums[i - 1]

    # Second pass: apply offsets to chunks
    for i in range(num_processes):
        chunks[i] = (chunks[i][0], chunks[i][1], chunks[i][2], offsets[i])

    with mp.Pool(processes=num_processes) as pool:
        final_results = pool.map(compute_prefix_sum_chunk, chunks)

    # Combine results into the final array
    final_array = [0] * len(arr)
    for start_idx, result in final_results:
        for i, val in enumerate(result):
            final_array[start_idx + i] = val

    return final_array

def MAIN(my_arr: list):

    result = parallel_prefix_sum(my_arr)


    return result


if __name__ == '__main__':
    # Example usage
    start = time.time()
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(MAIN(my_arr))
    end = time.time()
    print(end - start)
