def solution(board, moves):
    result = []
    k = 0
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                result.append(str(board[j][i - 1]))
                board[j][i - 1] = 0
                break

    while len(result) - 1 != k:
        if result[k] == result[k + 1]:
            result.pop(k)
            result.pop(k)
            k = 0
            answer += 2

            if len(result) == 0:
                break
        else:
            k += 1

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
