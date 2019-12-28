def minesweeper(bombs,num_rows,num_cols) :
    maps = [ [0 for _ in range(num_cols)] for _ in range(num_rows)  ]
    for bomb in bombs :
        for row in [bomb[0] - 1, bomb[0], bomb[0] + 1] :
            for col in [bomb[1] - 1, bomb[1], bomb[1] + 1] :
                if 0 <= row < num_rows and 0 <= col < num_cols:
                    maps[row][col] += 1
    for bomb in bombs :
        maps[bomb[0]][bomb[1]] = -1
    return maps

print(minesweeper([[0,0],[0,1]],3,4))