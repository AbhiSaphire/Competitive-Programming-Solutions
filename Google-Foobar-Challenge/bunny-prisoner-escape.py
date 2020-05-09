# ~~Abhishek K. Singh~~
# Solved in almost 7 hours
# Simple find shortest path problem with a tweak (of having power to convert one wall to path / change single 1 to 0)
# I am using Breadth First Search to calculate shortest path
# Approach is calculate shortest path from source to destination (using power) and again calculate shortest path from destination to source (using power)
# Calculate cost or length of shortest path comparing both top->bottom and bottom->top

def shortest_path_bfs(row, col, maze):
	board = [[None for i in range(len(maze[0]))] for i in range(len(maze))]
	board[row][col] = 1

	queue = [(row, col)]
	while queue:
		x, y = queue.pop(0)
		for i in [[1,0],[-1,0],[0,-1],[0,1]]:
			board_row, board_col = x + i[0], y + i[1]
			if 0 <= board_row < len(maze) and 0 <= board_col < len(maze[0]):
				if board[board_row][board_col] is None:
					board[board_row][board_col] = board[x][y] + 1
					if maze[board_row][board_col] == 1 :
						continue
					queue.append((board_row, board_col)) 
	return board

def solution(maze):
	source_to_dest = shortest_path_bfs(0, 0, maze)
	dest_to_source = shortest_path_bfs(len(maze)-1, len(maze[0])-1, maze)
	board = []

	returner = 2 ** 32-1
	for i in range(len(maze)):
		for j in range(len(maze[0])):
			if source_to_dest[i][j] and dest_to_source[i][j]:
				returner = min(source_to_dest[i][j] + dest_to_source[i][j] - 1, returner)
	return returner


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]]))
print(solution([[0, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 1, 0]]))
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0]]))
