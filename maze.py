import pygame
import time
import random

#set up pygame

WIDTH = 500
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
DISPLAY=pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()

class STACK:
	def __init__(self):
		self.stack = []
	def push(self, item):
		self.stack.append(item)
	def pop(self):
		del self.stack[-1]

#variables
grid = []
visited = []
maze_stack = STACK()

def build_grid(xpos, ypos, width, ncells_row):
	cell_width = int(width/ncells_row)
	for y in range(ypos, ypos + width, cell_width):
		grid.append([])
		for x in range(xpos, xpos + width, cell_width):
			pygame.draw.rect(DISPLAY, WHITE, (x, y, cell_width, cell_width), 2)
			grid[len(grid) - 1].append((x,y))
	pygame.display.flip()

def generate_maze():
	#maze parameters 
	current_cell = (20, 20)
	ncells_row = 20
	total_cells = ncells_row * ncells_row
	width = 460 
	
	#generate the starting grid
	build_grid(current_cell[0], current_cell[1], width, ncells_row)
	
	#start of recursive maze algoritm
	visited.append(current_cell)#                                         1. Make the initial cell the current cell and mark it as visited
	while (len(visited) < total_cells): #                                 2. While there are unvisited cells
		#get location of current cell in grid[] array
		for y, rows in enumerate(grid):#                                  	 2.1. If the current cell has any neighbours which have not been visited
			try:
				currentX = rows.index(current_cell)
				currentY = y
				break
			except:
				continue
		#find unvisited neighbours
		neighbours = []
		#top left corner
		if (currentX == 0 and currentY == 0):
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
		#bottem left corner
		elif (currentX == 0 and currentY == len(grid) - 1):
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
		#top right corner
		elif (currentX == len(grid[0]) - 1 and currentY == 0):
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
		#bottem right corner
		elif (currentX == len(grid[0]) - 1 and currentY == len(grid) - 1):
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
		#top row
		elif (currentY == 0):
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
		#bottem row
		elif (currentY == len(grid) - 1):
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
		#left column
		elif (currentX == 0):
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
		#right column
		elif (currentX == len(grid[0]) - 1):
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
		#anywhere else
		else:
			if (not(grid[currentY - 1][currentX] in visited)):
				neighbours.append(grid[currentY - 1][currentX])
			if (not(grid[currentY + 1][currentX] in visited)):
				neighbours.append(grid[currentY + 1][currentX])
			if (not(grid[currentY][currentX - 1] in visited)):
				neighbours.append(grid[currentY][currentX - 1])
			if (not(grid[currentY][currentX + 1] in visited)):
				neighbours.append(grid[currentY][currentX + 1])
			#2.1.1. Choose randomly one of the unvisited neighbours
			#2.1.2. Push the current cell to the stack
			#2.1.3. Remove the wall between the current cell and the chosen cell
			#2.1.4. Make the chosen cell the current cell and mark it as visited
		#2.2. Else if stack is not empty
			#2.2.1. Pop a cell from the stack
			#2.2.3. Make it the current cell
	
	
generate_maze()


running = True
while running:
    # keep running at the right speed
	clock.tick(FPS)
    # process input (events)
	for event in pygame.event.get():
        # check for closing the window
		if event.type == pygame.QUIT:
			running = False