import string
import time
import random
import matplotlib.pyplot as plt
from faker import Faker


def word_in_text1(text, word):
    # time complexity: O(n)
    lst = text.split(' ')
    count = 0
    for i in range(len(lst)):
        if lst[i] == word:
            count += 1
    return count


def word_in_text2(text, word):
    # time complexity : O(n)
    word_count = {}

    for i in text.split():
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    if word_count[word]:
        return word_count[word]
    else:
        return 0

def test_time_comp(func, text, word):
    start = time.perf_counter()
    func(text, word)
    end = time.perf_counter()
    # print(f'for {n}: {end - start}')
    return end - start

def generate_text(n):
    faker = Faker()
    return ' '.join(faker.words(n))

def run_tests():
    results_func1 = []
    results_func2 = []
    words_num = [1, 10, 100, 250, 500, 700, 1000, 2500]
    texts = []
    for i in words_num:
        texts.append(generate_text(i))

    for text in texts:
        results_func1.append(test_time_comp(word_in_text1, text, text.split(' ')[random.randint(0, len(text.split(' '))-1 )] ))
        results_func2.append(test_time_comp(word_in_text2, text, text.split(' ')[random.randint(0, len(text.split(' '))-1 )] ))

    plt.plot(words_num, results_func1, 'r')
    plt.plot(words_num, results_func2, 'g')
    plt.show()

run_tests()

