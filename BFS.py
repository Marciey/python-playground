from pyamaze import maze, agent, COLOR, textLabel

def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    path_length = {start: 0}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                path_length[childCell] = path_length[currCell] + 1  # Update the path length for the child cell

    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath, path_length[(1, 1)]

if __name__ == "__main__":
    m = maze(5, 5)
    m.CreateMaze() 
    path, length = BFS(m)
    a = agent(m, footprints=True)
    m.tracePath({a: path})
    l = textLabel(m, 'Length of Shortest Path', length + 1)
    m.run()