import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Game variables
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 'X'  # X goes first
game_over = False
winner = None

# Functions
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                # Draw X
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                ((col + 1) * SQUARE_SIZE - SPACE, (row + 1) * SQUARE_SIZE - SPACE),
                                CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                ((col + 1) * SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                (col * SQUARE_SIZE + SPACE, (row + 1) * SQUARE_SIZE - SPACE),
                                CROSS_WIDTH)
            elif board[row][col] == 'O':
                # Draw O
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win():
    global winner
    
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            pygame.draw.line(screen, (255, 0, 0),
                             (0, (row + 0.5) * SQUARE_SIZE),
                             (WIDTH, (row + 0.5) * SQUARE_SIZE),
                             LINE_WIDTH)
            return True
    
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            pygame.draw.line(screen, (255, 0, 0),
                             ((col + 0.5) * SQUARE_SIZE, 0),
                             ((col + 0.5) * SQUARE_SIZE, HEIGHT),
                             LINE_WIDTH)
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)
        return True
        
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        winner = board[2][0]
        pygame.draw.line(screen, (255, 0, 0), (0, HEIGHT), (WIDTH, 0), LINE_WIDTH)
        return True
        
    return False

def reset_game():
    global board, player, game_over, winner
    screen.fill(BG_COLOR)
    draw_lines()
    player = 'X'
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    game_over = False
    winner = None

# Draw initial game board
draw_lines()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win():
                    game_over = True
                elif is_board_full():
                    game_over = True
                    winner = "Tie"
                player = 'O' if player == 'X' else 'X'
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                
    draw_figures()
    
    if game_over:
        font = pygame.font.SysFont(None, 40)
        if winner == "Tie":
            text = font.render("Game Over - It's a Tie! Press 'r' to restart", True, (255, 255, 255))
        else:
            text = font.render(f"Game Over - {winner} wins! Press 'r' to restart", True, (255, 255, 255))
        
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        screen.blit(text, text_rect)
    
    pygame.display.update()
