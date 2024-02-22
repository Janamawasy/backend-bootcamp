import random

def prime(x):
    prime_num_list = [2, 3]
    main_num_list = [random.randint(4, 150) for _ in range(x)]
    print(f'main_num_list : {main_num_list}')
    copy_main_list = main_num_list[:]
    while len(copy_main_list) > 0:  # Use > instead of >= to avoid unnecessary iteration
        for i in copy_main_list[:]:  # Iterate over a copy of main_num_list
            w = 0
            for j in prime_num_list:
                if i > j:
                    if i % j == 0:
                        # not prime
                        # print(i)
                        # print(copy_main_list)
                        copy_main_list.remove(i)
                        break  # Break the inner loop after removing the non-prime number
                    else:
                        w += 1
                else:
                    w += 1
            if w == len(prime_num_list):
                # i is prime num
                copy_main_list.remove(i)
                prime_num_list.append(i)
                copy_main_list = check_multiples(i, copy_main_list)
        if len(copy_main_list) == 0:
            print(f'prime_num_list: {prime_num_list}')
            break

def check_multiples(value, lst):
    copy_lst = lst[:]
    for i in lst[:]:
        if i % value == 0:
            copy_lst.remove(i)
    return copy_lst

prime(15)
