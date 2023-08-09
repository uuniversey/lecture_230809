

# 2005. 파스칼의 삼각형

# import sys
# sys.stdin = open('input_2005.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * (k+1) for k in range(N)]   # 빈 행렬을 층의 수만큼의 원소 개수를 가지게 만들기
#
#     for i in range(N):
#         if i == 0:          # 1층은 항상 1
#             arr[0] = [1]
#         elif i == 1:        # 2층도 항상 1 1
#             arr[i][0] = 1
#             arr[i][1] = 1
#         else:
#             for j in range(i+1):
#                 if j != i and j != 0:   # 나머지 중간 부분은 그 전층을 참고하여 더해서 계산
#                     arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#                 else:   # 3층부터는 맨 처음과 맨끝은 1
#                     arr[i][j] = 1
#
#     print(f'#{tc}')
#     for k in arr:
#         print(*k)   # 리스트 형식으로 모아놨기 때문에 언패킹
#



# 1234. 비밀번호

# import sys
# sys.stdin = open('input_1234.txt', 'r')
#
#
# def push(mine):
#     global top
#     top += 1
#     stack[top] = mine
#
#
# def wj_pop():
#     global top
#     if top == -1:
#         return 0
#     else:
#         stack[top] = 0              # pop 되는 곳에 0을 넣어준다.
#         top -= 1
#         return stack[top+1]
#
# T = 10
# for tc in range(1, T+1):
#     N, password = list(map(str, input().split()))
#     top = -1
#     password = list(str(password))
#     stack = [0] * 100
#     result = ''
#
#     for num in password:
#         if top == -1:              # 0번 인덱스는 비교할 여지 없으므로 그냥 push
#             push(num)
#         elif num == stack[top]:    # num이랑 방금 push한 원소가 같으면 pop
#             wj_pop()
#         else:
#             push(num)              # 안 같으면 계속 push
#
#     for i in stack:
#         if type(i) == str:         # stack에 쌓은 str만 result에 붙여서 출력.
#             result += i
#
#     print(f'#{tc} {result}')





# 18224. 괄호검사

# import sys
# sys.stdin = open('input_18224.txt', 'r')
#
#
# def push(mine):                 # push 정의
#     global top
#     top += 1
#     return stack.append(mine)
#
#
# def wj_pop():                   # pop 정의
#     global top
#     if top == -1:
#         return print(f'#{tc} {0}')
#     else:
#         top -= 1
#         return stack[top+1]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     codes = list(map(str,input()))
#     stack = []
#     top = -1
#     result = 0                              # 결과 초기값, 최종적으로 0이면 비정상
#
#     for code in codes:
#         if code == '(' or code == '{':      # 왼쪽 괄호면 code(원소 하나하나)를 push한다.
#             push(code)
#         elif code == ')':                   # 오른쪽 소괄호 나오면 왼쪽 중괄호 나오는지 확인해서 나오면
#             if wj_pop() == '{':
#                 result = 0                  # 결과값 0
#
#         elif code == '}':                   # 오른쪽 중괄호 나오면 왼쪽 소괄호 나오는지 확인해서 나오면
#             if wj_pop() == '(':
#                 result = 0                  # 결과값 0
#
#     if top == -1:                           # for문 다 돌때까지 문제 없었으면 짝 맞는지 확인
#         result = 1                          # 짝이 맞는다면 top값은 -1이므로 결과값 1
#     else:
#         result = 0                          # top가 -1이 아니란 소리는 짝 안맞는다는 소리므로 결과값 0
#
#     print(f'#{tc} {result}')



# 18225. 반복문자 지우기
#
# import sys
# sys.stdin = open('input_18225.txt', 'r')
#
#
# def push(mine):
#     global top
#     top += 1
#     stack[top] = mine
#
#
# def wj_pop():
#     global top
#     if top == -1:
#         return 0
#     else:
#         stack[top] = 0              # pop 되는 곳에 0을 넣어준다.
#         top -= 1
#         return stack[top+1]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     my_str = list(map(str, input()))
#     top = -1
#     result = 0
#     stack = [0] * 1000
#
#     for word in my_str:
#         if stack[0] == 0:           # 0번 인덱스는 비교할 여지 없으므로 그냥 push
#             push(word)
#         elif word == stack[top]:    # word랑 방금 push한 원소가 같으면 pop
#             wj_pop()
#         else:                       # 안 같으면 계속 push
#             push(word)
#
#     for i in stack:
#         if type(i) == str:          # stack에 쌓은 str 개수 세주고 출력.
#             result += 1
#
#     print(f'#{tc} {result}')



# 18282. 연습문제2 괄호검사

# import sys
# sys.stdin = open('input_18282.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(str, input()))
#     result = 0
#     stack1 = []    # ( 를 채울 스택
#     stack2 = []    # ) 를 채울 스택
#
#     for i in range(len(arr)):
#         if len(stack2) > len(stack1):   # stack2의 개수가 먼저 증가했단건 (가 나오기 전에 )이 나왔단 소리니까 -1
#             result = -1
#             break
#         else:
#             if arr[i] == '(':           # ( 라면 스택1에
#                 stack1.append(arr[i])
#             elif arr[i] == ')':         # ) 라면 스택2에
#                 stack2.append(arr[i])
#
#     if len(stack1) == len(stack2):      # 개수가 서로 같으면 짝이 맞단 소리
#         result = 1
#     else:                               # 다르면 짝이 안 맞음
#         result = -1
#
#     print(f'#{tc} {result}')