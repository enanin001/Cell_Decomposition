import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 地图尺寸和障碍物定义
map_size = (40, 40)
grid = np.zeros(map_size)
obstacles = [(2, 2), (2, 3), (3, 2), (3, 3), (6, 6), (6, 7), (7, 6), (7, 7)]
#obstacles = [(0, 0), (0, 1), (1, 0), (1, 1)]

triangles = [
    [(5, 5), (5, 7), (7, 6)], [(10, 10), (10, 12), (12, 11)], [(15, 15), (15, 17), (17, 16)],
    [(20, 20), (20, 22), (22, 21)], [(25, 25), (25, 27), (27, 26)], [(30, 30), (30, 32), (32, 31)],
    [(35, 35), (35, 37), (37, 36)]
]
for triangle in triangles:
    for point in triangle:
        obstacles.append(point)


for obs in obstacles:
    if 0 <= obs[0] < map_size[0] and 0 <= obs[1] < map_size[1]:
        grid[obs] = 1  # 1代表障碍

# 每个单元的大小
cell_size = 2
n_cells_x = map_size[0] // cell_size
n_cells_y = map_size[1] // cell_size

# 创建一个格网表示地图的单元
cells = np.zeros((n_cells_x, n_cells_y))
for x in range(n_cells_x):
    for y in range(n_cells_y):
        sub_grid = grid[x*cell_size:(x+1)*cell_size, y*cell_size:(y+1)*cell_size]
        if np.any(sub_grid == 1):
            cells[x, y] = 1

# 预设起点和终点，确保它们不在边界上
start_point = (3, 2)
end_point = (10,15)

# 创建图表示分解后的单元
G = nx.grid_graph(dim=[n_cells_x, n_cells_y])
for x in range(n_cells_x):
    for y in range(n_cells_y):
        if cells[x, y] == 1:
            G.remove_node((x, y))

# 使用 A* 算法找到最短路径
if nx.has_path(G, start_point, end_point):
    path = nx.astar_path(G, start_point, end_point)
    fig, ax = plt.subplots()
    ax.imshow(cells.T, cmap='Greys', origin='lower', extent=[0, n_cells_x, 0, n_cells_y])
    x_coords, y_coords = zip(*path)
    ax.plot(x_coords, y_coords, 'o-', color='powderblue')
    plt.show(block=True)  # 确保窗口保持开启
    input("Press Enter to close...")
else:
    print("No path found between the start and end points.")
