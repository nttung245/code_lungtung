import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def sort_chunk(chunk):
    return sorted(chunk)


def merge_sorted_arrays(sorted_lists):
    while len(sorted_lists) > 1:
        next_round = []
        for i in range(0, len(sorted_lists), 2):
            if i + 1 < len(sorted_lists):
                merged = merge_two_arrays(sorted_lists[i], sorted_lists[i + 1])
                next_round.append(merged)
            else:
                next_round.append(sorted_lists[i])
        sorted_lists = next_round
    return sorted_lists[0] if sorted_lists else []


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


def MAIN(arrayA):
    n = len(arrayA)
    if n <= 100000:
        # Với mảng nhỏ: dùng sorted() luôn
        return sorted(arrayA)

    cpu_count = multiprocessing.cpu_count()
    num_chunks = min(cpu_count, 8)  # giới hạn để tránh overhead
    chunk_size = (n + num_chunks - 1) // num_chunks

    chunks = [arrayA[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

    with ProcessPoolExecutor(max_workers=num_chunks) as executor:
        sorted_chunks = list(executor.map(sort_chunk, chunks))

    return merge_sorted_arrays(sorted_chunks)
