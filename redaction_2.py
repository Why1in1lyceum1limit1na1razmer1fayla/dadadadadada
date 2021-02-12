from random import randrange

matrix = [[0 for i in range(10)] for j in range(22)]
matrix.append([1 for _ in range(10)])
kub = 1
pal = 2
zag1 = 3
zag2 = 4
g1 = 5
g2 = 6
tet = 7
histor_vpered = []
f = True
# генерация
pieces = [1, 2, 3, 4, 5, 6, 7]
order = []

pool = pieces * 5

firstPiece = [2, 5, 6, 7][randrange(4)]
print(firstPiece, '-')
histor_vpered.append(firstPiece)
history = [3, 4, 3, firstPiece]

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
    histor_vpered.pop(0)
    el = generat()
    histor_vpered.append(el)


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


def move():
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


cubik()
for i in range(21):
    qwe12312312 = move()
palka()

for i in range(21):
    qwe12312312 = move()
loh()
for i in range(21):
    qwe12312312 = move()
hol()
for i in range(21):
    qwe12312312 = move()

for i in range(len(matrix)):
    print(i, matrix[i])
print(histor_vpered, history)
