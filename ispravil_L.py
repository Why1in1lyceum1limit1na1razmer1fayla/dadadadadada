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
