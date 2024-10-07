# Cell_Decomposition



Outline


Concept Selection Motive
Approach Algorithm Overview
Implementation Approach
Parameter Setting
Challenges and Learnings
Visualization
Code Demonstration
Reference






Concept Selection Motive

In this assignment, I choose the method of combining Cell Decomposition and A* algorithm [1] mainly because these methods can effectively deal with the pathfinding problem in large-scale grid, especially when there are multiple obstacles, which is more practical for solving the path finding problem of realistic robots. The Cell Decomposition method simplifies the complexity of the map by dividing the map into smaller processing units, while the heuristic nature of the A* algorithm provides fast search performance. This combination not only reduces the computational load by simplifying the environment, but also improves the efficiency and quality of the wayfinding process, ensuring that the optimal or near-optimal path is found quickly and reliably.



Algorithm Overview

The algorithm used in the code is the A* algorithm, which is a heuristic search algorithm used to find the shortest path from the starting point to the end point in the graph. It combines the actual cost (the cost from the starting point to the current node) with a heuristic estimate (usually a cost function) to predict the best path from the current node to the destination node. Heuristic estimates are often based on functions such as Euclidean distance or Manhattan distance, which help guide the search process based on the nature of the path.

The A* algorithm is efficient because it combines the advantages of Dijkstra's algorithm and greedy best-first search. Dijkstra's algorithm ensures that the shortest path is found by systematically examining all possible paths, while the greedy best first search focuses on the path that is more likely to reach the target quickly. A* strikes a balance between the two, ensuring optimal solutions while significantly speeding up the search process. This makes A* the first choice for path planning problems, especially in environments with obstacles.

In the context of the code, the A* algorithm is used to find the path in the decomposed grid diagram. First, the map is divided into smaller units, each representing a 2x2 region of the actual map. Round and square obstacles are then added to the map, and the cells occupied by these obstacles are marked as impassable. After the graph is created, the A* algorithm searches for a path from the predefined starting point (1,1) to the end point (11,11). If a path is found, the code generates a graphical representation showing the obstacle and the path taken.

Implementation Approach 
Map and Obstacle definition: Initially, a 40x40 two-dimensional grid was defined to represent the map, which was large enough to show complex environments and different path choices. Create obstacles, including round and square obstacles, by marking specific cells on the grid, simulate the shape of obstacles that would appear in the real world, and test the performance of the algorithm under a variety of conditions.

Obstacle addition function: Defines the circle and square obstacle addition function, by calculating and modifying the value on the grid, precisely mark the position of the obstacle. This approach allows the dynamic addition or modification of obstacles on the map, giving the system the flexibility to adapt to different test scenarios or application requirements.

Cell decomposition: The further division of the map into smaller 2x2 units is the core of the unit decomposition strategy, which greatly reduces the complexity of data processing. This step optimizes storage space and speeds up processing by dividing large maps into smaller, more manageable chunks, simplifying the wayfinding process.

Graph creation and modification: Use the NetworkX library to create graphs based on subdivided cells as a basis for path search. In this diagram, cells containing obstacles are considered impassable and removed from the diagram to ensure the accuracy and effectiveness of path planning.

Pathfinding: The A* algorithm is used to find the shortest path from the beginning to the end of the graph. The algorithm effectively calculates the feasible path by considering the passability of each unit and its connection to other units. If there is a path, the system dynamically displays the path and the obstacles it passes through on the graphical interface to visually show the results and effectiveness of the algorithm.



Parameter Setting

In this code, several key parameters are used to define and manipulate the map, which are critical because they directly affect map layout and pathfinding performance:

map_size: This parameter defines the overall size of the map, which is set here to 40x40. This means that the map consists of 40 rows and 40 columns, for a total of 1600 cells. This size is large enough to show complex path planning scenarios, but small enough to keep the calculations manageable and efficient.

cell_size: The size of each cell is set to 2, indicating that each cell contains a 2x2 grid. This decomposition breaks down the original large grid into smaller units, each made up of four smaller units. This decomposition helps simplify complex map structures, making path searching more efficient and precise.

circle_obstacle and square_obstacle: These two parameters define the location and size of obstacles on the map. Set round and square obstacles with these parameters, specifying their central position, radius (circle), and side length (square). The presence of obstacles is an important factor in path planning because they affect the generation and selection of paths.



Visualization
Fig 01


Fig02

I tried to adjust the shape and position of obstacles, trying to test the ability of the algorithm to find the path, Fig02 is the final implementation version of the code.



Challenges and Learnings

The first challenge is to accurately represent the obstacles. In the code, it is crucial to accurately calculate the grid cells occupied by obstacles to ensure that the shape and position of obstacles are correctly reflected on the grid. This is achieved by performing mathematical calculations on the geometric properties of circular and square obstacles, including determining the radius of the circle and checking the boundary of the square. This method ensures accurate and correct representation of obstacles on the grid, providing the right environment for path planning.

The second one is about performance optimization. Since every operation on the grid involves looping and condition checking, optimizing performance is a major challenge. By pre-defining the size of the map and the size of the cell, and using the array operation effectively, the execution efficiency of the code is improved. For example, using NumPy for array operations instead of pure Python loops can significantly increase data processing speed and reduce algorithm runtime.

This project deepened my understanding of cell decomposition and A* algorithms, especially how to apply these theories to real-world problems. Practical coding not only enhanced my problem-solving skills, but also improved my understanding of handling and visualizing complex data structures. In addition, reviewing using Python libraries such as NumPy and NetworkX taught me how to deal with graphics and networking problems more efficiently.



Reference

[1] Xiang, D., Lin, H., Ouyang, J. et al. Combined improved A* and greedy algorithm for path planning of multi-objective mobile robot. Sci Rep 12, 13273 (2022). https://doi.org/10.1038/s41598-022-17684-0
