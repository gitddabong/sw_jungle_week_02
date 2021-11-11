#-*- coding:utf-8 -*-
import os 
def generate_folders(problems_str):
    '''generate_folder.py파일이 있는 위치에 백준코딩 문제 폴더 생성 함수 
    
    Args: 
        problems_str (str): whitespace로 구분된 백준 문제 번호 스트링
    Returns:
        None
    '''
    problems_list = problems_str.split()
    path_root = os.getcwd()
    for num in problems_list:
        os.mkdir(os.path.join(path_root, num))


if __name__ == '__main__':
    problems_str = '''1920
2805
2110
2470
11053
8983
2630
1629
6549
10830
2261
10828
10773
9012
17608
2493
10000
2504
2812
18258
2164
11866
3190
11279
1655
1715
13334
'''
    generate_folders(problems_str)
