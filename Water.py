import pygame
import numpy as np
import random

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((1280, 720))
screen = pygame.display.get_surface()
width,height = screen.get_width(), screen.get_height()
pygame.display.set_caption('water cellular automata')
rows = int(height / 8)
columns = int(width / 8)
field = np.zeros((rows, columns), dtype=np.int32)
for a in range(0, int((rows * columns) / 500)):
    r1 = random.randint(0, int((rows / 4) * 3))
    r2 = random.randint(0, int(columns - 1))
    field[r1, r2] = 21
def draw_text(text, pos):
    font = pygame.font.SysFont("arial", int(height / rows))
    y_pos = pos[1]
    x_pos = pos[0]
    for line in text.splitlines():
        for char in range(1, len(line)+1):
            text = font.render(line[:char], 1, (255, 0, 0))
            screen.blit(text, (x_pos, y_pos))
def physics():
    for y in np.arange(field.shape[0]):
        for x in np.arange(field.shape[1]):
            value = field[y, x]
            u = y - 1
            d = y + 1
            l = x - 1
            r = x + 1
            if not value >= 20:
                if not y - 1 < 0:
                    uppervalue = field[u, x]
                else:
                    uppervalue = 20
                if not y + 1 > (rows - 1):
                    undervalue = field[d, x]
                else:
                    undervalue = 20
                if not x - 1 < 0:
                    leftvalue = field[y, l]
                else:
                    leftvalue = 20
                if not x + 1 > (columns - 1):
                    rightvalue = field[y, r]
                else:
                    rightvalue = 20
                
                if value >= 1 and value <= 10:
                    if undervalue < 10:
                        field[y, x] -= 1
                        field[d, x] += 1
                    elif leftvalue < 10 and rightvalue < 10 and value >= 2:
                        field[y, x] -= 2
                        field[y, l] += 1
                        field[y, r] += 1
                    elif rightvalue < 10 and value > 1:
                        field[y, x] -= 1
                        field[y, r] += 1
                    elif leftvalue < 10 and value > 1:
                        field[y, x] -= 1
                        field[y, l] += 1
quitting = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quitting = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitting = True
            if event.key == pygame.K_1:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                column_width = width / columns
                row_height = height / rows
                for anzahl_columns in np.arange(field.shape[1]):
                    column = column_width * anzahl_columns
                    nächster_column = column_width * (anzahl_columns + 1)
                    for anzahl_rows in np.arange(field.shape[0]):
                        row = row_height * anzahl_rows
                        nächste_row = row_height * (anzahl_rows + 1)
                        if Mouse_x > column and Mouse_x <= nächster_column and Mouse_y > row and Mouse_y <= nächste_row:
                            field[anzahl_rows, anzahl_columns] = 21
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                column_width = width / columns
                row_height = height / rows
                for anzahl_columns in np.arange(field.shape[1]):
                    column = column_width * anzahl_columns
                    nächster_column = column_width * (anzahl_columns + 1)
                    for anzahl_rows in np.arange(field.shape[0]):
                        row = row_height * anzahl_rows
                        nächste_row = row_height * (anzahl_rows + 1)
                        if Mouse_x > column and Mouse_x <= nächster_column and Mouse_y > row and Mouse_y <= nächste_row:
                            if not field[anzahl_rows, anzahl_columns] >= 10:
                                field[anzahl_rows, anzahl_columns] += 1
            if event.button == 2:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                column_width = width / columns
                row_height = height / rows
                for anzahl_columns in np.arange(field.shape[1]):
                    column = column_width * anzahl_columns
                    nächster_column = column_width * (anzahl_columns + 1)
                    for anzahl_rows in np.arange(field.shape[0]):
                        row = row_height * anzahl_rows
                        nächste_row = row_height * (anzahl_rows + 1)
                        if Mouse_x > column and Mouse_x <= nächster_column and Mouse_y > row and Mouse_y <= nächste_row:
                            field[anzahl_rows, anzahl_columns] = 20
            if event.button == 3:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                column_width = width / columns
                row_height = height / rows
                for anzahl_columns in np.arange(field.shape[1]):
                    column = column_width * anzahl_columns
                    nächster_column = column_width * (anzahl_columns + 1)
                    for anzahl_rows in np.arange(field.shape[0]):
                        row = row_height * anzahl_rows
                        nächste_row = row_height * (anzahl_rows + 1)
                        if Mouse_x > column and Mouse_x <= nächster_column and Mouse_y > row and Mouse_y <= nächste_row:
                            field[anzahl_rows, anzahl_columns] = 0
    if quitting == True:
        break
    display.fill((55, 55, 55))
    for y in np.arange(field.shape[0]):
        for x in np.arange(field.shape[1]):
            value = field[y, x]
            d = y + 1
            if not y + 1 > (rows - 1):
                    undervalue = field[d, x]
            else:
                undervalue = 20
            if value == 21:
                if undervalue < 10:
                    d = y + 1
                    field[d, x] += 1
    physics()
    for y in np.arange(field.shape[0]):
        ypos = y * height / field.shape[0]
        for x in np.arange(field.shape[1]):
            xpos = x * width / field.shape[1]
            val = field[y, x]
            if field[y, x] > 0 and not field[y, x] > 10:
                pygame.draw.rect(display, (0, val / 12, 255 / val ), (xpos, ypos, np.math.ceil(width / field.shape[1]), np.math.ceil(height / field.shape[0])))
                #draw_text(str(val), (xpos, ypos))
            elif (field[y, x] == 20):
                pygame.draw.rect(display, (255, 255, 255), (xpos, ypos, np.math.ceil(width / field.shape[1]), np.math.ceil(height / field.shape[0])))
                #draw_text(str(val), (xpos, ypos))
            elif (field[y,x] == 21):
                pygame.draw.rect(display, (255, 0, 0), (xpos, ypos, np.math.ceil(width / field.shape[1]), np.math.ceil(height / field.shape[0])))
                #draw_text(str(val), (xpos, ypos))
    pygame.display.update()