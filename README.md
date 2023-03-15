# Balloon Shooting Game

## Features
- The balloon moves up and down randomly. (This was a little ambiguous to me, the way I implemented it was to give a 1% chance for the balloon to change direction every frame)
- The player can move the cannon up and down using the arrow keys.
- To shoot a bullet, the player presses the space key.
- The game ends when the balloon is shot down, and the number of missed shots is displayed.
- The bullet speed is 10 times the speed of the balloon.

## Versions
There are two versions of the Balloon Shooting Game available:
1. Original Version: This version follows the project requirements closely. The game ends when the balloon is shot down, and the number of missed shots is displayed at the end.
2. Modified Version: In this version, the game has some changes from the original requirements. The game does not end after shooting down one balloon; instead, it ends based on a timer. A new balloon appears after each successful shot, and the game continues until the timer runs out. I also changed the movement of the balloon to not randomly change while moving, it picks a random direction (up or down) and continues to move in that direction unit hitting the edge of the screen (im not sure if this is what you wanted in the original version)


## Requirements
Python 3.x
Pygame 2.3.0

## Installation
```
pip3 install -r requirements.txt
```

## Instructional Manual for Students to Create the Game Themselves
I have included and instructional manual "Student_Manual.pdf" as an example of a piece of content I would create for students if I were teaching them how to make this game. I included a few sections, up till making the classes.

This is just an example of the content I can create for students. The full manual will contain detailed explanations, step-by-step instructions, and examples to ensure that students have a comprehensive understanding of the project and can successfully create their own game.