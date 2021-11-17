# 1629 8 곱셈 (참조)

def power(a, b, c):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % c
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % c # b가 짝수인 경우
        else:
            return temp * temp * a % c # b가 홀수인 경우


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B, C)
    print(result)







# # 1629 8 곱셈 ()

# import sys
# from typing import Counter

# a, b, c = map(int,sys.stdin.readline().split())

# rest_list = []
# rule = False
# count = 1

# def is_rest(a, b, c, rule):
#     global count

#     if rule == False:
#         a *= a
#         rest = a % c
#         count += 1
#         for i in range(len(rest_list)):
#             if rest == rest_list[i]:
#                 rule = True
#                 is_rest(a, b, c, rule)
#         else:
#             rest_list.append(rest)
#             is_rest(a, b, c, rule)

#     if rule == True:
#         b % (len(rest_list))

