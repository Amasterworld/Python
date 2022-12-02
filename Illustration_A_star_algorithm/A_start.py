import pygame
import math
from queue import PriorityQueue

WIDTH = 800
EXTRA_WIDTH = 600  # WIDTH + 400
WIN = pygame.display.set_mode((WIDTH + EXTRA_WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

pygame.font.init()  # to write in Pygame
font = pygame.font.SysFont('Comic Sans MS', 30)


class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self,
	           other):  # is one magic method that is used to define or implement the functionality of the less than operator “<”
		return False


# calculate heuristic
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()


def algorithm(draw, grid, start, end):
	count = 0
	pq_spots = PriorityQueue()
	pq_spots.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())
	# add the start spot(cell) to the priority_queue
	pq_spots_hash = {start}

	while not pq_spots.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = pq_spots.get()[2]
		pq_spots_hash.remove(current)

		# if reach the end cell
		if current == end:
			reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in pq_spots_hash:
					count += 1
					pq_spots.put((f_score[neighbor], count, neighbor))
					pq_spots_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False


def make_grid(rows, width):
	grid = []
	gap = width // rows  # floor division
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows + 1):
			pygame.draw.line(win, BLUE, (j * gap, 0), (j * gap, width))


def intro_txt(lines_space, hor_space):
	title = font.render('A Star algorithm', False, (0, 0, 0))
	start_txt = font.render('Left click to put the start spot ', False, (0, 0, 0))
	end_txt = font.render('Second left click to place the end spot ', False, (0, 0, 0))
	ob_txt = font.render('left click on grid to make obstalces ', False, (0, 0, 0))
	run_txt = font.render('Press space to run the program', False, (0, 0, 0))
	reset_txt = font.render('Press c to reset the program', False, (0, 0, 0))

	WIN.blit(title, (WIDTH + 3*hor_space, 1 * lines_space))
	WIN.blit(start_txt, (WIDTH + hor_space, 3 * lines_space))
	WIN.blit(end_txt, (WIDTH + hor_space, 4 * lines_space))
	WIN.blit(ob_txt, (WIDTH + hor_space, 5 * lines_space))
	WIN.blit(run_txt, (WIDTH + hor_space, 6 * lines_space))
	WIN.blit(reset_txt, (WIDTH + hor_space, 7 * lines_space))


def running_txt(x) -> font:
	run_txt = {1: font.render('Path is Found', False, GREEN), 0: font.render('Path is NOT Found', False, RED),
	           "searching": font.render('Searching ', False, BLUE)}

	return run_txt.get(x)


def draw(win, grid, rows, width, found_path=None):
	lines_space = 50
	hor_space = 50

	win.fill(WHITE)
	intro_txt(lines_space, hor_space)

	for row in grid:
		for spot in row:
			spot.draw(win)
	if running_txt(found_path) is not None:
		WIN.blit(running_txt(found_path), (WIDTH + hor_space, 7 * lines_space))
	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos
	row = y // gap
	col = x // gap

	return row, col


def main(win, width):
	rows = 20  # the number of rows in the grid
	grid = make_grid(rows, width)

	start = None
	end = None
	found_path = None
	run = True

	while run:
		draw(win, grid, rows, width, found_path)
		pos = pygame.mouse.get_pos()
		y, _ = pos  # get coord x and y in the display
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			# if the curso is in grid and click LEFT
			if y < width and pygame.mouse.get_pressed()[0]:
				# pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				# left click to create a start point(spot)
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif y < width and pygame.mouse.get_pressed()[2]:  # RIGHT
				# pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				# press space to run the program if start and end spots created.
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					found_path = "searching"
					algorithm(lambda: draw(win, grid, rows, width, found_path), grid, start, end)
					if algorithm(lambda: draw(win, grid, rows, width, found_path), grid, start, end):
						found_path = True
					# draw(win, grid, rows, width, found_path)
					else:
						found_path = False
				# press C to reset

				if event.key == pygame.K_c:
					found_path = None
					start = None
					end = None
					grid = make_grid(rows, width)

	pygame.quit()


main(WIN, WIDTH)
