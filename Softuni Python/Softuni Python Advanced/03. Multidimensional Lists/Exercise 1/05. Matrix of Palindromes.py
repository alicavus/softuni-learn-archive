rows, cols = map(int, input().split())

for ridx in range(rows):
    cur_ch = ord('a') + ridx
    print(*[f'{chr(cur_ch)}{chr(cur_ch + cidx)}{chr(cur_ch)}' for cidx in range(cols)])