import sys

try:
    path = sys.argv[1]
    with open(path, 'r') as f:
        content = f.read().split('\n')
except Exception as e:
    sys.stderr.write(str(e))

def get_2d(data, M, N):
    arr_2d = []

    for i in range(M):
        new = []
        for j in range(N):
            new.append(data[i][j])
        arr_2d.append(new)
    
    return arr_2d

def land_check(data, M, N, row_new, col_new):
    if data[row_new][col_new] == '0':
        return 0
    
    data[row_new][col_new] = '0'

    if row_new != 0:
        land_check(data, M, N, row_new-1, col_new)
        if col_new != N - 1:
            land_check(data, M, N, row_new-1, col_new+1)
    
    if row_new != M - 1:
        land_check(data, M, N, row_new+1, col_new)
        if col_new != 0:
            land_check(data, M, N, row_new+1, col_new-1)
    
    if col_new != 0:
        land_check(data, M, N, row_new, col_new-1)
        if row_new != 0:
            land_check(data, M, N, row_new-1, col_new-1)
    
    if col_new != N - 1:
        land_check(data, M, N, row_new, col_new+1)
        if row_new != M - 1:
            land_check(data, M, N, row_new+1, col_new+1)

def count_islands(data):
    if data == None or len(data) == 0:
        return 0
    
    M = len(data)
    N = len(data[0])

    count = 0
    data_2d = get_2d(data, M, N)

    for row in range(M):
        for col in range(N):
            if data_2d[row][col] == '1':
                land_check(data_2d, M, N, row, col)
                count += 1
    return count

try:
    sys.stdout.write(str(count_islands(content)))
except Exception as e:
    sys.stderr.write(str(e))