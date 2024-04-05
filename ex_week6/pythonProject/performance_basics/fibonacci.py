import time
import matplotlib.pyplot as plt
def fibonacci_seq1(n):
    # time complexity: O(2^n)
    if n == 1:
        return [0,1]
    else:
        res = fibonacci_seq1(n-1)
        res.append(res[-1] + res[-2])
        return res

def fibonacci_seq2(n):
    # time complexity : O(n)
    seq = [0,1]
    for i in range(2,n):
        seq.append(seq[-1]+seq[-2])
    return seq

def test_time_comp(func, n):
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    # print(f'for {n}: {end - start}')
    return end - start


def run_tests():
    results_func1 = []
    results_func2 = []
    n = [1, 10, 100, 250, 400, 500, 600, 700, 800]
    for value in n:
        results_func1.append(test_time_comp(fibonacci_seq1, value))
        results_func2.append(test_time_comp(fibonacci_seq2, value))
    plt.plot(n, results_func1, 'r')
    plt.plot(n, results_func2, 'g')
    plt.show()

run_tests()