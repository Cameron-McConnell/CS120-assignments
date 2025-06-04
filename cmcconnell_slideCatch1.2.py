import sys
sys.path.append(r"C:\Users\cmac7\OneDrive - Ball State University\Desktop\CS 120")
import simpleGE


import pygame, random

class Flame(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("flame.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
       
class Knight(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("black_knight.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("castle2.png")
        
        self.sndFlame = simpleGE.Sound("click.wav")
        self.numFlame = 10
        self.score = 0
        self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
                
        self.knight = Knight(self)
        
        self.flame = []
        for i in range(self.numFlame):
            self.flame.append(Flame(self))
      
        self.sprites = [
                        self.knight,
                        self.flame,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for flame in self.flame:
            if flame.collidesWith(self.knight):
                flame.reset()
                self.sndFlame.play()
                self.score -= 1
                self.lblScore.text = f"Score: {self.score}"
        
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("castle2.png")
        self.response = "Quit"
         
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "You are a Dark Knight!",
        "Move with left and right arrow keys",
        "to dodge the flames as much as possible",
        "in the time provided.",
        "Highest score wins!"
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