def solution(keyinput, board):
    x, y = 0, 0  # 시작 위치
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    move = {
        "up":    (0, 1),
        "down":  (0, -1),
        "left":  (-1, 0),
        "right": (1, 0)
    }

    for key in keyinput:
        dx, dy = move[key]
        new_x, new_y = x + dx, y + dy

        # 맵 경계 확인
        if -x_limit <= new_x <= x_limit and -y_limit <= new_y <= y_limit:
            x, y = new_x, new_y

    return [x, y]