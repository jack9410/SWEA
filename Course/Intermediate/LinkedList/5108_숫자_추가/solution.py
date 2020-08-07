T = int(input())

for test_case in range(1, T+1):
    N, L, M = map(int, input().split())
    # print(N, L, M)
    lst = list(map(int, input().split()))
    # print(lst)

    for _ in range(L):
        insert_idx, insert_num = map(int, input().split())
        # print(insert_idx, insert_num)
        lst.insert(insert_idx, insert_num)

    # print(lst)
    print('#%d %d'%(test_case, lst[M]))