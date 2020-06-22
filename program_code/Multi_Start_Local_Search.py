import sys
import random

p=5 #初期解の数
list=[1,2,3,4] #English=1, Math=2, Physics=3, Chemistry=4

#配列内に同じ要素が存在していた場合->削除
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

#初期解の生成
def generate_initial_solution():
    initial_solution = []
    while len(initial_solution) != p:
        x=random.sample(list, len(list))
        initial_solution.append(x)
        initial_solution = get_unique_list(initial_solution)
    return initial_solution

#摂動(隣り合う要素を入れ替える(3回))
def perturbation():
    perturbation_array = [[0 for i in range(4)] for j in range(p*3)]
    for i in range(len(initial_solution)):
        l = initial_solution[i]
        if i == 0:
            perturbation_array[i][0] = l[1]
            perturbation_array[i][1] = l[0]
            perturbation_array[i][2] = l[2]
            perturbation_array[i][3] = l[3]

            perturbation_array[1][0] = l[0]
            perturbation_array[1][1] = l[2]
            perturbation_array[1][2] = l[1]
            perturbation_array[1][3] = l[3]

            perturbation_array[2][0] = l[0]
            perturbation_array[2][1] = l[1]
            perturbation_array[2][2] = l[3]
            perturbation_array[2][3] = l[2]
        else:
            perturbation_array[i*3][0] = l[1]
            perturbation_array[i*3][1] = l[0]
            perturbation_array[i*3][2] = l[2]
            perturbation_array[i*3][3] = l[3]

            perturbation_array[i*3+1][0] = l[0]
            perturbation_array[i*3+1][1] = l[2]
            perturbation_array[i*3+1][2] = l[1]
            perturbation_array[i*3+1][3] = l[3]

            perturbation_array[i*3+2][0] = l[0]
            perturbation_array[i*3+2][1] = l[1]
            perturbation_array[i*3+2][2] = l[3]
            perturbation_array[i*3+2][3] = l[2]
    return perturbation_array

#局所探索法
def local_search():
    final_array = []
    final_time = 0
    count = 0
    for i in range(len(perturbation_array)):
        total_time = 0
        A = perturbation_array[i][0]
        B = perturbation_array[i][1]
        C = perturbation_array[i][2]
        D = perturbation_array[i][3]
        A = A-1
        B = B-1
        C = C-1
        D = D-1
        A_time = array[0][A]
        B_time = array[1][B]
        C_time = array[2][C]
        D_time = array[3][D]
        total_time = A_time + B_time + C_time + D_time
        # print(total_time)
        if i == 0:
            final_time = total_time
            final_array.append(perturbation_array[i])
            comparison_total_time = total_time
        elif total_time == comparison_total_time:
            count += 1
            final_time = total_time
            final_array.append(perturbation_array[count])
        elif total_time < comparison_total_time:
            final_array = []
            # print(final_array)
            final_array.append(perturbation_array[i])
            final_time = total_time
            comparison_total_time = total_time
        # print(final_array)
    final_array = get_unique_list(final_array)
    print('最短時間:{0}'.format(final_time))
    print('組み合わせ:{0}'.format(final_array))

array=[
    #A
    [6,1,9,3],
    #B
    [2,5,7,8],
    #C
    [6,3,5,4],
    #D
    [3,5,2,1],
]

initial_solution = generate_initial_solution()
# print(initial_solution)
perturbation()
perturbation_array = perturbation()
# print(perturbation_array)
local_search()