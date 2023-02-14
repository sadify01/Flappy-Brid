import pygame, random
import os, sys
import pyautogui


def draw_window():
    for num in range(0, 5):
        window.blit(background, (background_x_pos + background_width * num, -250))

    window.blit(pipe_top, pipe_top_rect)
    window.blit(pipe_bottom, pipe_bottom_rect)
    window.blit(bird, bird_rect)

    for num in range(0, 4):
        window.blit(land, (land_x_pos + land_width * num, 1800))

    if len(str(score)) == 1:
        for num in str(score)[0]:
            window.blit(numbers[int(num)], (game_width/2, 100))

    if len(str(score)) == 2:
        for num in str(score)[0]:
            window.blit(numbers[int(num)], (game_width/2, 100))
        for num in str(score)[1]:
            window.blit(numbers[int(num)], (game_width/2 + 100, 100))


def check_collision():
    global game_over

    if bird_rect.colliderect(pipe_top_rect):
        game_over = True
    
    if bird_rect.colliderect(pipe_bottom_rect):
        game_over = True


pygame.init()

game_width = 3840
game_height = 2160
background_width = 1380
land_width = 1680
pipe_width = 260
splash_height = 300
scoreboard_height = 570
scoreboard_movement = 100
gravity = 1
bird_movement = 0
bird_rotation = 0
bird_color = "yellow"
frame = 2
frame_counter = 0
counter = 0
space_size = 500
game_active = False
game_over = False

window = pygame.display.set_mode((game_width, game_height), vsync=-1)
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Sweg Game")

background = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'sky_day.png')).convert()
background = pygame.transform.scale(background, (background_width, 2560))
background_x_pos = 0

birds = []
for num in range(1, 5):
    bird = pygame.image.load(os.path.join('Flappy Bird', 'assets', f'bird_{bird_color}_{num}.png')).convert_alpha()
    bird = pygame.transform.scale(bird, (170, 120))
    bird = pygame.transform.rotate(bird, bird_rotation)
    birds.append(bird)

bird_rect = bird.get_rect(center=(game_width/2, game_height/2))

pipe_top = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'pipe_top.png')).convert_alpha()
pipe_top = pygame.transform.scale(pipe_top, (pipe_width, 1600))
pipe_top_x_pos = game_width
pipe_top_y_pos = random.randint(-1200, -500)
pipe_top_rect = pipe_top.get_rect(topleft=(pipe_top_x_pos, pipe_top_y_pos))

pipe_bottom = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'pipe_bottom.png')).convert_alpha()
pipe_bottom = pygame.transform.scale(pipe_bottom, (pipe_width, 1600))
pipe_bottom_x_pos = pipe_top_x_pos
pipe_bottom_y_pos = pipe_top_rect.bottom + space_size
pipe_bottom_rect = pipe_bottom.get_rect(topleft=(pipe_bottom_x_pos, pipe_bottom_y_pos))

land = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'land.png')).convert()
land = pygame.transform.scale(land, (land_width, 560))
land_x_pos = 0

get_ready = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'get_ready.png')).convert_alpha()
get_ready = pygame.transform.scale(get_ready, (920, 250))
get_ready_rect = get_ready.get_rect(center=(game_width/2, game_height/3))

game_over_text = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'game_over.png')).convert_alpha()
game_over_text = pygame.transform.scale(game_over_text, (960, 210))
game_over_text_rect = game_over_text.get_rect(center=(game_width/2, game_height/3))

splash = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'splash.png')).convert_alpha()
splash = pygame.transform.scale(splash, (570, splash_height))
splash_rect = splash.get_rect(center=(game_width/2, game_height/2 + splash_height))

scoreboard = pygame.image.load(os.path.join('Flappy Bird', 'assets', 'scoreboard.png')).convert_alpha()
scoreboard = pygame.transform.scale(scoreboard, (1130, scoreboard_height))
scoreboard_rect = scoreboard.get_rect(center=(game_width/2, game_height + scoreboard_height))

score = 0
numbers = []
for num in range(0, 10):
    number = pygame.image.load(os.path.join('Flappy Bird', 'assets', f'font_big_{num}.png')).convert_alpha()
    if num == 1:
        number = pygame.transform.scale(number, (80, 180))
    else:
        number = pygame.transform.scale(number, (120, 180))
    numbers.append(number)

hit = pygame.mixer.Sound(os.path.join('Flappy Bird', 'assets', 'sounds', 'hit.ogg'))
hit.set_volume(0.3)
hit_played = False

swooshing = pygame.mixer.Sound(os.path.join('Flappy Bird', 'assets', 'sounds', 'swooshing.ogg'))
swooshing.set_volume(0.5)
swooshing_played = False

wing = pygame.mixer.Sound(os.path.join('Flappy Bird', 'assets', 'sounds', 'swooshing.ogg'))
wing.set_volume(0.5)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_SPACE:
                score_len = len(str(score))

                if game_over == False:
                    bird_movement = 0
                    bird_movement -= 18
                    bird_rotation = 30

                    score += 1

                    wing.play()

                if game_active == False:
                    if game_over == True:
                        game_over = False
                        hit_played = False
                        swooshing_played = False
                        counter = 0
                        scoreboard_movement = 100
                        pipe_top_x_pos = game_width
                        pipe_top_y_pos = random.randint(-1200, -500)
                        pipe_top_rect = pipe_top.get_rect(topleft=(pipe_top_x_pos, pipe_top_y_pos))
                        pipe_bottom_x_pos = pipe_top_x_pos
                        pipe_bottom_y_pos = pipe_top_rect.bottom + space_size
                        pipe_bottom_rect = pipe_bottom.get_rect(topleft=(pipe_bottom_x_pos, pipe_bottom_y_pos))

                        swooshing.play()

                        bird_rotation = 0
                        bird_rect.center = (game_width/2, game_height/2)

                    elif game_over == False:
                        game_active = True

    pipe_top_rect = pipe_top.get_rect(topleft=(pipe_top_x_pos, pipe_top_y_pos))
    pipe_bottom_x_pos = pipe_top_x_pos
    pipe_bottom_y_pos = pipe_top_rect.bottom + space_size
    pipe_bottom_rect = pipe_bottom.get_rect(topleft=(pipe_bottom_x_pos, pipe_bottom_y_pos))
    bird = pygame.transform.rotate(birds[frame], bird_rotation)

    draw_window()
    check_collision()

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        bird_rotation -= 2

        if game_over:
            pipe_top_x_pos -= 0
        else:
            pipe_top_x_pos -= 10

        if pipe_top_x_pos <= -pipe_width:
            pipe_top_x_pos = game_width
            pipe_top_y_pos = random.randint(-1200, -500)
            pipe_top_rect = pipe_top.get_rect(topleft=(pipe_top_x_pos, pipe_top_y_pos))
            pipe_bottom_x_pos = pipe_top_x_pos
            pipe_bottom_y_pos = pipe_top_rect.bottom + space_size
            pipe_bottom_rect = pipe_bottom.get_rect(topleft=(pipe_bottom_x_pos, pipe_bottom_y_pos))

        if bird_rotation <= -90:
            bird_rotation = -90

    else:
        if game_over == False:
            window.blit(get_ready, get_ready_rect)
            window.blit(splash, splash_rect)

    if game_over:
        score = 0

        if hit_played == False:
            hit_played = True
            hit.play()

        counter += 1
        if counter >= 30:
            if swooshing_played == False:
                swooshing_played = True
                swooshing.play()

            if scoreboard_rect.centery > game_height/2 + 120:
                scoreboard_movement -= 3.9
                scoreboard_rect.centery -= scoreboard_movement

        window.blit(scoreboard, scoreboard_rect)
        window.blit(game_over_text, game_over_text_rect)

    else:
        scoreboard_rect.centery = game_height + scoreboard_height/2

        frame_counter += 1
        if frame_counter >= 5:
            frame_counter = 0
            frame += 1
            if frame == 4:
                frame = 0
            bird = birds[frame]

        background_x_pos -= 1
        if background_x_pos <= -background_width:
            background_x_pos = 0

        land_x_pos -= 10
        if land_x_pos <= -land_width:
            land_x_pos = 0

    if bird_rect.bottom <= 0:
        game_over = True

    if bird_rect.bottom >= 1800:
        game_active = False
        game_over = True

    pygame.display.update()
