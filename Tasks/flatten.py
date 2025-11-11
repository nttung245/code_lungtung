from concurrent.futures import ThreadPoolExecutor
from os import cpu_count
import random

def scan(S):
    offset = [0] * (len(S) + 1)
    for i in range(1, len(S) + 1):
        offset[i] = offset[i - 1] + S[i - 1]
    return offset

def flatten(A, n):
    S = [len(row) for row in A]
        
    offset = scan(S)
        
    total_len = offset[-1]
    B = [0] * total_len
    
    def assign(i):
        off = offset[i]
        for j in range(S[i]):
            B[off + j] = A[i][j]
            
    with ThreadPoolExecutor(max_workers=cpu_count()) as exec:
        exec.map(assign, range(n))
        
    return B, total_len

def generate():
    return [[random.randint(0, 1000) for _ in range(1000)] for _ in range(1000)]

if __name__ == "__main__":
    # start = time.time()
    A = generate()
    res, total_len = flatten(A, len(A))
    print([res[0], res[-1], total_len])
    # print(f"Done in {time.time() - start:.2f} seconds")
