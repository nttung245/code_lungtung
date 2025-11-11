import time
from multiprocessing import Process, cpu_count, Array
import random
import numpy as np

class Flatten:
    def __init__(self, array: list[list[int]]):
        self.array = array
        self.n = len(array)

    @staticmethod
    def count(array, begin, end, shared_array):
        for i in range(begin, end):
            shared_array[i] = len(array[i])

    @staticmethod
    def scan_exclusive(shared_array) -> list:
        offset = [0]
        total = 0
        for i in range(len(shared_array) - 1):
            total += shared_array[i]
            offset.append(total)
        return offset

    @staticmethod
    def to_B(off: int, array, i: int, shared_array_A, shared_array_B):
        for j in range(shared_array_A[i]):
            shared_array_B[off + j] = array[i][j]

    def copy_A_to_B(self, shared_array_A, offset: list, begin: int, end: int, shared_array_B):
        for i in range(begin, end):
            off = offset[i]
            Flatten.to_B(off, self.array, i, shared_array_A, shared_array_B)

def main():
    # Create sample data
    array_2d = [[random.randint(0, 1000) for _ in range(1000)] for _ in range(1000)]

    #print("Sample check:", array_2d[0][0], array_2d[-1][-1])

    flattener = Flatten(array_2d)
    n = flattener.n
    num_processes = cpu_count()
    chunk_size = n // num_processes

    # Shared memory for sizes of subarrays
    shared_sizes = Array('i', n)  # 'i' = signed int

    # Count phase (parallel)
    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = n if i == num_processes - 1 else (i + 1) * chunk_size
        p = Process(target=Flatten.count, args=(array_2d, start, end, shared_sizes))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Compute exclusive scan
    offset = Flatten.scan_exclusive(shared_sizes)

    total_elements = sum(shared_sizes)
    shared_flat = Array('i', total_elements)  # Shared flat array

    # Copy phase (parallel)
    processes.clear()
    for i in range(num_processes):
        start = i * chunk_size
        end = n if i == num_processes - 1 else (i + 1) * chunk_size
        p = Process(target=flattener.copy_A_to_B, args=(shared_sizes, offset, start, end, shared_flat))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Output result
    result = [shared_flat[0], shared_flat[-1], len(shared_flat)]
    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    print(f"Done in {time.time() - start:.2f} seconds")
