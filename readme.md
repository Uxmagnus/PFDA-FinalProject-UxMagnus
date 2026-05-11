## Project Title: 
Star Wars Dice Roller
## URL to Video:
https://youtu.be/dai8agAMDvI
## URL to Repository:
https://github.com/Uxmagnus/PFDA-FinalProject-UxMagnus
## Description:
This project is a simple dice-roller program meant to be used with the Star Wars (Fantasy Flight Games) Table-top Role-playing game. The program provides a simple means of assembling a dice pool for checks, then outputting the results. Players adjust how many dice of each type (Proficiency, Ability, Boost, Challenge, Difficulty, Setback, Force) are in their pool via pressing the appropriate buttons on the GUI. Then, players generate the results of rolling their dice pool by pressing the "Roll" button. The program first outputs the results of the rolls in their original symbol forms, then translates the results of the symbols rolled into plain, understandable text. 

The python file itself handles the bulk of the required processes. On program startup, it takes the text from the .kv file and translates it into a graphical user interface. It also stores the quantites of each dice in the dice pool. The minimum amount of dice per type in the pool is 0, and the maximum is 5. The program stores the possible results of dice types via a key:value pair stored in a dictionary of dice types. When the "Roll" button is pressed, the program loops over every dice type an amount of times equal to however many dice of that type are in the pool, adding the results to the various counters present in the program. (EX: the program rolls 2 Ability Dice, generating 2 success and one advantage in total. The program records this in the success and advantage variables.) Once all dice have been rolled, the program outputs the results in the GUI, first in symbol form, then in plain english.

The .kv file includes instructions for how to build the GUI. Each element present in the GUI has certain instructions that the program has to take account of when building the GUI, like size or the font in text boxes (key to displaying the symbols). 

I wanted to design this dice roller to be relatively easy to understand. The adjustments being performed by arrow buttons can be slightly easier to work with for some. The program loops over every dice type instead of creating an array of dice to roll in part because it proved easier to code and provided similar results without overcomplicating the program. 

From a graphical perspective, the Force Dice adjustment buttons stick out like a sore thumb, due to the fact that they're so different from the other dice types. However, I beleive I've found a good position for them to be in within the scope of this program. If I ever come back to this program, I might try fussing around with it more to make it fit better overall within the GUI.