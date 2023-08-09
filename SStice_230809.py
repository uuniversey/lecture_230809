
# 스택의 구현

# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
#
# print(stack)



# pop 알고리즘

# top = -1
# stack = [0]
# def pop():
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top+1]
#
# print(pop())
#
# if top > -1:
#     top -= 1
#     print(stack[top+1])



# practice_stack

# stack = [0] * 10
# top = -1
#
# top += 1            # push(1)
# stack[top] = 1
#
# top += 1
# stack[top] = 2
#
# top += 1
# stack[top] = 3
#
# print(stack[top])   # pop()
# top -= 1
#
# top -= 1            # pop()
# print(stack[top+1])








# 수 이어가기 - study2

# 첫번째로 주어진 수 안에서 두번째 수를 선택한다. 두번째로 선택한 수에 따라 경우의 수가 바뀐다.
# 몇가지 경우 해보면서 느낀건데 주어진 숫자의 60퍼 ~ 65퍼 보면될듯


N = int(input())



# print(#최댓값)
# print(#그 배열 중 아무거나 하나, 사이에 빈칸 하나씩)
