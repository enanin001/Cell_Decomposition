import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 地图尺寸和障碍物定义
map_size = (40, 40)
grid = np.zeros(map_size)

# 固定分布的障碍物位置
circle_obstacles = [
    ((10, 10), 3),  # 圆形障碍物1，中心(10, 10)，半径3
    ((25, 25), 2)   # 圆形障碍物2，中心(25, 25)，半径2
]

square_obstacles = [
    (5, 5, 4),   # 正方形障碍物1，左上角(5, 5)，边长4
    (15, 15, 5), # 正方形障碍物2，左上角(15, 15)，边长5
    (30, 10, 3)  # 正方形障碍物3，左上角(30, 10)，边长3
]

# 添加圆形障碍物
def add_circle_obstacle(center, radius):
    for x in range(center[0] - radius, center[0] + radius + 1):
        for y in range(center[1] - radius, center[1] + radius + 1):
            if (x - center[0])**2 + (y - center[1])**2 <= radius**2:
                if 0 <= x < map_size[0] and 0 <= y < map_size[1]:
                    grid[x, y] = 1

# 添加正方形障碍物
def add_square_obstacle(top_left, size):
    for x in range(top_left[0], top_left[0] + size):
        for y in range(top_left[1], top_left[1] + size):
            if 0 <= x < map_size[0] and 0 <= y < map_size[1]:
                grid[x, y] = 1

# 将固定位置的障碍物添加到地图上
for center, radius in circle_obstacles:
    add_circle_obstacle(center, radius)

for top_left_x, top_left_y, size in square_obstacles:
    add_square_obstacle((top_left_x, top_left_y), size)

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
start_point = (1, 1)
end_point = (11, 11)

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
    ax.set_xlim([0, n_cells_x])
    ax.set_ylim([0, n_cells_y])

    # 绘制圆形障碍物
    for center, radius in circle_obstacles:
        ax.add_patch(patches.Circle((center[0] / cell_size, center[1] / cell_size), radius / cell_size, color='blue'))

    # 绘制正方形障碍物
    for top_left_x, top_left_y, size in square_obstacles:
        ax.add_patch(patches.Rectangle((top_left_x / cell_size, top_left_y / cell_size), size / cell_size, size / cell_size, color='yellow'))

    # 绘制路径
    x_coords, y_coords = zip(*path)
    ax.plot(x_coords, y_coords, 'o-', color='powderblue')
    plt.show(block=True)  # 确保窗口保持开启
    input("Press Enter to close...")
else:
    print("No path found between the start and end points.")
