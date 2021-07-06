# 크레인을 모두 작동시킨 후 터트러져 사라진 인형의 개수를 return하는 solution 함수 완성하기

# 크레인을 작동시킨 위치가 담긴 배열 moves
# 게임 화면의 격자 상태가 담긴 2차원 배열 board

import random

size_min = 5
size_max = 30
size = random.randint(size_min, size_max)

moves_min = 1
moves_max = 1000
moves_sample = random.randint(moves_min, moves_max)

board_sample = [[random.randint(0, 100 + 1) for i in range(size)] for j in range(size)]

board_1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves_1 = [0, 4, 2, 4, 0, 1, 0, 3]


def solution(board, moves):
    answer = 0
    basket = []
    for loc in moves:  # moves 만큼 실행
        for layer in board:
            if layer[loc] != 0:
                basket.append(layer[loc])
                layer[loc] = 0
                break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    print(basket)

    return answer


val = solution(board_1, moves_1)
print(val)
