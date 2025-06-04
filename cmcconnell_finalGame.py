import sys
sys.path.append(r"C:\Users\cmac7\OneDrive - Ball State University\Desktop\CS 120")
import simpleGE

import pygame, random

# Star class
class Star(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("circle_star_icon_yellow.svg")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        # Move to top of screen
        self.y = 10
        # Random x position
        self.x = random.randint(0, self.screenWidth)
        # Random downward speed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
class Bonus(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("circle_star_icon_blue.svg")
        self.setSize(30, 30)
        self.minSpeed = 8
        self.maxSpeed = 10
        self.reset()
        
    def reset(self):
        # Move to top of screen
        self.y = 10
        # Random x position
        self.x = random.randint(0, self.screenWidth)
        # Random downward speed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

# Player (Spaceship) class
class Spaceship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship1.png")
        self.setSize(70, 70)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

# Score label
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
# Timer label
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

# Game Scene
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background-1.jpg")
        
        self.sndCatch = simpleGE.Sound("pleasing-bell.wav")
        self.numStars = 10
        self.numBonus= 3
        self.score = 0
        self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
                
        self.spaceship = Spaceship(self)
        
        self.stars = []
        for i in range(self.numStars):
            self.stars.append(Star(self))
            
        self.bonus = []
        for i in range(self.numBonus):
            self.bonus.append(Bonus(self))
      
        self.sprites = [
                        self.spaceship,
                        self.stars,
                        self.lblScore,
                        self.lblTime,
                        self.bonus]
        
    def process(self):
        for star in self.stars:
            if star.collidesWith(self.spaceship):
                star.reset()
                self.sndCatch.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        for star in self.bonus:
            if star.collidesWith(self.spaceship):
                star.reset()
                self.sndCatch.play()
                self.score += 5
                self.lblScore.text = f"Score: {self.score}"
        
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()

# Instructions Scene
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background-1.jpg")
        self.response = "Quit"
         
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "Welcome to Star Collector!",
            "Use the left and right arrow keys",
            "to move your spaceship and catch falling stars.",
            "Each star you catch earns you a point.",
            "",
            "Good luck!"]
        
        self.directions.center = (320, 200)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Previous score: 0"
        self.lblScore.center = (320, 400)
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    
    def setPrevScore(self, prevScore):
        self.prevScore = prevScore
        self.lblScore.text = f"Last score: {self.prevScore}"
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()

# Main function
def main():
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions()
        instructions.setPrevScore(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False

if __name__ == "__main__":
    main()
