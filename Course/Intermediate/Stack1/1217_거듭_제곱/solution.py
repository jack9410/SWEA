for _ in range(1,11):
    t_case = int(input())
    a,b = map(int, input().split())
    answer = pow(a,b)
    print('#{} {}'.format(t_case, answer))