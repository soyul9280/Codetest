import sys
x = int(sys.stdin.readline())
# 파이썬에서 스택 사용하는 방법
stack = []
# 입력 받은 값 처리
for i in range(x):
    s = sys.stdin.readline().split( )
    if s[0] =='push':
        stack.append(s[1])
    elif s[0] =='pop':
        if len(stack) > 0: print(stack.pop())
        else: print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif s[0] == 'top':
        if len(stack)>0: print(stack[-1])
        else: print(-1)
