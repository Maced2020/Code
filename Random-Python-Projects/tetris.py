import pygame
import random

# Initialize pygame
pygame.init()
# You can change the font and size
score_font_style = pygame.font.SysFont("Arial", 24)
title_font_style = pygame.font.SysFont("Arial", 62)
level_font_style = pygame.font.SysFont("Arial", 24)

# Define colors
white = (255, 255, 255)
#red = (213, 50, 80)
#blue = (50, 153, 213)
grid_color = (160, 160, 160)
hud_text = (0, 0, 0)
#the color of the pieces
# pieces = (102, 78, 255)

# Define colors for each piece type
piece_colors = {
    'I': (0, 255, 255),  # Cyan
    'J': (0, 0, 255),    # Blue
    'L': (255, 165, 0),  # Orange
    'O': (255, 255, 0),  # Yellow
    'S': (0, 255, 0),    # Green
    'T': (128, 0, 128),  # Purple
    'Z': (255, 0, 0),    # Red
}


# Set display size
dis_width = 850
dis_height = 850
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Tetris Game')

# Tetris grid
grid_width = 10
grid_height = 20
block_size = 30  # Size of a single block
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

# Calculate grid start position (centered)
grid_start_x = (dis_width - grid_width * block_size) // 2
grid_start_y = (dis_height - grid_height * block_size) // 2

# Function to draw the grid
def draw_grid(grid):
    for y in range(grid_height):
        for x in range(grid_width):
            rect = (grid_start_x + x * block_size, grid_start_y + y * block_size, block_size, block_size)
            if grid[y][x] != 0:  # If the cell is occupied
                pygame.draw.rect(dis, grid[y][x], rect)
            pygame.draw.rect(dis, grid_color, rect, 1)  # Draw grid cell border





# Function to draw a tetris piece
def draw_piece(x, y, piece, shape_name):
    color = piece_colors[shape_name]
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                rect = (grid_start_x + (x + j) * block_size, grid_start_y + (y + i) * block_size, block_size, block_size)
                pygame.draw.rect(dis, color, rect)


# Define Tetris pieces
tetris_shapes = {
    'I': [[1, 1, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'Z': [[1, 1, 0], [0, 1, 1]]
}



# Function to clear complete lines
def clear_lines(grid):
    lines_cleared = 0
    y = len(grid) - 1
    while y >= 0:
        if all(grid[y]):
            del grid[y]
            grid.insert(0, [0 for _ in range(grid_width)])
            lines_cleared += 1
        else:
            y -= 1
    return lines_cleared


# Function to lock piece and clear lines
def lock_and_clear(grid, piece, x, y):
    lock_piece(grid, piece, x, y)
    return clear_lines(grid)


# Function to generate a random piece
def get_random_piece():
    shape = random.choice(list(tetris_shapes.keys()))
    return tetris_shapes[shape], shape

# Function to check collision
def check_collision(grid, piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                if x + j < 0 or x + j >= grid_width or y + i < 0 or y + i >= grid_height or grid[y + i][x + j]:
                    return True
    return False

# Function to lock piece
def lock_piece(grid, piece, shape_name, x, y):
    color = piece_colors[shape_name]
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell and y + i >= 0:
                grid[y + i][x + j] = color


# Function to rotate piece
def rotate_piece(piece):
    return [list(row) for row in zip(*piece[::-1])]

# Initialize clock
clock = pygame.time.Clock()

# Game loop
def gameLoop():
    current_piece, shape_name = get_random_piece()
    piece_x = (grid_width - len(current_piece[0])) // 2
    piece_y = 0  # Start piece at the top of the grid
    score = 0  # Initialize score
    speed = 2
    level = 1
    last_speed_increase_score = 0  # Track the score at the last speed increase

    game_over = False

    while not game_over:
        dis.fill(white)  # Clear screen
        draw_piece(piece_x, piece_y, current_piece, shape_name)
        draw_grid(grid)  # Draw the grid


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(grid, current_piece, piece_x - 1, piece_y):
                        piece_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(grid, current_piece, piece_x + 1, piece_y):
                        piece_x += 1
                elif event.key == pygame.K_DOWN:
                    while not check_collision(grid, current_piece, piece_x, piece_y + 1):
                        piece_y += 1
                elif event.key == pygame.K_SPACE:
                    rotated_piece = rotate_piece(current_piece)
                    if not check_collision(grid, rotated_piece, piece_x, piece_y):
                        current_piece = rotated_piece

        if not check_collision(grid, current_piece, piece_x, piece_y + 1):
            piece_y += 1
        else:
            lock_piece(grid, current_piece, shape_name, piece_x, piece_y)  # Pass shape_name
            lines_cleared = clear_lines(grid)  # Check and clear lines
            score += lines_cleared * 100  # Update score based on lines cleared
            current_piece, shape_name = get_random_piece()
            piece_x = (grid_width - len(current_piece[0])) // 2
            piece_y = 0
            if score - last_speed_increase_score >= 200:
                speed += 0.5  # Increase game speed
                level += 1
                last_speed_increase_score = score
            if check_collision(grid, current_piece, piece_x, piece_y):
                game_over = True
        
        score_text = score_font_style.render(f'Score: {score}', True, hud_text)
        title_text = title_font_style.render(f'TETRIS', True, hud_text)
        level_text = level_font_style.render(f'Level: {level}', True, hud_text)
        if game_over:
            game_over_text = title_font_style.render('Game Over', True, hud_text)
            text_rect = game_over_text.get_rect(center=(dis_width / 2, dis_height / 2))
            dis.blit(game_over_text, text_rect)
        dis.blit(score_text, (10, 10))  # Position the score text in the top-left corner
        dis.blit(level_text, (10, 35))
        dis.blit(title_text, (350, 10))
        pygame.display.update()  # Update the display
        clock.tick(speed)  # Control the frame rate

    pygame.quit()
    quit()




gameLoop()