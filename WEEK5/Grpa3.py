#Implement all the given functions that are used to solve the below problems. 

def index_of_first_occurance(row: list, elem):
    '''
    Given a list find the index of first occurrence of elem in it.
    '''
    for i in range(len(row)):
        if row[i] == elem:
            return i
    return -1


def index_of_last_occurance(row: list, elem):
    '''
    Given a list find the index of last occurrence of elem in it.
    '''
    for i in range(len(row) - 1, -1, -1):
        if row[i] == elem:
            return i
    return -1


def is_valid_coordinate(x: int, y: int, M):
    '''
    Checks if x,y is a valid coordinate in matrix M.
    '''
    return 0 <= x < len(M) and 0 <= y < len(M[0])


def valid_adjacent_coordinates(x: int, y: int, M):
    '''
    Create a set of valid adjacent coordinates.
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    return {
        (x1, y1)
        for dx, dy in directions
        for x1, y1 in [(x + dx, y + dy)]
        if is_valid_coordinate(x1, y1, M)
    }


def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find adjacent coordinate having given value.
    '''
    adjacents = valid_adjacent_coordinates(*curr_coords, M)

    if prev_coords is not None:
        adjacents.discard(prev_coords)

    for coord in adjacents:
        if M[coord[0]][coord[1]] == value:
            return coord

    return None


def get_path_coordinates(M):
    '''
    Given matrix M, find the path formed by 1 from last row to first row.
    '''
    x_start = len(M) - 1
    x_end = 0

    y_start = index_of_last_occurance(M[-1], 1)
    y_end = index_of_first_occurance(M[0], 1)

    path = []
    curr = (x_start, y_start)
    prev = None

    while curr != (x_end, y_end):
        path.append(curr)
        next_coord = next_coordinate_with_value(curr, 1, M, prev)
        prev = curr
        curr = next_coord

    path.append(curr)

    return path[::-1]


def print_path(M):
    path = get_path_coordinates(M)

    for coord in path:
        print(coord)


def alternate_path(M):
    path = get_path_coordinates(M)

    for i, coord in enumerate(path):
        if i % 2 == 0:
            M[coord[0]][coord[1]] = 2


def count_path(M):
    path = get_path_coordinates(M)

    for i, coord in enumerate(path):
        M[coord[0]][coord[1]] = i + 1


def mirror_horizontally(M):
    path = get_path_coordinates(M)
    cols = len(M[0])

    for coord in path:
        mirror_x = coord[0]
        mirror_y = cols - 1 - coord[1]
        M[mirror_x][mirror_y] = 1


def mirror_vertically(M):
    path = get_path_coordinates(M)
    rows = len(M)

    for coord in path:
        mirror_x = rows - 1 - coord[0]
        mirror_y = coord[1]
        M[mirror_x][mirror_y] = 1 