# 定义数独棋盘
# 定义数独难度
difficulty = "easy"

# 初始化数独棋盘
def gen_puzz():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # 根据难度设置空白格数量
    if difficulty == "easy":
        blank_count = 5
    elif difficulty == "medium":
        blank_count = 40
    elif difficulty == "hard":
        blank_count = 50
    else:
        blank_count = 30
    # 随机生成数独棋盘
    generate_board(board)
    # 随机挖空格
    dig_holes(blank_count, board)
    print(board)
    return board

# 随机生成数独棋盘
def generate_board(board):
    import random
    # 定义数字范围
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 随机填充第一行
    random.shuffle(nums)
    for i in range(9):
        board[0][i] = nums[i]
    # 递归填充数独棋盘
    fill_board(0, 0, board)


# 递归填充数独棋盘
def fill_board(row, col, board):
    import random
    # 判断是否填充完成
    if row == 8 and col == 9:
        return True
    # 判断是否填充完一行
    if col == 9:
        row += 1
        col = 0
    # 判断当前位置是否已填充
    if board[row][col] > 0:
        return fill_board(row, col + 1, board)
    # 随机填充数字
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)
    for num in nums:
        if is_valid(row, col, num, board):
            board[row][col] = num
            if fill_board(row, col + 1, board):
                return True
            board[row][col] = 0
    return False

# 判断填充数字是否合法
def is_valid(row, col, num, board):
    # 判断行是否合法
    for i in range(9):
        if board[row][i] == num:
            return False
    # 判断列是否合法
    for i in range(9):
        if board[i][col] == num:
            return False
    # 判断宫是否合法
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def dig_holes(blank_count, board):
    import random
    # 随机挖空格
    for i in range(blank_count):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        # 判断当前位置是否已挖空
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        # 挖空当前位置
        board[row][col] = 0


gen_puzz()
