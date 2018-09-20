from copy import deepcopy

SIZE = 3

target = []
pos_in_target = {}
path = {}


def initial():
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            if i == j == SIZE - 1:
                row.append(0)
            else:
                row.append(i * SIZE + j + 1)
            pos_in_target[row[-1]] = (i, j)
        target.append(row)


def manhattan_distance(table):
    distance = 0
    for i in range(SIZE):
        for j in range(SIZE):
            num = table[i][j]
            if num != 0:
                ii, jj = pos_in_target[num]
                distance += (abs(i - ii) + abs(j - jj))
    return distance


def is_target(table):
    for i in range(SIZE):
        for j in range(SIZE):
            if table[i][j] != target[i][j]:
                return False
    return True


def print_path(depth):
    for i in range(depth):
        print(path[i], end='')


def is_contrary_direction(direction1, direction2):
    if direction1 == 'u' and direction2 == 'd':
        return True
    if direction1 == 'd' and direction2 == 'u':
        return True
    if direction1 == 'l' and direction2 == 'r':
        return True
    if direction1 == 'r' and direction2 == 'l':
        return True
    return False


def delta(direction):
    i, j = 0, 0
    if direction == 'u':
        i = -1
    elif direction == 'd':
        i = 1
    elif direction == 'l':
        j = -1
    elif direction == 'r':
        j = 1
    return i, j


def search(table0, i0, j0, direction0, depth0, cost0, limit):
    if is_target(table0):
        print_path(depth0)
        return True
    if depth0 == limit:
        return False
    for direction in ['u', 'd', 'l', 'r']:
        table = deepcopy(table0)
        if is_contrary_direction(direction, direction0):
            continue
        di, dj = delta(direction)
        i, j = i0 + di, j0 + dj
        if i < 0 or j < 0 or i >= SIZE or j >= SIZE:
            continue
        table[i0][j0] = table[i][j]
        table[i][j] = 0
        if direction == 'u' and i < pos_in_target[table[i0][j0]][0]:
            cost = cost0 - 1
        elif direction == 'd' and i > pos_in_target[table[i0][j0]][0]:
            cost = cost0 - 1
        elif direction == 'l' and j < pos_in_target[table[i0][j0]][1]:
            cost = cost0 - 1
        elif direction == 'r' and j > pos_in_target[table[i0][j0]][1]:
            cost = cost0 - 1
        else:
            cost = cost0 + 1
        depth = depth0 + 1
        if depth + cost > limit:
            continue
        path[depth0] = direction
        if search(table, i, j, direction, depth, cost, limit):
            return True
    return False


def main():
    initial()
    table0 = []
    i0 = j0 = 0
    for i in range(SIZE):
        row = [int(_) for _ in input().split()]
        assert len(row) == 3
        if 0 in row:
            i0 = i
            j0 = row.index(0)
        table0.append(row)
    cost0 = manhattan_distance(table0)
    limit = cost0
    while True:
        if search(table0, i0, j0, 'x', 0, cost0, limit):
            break
        limit += 1


if __name__ == '__main__':
    main()
