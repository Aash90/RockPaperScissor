# RockPaperScissor
A python based terminal game for 2 players

It is based on rules specified in [GAME_RULES](https://github.com/Aash90/RockPaperScissor/blob/master/game_objects.py).
These rules can be modified inorder to add or delete new objects.

_Note: Developed and tested on Windows 10 with Python3_

# Requirements
- Python3

# How to Use
1. Download the files [GAME](https://github.com/Aash90/RockPaperScissor/blob/master/game.py), and [GAME_RULES](https://github.com/Aash90/RockPaperScissor/blob/master/game_objects.py)

2. Make sure both of the above files are in same directory.
3. On Windows:

    Click on the **_game.py_** file
       
       OR
       
    From terminal execute cmd as shown below
    ``` 
    C:\>python game.py
    ```

# Sample Runs
- When you execute the Game you see a Game Menu
```
                  Game Menu
========================================
 1. Player v/s Computer
 2. Computer v/s Computer
 X. Exit Game

 Choose game option:
```
- Then if you choose option **1. Player v/s Computer**, it will ask user name and then takes you to a mode of **_Player v/s Computer_** game

```
 ============== Player-X v/s Computer(SkyNet-X) : Game Started ============

         Object List
----------------------------------------
1 . Rock
2 . Paper
3 . Scissor
4 . Lizard
5 . Spock
S . Get Play Score
X . Exit Play

Player-X enter a choice to Throw:
```
- Here user need to add a _choice_ option to throw for the Game.
For E.g.
```
Player-X enter a choice to Throw: 3
```
This way user Choose to throw **Scissor** for the game.
After this Computer chooses a option for itself in the Game. And then based on the rules defined in the [GAME_RULES](https://github.com/Aash90/RockPaperScissor/blob/master/game_objects.py) Winner is decided.
```
 ********************************************* Result ******************************************
 SkyNet-X throws: Spock           Player-X throws: Scissor          -----> SkyNet-X Wins <-----
 ***********************************************************************************************
```
As you can see the above match is won by _SkyNet-X_(A computer opponent in the Game)

- User can play multiple rounds to their wish. And see the overall score. For this user need to enter option **S** , Its for _Get Play Score_

```
=============== Score Board ============
        SkyNet-X: 2,   Player-X: 1
========================================

Player-X enter a choice to Throw: S

```
- Using **X** will get you back to main _Game Menu_

- If you want to choose option **2. Computer v/s Computer** then enter **2** as your choice in main Game Menu.
- It will take you to the Window of **Computer Arena**, where 2 computers battel for win _Jarvis v/s SkyNet-X_
```
============== Jarvis v/s SkyNet-X : Game Started ============
         Option List
----------------------------------------
P . Throw
S . Check Score
X . Exit Play

Enter Option to play:
```
- Unlike Player v/s Computer this window has no options for choice of objects. It has only option to start the **Play**(a.k.a Fight). Enter option **P** to initiate the match and then wait for the count down when each of the computer throw a object of their choice.
```      
Enter Option to play: P

         Option List
----------------------------------------
P . Throw
S . Check Score
X . Exit Play

 Waiting for Throw...: 1
 :
 : 
....  !! Throw !! ...: 3
********************************************* Result *********************************************
Jarvis throws: Scissor          SkyNet-X throws: Rock           -----> SkyNet-X Wins <-----
****************************************************************************************************
Enter Option to play:
```

Here also the Winner is decided by the same rules as per [GAME_RULES](https://github.com/Aash90/RockPaperScissor/blob/master/game_objects.py)

- Same as earlier you can use **S** to see score of the match and **X** to return back to main menu.
```
========= Score Board ===============
  Jarvis: 1,     SkyNet-X: 1
=====================================

Enter Option to play: S
```

