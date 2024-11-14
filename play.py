class TicTacToe:
    field = [[0 for _ in range(3)] for _ in range(3)]
    motion = False
    coords = [0,0]



    def set_coords(self, x, y):
        self.coords[0] = x
        self.coords[1] = y

    def do_motion(self):
        if self.field[self.coords[0]][self.coords[1]] == 0:
            if self.motion == False:
                self.motion = True
                self.field[self.coords[0]][self.coords[1]] = 1
            elif self.motion == True:
                self.motion = False
                self.field[self.coords[0]][self.coords[1]] = 2

    # Вернет 0, если игра продолжается, 1/2, если выйграли крестики/нолики, 3, если поле переполнено
    def check_win(self) -> int:
        num = 0
        order = [[[0,0],[1,1],[2,2]],
                 [[0,2],[1,1],[2,0]],
                 [[0,0], [0,1], [0,2]],
                 [[1,0], [1,1], [1,2]],
                 [[2,0], [2,1], [2,2]],
                 [[0,0], [1,0], [2,0]],
                 [[0,1], [1,1], [2,1]],
                 [[0,2], [1,2], [2,2]]]
        check_full = True
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 0: check_full = False
        for i in range(8):
            if self.field[order[i][0][0]][order[i][0][1]] == self.field[order[i][1][0]][order[i][1][1]] == self.field[order[i][2][0]][order[i][2][1]]:
                if self.field[order[i][0][0]][order[i][0][1]] == 1:
                    num = 1
                    check_full = False
                if self.field[order[i][0][0]][order[i][0][1]] == 2:
                    num = 2
                    check_full = False
        if check_full: return 3
        else: return num



