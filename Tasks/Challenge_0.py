import time
from concurrent.futures import ProcessPoolExecutor

def prefix_sum_chunk(chunk):
    """Tính prefix sum trong 1 chunk, trả về (prefix_chunk, tổng cuối cùng của chunk)"""
    result = []
    total = 0
    for x in chunk:
        total += x
        result.append(total)
    return result, total

def MAIN(arrayA):
    n = len(arrayA)

    # Tạm chia mảng thành 8 phần — con số hợp lý, không cần os/cpu_count
    # Executor sẽ dùng số core phù hợp tự động
    num_chunks = 192
    chunk_size = (n + num_chunks - 1) // num_chunks
    chunks = [arrayA[i:i + chunk_size] for i in range(0, n, chunk_size)]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(prefix_sum_chunk, chunks))

    offsets = [0]
    for _, chunk_sum in results[:-1]:
        offsets.append(offsets[-1] + chunk_sum)

    answer = []
    for (prefix_chunk, _), offset in zip(results, offsets):
        adjusted_chunk = [x + offset for x in prefix_chunk]
        answer.extend(adjusted_chunk)

    return answer

if __name__ == "__main__":
    A = list(range(1, 1_000_000))
    start = time.perf_counter()
    result = MAIN(A)
    end = time.perf_counter()

    print(result[:10])
    print(f"Thời gian thực thi: {end - start:.6f} giây")
