import sys
sys.path.append(r"C:\Users\cmac7\OneDrive - Ball State University\Desktop\CS 120")
import simpleGE

import pygame, random




class Knight(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("black_knight.png")
        self.setSize(50, 50)
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("castle2.png")
        self.knight = Knight(self)
      
        self.sprites = [self.knight]
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()