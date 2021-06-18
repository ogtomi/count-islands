path = 'D:\Random\count-islands\data.txt'
with open(path, 'r') as f:
    content = f.read().split('\n')

def get_2d(data, M, N):
    arr_2d = []

    for i in range(N):
        new = []
        for j in range(M):
            new.append(data[i][j])
        arr_2d.append(new)
    
    return arr_2d

def land_check(data, M, N, row_new, col_new):
    if data[row_new][col_new] == '0':
        return

    data[row_new][col_new] = '0'

    if row_new != 0:
        land_check(data, M, N, row_new-1, col_new)
        if col_new != M - 1:
            land_check(data, M, N, row_new-1, col_new+1)
    
    if row_new != N - 1:
        land_check(data, M, N, row_new+1, col_new)
        if col_new != 0:
            land_check(data, M, N, row_new+1, col_new-1)
    
    if col_new != 0:
        land_check(data, M, N, row_new, col_new-1)
        if row_new != 0:
            land_check(data, M, N, row_new-1, col_new-1)
    
    if col_new != M - 1:
        land_check(data, M, N, row_new, col_new+1)
        if row_new != N - 1:
            land_check(data, M, N, row_new+1, col_new+1)

def count_islands(data):
    M = len(data[0])
    N = len(data)
        
    count = 0
    data_2d = get_2d(data, M, N)

    for row in range(N):
        for col in range(M):
            if data_2d[row][col] == '1':
                land_check(data_2d, M, N, row, col)
                count += 1
    return count

print(count_islands(content))
