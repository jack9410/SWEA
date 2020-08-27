import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')



def merge(left, right):
    global cnt

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    leftList = merge_sort(lst[:mid])
    rightList = merge_sort(lst[mid:])
    return merge(leftList, rightList)



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    # print(lst)

    print('#{} {} {}'.format(test_case, lst[N//2], cnt))