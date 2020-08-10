import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

symbol = ['+', '*']


for test_case in range(1,11):
    N = int(input())
    line = input()
    stack = []
    
    # 후위표기법 변환
    prefix_notation = ''
    for i in line:
        if i not in symbol:
            prefix_notation += i
        else:
            if not stack:
                stack.append(i)
            else:
                if i == '*':
                    if stack[-1] == '+':
                        stack.append(i)
                    else:
                        prefix_notation += stack.pop()
                        stack.append(i)
                elif i == '+':
                    prefix_notation += stack.pop()
                    stack.append(i)
        # print(prefix_notation)
        # print(stack)

    while stack:
        prefix_notation += stack.pop()
    # print(prefix_notation)

    # stack으로 계산
    for i in prefix_notation:
        if i not in symbol:
            stack.append(i)
        else:
            if i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            if i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)

    print('#{} {}'.format(test_case, stack[0]))