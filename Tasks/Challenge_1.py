import concurrent.futures
import random
import time

def MAIN(input_filename="input.txt"):
    time_start = time.time()
    with open(input_filename, "r") as file:
        lines = file.readlines()

    n, q = map(int, lines[0].strip().split())

    indices = [int(lines[i].strip()) for i in range(1, n + 1)]

    data = [indices[i:i+950] for i in range(0, n, 950)]

    with concurrent.futures.ProcessPoolExecutor() as exe:
        res = list(exe.map(Parallel, data, [q] * n))
     
    results = [item for row in res for item in row]  
    end_time = time.time()
    print(f"Thời gian thực thi: {end_time - time_start:.6f} giây") 
    return results

def Matrix_Multiply(mat_a, mat_b, q):    
    mat_res = [[0, 0], [0, 0]]
    mat_res[0][0] = (mat_a[0][0] * mat_b[0][0] + mat_a[0][1] * mat_b[1][0]) % q
    mat_res[0][1] = (mat_a[0][0] * mat_b[0][1] + mat_a[0][1] * mat_b[1][1]) % q
    mat_res[1][0] = (mat_a[1][0] * mat_b[0][0] + mat_a[1][1] * mat_b[1][0]) % q
    mat_res[1][1] = (mat_a[1][0] * mat_b[0][1] + mat_a[1][1] * mat_b[1][1]) % q
    return mat_res

def Matrix_Power(matrix, n, q):
    result = [[1, 0], [0, 1]]
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = Matrix_Multiply(result, base, q)
        base = Matrix_Multiply(base, base, q)
        n //= 2

    return result

def Fibonacci(n, q):
    if n == 0 or n == 1:
        return 1
    n += 1

    matrix = [[1, 1], [1, 0]]
    result = Matrix_Power(matrix, n // 2, q)
    if n % 2 == 0:
        return Matrix_Multiply(result, result, q)[0][1] % q
    res = (pow(result[0][0], 2) + pow(result[0][1], 2)) % q
    return res

def Parallel(lst, q):
    return [Fibonacci(x, q) for x in lst]

if __name__ == "__main__":
    # print(MAIN())
    MAIN()
