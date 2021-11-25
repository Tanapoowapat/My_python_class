import pygame
import random
from pygame import mixer
import os

pygame.init()
pygame.font.init()
pygame.display.set_caption("Tetris")

# setup game window
window_width = 800
window_height = 700
play_width = 300        # ความกว้างของพื้นที่เล่น
play_height = 550       # ความสูงของพื้นที่เล่น
box_size = 25           # ขนาดของรูปร่าง
x_margin = (window_width - play_width) // 2 # ระยะขอบจากด้านข้าง
top_margin = window_height - play_height    # ระยะขอบจากด้านบน
game_window = pygame.display.set_mode((window_width, window_height))


#load image
bg = pygame.image.load("assert/bg.jpg")
bg_main_game  = pygame.image.load("assert/bg_main_game.jpg")

#setup sound effect
mixer.music.load("assert/music/Tetris.wav")
clear_row_sound = mixer.Sound("assert/music/clearline.wav")
game_over_sound = mixer.Sound("assert/music/gameover.wav")

#setup color
salmon = (250, 128, 114)
pink = (255, 182, 193)
tomato = (255, 99, 71)
yellow = (255, 255, 224)
purple = (138, 43, 226)
lime = (0, 255, 0)
blue = (23, 104, 238)
white = (255,255,255)
red = (190, 0 ,0)

#setup shape
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


# นำตัวแปรรูปร่างด้านบนมา นำมาใส่ใน list
shapes = [S, Z, I, O, J, L, T]
# เก็บค่าสีไว้ใน list
shape_colors = [(salmon), (tomato), (yellow), (lime), (purple), (blue), (pink)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] # นำ list รูปร่างมาใส่สีตาม ตำแหน่ง
        self.rotation = 0

def convert_shape(shape):

    #
    #
    # หาเลข 0


    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line) # ['.','.','0','.','.']
        for j, column in enumerate(row):
            if column == '0': # หาเลข 0
                positions.append((shape.x + j, shape.y + i))


    # ขยับรูปร่าง
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions



def get_shape():
    return Piece(5, 0, random.choice(shapes))


def next_shape(shape, game_window):

    # เหมือน covert shape แต่จะวาวดรูปร่างแทน

    font = pygame.font.SysFont('itim', 30)
    next_shape_label = font.render('Next Shape', 1,(white))
    word_x = x_margin + play_width + 50
    word_y = top_margin + play_height/2 - 180

    format = shape.shape[shape.rotation % len(shape.shape)]
    for y, line in enumerate(format):
        row = list(line)
        for x, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(game_window, shape.color, (word_x + x * box_size, word_y-10 + y * box_size, box_size, box_size), 0)

    game_window.blit(next_shape_label, (word_x + 10, word_y - 30))

# เข็คว่าตำแหน่งรูปร่างที่จะตกไปนั้นว่างหรือไม่
# ส่งค่า grid และ shape
# สร้าง List ขึ้นมาและเเช็คว่า ตำแหน่งนั้นมีสีหรือไม่
#

def empty_space(shape, grid):
    accept_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accept_pos = [j for sub in accept_pos for j in sub]
    format = convert_shape(shape)
    for pos in format:
        if pos not in accept_pos:
            if pos[1] > -1:
                return False
    return True

class play_zone():

    # สร้างตาราง x = 10 , y 20 และเก็บค่าสีเเข้าใน list
    # lock_position เป็น Dictionary ใช้เก็บค่าสีโดยอ้างอิง จากตำแหน่งใน Grid
    # sample data in Dictionary = ((x,y):(tomato))
    def create_grid(lock_position={}):
        grid = [[(0,0,0) for __ in range(10)]for __ in range(20)]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if (y,x) in lock_position:
                    c = lock_position[(y,x)]
                    grid[x][y] = c
        return grid


    #วาดเส้นแบ่งระหว่าง Grid
    def draw_grid(game_window,grid):
        lx = x_margin
        ly = top_margin
        for x in range(len(grid)):
            pygame.draw.line(game_window, (128, 128, 128), (lx, ly + x * box_size),
                         (lx + play_width-50, ly + x * box_size))  # x
            for y in range(len(grid[x])):
                pygame.draw.line(game_window, (128, 128, 128), (lx + y * box_size, ly),
                             (lx + y * box_size, ly + play_height-50))  # y


    #วาดพื้นที่เล่น
    def draw_window(game_window, grid, score=0, last_score=0, level=0):

        game_window.blit(bg_main_game, (0, 0))
        font = pygame.font.SysFont('impact', 60)


        #วาดพื้นหลังสีเทา
        pygame.draw.rect(game_window, (128,128,128), pygame.Rect(x_margin-50, top_margin-60, play_width + 50, play_height + 30))
        #วาดกรอบสีดำครอบพื้นหลัง
        pygame.draw.rect(game_window, (0,0,0),
                         pygame.Rect(x_margin - 50, top_margin - 60, play_width + 50, play_height + 30),5)

        label = font.render('Tertis', True, (255, 0, 0))
        label_x = x_margin + play_width - 250
        label_y = top_margin + play_height - 620
        game_window.blit(label,( label_x , label_y))

        # current score
        font = pygame.font.SysFont('impact', 24)
        score_label = font.render('Score: ' + str(score), 1, (255, 255, 255))
        score_label_x = x_margin + play_width + 50
        score_label_y = top_margin + play_height / 2 - 150
        game_window.blit(score_label, (score_label_x + 5, score_label_y + 70 ))

        # last score
        last_score_label = font.render('High Score: ' + str(last_score), 1, (255, 255, 255))
        last_score_label_x = x_margin + play_width + 50
        last_score_label_y = top_margin + play_height/ 2 - 150
        game_window.blit(last_score_label, (last_score_label_x + 5, last_score_label_y + 100))

        # Level
        level_label = font.render('Current level : ' + str(level), 5, (255, 255, 255))
        level_label_x = x_margin + play_width + 50
        level_label_y = top_margin + play_height/ 2 - 150
        game_window.blit(level_label, (level_label_x + 5, level_label_y + 130))

        # วาดพื้นที่เล่น
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                pygame.draw.rect(game_window, grid[x][y],
                                 (x_margin + y * box_size, top_margin + x * box_size, box_size, box_size), 0)


        play_zone.draw_grid(game_window, grid)
        #วาดกรอบพื้นที่เล่น
        pygame.draw.rect(game_window, (red), (x_margin, top_margin, play_width-50, play_height - 50), 5)


    # เช็คตำแหน่ง (x,y) ใน Dictionary ว่า y น้อยกว่า 1 หรือไม่

    def check_conner(lock_pos):
        for pos in lock_pos:
            x, y = pos
            if y < 1:
                mixer.Sound.play(game_over_sound)
                return True
        return False


    # เช็คแถวว่าเต็มไหมหลักการเช็คคือจะเช็คสีใน grid หากมีสีอื่นที่ไม่ใช่สีดำจะลบค่า Lock_position

    def check_tetris(grid, lock_pos):
        index = 0
        increases = 0
        for i in range(len(grid) - 1, -1, -1):
            row = grid[i]
            if (0, 0, 0) not in row:
                increases += 1
                index = i
                for j in range(len(row)):
                    del lock_pos[(j, i)]

        if increases > 0:
            for key in sorted(list(lock_pos), key = lambda x: x[1])[::-1]:
                # sample data [(0,1),(0,0)]
                x, y = key
                # เช็คว่า y อยู่สูงกว่าแถวที่เรานำออกไป
                if y < index:
                    newKey = (x, y + increases)
                    mixer.Sound.play(clear_row_sound)
                    lock_pos[newKey] = lock_pos.pop(key)

        return increases

#score
def update_score(score):
    high_score = get_high_score()
    if os.path.exists('scores.txt'):
        with open('scores.txt','w') as f:
            if int(high_score) > score:
                f.write(str(high_score))
            else:
                f.write(str(score))

def get_high_score():
    if os.path.exists('scores.txt'):
        with open('scores.txt', 'r') as f:
            line = f.readlines()
            high_score = line[0].strip()
        return high_score

def main_game():

    run = True
    lock_position = {}

    change_piece = False #เช็คว่าต้องเปลี่ยนรูปร่างไหม
    current_piece = get_shape() #รูปร่างปัจจุบัน
    next_piece = get_shape() #รูปร่างต่อไปที่จะตก

    clock = pygame.time.Clock()
    fall_time = 0   #เก็บค่า loop ว่ารันไปแล้วกี่ครั้ง
    fall_speed = 0.30 #ความเร็วของรูปร่างที่จะตกลงมา

    #set up score
    level = 0
    high_score = get_high_score()
    score = 0

    #mixer.music.play(-1)

    #game running
    while run:


        grid = play_zone.create_grid(lock_position)
        fall_time += clock.get_rawtime() #จะเช็คว่า while lopp ทำงานนานเท่าไหร่
        clock.tick()

        #game control
        pressed = lambda key: event.type == pygame.KEYDOWN and event.key == key #สร้าง function มาเก็บค่าเวลากด คีบอร์ดไว้

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                update_score(score)
            if pressed(pygame.K_ESCAPE):
                run = False
                update_score(score)
                game_over()
            elif pressed(pygame.K_LEFT):
                current_piece.x -= 1
                if not(empty_space(current_piece, grid)):
                    current_piece.x += 1
            elif pressed(pygame.K_RIGHT):
                current_piece.x += 1
                if not (empty_space(current_piece, grid)):
                    current_piece.x -= 1
            elif pressed(pygame.K_DOWN):
                current_piece.y += 1
                if not(empty_space(current_piece, grid)):
                    current_piece.y -= 1
            elif pressed(pygame.K_UP):
                current_piece.rotation += 1
                if not (empty_space(current_piece, grid)):
                    current_piece.rotation -= 1


        #incress level
        if score >= 1000 and score < 2000:
            level = 1
            fall_speed = 0.25
        elif score >= 2000 and score < 3000:
            level = 2
            fall_speed  = 0.20
        elif score >= 3000 and score < 4000:
            level = 3
            fall_speed = 0.15
        elif score >= 4000 and score < 5000:
            level = 4
            fall_speed = 0.10
        elif score >= 5000:
            level = 5
            fall_speed = 0.09

        # get shape to fall
        if fall_time / 1000 >= fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not (empty_space(current_piece, grid)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True


        # get shape
        shape_pos = convert_shape(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                try:
                    grid[y][x] = current_piece.color
                except IndexError:
                    continue

        #get next shpae
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                lock_position[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += play_zone.check_tetris(grid, lock_position) * 100

        play_zone.draw_window(game_window, grid, score, high_score, level)
        next_shape(next_piece, game_window)
        pygame.display.update()


        if play_zone.check_conner(lock_position):
            update_score(score)
            run = False
            game_over()
            pygame.display.update()

def main_menu():

    game_window.blit(bg,(0,0))
    wood_sign = pygame.image.load('assert/wood.png')
    wood_sign = pygame.transform.scale(wood_sign,(700,350))
    game_window.blit(wood_sign,(55,top_margin + 40))
    mixer.music.stop()
    high_score = get_high_score()
    run = True
    while run:

        #Intro Label
        font = pygame.font.SysFont("itim", 48)
        Game_Over_label = font.render('Tanapoowapat Yomsarn 64015060', True, (0,0,0))
        Game_Over_label_x = x_margin + play_width - 410
        Game_Over_label_y = top_margin + play_height - 420
        game_window.blit(Game_Over_label, (Game_Over_label_x, Game_Over_label_y ))

        #Welcome label
        label = font.render('Welcome to Tetris', True, (0, 0, 0))
        label_x = x_margin + play_width - 280
        label_y = top_margin + play_height - 350
        game_window.blit(label, (label_x, label_y))

        # show high score
        high_score_label = font.render('High score : ' + str(high_score), True, (0, 0, 0))
        high_score_label_x = x_margin + play_width - 270
        high_score_label_y = top_margin + play_height - 250
        game_window.blit(high_score_label, (high_score_label_x, high_score_label_y))

        play_again_label = font.render('Press any key to play!', True, (0,0,0))
        play_again_x = x_margin + play_width - 300
        play_again_y = top_margin + play_height - 300
        game_window.blit(play_again_label, (play_again_x, play_again_y))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                main_game()

def game_over():
    game_window.blit(bg,[0,0])
    wood_sign = pygame.image.load('assert/wood.png')
    wood_sign = pygame.transform.scale(wood_sign, (700, 350))
    game_window.blit(wood_sign, (55, top_margin + 40))
    mixer.music.stop()

    high_score = get_high_score()

    run = True
    while run:



        font = pygame.font.SysFont("itim", 48)

        #game over label
        Game_Over_label = font.render('Game Over!', True , (0,0,0))
        Game_Over_label_x = x_margin + play_width - 240
        Game_Over_label_y = top_margin + play_height - 400
        game_window.blit(Game_Over_label, (Game_Over_label_x, Game_Over_label_y))

        #ask play again
        play_again_label = font.render('Press any key to play again!', True, (0,0,0))
        play_again_x = x_margin + play_width - 350
        play_again_y = top_margin + play_height - 350
        game_window.blit(play_again_label, (play_again_x , play_again_y ))


        #show high score
        high_score_label = font.render('High score : '+str(high_score), True, (0, 0, 0))
        high_score_label_x = x_margin + play_width - 270
        high_score_label_y = top_margin + play_height - 300
        game_window.blit(high_score_label, (high_score_label_x, high_score_label_y))


        pygame.display.update()
        pygame.time.delay(60)

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
            else:
                main_game()

main_menu()