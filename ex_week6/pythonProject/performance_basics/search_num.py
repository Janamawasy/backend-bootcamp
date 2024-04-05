import time
import random
import matplotlib.pyplot as plt

def search_num1(lst, num):
    # time complexity : O(n)
    for i in range(len(lst)):
        if lst[i] == num:
            return i

def search_num2(lst, num):
    # time complexity: O(n*log(n)) -> O(log(n)) for each recursive calls, O(n) slicing operations
    middle = len(lst)//2
    if lst[middle] > num:
        return search_num2(lst[:middle], num)
    if lst[middle] < num:
        index = search_num2(lst[middle+1:], num)
        return index + middle + 1
    if lst[middle] == num:
        return middle

def search_num3(lst, num):
    # time complexity: O(log(n))
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == num:
            return middle
        if lst[middle] < num:
            low = middle + 1
        if lst[middle] > num:
            high = middle -1
    return -1

def test_time_comp(func, lst, n):
    start = time.perf_counter()
    func(lst, n)
    end = time.perf_counter()
    # print(f'for {n}: {end - start}')
    return end - start

# lst = [1,2,4,5,6,7,9,25,67,88,244,344, 423, 466, 488, 854,1000,29874, 49322, 50000, 54000]
#
# test_time_comp2(search_num1, lst,88)
# test_time_comp2(search_num1, lst,2)
# print('--------------------------')
# test_time_comp2(search_num2, lst,88)
# test_time_comp2(search_num2, lst,2)
# print('--------------------------')
# test_time_comp(search_num3, lst,88)
# test_time_comp(search_num3, lst,2)

def generate_lst(n):
    '''
    n - lst length
    '''
    lst = []
    for i in range(n):
        value = random.randint(1,1000000)
        lst.append(value)
    lst = sorted(lst)
    return lst

def run_tests():
    results_func1 = []
    results_func2 = []
    results_func3 = []
    lsts = []
    lst_len = [10, 100, 250, 500, 750, 1000, 2500]
    for i in lst_len:
        lsts.append(generate_lst(i))

    for lst in lsts:
        results_func1.append(test_time_comp(search_num1, lst, lst[random.randint(0, len(lst)-1)]))
        results_func2.append(test_time_comp(search_num2, lst, lst[random.randint(0, len(lst)-1)]))
        results_func3.append(test_time_comp(search_num3, lst, lst[random.randint(0, len(lst)-1)]))

    plt.plot(lst_len, results_func1, 'r')
    plt.plot(lst_len, results_func2, 'g')
    plt.plot(lst_len, results_func3, 'y')
    plt.show()

run_tests()