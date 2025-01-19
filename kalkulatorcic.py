import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kalkulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

font = pygame.font.Font(None, 50)

button_width = 80
button_height = 80
button_margin = 10

buttons = [
    {'label': '7', 'pos': (10, 150)}, {'label': '8', 'pos': (100, 150)}, {'label': '9', 'pos': (190, 150)}, {'label': '/', 'pos': (280, 150)},
    {'label': '4', 'pos': (10, 240)}, {'label': '5', 'pos': (100, 240)}, {'label': '6', 'pos': (190, 240)}, {'label': '*', 'pos': (280, 240)},
    {'label': '1', 'pos': (10, 330)}, {'label': '2', 'pos': (100, 330)}, {'label': '3', 'pos': (190, 330)}, {'label': '-', 'pos': (280, 330)},
    {'label': '0', 'pos': (10, 420)}, {'label': '.', 'pos': (100, 420)}, {'label': '=', 'pos': (190, 420)}, {'label': '+', 'pos': (280, 420)},
    {'label': 'C', 'pos': (10, 510)}
]

current_expression = ""

def draw_text(surface, text, pos, color=BLACK):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, pos)

def draw_buttons():
    for button in buttons:
        rect = pygame.Rect(button['pos'][0], button['pos'][1], button_width, button_height)
        pygame.draw.rect(screen, LIGHT_GRAY, rect)
        pygame.draw.rect(screen, GRAY, rect, 2)
        draw_text(screen, button['label'], (button['pos'][0] + 25, button['pos'][1] + 20))

def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, GRAY, (10, 10, WIDTH - 20, 120))
    draw_text(screen, current_expression, (20, 50))

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for button in buttons:
                rect = pygame.Rect(button['pos'][0], button['pos'][1], button_width, button_height)
                if rect.collidepoint(mouse_pos):
                    label = button['label']
                    if label == '=':
                        current_expression = evaluate_expression(current_expression)
                    elif label == 'C':
                        current_expression = ""
                    else:
                        current_expression += label

    pygame.display.flip()

pygame.quit()
sys.exit()
