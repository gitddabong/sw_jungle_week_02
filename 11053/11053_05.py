# 1053 05 가장 긴 증가하는 수열(참조)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
cache = [0] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j] and cache[i] < cache[j]:
            cache[i] = cache[j]
    cache[i] += 1

print(max(cache))






# # 11053 05 가장 긴 증가하는 부분 수열 (이 아이디어가 아닌 듯)


# from __future__ import annotations
# from typing import Any, Type
# import sys

# class Node:
#     """이진 검색 트리의 노드"""
#     def __init__(self, key: Any, value: Any, level: int, left: Node = None,
#                  right: Node = None):
#         """생성자"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.level = level  # 레벨
#         self.left = left    # 왼쪽 포인터(왼쪽 자식 참조)
#         self.right = right  # 오른쪽 포인터(오른쪽 자식 참조)

# class BinarySearchTree:
#     """이진 검색 트리"""

#     def __init__(self):
#         """초기화"""
#         self.root = None  # 루트
    
#     def add(self, key: Any, value: Any) -> bool:

#         def add_node(node: Node, key: Any, value: Any) -> None:
#             if key == node.key:
#                 return False
#             elif key < node.key:
#                 if node.left is None:
#                     node.left = Node(key, value, level + 1, None, None)
#                 else:
#                     add_node(node.left, key, value)
#             else:
#                 if node.right is None:
#                     node.right = Node(key, value, level + 1, None, None)
#                 else:
#                     add_node(node.right, key, value)
#             return True
        
#         if self.root is None:
#             level = 0
#             self.root = Node(key, value, level, None, None)
#             return True
#         else:
#             return add_node(self.root, key, value)


# n = int(sys.stdin.readline())
# data = list(map(int,sys.stdin.readline().split()))
# tree = BinarySearchTree()
# for i in range(n):
#     tree.add(i, data[i])
