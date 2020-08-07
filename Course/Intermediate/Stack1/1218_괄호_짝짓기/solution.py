import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

start = ['(', '{', '[', '<']
end = [')', '}', ']', '>']

for t_case in range(1,11):
    answer = True
    stack = []
    p_num = int(input())
    # print(p_num)a
    line = input()

    for i in line:
        if i in start:
            stack.append(i)
        if i in end:
            try:
                tmp = stack.pop()
            except IndexError:
                answer = False
            if i == ')':
                if tmp == '(':
                    continue
                else:
                    answer = False
                    break
            elif i == '}':
                if tmp == '{':
                    continue
                else:
                    answer = False
                    break
            elif i == ']':
                if tmp == '[':
                    continue
                else:
                    answer = False
                    break
            elif i == '>':
                if tmp == '<':
                    continue
                else:
                    answer = False
                    break
    
    if answer:
        print('#{} {}'.format(t_case, 1))
    else:
        print('#{} {}'.format(t_case, 0))
                