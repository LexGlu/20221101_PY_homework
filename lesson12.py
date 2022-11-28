import math

def task1():
    x = input('Enter nums as string: ').split()

    for element in x:
        print('*' * int(element))


# task1()


def task2(n):
    # n < p < 2n
    # n(2 ≤ n ≤ 50000)

    prime_nums = []
    count = 0

    # simple func. O(n) complexity.
    # def is_prime(num):
    #     for i in range(2, n):
    #         if not num % i:
    #             return False
    #     return True

    # O(√n) complexity, much faster
    def is_prime(num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if not num % i:
                return False
        return True

    for j in range(n + 1, 2 * n):
        if is_prime(j):
            prime_nums.append(j)
            count += 1

    print(f'Count of prime nums: {count}, list of prime nums: {prime_nums}')


task2(50000)


    # n < p < 2n
    # n(2 ≤ n ≤ 50000)


def task3(n):
    # min_n = min(n)
    # max_n = max(n)

    max_n, min_n = n[0], n[0]

    for i in n:
        if i > max_n:
            max_n = i
        if i < min_n:
            min_n = i

    print(f'min num: {min_n}, max num: {max_n}')



tup = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)

# task3(tup)


def task4(tup):
    print(tup[::-1])


tup4 = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# task4(tup4)


def task5(tup):
    lst = []
    count = 0

    for i in tup:
        if i % 2:
            lst.append(i)
            count += 1

    avg = sum(lst) / count

    print(f'avg: {avg}')


tup5 = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# task5(tup5)


def task6(inp):
    lst = [int(x) for x in inp.split()]
    print(f'list: {lst[1::3]}')


string = '8 32 5 87 2 43 53 23 5'

# task6(string)


def task7(lst_of_dicts):
    data = {}

    for d in lst_of_dicts:
        data[d[0]] = {'salary': d[1], 'gender': d[2], 'passport': d[3]}

    print(data)



inp = [
    ('Bob Moore', 330000, 'M', '1635777202'),
    ('Gina Moore', 12500, 'F', '1639999999'),
]

# task7(inp)


def task8(l1, l2):
    s1, s2 = set(l1), set(l2)
    res = sorted(list((s1 - s2)))
    print(res)


lst1 = [1, 3, 2, 5]
lst2 = [4, 3, 2, 6]
# task8(lst1, lst2)
