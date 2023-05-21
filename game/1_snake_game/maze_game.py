# Add background image and music

import pygame
from pygame.locals import *
import time
import random
from dataLoader import DataLoader
from exceptions import GameException

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)
SCREEN_WIDTH = SIZE * 11
SCREEN_HEIGHT = SIZE * 11
SPEED = 10
MOVES_TIMER = 0.7
DELAY = 3

class Maze:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/wall.jpg").convert()
        self.width = 11
        self.height = 11
        self.matrix = [
        #   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
            1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
            1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1,
            1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1,
            1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1,

        ]


    def draw(self):
        bx = 0
        by = 0
        for i in range(0, self.width * self.height):
            if self.matrix[bx + (by * self.width)] == 1:
                self.parent_screen.blit(self.image, (bx * SIZE, by * SIZE))

            bx = bx + 1
            if bx > self.width - 1:
                bx = 0
                by = by + 1
        pygame.display.flip()


class Player:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.x = SIZE * 5
        self.y = SIZE * 0
        self.posX = 5
        self.posY = 0

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        print("left")
        if(self.x == 0):
            return
        self.x -= 40
        self.posX -= 1
        self.draw()

    def move_right(self):
        print("right")
        if(self.x == SCREEN_WIDTH):
            return
        self.x += 40
        self.posX += 1
        self.draw()

    def move_up(self):
        print("up")
        if(self.y == 0):
            return
        self.y -= 40
        self.posY -= 1
        self.draw()

    def move_down(self):
        print("down")
        if(self.y == SCREEN_HEIGHT):
            return
        self.y += 40
        self.posY += 1
        self.draw()


class Game:
    def __init__(self, ):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Apple Game")
        self.move_generator = DataLoader().move_generator()
        pygame.mixer.init()

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player(self.surface)
        self.player.draw()
        self.maze = Maze(self.surface)

    def play_sound(self, sound_name):
        if sound_name == "win":
            sound = pygame.mixer.Sound("resources/win.mp3")
        elif sound_name == 'lose':
            sound = pygame.mixer.Sound("resources/lose.mp3")
        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.player = Player(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def collision_with_wall(self):
        if self.maze.matrix[self.player.posX + (self.maze.width * self.player.posY)] == 1:
            return True
        return False

    def reach_goal(self):
        if self.maze.matrix[self.player.posX + (self.maze.width * self.player.posY)] == 2:
            return True
        return False

    def play(self):
        self.render_background()
        self.maze.draw()
        self.player.draw()
        # self.display_score()
        pygame.display.flip()

        if self.reach_goal():
            self.play_sound("win")
            raise GameException("win")

        if self.collision_with_wall():
            self.play_sound("lose")
            raise GameException("collision")

    def show_game_over(self, state):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)

        if state == "win":
            line1 = font.render("Congratulations! You Won!", True, (255, 255, 255))
            self.surface.blit(line1, (50, 50))
            line2 = font.render("To play again press Enter.", True, (255, 255, 255))
            line3 = font.render("To exit press Escape!.", True, (255, 255, 255))
            self.surface.blit(line2, (50, 120))
            self.surface.blit(line3, (50, 190))
        elif state == "lose":
            line1 = font.render("Sorry You Lost :(", True, (255, 255, 255))
            self.surface.blit(line1, (50, 50))
            line2 = font.render("To play again press Enter.", True, (255, 255, 255))
            line3 = font.render("To exit press Escape!.", True, (255, 255, 255))
            self.surface.blit(line2, (50, 120))
            self.surface.blit(line3, (50, 190))
        elif state == "no moves":
            line1 = font.render("You have no moves left", True, (255, 255, 255))
            self.surface.blit(line1, (50, 50))
        pygame.mixer.music.pause()
        pygame.display.flip()


    def run(self):
        running = True
        pause = False
        start_time = time.time()
        while running:

            # 1 1 3 3 1 1 3 3 1 1 4 4 1 1 2 2 1 2 2 1 4

            '''
            class_names = {
                0: 'Up',
                1: 'Down',
                2: 'Right',
                3: 'Left',
                4: 'Blink'
            }
            '''



            next_move = None

            now = time.time()

            if now - start_time > MOVES_TIMER:
                try:
                    next_move = next(self.move_generator)
                except:
                    self.show_game_over("no moves")
                    pause = True
                print("next move", next_move)
                start_time = now

            if next_move == 4:
                if pause:
                    print("unpause")
                else:
                    time.sleep(DELAY)
                    print("pause")
                pause = not pause

            if not pause:
                 if next_move == 0:
                     self.player.move_up()

                 if next_move == 1:
                     self.player.move_down()

                 if next_move == 2:
                     self.player.move_right()

                 if next_move == 3:
                     self.player.move_left()



            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:

                        if event.key == K_LEFT:
                            self.player.move_left()

                        if event.key == K_RIGHT:
                            self.player.move_right()

                        if event.key == K_UP:
                            self.player.move_up()

                        if event.key == K_DOWN:
                            self.player.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()

            except GameException as e:

                print(e.message)

                if e.message == "collision":
                    self.show_game_over("lose")
                elif e.message == "win":
                    self.show_game_over("win")

                pause = True
                time.sleep(DELAY*2)
                self.reset()

            time.sleep(1/SPEED)


if __name__ == '__main__':
    game = Game()
    game.run()