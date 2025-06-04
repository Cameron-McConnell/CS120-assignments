# cmcconnell_finalGame.py
Project summary
  The Star Collector game is a simple 2D arcade-style game built with the simpleGE framework and pygame. The goal of the game is to:
  - Reinforce OOB (object-oriented programming) concepts, for example, classes, inheritance, and encapsulation
  - Practice game design principles such as sprite management, collision detection, and time-based gameplay
  - Use an iterative design apporach by reusing and modifying an existing game strucutre
  - Deliver an egaging, replayable game with straightforward controls and scoring
Player Instructions
  Objective:
    - Catch as many falling stars as possible before the time runs out
  Controls
    - Use the left and right arrow keys to move the spaceship
  Scoring
    - Each time you catch a star(yellow), your score increases by 1
    - Each time you catch a bonus star(blue), your score increases by 5
  Timer
    - You have 10 seconds to collect as many stars as you can
  Replay
    - After the game ends, you can restart to try for a higher score
Technologies and Techniques
  - Thonny programming language
  - simpleGE framework:
      *Handles game scenes, sprite management, collision detection, and labels
      *Allows rapid prototyping of 2D games
  - pygame Library:
      *Provides underlying graphic, input and sound functionality
  - Object-Oriented Programming
      *classes: Star, Bonus, Spaceship, LblScore, LblTime, Game, Instructions
      *methods: reset, process, collidesWith, setImage, setSize
  - Sprite-Based Game Design:
      *PLayer and stars represented as sprites with images and behaviors
  - Event Loop and Timer:
      *Timer to limit the game session
      *Event-driven input handling for player movement
Citations
  - simpleGE Framework
      *https://github.com/twopiharris/BSU-CS120/blob/main/gameState/simpleGE.py
  - pygame Library
      *Shinners, Pete et al. http://www.pygame.org/



Description
  - I leanred how to adapt an existing game frameworkto design a different but related game. I saw how reusing class structures and method names can make transitioning from on game to another much smoother. I also learned how to structure game loops, handle collisions, and integrate GUI elements like labels and timers consistently. One challenge was ensuring that the collision logic felt rewarding, for instance, increasing the score, instead of punishing the player. Finally, deciding on appropriate placeholder images and sounds was tricky due to the fact that I needed to import them to the woring directory. I would like to improve or add more features like power-ups and even multiple levels of difficulty. I would also like to add background music and refining the sound design which would make the game more immersive.I would do things differently in the aspect of making a game design document(GDD) with more clear goals, features, and assests. I would also test collision boundaries and adjust difficulty scaling as I build the game rather than at the end. The original design document was very broad. I stayed close to strucutre and flow, however, I switched the collision logic from a negative to a positive which changed the core gameplay loop, and finally, I kept the time-based session similar, but I want to expand with more dynamic challenges in the future. I stayed on track by referring back to the game's core objective and mirrored which kept things organized and easy to debug.








Import simpleGE
Import pygame, random

Class Flame(simpleGE.Sprite):
    Function __init__(scene):
        Call super().__init__(scene)
        Call setImage("flame.png")
        Call setSize(25, 25)
        Set minSpeed = 3
        Set maxSpeed = 8
        Call reset()
    
    Function reset():
        Set y = 10
        Set x = random.randint(0, screenWidth)
        Set dy = random.randint(minSpeed, maxSpeed)
    
    Function checkBounds():
        If bottom > screenHeight:
            Call reset()

Class Knight(simpleGE.Sprite):
    Function __init__(scene):
        Call super().__init__(scene)
        Call setImage("black_knight.png")
        Call setSize(50, 50)
        Set position = (320, 400)
        Set moveSpeed = 5
    
    Function process():
        If isKeyPressed(pygame.K_LEFT):
            Subtract moveSpeed from x
        If isKeyPressed(pygame.K_RIGHT):
            Add moveSpeed to x

Class LblScore(simpleGE.Label):
    Function __init__():
        Call super().__init__()
        Set text = "Score: 0"
        Set center = (100, 30)

Class LblTime(simpleGE.Label):
    Function __init__():
        Call super().__init__()
        Set text = "Time left: 10"
        Set center = (500, 30)

Class Game(simpleGE.Scene):
    Function __init__():
        Call super().__init__()
        Call setImage("castle2.png")
        Set sndFlame = simpleGE.Sound("click.wav")
        Set numFlame = 10
        Set score = 0
        Set lblScore = LblScore()
        Set timer = simpleGE.Timer()
        Set timer.totalTime = 10
        Set lblTime = LblTime()
        Set knight = Knight(self)
        Initialize flame list as empty
        For i in range(numFlame):
            Append new Flame(self) to flame
        Set sprites = [knight, flame, lblScore, lblTime]
    
    Function process():
        For each flame in flame:
            If flame.collidesWith(knight):
                Call flame.reset()
                Call sndFlame.play()
                Subtract 1 from score
                Update lblScore.text = f"Score: {score}"
        Update lblTime.text = f"Time Left: {timer.getTimeLeft():.2f}"
        If timer.getTimeLeft() < 0:
            Print score
            Call stop()

Class Instructions(simpleGE.Scene):
    Function __init__():
        Call super().__init__()
        Call setImage("castle2.png")
        Set response = "Quit"
        Set directions = simpleGE.MultiLabel()
        Set directions.textLines = [instructions text]
        Set directions.center = (320, 200)
        Set directions.size = (500, 250)
        Set btnPlay = simpleGE.Button()
        Set btnPlay.text = "Play"
        Set btnPlay.center = (100, 400)
        Set btnQuit = simpleGE.Button()
        Set btnQuit.text = "Quit"
        Set btnQuit.center = (540, 400)
        Set lblScore = simpleGE.Label()
        Set lblScore.text = "Previous score: 0"
        Set lblScore.center = (320, 400)
        Set sprites = [directions, btnPlay, btnQuit, lblScore]
    
    Function setPrevScore(prevScore):
        Set prevScore = prevScore
        Update lblScore.text = f"Last score: {prevScore}"
    
    Function process():
        If btnPlay.clicked:
            Set response = "Play"
            Call stop()
        If btnQuit.clicked:
            Set response = "Quit"
            Call stop()

Function main():
    Set keepGoing = True
    Set lastScore = 0
    While keepGoing:
        Create instructions = Instructions()
        Call instructions.setPrevScore(lastScore)
        Call instructions.start()
        If instructions.response == "Play":
            Create game = Game()
            Call game.start()
            Set lastScore = game.score
        Else:
            Set keepGoing = False

If __name__ == "__main__":
    Call main()






+---------------------------------------------------------------------+
|                                                          	          |
|                    	castle2.png background                	        |
|                                                          	          |
|         	 [ directions.textLines displayed here ]                  |
|                                                          	          |
|  		              - You are a Dark Knight!                          |
|        - Move with left and right arrow keys to dodge flames      	|
|  		                  - Highest score wins!                         |
|                                                          	          |
|               	 [ btnPlay ]          [ btnQuit ]                   |
|                                                      		            |
|            		 Last score: <previous score>                         |
+---------------------------------------------------------------------+












+---------------------------------------------------------------------+
|                                                          	          |
|                    	castle2.png background                	        |
|                                                          	          |
|    	 Score: <score>                        Time: <time>   	        |
|                                                          	          |
|     	( flames fall from top towards bottom )              	        |
|                                                          	          |
|           	     ( black_knight.png sprite at bottom )              |
|                                                          	          |
|         - flames reset when they collide with the knight    	      |
|  	- knight moves left and right with arrow keys   	                |
|                                                          	          |
+---------------------------------------------------------------------+
