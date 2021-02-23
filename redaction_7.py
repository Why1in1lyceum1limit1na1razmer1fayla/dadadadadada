from random import randrange
import pygame

matrix = [[0 for i in range(10)] for j in range(22)]
matrix.append([-1 for _ in range(10)])
kub = 1
pal = 2
zag1 = 3
zag2 = 4
g1 = 5
g2 = 6
tet = 7
histor_vpered = []
f = True
pieces = [1, 2, 3, 4, 5, 6, 7]
order = []

pool = pieces * 5

firstPiece = [2, 5, 6, 7][randrange(4)]
print(firstPiece, '-')
histor_vpered.append(firstPiece)
history = [3, 4, 3, firstPiece]


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * self.w for _ in range(self.h)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, c_size):
        self.left = left
        self.top = top
        self.cell_size = c_size

    def render(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                pygame.draw.rect(screen, (128, 128, 128),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):  # получаем координаты мыши
        cell = self.get_cell(mouse_pos)
        if cell is True:
            self.on_click(cell)
        else:
            print(cell)

    def get_coords(self):
        y, x = self.left, self.top
        sp = []
        sp1 = []
        for i in range(21):
            for j in range(10):
                sp.append((x + i * 30 + 1, 1 + y + j * 30))
            sp1.append(sp)
            sp = []
        return sp1

    def get_cell(self, mouse_pos):  # возвращает координаты ячейки поле (board[x][y])
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x > self.w or cell_y < 0 or cell_y > self.h:
            return None
        return cell_x, cell_y

    def on_click(self, cell):  # событие по нажатию мыши
        print(cell)


def spawn():
    global tturning, holturning
    tturning, holturning = 0, 0
    sp = queue()
    if sp == 1:
        cubik()
    if sp == 2:
        palka()
    if sp == 3:
        snake()
    if sp == 4:
        ekans()
    if sp == 5:
        loh()
    if sp == 6:
        hol()
    if sp == 7:
        bukva()


def generat():
    for roll in range(6):
        i = randrange(35)
        piece = pool[i]
        if piece not in history or roll == 5:
            break
        if len(order) != 0:
            pool[i] = order[0]
    if piece in order:
        order.remove(piece)
    order.append(piece)

    pool[i] = order[0]

    history.pop(0)
    history.append(piece)
    return piece


# Заполнение истории на 5 вперед
for i in range(5):
    histor_vpered.append(generat())


# изменение истории вперед
def queue():
    el = generat()
    histor_vpered.append(el)
    return histor_vpered.pop(0)


def proigrish():
    global matrix
    matrix = [[0 for i in range(10)] for j in range(22)]
    matrix.append([-1 for _ in range(10)])
    spawn()


# появление фигуры\/\/\/
def cubik():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[0][4] = 10
        matrix[0][5] = 10
        matrix[1][4] = 10
        matrix[1][5] = 10
    else:
        proigrish()


def palka():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[1][4] = 20
        matrix[1][5] = 20
        matrix[1][6] = 20
        matrix[1][3] = 20
    else:
        proigrish()


def snake():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[1][4] = 30
        matrix[1][5] = 30
        matrix[0][6] = 30
        matrix[0][5] = 30
    else:
        proigrish()


def ekans():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[0][3] = 40
        matrix[1][4] = 40
        matrix[1][5] = 40
        matrix[0][4] = 40
    else:
        proigrish()


def loh():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[1][3] = 50
        matrix[1][4] = 50
        matrix[1][5] = 50
        matrix[0][5] = 50
    else:
        proigrish()


def hol():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[1][3] = 60
        matrix[1][4] = 60
        matrix[1][5] = 60
        matrix[0][3] = 60
    else:
        proigrish()


def bukva():
    if matrix[1][4] == 0 and matrix[1][5] == 0:
        matrix[1][3] = 70
        matrix[1][4] = 70
        matrix[1][5] = 70
        matrix[0][4] = 70
    else:
        proigrish()


# --- #
cnt_ce = 0


def stop():
    global cnt_ce
    for i in range(1, 22):
        for j in range(10):
            if matrix[i][j] > 8:
                matrix[i][j] = matrix[i][j] // 10
                cnt_ce = 0


def move_down():
    for i in range(0, 22):
        for j in range(10):
            if matrix[i][j] > 9:
                if matrix[i + 1][j] < 8 and matrix[i + 1][j] != 0:
                    stop()
                    return ''
    for i in range(21, -1, -1):
        for j in range(9, -1, -1):
            if matrix[i][j] > 8:
                matrix[i + 1][j] = matrix[i][j]
                matrix[i][j] = 0


def move_right():
    q = []
    for i in range(0, 22):
        for j in range(10):
            if matrix[i][j] > 9:
                q.append((i, j))
    for k in q:
        if k[1] == 9:
            return
        if matrix[k[0]][k[1] + 1] != 0 and matrix[k[0]][k[1] + 1] < 9:
            return

    for k in q[::-1]:
        i = k[0]
        j = k[1]
        qwe = matrix[i][j]
        matrix[i][j] = 0
        matrix[i][j + 1] = qwe


def move_left():
    q = []
    for i in range(0, 22):
        for j in range(10):
            if matrix[i][j] > 9:
                q.append((i, j))
    for k in q:
        if k[1] == 0:
            return
        if matrix[k[0]][k[1] - 1] != 0 and matrix[k[0]][k[1] - 1] < 9:
            return

    for k in q:
        i = k[0]
        j = k[1]
        qwe = matrix[i][j]
        matrix[i][j] = 0
        matrix[i][j - 1] = qwe


tturning = 0


def turn():
    q = []
    for i in range(0, 22):
        for j in range(10):
            if matrix[i][j] > 9:
                q.append((i, j))
    figura = matrix[q[0][0]][q[0][1]] // 10
    if figura == 1:
        return
    if figura == 2:
        if q[0][1] == q[1][1] - 1:
            # horizontale
            x, y = q[2]
            if x != 21 and x > 1:
                if matrix[x + 1][y] == matrix[x - 1][y] == matrix[x - 2][y] == 0:
                    matrix[x + 1][y] = 20
                    matrix[x - 1][y] = 20
                    matrix[x - 2][y] = 20
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 20
            elif x == 21:
                if matrix[x - 1][y] == matrix[x - 3][y] == matrix[x - 2][y] == 0:
                    matrix[x - 1][y] = 20
                    matrix[x - 3][y] = 20
                    matrix[x - 2][y] = 20
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 20
            elif x < 2:
                if matrix[0][y] == matrix[1][y] == matrix[2][y] == matrix[3][y] == 0:

                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[0][y] = 20
                    matrix[1][y] = 20
                    matrix[3][y] = 20
                    matrix[2][y] = 20
        else:
            x, y = q[1]
            if y != 0 and y < 8:
                if matrix[x][y - 1] == matrix[x][y + 2] == matrix[x][y + 1] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 20
                    matrix[x][y + 2] = 20
                    matrix[x][y + 1] = 20
                    matrix[x][y] = 20  # кринж, доделать
                if matrix[x][y - 1] != 0 and matrix[x][y + 2] == matrix[x][y + 1] == 0 and y != 7:
                    if matrix[x][y + 2] == matrix[x][y + 3]:
                        for i in q:
                            matrix[i[0]][i[1]] = 0
                        matrix[x][y + 3] = 20
                        matrix[x][y + 2] = 20
                        matrix[x][y + 1] = 20
                        matrix[x][y] = 20
            if y == 0:
                if matrix[x][y + 1] == matrix[x][y + 2] == matrix[x][y + 3] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y + 1] = 20
                    matrix[x][y + 2] = 20
                    matrix[x][y + 3] = 20
                    matrix[x][y] = 20
            if y == 8:
                if matrix[x][y + 1] == matrix[x][y - 2] == matrix[x][y - 1] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 20
                    matrix[x][y - 2] = 20
                    matrix[x][y + 1] = 20
                    matrix[x][y] = 20
            if y == 9:
                if matrix[x][y - 1] == matrix[x][y - 2] == matrix[x][y - 3] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 20
                    matrix[x][y - 2] = 20
                    matrix[x][y - 3] = 20
                    matrix[x][y] = 20

    if figura == 3:
        if matrix[q[3][0]][q[3][1] - 1] != 30:
            if q[3][1] == 1:
                if matrix[q[3][0]][q[3][1] - 1] == 0 and matrix[q[3][0] - 1][q[3][1] + 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[1][0]][q[1][1]] = 0
                    matrix[q[3][0]][q[3][1] - 1] = 30
                    matrix[q[3][0] - 1][q[3][1] + 1] = 30
                    return
                return
            if q[3][1] != 1:
                if matrix[q[3][0]][q[3][1] - 1] == 0 and matrix[q[3][0]][q[3][1] - 2] == 0:
                    matrix[q[3][0]][q[3][1]] = 0
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[3][0]][q[3][1] - 1] = 30
                    matrix[q[3][0]][q[3][1] - 2] = 30
                    return
                if q[3][1] != 9:
                    if matrix[q[3][0]][q[3][1] - 1] == 0 and matrix[q[3][0] - 1][q[3][1] + 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[3][0]][q[3][1] - 1] = 30
                        matrix[q[3][0] - 1][q[3][1] + 1] = 30
                        return
        if matrix[q[3][0]][q[3][1] + 1] == 0 and matrix[q[0][0] - 1][q[0][1]] == 0:
            matrix[q[3][0]][q[3][1]] = 0
            matrix[q[3][0]][q[3][1] - 1] = 0
            matrix[q[3][0]][q[3][1] + 1] = 30
            matrix[q[0][0] - 1][q[0][1]] = 30
            return
        if matrix[q[0][0] - 1][q[0][1]] == 0 and matrix[q[0][0] - 1][q[0][1] + 1] == 0 and matrix[q[0][0] - 2][
            q[0][1]] == 0:
            matrix[q[3][0]][q[3][1]] = 0
            matrix[q[3][0]][q[3][1] - 1] = 0
            matrix[q[0][0]][q[0][1]] = 0
            matrix[q[0][0] - 1][q[0][1]] = 30
            matrix[q[0][0] - 1][q[0][1] + 1] = 30
            matrix[q[0][0] - 2][q[0][1]] = 30
            return
        if matrix[q[3][0]][q[3][1] + 1] == 0 and matrix[q[3][0] + 1][q[3][1] + 1] == 0:
            matrix[q[3][0]][q[3][1] - 1] = 0
            matrix[q[3][0] - 1][q[3][1] + 1] = 0
            matrix[q[3][0] + 1][q[3][1] + 1] = 30
            matrix[q[3][0]][q[3][1] + 1] = 30
            return
        return

    if figura == 4:
        if q[1][1] == 0:
            if matrix[q[1][0] + 1][q[1][1] + 1] == 0 and matrix[q[1][0] + 1][q[1][1] + 2] == 0:
                matrix[q[1][0] + 1][q[1][1]] = 0
                matrix[q[1][0] - 1][q[1][1] + 1] = 0
                matrix[q[1][0] + 1][q[1][1] + 1] = 40
                matrix[q[1][0] + 1][q[1][1] + 2] = 40
                return
            return
        if matrix[q[1][0]][q[1][1] + 1] != 40:
            if matrix[q[1][0]][q[1][1] + 1] == 0 and matrix[q[1][0] - 1][q[1][1] + 1] == 0:
                matrix[q[1][0]][q[1][1] - 1] = 0
                matrix[q[1][0] + 1][q[1][1] + 1] = 0
                matrix[q[1][0]][q[1][1] + 1] = 40
                matrix[q[1][0] - 1][q[1][1] + 1] = 40
                return
            if matrix[q[1][0]][q[1][1] + 1] == 0 and matrix[q[1][0] + 2][q[1][1]] == 0:
                matrix[q[1][0]][q[1][1] - 1] == 0
                matrix[q[1][0]][q[1][1]] == 0
                matrix[q[1][0]][q[1][1] + 1] == 40
                matrix[q[1][0] + 2][q[1][1]] == 40
                return
            if matrix[q[1][0] - 1][q[1][1]] == 0 and matrix[q[1][0] - 2][q[1][1] + 1] == 0 and matrix[q[1][0] - 1][
                q[1][1] + 1] == 0:
                matrix[q[1][0]][q[1][1] - 1] = 0
                matrix[q[1][0] + 1][q[1][1]] = 0
                matrix[q[1][0] + 1][q[1][1] + 1] = 0
                matrix[q[1][0] - 2][q[1][1] + 1] = 40
                matrix[q[1][0] - 1][q[1][1]] = 40
                matrix[q[1][0] - 1][q[1][1] + 1] = 40
                return
        if q[1][0] != 0:
            if matrix[q[1][0]][q[1][1] - 1] == 0 and matrix[q[1][0] + 1][q[1][1] + 1] == 0:
                matrix[q[1][0]][q[1][1] + 1] = 0
                matrix[q[1][0] - 1][q[1][1] + 1] = 0
                matrix[q[1][0] + 1][q[1][1] + 1] = 40
                matrix[q[1][0]][q[1][1] - 1] = 40
                return
        if q[1][0] != 8:
            if matrix[q[1][0] + 1][q[1][1] + 1] == 0 and matrix[q[1][0] + 1][q[1][1] + 2] == 0:
                matrix[q[1][0] + 1][q[1][1]] = 0
                matrix[q[1][0] - 1][q[1][1] + 1] = 0
                matrix[q[1][0] + 1][q[1][1] + 1] = 40
                matrix[q[1][0] + 1][q[1][1] + 2] = 40
                return
        return

    if figura == 5:
        if q[0][1] != 9:
            if matrix[q[0][0] + 1][q[0][1]] == 50 and matrix[q[0][0]][q[0][1] + 1] == 50 and matrix[q[0][0] + 1][
                q[0][1] + 1] != 50:
                # first
                if matrix[q[0][0] - 1][q[0][1] + 1] == 0 and matrix[q[0][0] + 1][q[0][1] + 1] == 0 and \
                        matrix[q[0][0] - 1][q[0][1]] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[0][0]][q[0][1] + 2] = 0
                    matrix[q[0][0] + 1][q[0][1]] = 0
                    matrix[q[0][0] - 1][q[0][1] + 1] = 50
                    matrix[q[0][0] + 1][q[0][1] + 1] = 50
                    matrix[q[0][0] - 1][q[0][1]] = 50
                    return
                if matrix[q[0][0] - 1][q[0][1] + 1] == 0 and matrix[q[0][0] - 2][q[0][1] + 1] == 0 and \
                        matrix[q[0][0] - 2][q[0][1]] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[0][0] + 1][q[0][1]] = 0
                    matrix[q[0][0]][q[0][1] + 2] = 0
                    matrix[q[0][0] - 1][q[0][1] + 1] = 50
                    matrix[q[0][0] - 2][q[0][1] + 1] = 50
                    matrix[q[0][0] - 20][q[0][1]] = 50
                    return
                if matrix[q[0][0] + 1][q[0][1] + 1] == 0 and matrix[q[0][0] + 2][q[0][1] + 1] == 0:
                    matrix[q[0][0] + 1][q[0][1]] = 0
                    matrix[q[0][0]][q[0][1] + 2] = 0
                    matrix[q[0][0] + 1][q[0][1] + 1] = 50
                    matrix[q[0][0] + 2][q[0][1] + 1] = 50
                    return
                if matrix[q[0][0] + 1][q[0][1] + 2] == 0 and matrix[q[0][0] - 1][q[0][1] + 1] == 0 and \
                        matrix[q[0][0] - 1][q[0][1] + 2]:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[0][0]][q[0][1] + 1] = 0
                    matrix[q[0][0] + 1][q[0][1]] = 0
                    matrix[q[0][0] + 1][q[0][1] + 2] = 50
                    matrix[q[0][0] - 1][q[0][1] + 1] = 50
                    matrix[q[0][0] - 1][q[0][1] + 2] = 50
                    return
                if q[0][1] != 0:
                    if matrix[q[0][0] - 1][q[0][1]] == 0 and matrix[q[0][0] - 1][q[0][1] - 1] == 0:
                        matrix[q[0][0]][q[0][1] + 1] = 0
                        matrix[q[0][0]][q[0][1] + 2] = 0
                        matrix[q[0][0] - 1][q[0][1]] = 50
                        matrix[q[0][0] - 1][q[0][1] - 1] = 50
                        return
                return
            if matrix[q[0][0]][q[0][1] + 1] != 50 and matrix[q[0][0] + 1][q[0][1] + 1] != 50 and matrix[q[0][0] + 1][
                q[0][1]] == 50 and matrix[q[0][0] + 2][q[0][1]] == 50:
                # --------------------------
                if q[0][1] != 0:
                    if matrix[q[0][0] + 2][q[0][1] - 1] == 0 and matrix[q[0][0] + 1][q[0][1] + 1] == 0 and \
                            matrix[q[0][0] + 1][q[0][1] - 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[0][0] + 2][q[0][1]] = 0
                        matrix[q[0][0] + 2][q[0][1] + 1] = 0
                        matrix[q[0][0] + 2][q[0][1] - 1] = 50
                        matrix[q[0][0] + 1][q[0][1] + 1] = 50
                        matrix[q[0][0] + 1][q[0][1] - 1] = 50
                        return
                if q[0][1] != 8:
                    if matrix[q[0][0] + 1][q[0][1] + 1] == 0 and matrix[q[0][0] + 1][q[0][1] + 2] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 1][q[0][1] + 2] = 50
                        matrix[q[0][0] + 1][q[0][1] + 1] = 50
                        return
                if q[0][1] > 1:
                    if matrix[q[0][0] + 1][q[0][1] - 1] == 0 and matrix[q[0][0] + 1][q[0][1] - 2] == 0 and \
                            matrix[q[0][0] + 2][q[0][1] - 2] == 0:
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[0][0] + 1][q[0][1] - 1] = 50
                        matrix[q[0][0] + 1][q[0][1] - 2] = 50
                        matrix[q[0][0] + 2][q[0][1] - 2] = 50
                        return
                if q[0][1] != 0:
                    if matrix[q[0][0] + 3][q[0][1] - 1] == 0 and matrix[q[0][0] + 2][q[0][1] - 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[0][0] + 1][q[0][1]] = 0
                        matrix[q[0][0] + 3][q[0][1] - 1] = 50
                        matrix[q[0][0] + 2][q[0][1] - 1] = 50
                        return

                    if matrix[q[0][0]][q[0][1] - 1] == 0 and matrix[q[0][0]][q[0][1] + 1] == 0 and matrix[q[0][0] + 1][
                        q[0][1] - 1] == 0:
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0]][q[0][1] - 1] = 50
                        matrix[q[0][0]][q[0][1] + 1] = 50
                        matrix[q[0][0] + 1][q[0][1] - 1] = 50
                        return
                return
            if matrix[q[0][0]][q[0][1] + 1] != 50 and matrix[q[0][0] + 1][q[0][1] + 1] != 50 and matrix[q[0][0] + 1][
                q[0][1]] == 50 and matrix[q[0][0] + 2][q[0][1]] != 50:
                if matrix[q[0][0]][q[0][1] - 2] == 0 and matrix[q[0][0]][q[0][1] - 1] == 0 and matrix[q[0][0] + 2][
                    q[0][1] - 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[1][0]][q[1][1]] = 0
                    matrix[q[3][0]][q[3][1]] = 0
                    matrix[q[0][0] + 2][q[0][1] - 1] = 50
                    matrix[q[0][0]][q[0][1] - 1] = 50
                    matrix[q[0][0] + 2][q[0][1]] = 50
                    return
                if matrix[q[0][0]][q[0][1] - 2] == 0 and matrix[q[0][0] + 2][q[0][1] - 2] == 0 and matrix[q[0][0] + 2][
                    q[0][1] - 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[2][0]][q[2][1]] = 0
                    matrix[q[3][0]][q[3][1]] = 0
                    matrix[q[0][0]][q[0][1] - 2] = 50
                    matrix[q[0][0] + 2][q[0][1] - 2] = 50
                    matrix[q[0][0] + 2][q[0][1] - 1] = 50
                    return
                if q[0][1] != 9:
                    if matrix[q[0][0] + 2][q[0][1]] == 0 and matrix[q[0][0] + 2][q[0][1] + 1] == 0:
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[0][0] + 2][q[0][1]] = 50
                        matrix[q[0][0] + 2][q[0][1] + 1] = 50
                        return
                if matrix[q[0][0]][q[0][1] - 1] == 0 and matrix[q[0][0] - 1][q[0][1] - 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[1][0]][q[1][1]] = 0
                    matrix[q[0][0]][q[0][1] - 1] = 50
                    matrix[q[0][0] - 1][q[0][1] - 1] = 50
                    return
                if q[0][0] != 21:
                    if matrix[q[0][0] + 3][q[0][1]] == 0 and matrix[q[0][0] + 3][q[0][1] - 1] == 0 and \
                            matrix[q[0][0] + 2][q[0][1] - 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 3][q[0][1]] = 50
                        matrix[q[0][0] + 3][q[0][1] - 1] = 50
                        matrix[q[0][0] + 2][q[0][1] - 1] = 50
                        return
                return
            if matrix[q[0][0]][q[0][1] + 1] == 50 and matrix[q[0][0] + 1][q[0][1] + 1] == 50 and matrix[q[0][0] + 1][
                q[0][1]] != 50:
                if q[0][1] < 8:
                    if matrix[q[0][0]][q[0][1] + 2] == 0 and matrix[q[0][0] + 1][q[0][1] + 2] == 0 and \
                            matrix[q[0][0] + 1][q[0][1]] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 1][q[0][1] + 2] = 50
                        matrix[q[0][0]][q[0][1] + 2] = 50
                        matrix[q[0][0] + 1][q[0][1]] = 50
                        return
                if q[0][1] < 8:
                    if matrix[q[0][0] + 1][q[0][1] + 2] == 0 and matrix[q[0][0] + 1][q[0][1] + 3] == 0 and \
                            matrix[q[0][0]][q[0][1] + 3] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 1][q[0][1] + 2] = 50
                        matrix[q[0][0] + 1][q[0][1] + 3] = 50
                        matrix[q[0][0]][q[0][1] + 3]
                        return
                if q[0][1] != 0:
                    if matrix[q[0][0] + 1][q[0][1]] == 0 and matrix[q[0][0] + 1][q[0][1] - 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 1][q[0][1]] = 50
                        matrix[q[0][0] + 1][q[0][1] - 1] = 50
                        return
                if q[0][1] != 9:
                    if matrix[q[0][0]][q[0][1] + 2] == 0 and matrix[q[0][0] - 1][q[0][1] + 2] == 0:
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0]][q[0][1] + 2] = 50
                        matrix[q[0][0] - 1][q[0][1] + 2] = 50
                        return
                    if matrix[q[0][0] + 1][q[0][1] + 2] == 0 and matrix[q[0][0] + 2][q[0][1] + 2] == 0 and \
                            matrix[q[0][0] + 2][q[0][1]] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[1][0]][q[1][1]] = 0
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[0][0] + 1][q[0][1] + 2] = 50
                        matrix[q[0][0] + 2][q[0][1] + 2] = 50
                        matrix[q[0][0] + 2][q[0][1]] = 50
                        return
                    return
                return
            return
        if q[0][1] == 9:
            if matrix[q[0][0] + 2][q[0][1]] == 0 and matrix[q[0][0] + 2][q[0][1] - 1] == 0 and matrix[q[0][0]][
                q[0][1] - 1] == 0:
                matrix[q[0][0]][q[0][1]] = 0
                matrix[q[1][0]][q[1][1]] = 0
                matrix[q[3][0]][q[3][1]] = 0
                matrix[q[0][0] + 2][q[0][1]] = 50
                matrix[q[0][0] + 2][q[0][1] - 1] = 50
                matrix[q[0][0]][q[0][1] - 1] = 50
                return
            if matrix[q[0][0] + 2][q[0][1] - 1] == 0 and matrix[q[0][0] + 2][q[0][1] - 2] == 0 and matrix[q[0][0]][
                q[0][1] - 2] == 0:
                matrix[q[0][0]][q[0][1]] = 0
                matrix[q[2][0]][q[2][1]] = 0
                matrix[q[3][0]][q[3][1]] = 0
                matrix[q[0][0] + 2][q[0][1] - 1] = 50
                matrix[q[0][0] + 2][q[0][1] - 2] = 50
                matrix[q[0][0]][q[0][1] - 2] = 50
                return
            if q[0][0] != 21:
                if matrix[q[0][0] + 3][q[0][1]] == 0 and matrix[q[0][0] + 3][q[0][1] - 1] == 0 and matrix[q[0][0] + 2][
                    q[0][1] - 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[1][0]][q[1][1]] = 0
                    matrix[q[3][0]][q[3][1]] = 0
                    matrix[q[0][0] + 3][q[0][1]] = 50
                    matrix[q[0][0] + 3][q[0][1] - 1] = 50
                    matrix[q[0][0] + 2][q[0][1] - 1] = 50
                    return
            if matrix[q[0][0]][q[0][1] - 1] == 0 and matrix[q[0][0] - 1][q[0][1] - 1] == 0:
                matrix[q[0][0]][q[0][1]] = 0
                matrix[q[1][0]][q[1][1]] = 0
                matrix[q[0][0]][q[0][1] - 1] = 50
                matrix[q[0][0] - 1][q[0][1] - 1] = 50
                return
            return
        return

    if figura == 6:
        global holturning
        holturning += 1
        if holturning % 4 == 1:
            x, y = q[2][0], q[2][1]
            if matrix[x - 1][y] == matrix[x - 1][y + 1] == matrix[x + 1][y] == 0:
                matrix[x - 1][y] = 60
                matrix[x - 1][y + 1] = 60
                matrix[x + 1][y] = 60
                for i in q:
                    matrix[i[0]][i[1]] = 0
                matrix[x][y] = 60
            else:
                if matrix[x - 1][y] != 0 and matrix[x - 1][y] == matrix[x - 1][y + 1] == 0:
                    matrix[x - 2][y] = 60
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x - 1][y] = 60
                    matrix[x - 2][y + 1] = 60
                    matrix[x][y] = 60
                elif (matrix[x - 1][y] != 0 or matrix[x - 1][y + 1] != 0) and matrix[x + 1][y - 1] == 0 and (
                        (matrix[x][y - 1] == 0 and matrix[x - 1][y - 1]) or (
                        matrix[x][y - 2] == 0 and matrix[x - 2][y - 2])) == 0:
                    co = 0
                    co += 0 if matrix[x - 1][y] != 0 else 2
                    co += 0 if matrix[x - 1][y + 1] != 0 or co == 2 else 1
                    if y != 0 and co == 1:
                        y -= 1
                        matrix[x][y] = 60
                        matrix[x - 1][y] = 60
                        matrix[x - 1][y + 1] = 60
                        matrix[x + 1][y] = 60
                        for i in q:
                            matrix[i[0]][i[1]] = 0
                    elif y > 1 and co == 2:
                        y -= 2
                        matrix[x][y] = 60
                        matrix[x - 1][y] = 60
                        matrix[x - 1][y + 1] = 60
                        matrix[x + 1][y] = 60
                        for i in q:
                            matrix[i[0]][i[1]] = 0
                    else:
                        holturning -= 1
                else:
                    holturning -= 1
        elif holturning % 4 == 2:
            x, y = q[2][0], q[2][1]
            if y != 0:
                if matrix[x][y - 1] == matrix[x][y + 1] == matrix[x + 1][y + 1] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x + 1][y + 1] = 60
                    matrix[x][y + 1] = 60
                    matrix[x][y - 1] = 60

                elif matrix[x - 1][y - 1] == matrix[x - 1][y + 1] == matrix[x][y + 1] == 0 and matrix[x + 1][
                    y + 1] != 0:
                    x -= 1
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x + 1][y + 1] = 60
                    matrix[x][y + 1] = 60
                    matrix[x][y - 1] = 60

                elif matrix[x][y - 1] == matrix[x][y - 2] == 0 and matrix[x][y + 1] != 0 and y > 1:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x + 1][y] = 60
                    matrix[x][y - 1] = 60
                    matrix[x][y - 2] = 60

                elif matrix[x][y + 2] == matrix[x + 1][y + 2] == 0 and matrix[x][y - 1] != 0 and y < 8:

                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x][y + 1] = 60
                    matrix[x][y + 2] = 60
                    matrix[x + 1][y + 2] = 60
                else:
                    holturning -= 1
            elif y == 0:
                if matrix[x][y + 2] == matrix[x + 1][y + 2] == 0 == matrix[x][y + 1]:
                    matrix[x][y + 2] = 60
                    matrix[x + 1][y + 2] = 60
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x][y + 1] = 60

                else:
                    holturning -= 1
            else:
                holturning -= 1

        elif holturning % 4 == 3:
            x, y = q[1][0], q[1][1]

            if matrix[x - 1][y] == matrix[x + 1][y] == matrix[x + 1][y - 1] == 0:
                matrix[x - 1][y] = 60
                matrix[x + 1][y] = 60
                matrix[x + 1][y - 1] = 60
                for i in q:
                    matrix[i[0]][i[1]] = 0
                matrix[x][y] = 60
            elif matrix[x - 1][y] == matrix[x - 2][y] == matrix[x][y - 1] == 0 and (
                    matrix[x + 1][y] != 0 or matrix[x + 1][y - 1] != 0):
                for i in q:
                    matrix[i[0]][i[1]] = 0
                matrix[x][y] = 60
                matrix[x - 1][y] = 60
                matrix[x - 2][y] = 60
                matrix[x][y - 1] = 60
            else:
                holturning -= 1
        elif holturning % 4 == 0:
            x, y = q[1][0], q[1][1]
            if y != 9:
                if matrix[x - 1][y - 1] == matrix[x][y - 1] == matrix[x][y + 1] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 60
                    matrix[x - 1][y - 1] = 60
                    matrix[x][y - 1] = 60
                    matrix[x][y + 1] = 60
                elif y != 1 and matrix[x][y + 1] != 0 and matrix[x][y - 1] == matrix[x][y - 2] == matrix[x - 1][
                    y - 2] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 60
                    matrix[x][y - 2] = 60
                    matrix[x - 1][y - 2] = 60
                    matrix[x][y] = 60
                else:
                    holturning -= 1
            elif y == 9:
                if matrix[x][y - 1] == matrix[x][y - 2] == matrix[x - 1][y - 2] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 60
                    matrix[x][y - 2] = 60
                    matrix[x - 1][y - 2] = 60
                    matrix[x][y] = 60
                else:
                    holturning -= 1
            else:
                holturning -= 1
    if figura == 7:
        global tturning
        tturning += 1
        tturning %= 4
        if tturning == 1:  # уже понял
            x, y = q[2][0], q[2][1]
            if matrix[x + 1][y] == 0:
                matrix[q[1][0]][q[1][1]] = 0
                matrix[x + 1][y] = 70
            else:
                if matrix[x + 2][y] == 0 == matrix[x - 1][y + 1]:
                    x -= 1
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 70
                    matrix[x + 1][y] = 70
                    matrix[x - 1][y] = 70
                    matrix[x][y + 1] = 70
                else:
                    tturning -= 1
        elif tturning == 2:
            x, y = q[1][0], q[1][1]
            if y != 0:
                if matrix[x][y - 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[x][y - 1] = 70
                elif matrix[x][y + 1] == matrix[x + 1][y + 1] == matrix[x][y + 2] == 0:
                    y += 1
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 70
                    matrix[x + 1][y] = 70
                    matrix[x][y - 1] = 70
                    matrix[x][y + 1] = 70
                else:
                    tturning -= 1

            else:
                if matrix[x - 1][y + 1] == 0 and matrix[x][y + 2] == 0:
                    y += 1
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 70
                    matrix[x + 1][y] = 70
                    matrix[x][y - 1] = 70
                    matrix[x][y + 1] = 70
                else:
                    tturning -= 1
        elif tturning == 3:
            x, y = q[1][0], q[1][1]
            if matrix[x - 1][y] == 0:
                matrix[x][y + 1] = 0
                matrix[x - 1][y] = 70
            else:
                tturning -= 1
        elif tturning == 0:
            x, y = q[2][0], q[2][1]
            if y != 9:
                if matrix[x][y + 1] == 0:
                    matrix[x][y + 1] = 70
                    matrix[x + 1][y] = 0
                else:
                    y -= 1
                    if matrix[x - 1][y] == 0 == matrix[x][y - 1]:
                        for i in q:
                            matrix[i[0]][i[1]] = 0
                        matrix[x][y] = 70
                        matrix[x - 1][y] = 70
                        matrix[x][y - 1] = 70
                        matrix[x][y + 1] = 70
                    else:
                        tturning -= 1
            if y == 9:
                if matrix[x - 1][y - 1] == 0 == matrix[x][y - 2]:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 70
                    matrix[x - 1][y - 1] = 70
                    matrix[x][y - 1] = 70
                    matrix[x][y - 2] = 70
                else:
                    tturning -= 1
        else:
            tturning -= 1
            return


def probel():
    for i in range(24):
        move_down()


def udalenie():
    for i in range(22):
        da = 0
        for j in range(10):
            if matrix[i][j] == 0:
                da = 1
                break
        if da == 0:
            matrix.pop(i)
            matrix.insert(0, ([0] * 10))


holturning = 0



c = 0


def ceshka():
    global c
    global cnt_ce
    if cnt_ce == 0:
        if c == 0:
            for i in range(22):
                for j in range(10):
                    if matrix[i][j] > 9:
                        ce = matrix[i][j] // 10
                        matrix[i][j] = 0
            c = ce
            spawn()
        else:
            for i in range(22):
                for j in range(10):
                    if matrix[i][j] > 9:
                        ce = matrix[i][j] // 10
                        matrix[i][j] = 0
            if c == 1:
                cubik()
            elif c == 2:
                palka()
            elif c == 3:
                snake()
            elif c == 4:
                ekans()
            elif c == 5:
                loh()
            elif c == 6:
                hol()
            elif c == 7:
                bukva()
            c = ce
    cnt_ce += 1

"""
hol()
move_down()
move_down()
for i in range(len(matrix)):
    print(i, matrix[i])
print()
print()
turn() 
for i in range(len(matrix)):
    print(i, matrix[i])
print()
print()
turn() 
for i in range(len(matrix)):
    print(i, matrix[i])
print()
print()
turn()
for i in range(len(matrix)):
    print(i, matrix[i])
print()
print()
turn()


for i in range(len(matrix)):
    print(i, matrix[i])
print(histor_vpered, history)
"""

picture = 0
pictures = ['cubiks', 'cats', 'osmin', 'coals'] # тут названия папок с темами
pygame.init()
move_down_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_down_event, 1000)
size = width, height = 960, 784
screen = pygame.display.set_mode(size)
pygame.display.flip()
running = True
a = Board(10, 21)
a.set_view(60, 17, 30)
koords = a.get_coords()
print(koords[0][0])
a.render(screen)
clock = pygame.time.Clock()
pygame.display.flip()
for i in range(len(matrix)):
    print(i, matrix[i])
print(histor_vpered, history)
count_cringe = 0
while running:
    if count_cringe % 2 == 0:
        pic1 = pygame.image.load(f'img/{pictures[picture]}/1.png')
        pic1.set_colorkey((255, 255, 255))
        pic2 = pygame.image.load(f'img/{pictures[picture]}/2.png')
        pic2.set_colorkey((255, 255, 255))
        pic3 = pygame.image.load(f'img/{pictures[picture]}/4.png')
        pic3.set_colorkey((255, 255, 255))
        pic4 = pygame.image.load(f'img/{pictures[picture]}/3.png')
        pic4.set_colorkey((255, 255, 255))
        pic5 = pygame.image.load(f'img/{pictures[picture]}/5.png')
        pic5.set_colorkey((255, 255, 255))
        pic6 = pygame.image.load(f'img/{pictures[picture]}/6.png')
        pic6.set_colorkey((255, 255, 255))
        pic7 = pygame.image.load(f'img/{pictures[picture]}/7.png')
        pic7.set_colorkey((255, 255, 255))
        screen.fill((0, 0, 0))
    else:
        pic1 = pygame.image.load('img/cats/cring.jpg')
        pic2 = pygame.image.load('img/cats/cring.jpg')
        pic3 = pygame.image.load('img/cats/cring.jpg')
        pic4 = pygame.image.load('img/cats/cring.jpg')
        pic5 = pygame.image.load('img/cats/cring.jpg')
        pic6 = pygame.image.load('img/cats/cring.jpg')
        pic7 = pygame.image.load('img/cats/cring.jpg')

        pic = pygame.image.load('img/cats/cring.jpg')
        pic = pygame.transform.scale(pic, (960, 784))
        pia11 = pic.get_rect(bottomright=(960, 784))
        screen.blit(pic, pia11)
    pic1 = pygame.transform.scale(pic1, (30, 30))
    pic2 = pygame.transform.scale(pic2, (30, 30))
    pic3 = pygame.transform.scale(pic3, (30, 30))
    pic4 = pygame.transform.scale(pic4, (30, 30))
    pic5 = pygame.transform.scale(pic5, (30, 30))
    pic6 = pygame.transform.scale(pic6, (30, 30))
    pic7 = pygame.transform.scale(pic7, (30, 30))
    pic1.set_colorkey((255, 255, 255))
    pic2.set_colorkey((255, 255, 255))
    pic3.set_colorkey((255, 255, 255))
    pic4.set_colorkey((255, 255, 255))
    pic5.set_colorkey((255, 255, 255))
    pic6.set_colorkey((255, 255, 255))
    pic7.set_colorkey((255, 255, 255))
    a.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                turn()
            if event.key == pygame.K_SPACE:
                probel()
            if event.key == pygame.K_RIGHT:
                move_right()
            if event.key == pygame.K_LEFT:
                move_left()
            if event.key == pygame.K_DOWN:
                move_down()
            if event.key == pygame.K_c:
                ceshka()
            if event.key == pygame.K_1:
                picture = 0
            if event.key == pygame.K_2:
                picture = 1
            if event.key == pygame.K_3:
                picture = 2
            if event.key == pygame.K_4:
                picture = 3
            if event.key == pygame.K_k:
                count_cringe += 1
        if event.type == move_down_event:
            move_down()
    t = False
    for i in range(1, 22):
        for j in range(10):

            qq = matrix[i][j]
            if matrix[i][j] == 0:
                continue
            if matrix[i][j] > 9:
                t = True
            if qq == 1 or qq == 10:
                y, x = koords[i - 1][j]
                pia = pic1.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic1, pia)
            if qq == 2 or qq == 20:
                y, x = koords[i - 1][j]
                pia = pic2.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic2, pia)
            if qq == 3 or qq == 30:
                y, x = koords[i - 1][j]

                pia = pic3.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic3, pia)
            if qq == 4 or qq == 40:
                y, x = koords[i - 1][j]
                pia = pic4.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic4, pia)
            if qq == 5 or qq == 50:
                y, x = koords[i - 1][j]

                pia = pic5.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic5, pia)
            if qq == 6 or qq == 60:
                y, x = koords[i - 1][j]
                pia = pic6.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic6, pia)
            if qq == 7 or qq == 70:
                y, x = koords[i - 1][j]
                pia = pic7.get_rect(
                    bottomright=(x + 28, y + 28))
                screen.blit(pic7, pia)

    if not t:
        udalenie()
        spawn()

    if t:
        pass
        # вот тут должно быть опускание фигурки сомо по себе которое
        # и поидее все, весь геймплей готов будет

    pygame.display.flip()
