import random

import math_assertion
import dict_assertion
import list_assertion


def math_test():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f'test between {num1} and {num2}')
    print('is greater: ', math_assertion.is_bigger(num1,num2))
    print('is smaller: ', math_assertion.is_smaller(num1,num2))
    print('is equal: ', math_assertion.is_equal(num1, num2))

def list_test():
    lst = [1,2,3,[4,5,[6,7]]]
    val = 7
    print(f'test if {val} in {lst} ')
    print(list_assertion.value_in_list(val,lst))
    assert list_assertion.value_in_list(val,lst)


def dict_test():
    dict = {1:2,3:4,5:{6:7,8:{9:10}}}
    k = 8
    val = 10
    print(f'test if key {k} in dictionary {dict} :')
    print(dict_assertion.key_in_dict(k,dict))
    print(f'test if value {val} in dictionary {dict}')
    print(dict_assertion.value_in_dict(val,dict))
    assert dict_assertion.key_in_dict(k,dict)
    assert dict_assertion.value_in_dict(val,dict)

if __name__ == '__main__':
    math_test()
    print('-----------')
    list_test()
    print('-----------')
    dict_test()