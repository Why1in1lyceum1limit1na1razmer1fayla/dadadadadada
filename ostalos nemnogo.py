from random import randrange
import pygame
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
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
                pygame.draw.rect(screen, (255, 255, 255),
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
        x, y = self.left, self.top
        sp = []
        sp1 = []
        for i in range(21):
            for j in range(10):
                sp.append((x + i * 25 + 1, 1 + y + j * 25))
            sp1.append(sp)
            sp =[]
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
    print('loh')


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

def stop():
    for i in range(2, 22):
        for j in range(10):
            if matrix[i][j] > 8:
                matrix[i][j] = matrix[i][j] // 10


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
        # palka
        osn = q[1]
        osng = q[2]
        x, y = osn[0], osn[1]
        if matrix[q[0][1]] == matrix[q[1][1]]:
            if y != 9 and y >= 2:
                if matrix[x][y + 1] == 0 and matrix[x][y - 1] == 0 and matrix[x][y - 2] == 0:
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y + 1] = 20
                    matrix[x][y - 1] = 20
                    matrix[x][y - 2] = 20
                else:
                    a = 7
                    b = 0
                    if y == 3:
                        b = 1
                    count = 0
                    flag1 = -1
                    for i in range(b, a):
                        if count == 3:
                            flag1 = y - 3 + i - 1
                            break
                        if i == 3:
                            continue
                        if matrix[x][y - 3 + i] == 0:
                            count += 1
                        else:
                            count = 0
                    if flag1 == -1:
                        return
                    else:
                        zz = 3
                        while zz != 0:
                            if matrix[x][flag1] == 20:
                                flag1 -= 1
                                continue
                            matrix[x][flag1] = 20
                            flag1 -= 1
                            zz -= 1
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
            if y == 9:
                if matrix[x][y - 1] == 0 and matrix[x][y - 2] == 0 and matrix[x][y - 3] == 0:
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 20
                    matrix[x][y - 2] = 20
                    matrix[x][y - 3] = 20
            if y == 0:
                if matrix[x][y + 1] == 0 and matrix[x][y + 2] == 0 and matrix[x][y + 3] == 0:
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y + 1] = 20
                    matrix[x][y + 2] = 20
                    matrix[x][y + 3] = 20
            if y == 1:
                if matrix[x][y + 1] == 0 and matrix[x][y + 2] == 0 and matrix[x][y - 1] == 0:
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y + 1] = 20
                    matrix[x][y + 2] = 20
                    matrix[x][y - 1] = 20
                elif matrix[x][y + 1] == 0 and matrix[x][y + 2] == 0 and matrix[x][y + 3] == 0:
                    for i in q:
                        if osn == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y + 1] = 20
                    matrix[x][y + 2] = 20
                    matrix[x][y + 3] = 20
            else:
                return
            # вертикально
        else:
            x, y = osng[0], osng[1]
            zz = 3
            if x < 20:
                if matrix[x - 2][y] == 0 and matrix[x + 1][y] == 0 and matrix[x - 1][y] == 0:
                    matrix[x - 2][y] = 20
                    matrix[x - 1][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                elif matrix[x - 1][y] == 0 and matrix[x + 1][y] == 0 and matrix[x + 2][y] == 0:
                    matrix[x + 2][y] = 20
                    matrix[x - 1][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                elif matrix[x + 3][y] == 0 and matrix[x + 1][y] == 0 and matrix[x + 2][y] == 0:
                    matrix[x + 2][y] = 20
                    matrix[x + 3][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
            if x == 20:
                if matrix[x - 1][y] == 0 and matrix[x + 1][y] == 0 and matrix[x + 2][y] == 0:
                    matrix[x + 2][y] = 20
                    matrix[x - 1][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
                elif matrix[x + 3][y] == 0 and matrix[x + 1][y] == 0 and matrix[x + 2][y] == 0:
                    matrix[x + 2][y] = 20
                    matrix[x + 3][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
            if x == 21:
                if matrix[x + 3][y] == 0 and matrix[x + 1][y] == 0 and matrix[x + 2][y] == 0:
                    matrix[x + 2][y] = 20
                    matrix[x + 3][y] = 20
                    matrix[x + 1][y] = 20
                    for i in q:
                        if osng == i:
                            continue
                        matrix[i[0]][i[1]] = 0
        return
        # горизонтально
    if figura == 3:
        if matrix[q[3][0]][q[3][1] - 1] != 30:
            if q[0][1] != 0:
                if matrix[q[3][0]][q[3][1] - 1] == 0 and matrix[q[3][0]][q[3][1] - 2] == 0:
                    matrix[q[3][0]][q[3][1]] = 0
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[3][0]][q[3][1] - 1] = 30
                    matrix[q[3][0]][q[3][1] - 2] = 30
                    return
            if q[3][1] != 9:
                if matrix[q[3][0]][q[3][1] - 1] == 0 and matrix[q[3][0]][q[3][1] + 1] == 0:
                    matrix[q[0][0]][q[0][1]] = 0
                    matrix[q[3][0]][q[3][1] - 1] = 30
                    matrix[q[3][0]][q[3][1] + 1] = 30
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
                    if matrix[q[0][0] + 2][q[0][1]] == 0 and matrix[q[0][0] + 1][q[0][1] + 2] == 0 and \
                            matrix[q[0][0] + 1][q[0][1] + 1] == 0:
                        matrix[q[0][0]][q[0][1]] = 0
                        matrix[q[2][0]][q[2][1]] = 0
                        matrix[q[3][0]][q[3][1]] = 0
                        matrix[q[0][0] + 2][q[0][1]] = 50
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
                if q[0][1] != 9:
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

    if figura == 6:
        global holturning
        holturning += 1
        holturning %= 4
        if holturning == 1:
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
        elif holturning == 2:
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
                if matrix[x][y + 2] == matrix[x + 1][y + 2] == 0 and matrix[x][y - 1] != 0 and y < 8:
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

        elif holturning == 3:
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
        elif holturning == 0:
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
            if y == 9:
                if y != 1 and matrix[x][y + 1] != 0 and matrix[x][y - 1] == matrix[x][y - 2] == matrix[x - 1][
                    y - 2] == 0:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y - 1] = 60
                    matrix[x][y - 2] = 60
                    matrix[x - 1][y - 2] = 60
                    matrix[x][y] = 60
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
            print(x, y)
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
                if matrix[x - 1][y] == 0 == matrix[x][y - 1]:
                    for i in q:
                        matrix[i[0]][i[1]] = 0
                    matrix[x][y] = 70
                    matrix[x - 1][y] = 70
                    matrix[x][y - 1] = 70
                    matrix[x][y + 1] = 70
                else:
                    tturning -= 1
        else:
            tturning -= 1
            return


def poribel():
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

pygame.init()
size = width, height = 960, 784
screen = pygame.display.set_mode(size)
pygame.display.flip()
running = True
a = Board(10, 21)
a.set_view(60, 17, 25)
koords = a.get_coords()
print(koords[0][0])
a.render(screen)
pygame.display.flip()
cubik()
move_down()
move_left()
move_left()
move_left()
move_left()
for i in range(len(matrix)):
    print(i, matrix[i])
print(histor_vpered, history)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            a.get_click(event.pos)
    for i in range(1, 22):
        for j in range(10):
            t = False
            qq = matrix[i][j]
            if matrix[i][j] == 0:
                continue
            if matrix[i][j] > 9:
                t = True
            elif qq == 1 or qq == 10:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/1.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 2 or qq == 20:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/2.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 3 or qq == 30:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/3.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 4 or qq == 40:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/4.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 5 or qq == 50:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/5.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 6 or qq == 60:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/6.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
            elif qq == 7 or qq == 70:
                x, y = koords[i - 1][j]
                pic = pygame.image.load('img/cats/7.png')
                pic.set_colorkey((255, 255, 255))
                pia = pic.get_rect(
                    bottomright=(x + 23, y + 23))
                screen.blit(pic, pia)
    
    if not t:
        udalenie()
        spawn()
    if t:
        pass # вот тут должно быть опускание фигурки сомо по себе которое
        # и поидее все, весь геймплей готов будет

    pygame.display.flip()
