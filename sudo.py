import turtle
import gen_puzzle
import time

class SudokuGame:
    def __init__(self):
        self.board = [
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
        self.generated = 81 * [False]
        self.turtles = {}

        self.screen = turtle.Screen()
        self.screen.setup(500, 500)
        self.screen.title("数独游戏")
        self.screen.bgcolor("#ffffff")

        self.board_size = 450
        self.cell_size = self.board_size / 9
        self.start_time = 0

        self.pen = turtle.Turtle()


    def draw_board(self):
        left_min, left_up = -self.board_size / 2 -5 ,  self.board_size / 2 + 5
        board_size = self.board_size
        cell_size = self.cell_size

        self.pen.speed(0)
        self.pen.pensize(3)
        self.pen.penup()

        self.pen.goto(left_min, left_up)
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(board_size)
            self.pen.right(90)
            
        # 绘制横线
        for i in range(1, 9):
            self.pen.penup()
            self.pen.goto(left_min, left_up - i * cell_size)
            self.pen.pendown()
            self.pen.forward(board_size)
        
        # 绘制竖线
        self.pen.right(90)
        for i in range(1, 9):
            self.pen.penup()
            self.pen.goto(left_min + i * cell_size, left_up)
            self.pen.pendown()
            self.pen.forward(board_size)
        
        # 绘制粗线
        self.pen.pensize(5)
        for i in range(1, 3):
            self.pen.penup()
            self.pen.goto(left_min + i * cell_size * 3, left_up)
            self.pen.pendown()
            self.pen.forward(board_size)
            
        self.pen.left(90)
        for i in range(1, 3):
            self.pen.penup()
            self.pen.goto(left_min, left_up - i * cell_size * 3)
            self.pen.pendown()
            self.pen.forward(board_size)
     
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.pen.penup()
                    y = left_up - i * cell_size - cell_size * 3 / 4
                    x = left_min + j * cell_size + cell_size / 2
                    self.pen.goto(x, y)
                    self.pen.write(str(self.board[i][j]), align='center', font=('Arial', 20, 'normal'))

        self.pen.hideturtle()

    def is_valid(self, row, col, num):
        # 判断行是否合法
        for i in range(9):
            if self.board[row][i] == num:
                return False
        # 判断列是否合法
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # 判断宫是否合法
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True


    def handle_click(self, x, y):
        left_min, left_up = -self.board_size / 2 -5 ,  self.board_size / 2 + 5
        if left_min < x < left_min + self.board_size and -self.board_size + left_up< y < left_up:
            # 将坐标转换成矩阵索引
            row = int((left_up - y) // self.cell_size)
            col = int((x - left_min) // self.cell_size)
            print(row, col)

            # 标记选中格子
#            self.pen.speed(0)
#            self.pen.pencolor("#000000")
#            self.pen.penup()
#            self.pen.goto(left_min + col * 30, left_up - row * 30)
#            self.pen.pendown()
#            self.pen.goto(left_min + (col + 1) * 30, left_up - row * 30)
#            self.pen.goto(left_min + (col + 1) * 30, left_up - (row + 1) * 30)
#            self.pen.goto(left_min + col * 30, left_up - (row + 1) * 30)
#            self.pen.goto(left_min + col * 30, left_up - row * 30)
#
            # 处理数字输入
            value = self.screen.numinput("数独游戏", "请输入数字(1-9):", minval=1, maxval=9)
            while value is not None and not self.is_valid(row, col, value): 
                value = self.screen.numinput("数独游戏", "输入的数字不符合规则，请重新输入", minval=1,maxval=9)
                value = int(value) if value is not None else None
            print(value)

            key = row * 9 + col
            if value is not None and not self.generated[key]:
                self.board[row][col] = int(value)
                y = left_up -  row * self.cell_size - self.cell_size * 3 / 4
                x = left_min + col * self.cell_size + self.cell_size / 2

                t = self.turtles[key] if key in self.turtles else turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.clear()

                t.color("green")
                t.goto(x, y)
                t.write(str(self.board[row][col]), align='center', font=('Arial', 20, 'normal'))
                self.turtles[key] = t

                if self.is_board_full():
                    t = turtle.Turtle()
                    end_time = time.time()
                    duration = end_time - self.start_time
                    print(end_time, duration)
                    t.color("red")
                    t.write("Congratulations! You solved the Sudoku puzzle in %.1fs!" % (duration), align="center", font=("Arial", 15, "normal"))
                    t.hideturtle()
            

    def is_board_full(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def generate_puzzle(self):
        a =  [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
        board = gen_puzzle.gen_puzz()
        print(board)
        return board

    def init_board(self):
        # 随机生成一个数独谜题
        puzzle = self.generate_puzzle()

        # 初始化棋盘
        self.board = [[0] * 9 for _ in range(9)]

        # 复制数独谜题到棋盘
        for i in range(9):
            for j in range(9):
                self.board[i][j] = puzzle[i][j]             
                self.generated[i * 9 + j] = True if self.board[i][j] > 0 else False


    def start_game(self):
        # 初始化棋盘
        self.init_board()

        # 绘制棋盘
        self.draw_board()

        self.start_time = time.time()
        print(self.start_time)
        # 注册点击事件处理函数
        turtle.onscreenclick(self.handle_click)

        # 进入主循环
        turtle.mainloop()

game = SudokuGame()
game.start_game()
