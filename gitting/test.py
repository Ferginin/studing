# a = input()
# i = 0
# ln = len(a)-1
# for i in range(ln+1):
#     if (a[i] == "a") and (i <= ln):
#         a = a[:i] + 'o' + a[i+1:]
#     elif (a[i] == "T") and (i <= ln):
#         a = a[:i] + 'R' + a[i+1:]
# print(a)

# lst = list(input().split())
# print(lst*3)

# lst = list(map(int, input().split()))
# mx = min(lst)
# mxi = 0
# l = 0
# for i in lst:
#     if mx < i:
#         mx = i
#     l += 1
# i = 0
# while (mx != lst[i]) and (i < l):
#     i+=1
# print(i)

# lst = list(input().split())
# k = 0
# for i in lst:
#     if(len(i) > 3):
#         lst[k] = lst[k].lower()
#     if(len(i)%2 == 1):
#         lst[k] = i.capitalize()
#     k+=1
# print(lst)

# N = int(input())
# lst = list()
# for i in range(N):
#     lst.append(i)
# print(lst)

# s = input().strip().split()
# lst = list()
# lst_res = list()
# for key in s:
#     lst.append(int(key))
# for key in lst:
#     if key % 2 == 0:
#         lst_res.append(key)
# print(lst_res)

# lst = list(int(input().strip().split()))

# lst = list(map(int, input().strip().split()))
# lst_res = list()
# k = 0
# for i in lst:
#     lst_res.append((k,i))
#     k += 1
# print(lst_res)

# lst = list(input().strip().split())
# k = 0
# for key in lst:
#     lst[k] = lst[k].upper()
#     k += 1
# print(lst)

# lst = list(input().strip().split('\t'))
# mx_count = 0
# for key in lst:
#     if lst.count(key) > mx_count:
#         mx_count = lst.count(key)
# print(mx_count)

# lst = list(input().strip().split())
# dc = dict()
# dc = {key: ord(key) for key in lst}
# print(dc)

# def check_list(numbers):
#     mx = max(numbers)
#     mn = min(numbers)
#     sr = mx-mn
#     k = 0
#     for i in numbers:
#         k+=1
#     return k, sr

# def my_det(numbers):
#     D = numbers[1]*numbers[1] - 4*numbers[0]*numbers[2]
#     return D

# import math
# def squares(radiuses):
#     i = 0
#     for key in radiuses:
#         radiuses[i] = round(math.pi * key*key,2)
#         i+=1
#     return radiuses

# import math
# def find_solution(list):
#     d = (list[1]*list[1])-(4*list[0]*list[2])
#     if(d < 0):
#         return None
#     if(d==0):
#         x = round(-list[1]/(2*list[0]),2)
#         return x
#     if(d > 0):
#         x1 = round((-list[1] - math.sqrt(d))/(2*list[0]), 2)
#         x2 = round((-list[1] + math.sqrt(d))/(2*list[0]), 2)
#         return x1, x2

# A = [11000]
# print(id(A))
# B = A[:]
# print(id(B))
# B[0] = "bob"
# print(id(A))
# print(id(B))
# print(B)

# s = input()
# k = 0
# for i in s:
#     if(i.isalpha()):
#         k+=1
# print(k)

# s = input()
# k = 0
# for i in s:
#     if(i.isdigit()):
#         k+=1
# print(k)

# s = input()
# lst = list()
# for key in s:
#     if(key.isalpha() == False) and (key.isdigit() == False):
#         lst.append(key)
# print(lst)

# lst = list(input().strip().split())
# lstres = list()
# k = 0
# for keys in lst:
#     if(len(keys) % 2 == 0):
#         k+=1
# print(k)

# def create_dict(st):
#     d = dict()
#     st1 = st.strip().split()
#     lst = list()
#     for key in st1:
#         lst.append(key)
#     d = d.fromkeys(lst)
#     return (d)

# create_dict("asg asg drtu asgadsg")

# def create_dict(st):
#     d = dict()
#     st1 = st.strip().split()
#     lst = list()
#     for key in st1:
#         lst.append(key)
#     d = {key: len(key) for key in lst}
#     return (d)

# print(create_dict("asg asdshg drtu asgadsg"))

# def create_dict(st):
#     d = dict()
#     d = {key: ord(key) for key in st}
#     return (d)

# print(create_dict("asgasd"))

# def check_dict(dct, inp_str):
#     ln = len(inp_str)
#     lst_keys = list(dct.keys())
#     for key in lst_keys:
#         if(int(key) == ln):
#             return dct.get(key)
#     dct[len(inp_str)] = inp_str
#     return dct

# print(check_dict({'3': "sdg", '5': "dsgrt", '2': "as", '8': "sdhsdhuj"}, "dsgrts"))

# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#         pass


# class MyStr(str):
#     def join(self):
#         return super().join()

# class MyStr(str):
#     def join(self, iterable):
#         new_iterable = []
#         for item in iterable:
#             if isinstance(item, str):
#                 new_iterable.append(item)
#             else:
#                 new_iterable.append(str(item))
#         return super().join(new_iterable)

# def do_filter(lst):
#     return list(filter(lambda x: x%2==1, lst))

# def do_map(lst):
#     lst = list(map(lambda x: x*2, lst))
#     return lst

# print(do_map([2, 3, 6]))

# def create_pairs(lst):
#     return dict(zip(lst[0], lst[1]))

# print(create_pairs(['1245', 'reye']))

# def do_lambda(lst):
#     lst_res = list(map(lambda y: y**2, filter(lambda x: x%2==0, lst)))
#     return lst_res

# print(do_lambda([2,3,4,5]))

# class MyList(list):
#     def append(self, value):
#         if isinstance(value, int) or isinstance(value, float):
#             super().append(value)
    
# l = MyList()
# # l.append(5)
# l.append('a')
# l.append(6)
# print(l)

# class MyStr(str):
#     def __len__(self):
#         return len(list(filter(lambda x: x.isdigit(), self)))
           

# a = MyStr("ages25dg63")
# print(len(a))

# class MyList(list):
#     def __len__(self):
#         return len(list(filter(lambda x: isinstance(x, int) or isinstance(x, float), self)))
    
# a = MyList([12, -52, 'fd', '32t'])
# print(len(a))

# def solve(lst):
#     return list(filter(lambda x: ((len(str(x)) == 3) and (str(x)[0] != '-')) or ((len(str(x)) == 4) and (str(x)[0] == '-')), lst))

# a = [-53, 123,24215,3,412]
# print(solve(a))

# import math
# def solve(lst):
#     return list(map(lambda x: round(math.sqrt(x), 2), filter(lambda y: y%2 == 0, lst)))

# a = [-53, 126, 24215, 4, 412]
# print(solve(a))

# def solve(lst):
#     res_list = list()
#     for st in lst:
#         if(sum(key.isdigit() for key in st) >=3):
#             res_list.append(st)
#     return res_list

# a = ['as', 'asfg12l6', '125512', 'sdgshdf']
# print(solve(a))

# def solve(lst):
#     res_list = list()
#     for st in lst:
#         if (sum((key.isdigit() for key in st)) == 0 and (st[0].isupper())):
#             res_list.append(st)
#     return res_list

# a = ['as', 'Asfg12l6', '125512', 'Sdgshdf']
# print(solve(a))


# class Student:
#     def __init__(self, group = 2303, surname = 'Петров'):
#         self.group = group
#         self.surname = surname

# a = Student(1234)
# print(a.group)
# print(a.surname)

# import math
# class Circle:
#     def __init__(self, radius = math.pi, center = (0, 0)):
#         self.radius = radius
#         self.center = center

# a = Circle(13.56, (1, 12))
# print(a.radius)
# print(a.center)

# class Student:
#     def __init__(self, group = 2303, surname = 'Петров'):
#         self.group = group
#         self.surname = surname
#     def __str__(self):
#         return f"{self.group}: {self.surname}"
        
# a = Student()
# print(a)

# import math
# class Circle:
#     def __init__(self, radius = round(math.pi, 2), center = (0, 0)):
#         self.radius = radius
#         self.center = center
#     def __str__(self):
#         return f"Circle: radius={self.radius}; center={self.center}"

# a = Circle(13.56, (1, 12))
# print(a)

# # #create_matrix
# import numpy as np
# def create_matrix(data):
#     return np.array(data)
# A = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# A = create_matrix(A)
# print(A)'

# import numpy as np
# def get_info(data):
#     sum_x = len(data.sum(axis=1))
#     sum_y = len(data.sum(axis=0))
#     return (sum_x, sum_y)
# a = np.array([[1, 2, 3], [1, 2, 3]])
# print(get_info(a))


# import numpy as np
# def solve_system(data, result):
#     return np.linalg.solve(data, result)

# import numpy as np

# def hsum_array(matrix):
#     # Суммируем элементы по каждой строке и возвращаем вектор сумм
#     return np.sum(matrix, axis=1)

# # Пример использования функции
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# result = hsum_array(matrix)
# print(result)

# import numpy as np
# def min_array(data):
#     return np.min(data)
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# result = min_array(matrix)
# print(result)

# import numpy as np
# def mean_array(data):
#     return round(np.mean(data), 2)
# matrix = np.array([[5, 10, 3], [8, 2, 9], [4, 7, 1]])
# mean_value = mean_array(matrix)
# print(mean_value)

# import numpy as np
# def cos_array(angle_matrix):
#     rows, cols = angle_matrix.shape
#     cos_values = np.zeros((rows, cols))
    
#     for i in range(rows):
#         for j in range(cols):
#             cos_val = round(np.cos(angle_matrix[i, j]), 2)
#             cos_values[i, j] = cos_val
    
#     return cos_values

# # Пример использования функции
# angle_matrix = np.array([[157, 136, 209], [43, 103, 170], [184, 11, 36]])
# cosine_matrix = cos_array(angle_matrix)
# print(cosine_matrix)

# import numpy as np

# def cov_array(data_matrix):
#     cov_matrix = np.cov(data_matrix)
#     rows, cols = cov_matrix.shape
#     rounded_cov_matrix = np.zeros((rows, cols))
    
#     for i in range(rows):
#         for j in range(cols):
#             rounded_cov_matrix[i, j] = round(cov_matrix[i, j], 2)
    
#     return rounded_cov_matrix

# # Пример использования функции
# data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# covariance_matrix = cov_array(data_matrix)
# print(covariance_matrix)


# st = input()
# ks = 0
# kd = 0
# for i in range(len(st)):
#     if(st[i].isdigit()):
#         kd+=1
#     if(st[i].isalpha()):
#         ks+=1
# if(ks == kd):
#     print("True")
# else:
#     print("False")

# st = input()
# res = list()
# for i in range(len(st)):
#     if(i % 3 == 0):
#         res.append('-')
#     else:
#         res.append(st[i])
# print("".join(res))

# st = input()
# res = list()
# for i in range(len(st)):
#     if(st[i].isalpha()):
#         res.append(st[i].upper())
#     elif(st[i].isdigit()):
#         res.append(st[i])
# print("".join(res))

# def three_alf(data):
#     k = 0
#     for key in data:
#         if(key in alf):
#             k+=1
#     if k>=3:
#         return True
#     else:
#         return False
    
# res = list()
# alf = 'aeiouyAEIOUY'
# st = input().split(" ")
# for i in st:
#     if(three_alf(i)):
#         res.append(i)
# print(res)


# def num_count(st, key):
#     for i in st:
#         if(i == key):
#             k+=1
#     return(k>3)

# st = input().split(" ")
# res = list()
# alf = (st)
# # for i in st:
# #     alf.__add__(i)
# print(alf)


# # Ввод данных с клавиатуры
# input_string = input("Введите элементы списка через пробел: ")
# # Переход от строки к списку целых чисел
# input_list = list(map(int, input_string.split()))
# # Создание нового списка только с элементами, встречающимися более 2 раз
# result_list = [x for x in input_list if input_list.count(x) > 2]
# # Вывод результата
# print(result_list)


# st = input().split()
# res = list()
# for i in range(len(st)):
#     fl = False
#     for j in range(len(st)):
#         if(i != j):
#             if(abs(int(st[i])) % abs(int(st[j])) == 0):
#                 fl = True
#     if(fl):
#         res.append(int(st[i]))
# print(res)

# import math
# def solve(data):
#     res = list()
#     for key in data:
#         if(key % 2 == 0):
#             res.append(round(math.sqrt(key), 2))
#     return res

# print(solve([52, 8, 51, 66, 42]))

# def solve(obj):
#     res = list()
#     for key in obj:
#         fl = True
#         if(key[0].isupper()):
#             for a in key:
#                 if(a.isdigit()):
#                     fl = False
#             if(fl):
#                 res.append(key)
#     return(res)

# print(solve(['zUHfBaNV', 'VIF9x', 'OkOeLg']))


# def check_inheritance(data):
#     res = list()
#     for i in range(len(data)-1):
#         if(issubclass(data[-1], data[i])):
#             res.append(data[i])
#     return res

# print(check_inheritance([int, str, complex, dict, bool]))

# def check_instance(data):
#     res = list()
#     for key in data[0]:
#         if(isinstance(data[1], key)):
#             res.append(key)
#     return res

# print(check_instance([[int, str, complex, dict], 'Hello']))


# def iter(data):
#     if data is not None:
#         print(data[0])
#         iter(data[1])

# iter((1, (2, (3, (4, (5, None))))))

# def prepend(x, data):
#     return (x, data)

# def reverse(node):
#     prev = None
#     current = node

#     while current:
#         next_node = current[1]
#         current = (current[0], prev)
#         prev = current
#         current = next_node
#     return prev

# print(reverse((1, (3, (6, (8, None))))))

def binary_search(x, key, start, end):
    if start > end:
        return -start - 1
    mid = (start + end) // 2
    mid_val = x[mid]
    if key == mid_val:
        return mid
    elif key < mid_val:
        return binary_search(x, key, start, mid - 1)
    else:
        return binary_search(x, key, mid + 1, end)

# arr = [1, 3, 5]
# print(binary_search(arr, 1, 0, len(arr) - 1))

def swap(x, old, new):
    if(new > old):
        i = new
        while i != old:
            x[i], x[i-1] = x[i-1], x[i]
            i-=1
    elif(new < old):
        i = old
        while i != new:
            x[i], x[i-1] = x[i-1], x[i]
            i-=1
    return x

# x = [2, 3, 4, 1]
# swap(x, 3, 0)
# print(x)

def sort(x):
    for i in range(len(x)):
        for j in range(i):
            if(x[i] < x[j]):
                swap(x, i, j)
    return x

print(sort([5,3,9,1,2]))