import pygame
import math



WIDTH = 800
EXTRA_WIDTH = 600  # WIDTH + 400
WIN = pygame.display.set_mode((WIDTH + EXTRA_WIDTH, WIDTH))
pygame.display.set_caption("Illustation for minimum path sum")

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

    def __init__(self, row, col, width, total_rows, val = 0):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.val = val    #store value for each cell

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

    def draw_spot(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))



        def __lt__(self,
                    other):  # is one magic method that is used to define or implement the functionality of the less than operator “<”
            return False

def make_grid(rows, width):
    gap = width // rows  # floor division
    grid = [[Spot(i, j, gap, rows) for j in range(rows)] for i in range(rows)]
    return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows + 1):
			pygame.draw.line(win, BLUE, (j * gap, 0), (j * gap, width))

def intro_txt(lines_space, hor_space, min_sum):
	title = font.render('Illustration the problem ', False, (0, 0, 0))
	start_txt = font.render('Move curso mouse to the cell ', False, (0, 0, 0))
	end_txt = font.render('Type the number(0 - 999) on the cells ', False, (0, 0, 0))
	#ob_txt = font.render('left click on grid to make obstalces ', False, (0, 0, 0))
	run_txt = font.render('Press space to run re-run the program', False, (0, 0, 0))
	#reset_txt = font.render('Press c to reset the program', False, (0, 0, 0))

	WIN.blit(title, (WIDTH + 3*hor_space, 1 * lines_space))
	WIN.blit(start_txt, (WIDTH + hor_space, 3 * lines_space))
	WIN.blit(end_txt, (WIDTH + hor_space, 4 * lines_space))
	#WIN.blit(ob_txt, (WIDTH + hor_space, 5 * lines_space))
	WIN.blit(run_txt, (WIDTH + hor_space, 6 * lines_space))
	#WIN.blit(reset_txt, (WIDTH + hor_space, 7 * lines_space))




def draw(win, grid, rows, width, min_sum = 0):
    lines_space = 50
    hor_space = 50

    win.fill(WHITE)
    intro_txt(lines_space, hor_space, min_sum)

    def draw_number(val, color = BLACK):

        if color == BLACK:
            text = font.render(val, True, color)
            text_rect = text.get_rect()
            text_rect.center = (spot.x + spot.width // 2, spot.y + spot.width // 2)
            # Draw the number in each cell
            win.blit(text, text_rect)

        # Draw the final result number
        elif color == ORANGE:

            text = font.render("Min path sum = ", True, color)
            win.blit(text, (WIDTH + hor_space, 10 * lines_space))

            loca_hor_space = 350
            res = font.render(val, True, color)
            win.blit(res, (WIDTH + loca_hor_space, 10 * lines_space))

    #draw the number in each cell
    for row in grid:
        for spot in row:
            spot.draw_spot(win)

            val = str(spot.val)
            draw_number(val)

    #draw the final result with ORANGE color        
    res = str(min_sum)
    draw_number(res, ORANGE)   

	#if running_txt(found_path) is not None:
	#	WIN.blit(running_txt(found_path), (WIDTH + hor_space, 7 * lines_space))
    draw_grid(win, rows, width)
    pygame.display.update()

def get_mouse_pos(pos, rows, width):
	gap = width // rows
	y, x = pos
	row = y // gap
	col = x // gap

	return row, col             

def algorithmMinPathSum(draw, grid, rows, path):

    #store a path having the smallest sum
    #using dynamic programming to solve this problem, TC O(m*n) SC(m*n). Note that can be optimized to SC(m)
    min_sum = [[0]*rows for _ in range(rows)] #if use numpy then min_sum = np.zeros((row, row), dtype = int) 

    #base condtion
    min_sum[0][0] = grid[0][0].val
    #print(grid[0][0].val)
    path[0][0] = (0,0)


    for i in range(1, rows):
        min_sum[0][i] = grid[0][i].val + min_sum[0][i-1]
        path[0][i] = (0, i-1)

    for j in range(1, rows):
        min_sum[j][0] = grid[j][0].val + min_sum[j-1][0]
        path[j][0] = (j-1, 0)

    """
    after two above for loops min_sum has a form  x1 x2 x3
                                                  x4 0  0
                                                  x5 0  0
                                                
    """
    #now to find the smallest length we so we always choose smaller value if it is possible
    for i in range(1, rows):
        for j in range(1, rows):
            # if we do not need to track a path: min_sum[i][j] = grid[i][j] + min(min_sum[i-1][j], min_sum[i][j-1]) is enough
            if min_sum[i-1][j] < min_sum[i][j-1]:
                min_sum[i][j] = grid[i][j].val + min_sum[i-1][j]
                path[i][j] = (i-1, j)
            else:
                min_sum[i][j] = grid[i][j].val + min_sum[i][j-1]
                path[i][j] = (i, j-1)

    def  reconstruct_path():

        i, j = rows - 1, rows - 1
        grid[i][j].make_path()
        #store the smallest path from the last point(row-1, row-1) to the initial point (0,0)
        p = [(i, j)]
        while i != 0 or j != 0:

            i, j = path[i][j]
            grid[i][j].make_path()
            draw()

    reconstruct_path()

    return min_sum[-1][-1] #return min_sum[row-1][row-1]

def reset_old_path(draw,path, rows, grid):

        i, j = rows - 1, rows - 1
        grid[i][j].color = WHITE
        #store the smallest path from the last point(row-1, row-1) to the initial point (0,0)
        p = [(i, j)]
        while i != 0 or j != 0:

            i, j = path[i][j]
            grid[i][j].color = WHITE
            draw()

def main(win, width):

    rows = 4  # the number of rows in the grid
    grid = make_grid(rows, width)
    min_sum = 0
    run = True
    path = [[(0, 0)]* rows for _ in range(rows)]

    while run:

        draw(win, grid, rows, width, min_sum)
        pos = pygame.mouse.get_pos()
        y, _ = pos  # get coord x and y in the display
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:

                # Get the row and column of the cell that has focus
                row, col = get_mouse_pos(pos, rows, width)
                val = str(grid[row][col].val)

                #if val still can be deleted then delete last char else  assign value at cel = 0
                if  event.key == pygame.K_BACKSPACE:
                    if val[0:-1]:

                        grid[row][col].val = int (val[0:-1])  
                    else:
                        grid[row][col].val = 0

                if event.unicode.isnumeric():
                    # Handle key presses                   
                    #if the value is 0 the replace it with the user input number
                    if val == "0":
                        grid[row][col].val  = int(event.unicode)
                    #if  the length of value is smaller than 3, then concatenate(append) it
                    elif len(val) < 3:
                        val += event.unicode
                        grid[row][col].val = int(val)                


                #if the old path is painted then reset it(to be white color) if the user presses space button again

                if grid[rows-1][rows-1].color == PURPLE and event.key == pygame.K_SPACE:
                        reset_old_path(lambda: draw(win, grid, rows, width), path, rows, grid)

                #Press Space button to get the result and draw the  path
                if event.key == pygame.K_SPACE:
                    min_sum = algorithmMinPathSum(lambda: draw(win, grid, rows, width), grid, rows, path)

    pygame.quit()
main(WIN, WIDTH)     