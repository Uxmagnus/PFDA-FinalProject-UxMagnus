# Genesys System Dice Roller

## Repository
https://github.com/Uxmagnus/PFDA-FinalProject-UxMagnus.git

## Description
A simple dice-rolling application for the Genesys and Star Wars Fantasy Flight Games TTRPG systems, made for those who don't like rolling lots of dice. Fancy "rolling" animations may or may not be involved.

## Features
- Customizable randomization via lists.
	- Takes in a list of possible dice roll results, then returns one of the contents of the list (which will be parsed)
- Results Parsing
	- Program will automatically translate the string contents of the returned list item into values which can be summed up and displayed.
- Graphical Display
	- The program will display both the results of each individual roll and the overall result of the combined roll.

## Challenges
- I'll need to learn how to build a GUI
- I'll also need to learn how to interpret string responses from arrays.
- I might also have to learn how to manipulate Python's randomization functions to achieve better-than-mean results.

## Outcomes
Ideal Outcome:
- A functioning Dice-rolling application that allows the user to input how many dice of the six given variaties of Genesys/Star Wars dice they'd like to use, then displays either symbols or plain text informing the user of the roll's result.

Minimal Viable Outcome:
- A functioning Dice-rolling application that allows the user to input how many dice of the six given variaties of Genesys/Star Wars dice they'd like to use, then displays plain text informing the user of the roll's result.

## Milestones

- Week 1
  1. Basic Setup of code infrastructure
  2. Make Randomization function according to my specifications in Features

- Week 2
  1. Begin implementing GUI. Create an interface where users can tap buttons to adjust the amount of dice rolled per type of dice.
  2. Create a way to display roll results within the GUI according to the specifications listed in Features

- Week N (Final)
  1. Make fancy result generation animation?
  2. Goal 2