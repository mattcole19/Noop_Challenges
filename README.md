# Noop_Challenges
This repository includes my implementations and solutions to the Noop Challenges posted in June 2019.  
You can learn more about them here -> https://noopschallenge.com/

## Mazebot

### Challenge Overview
The mazebot challenge essentially just randomly generates a maze with starting and ending points and has the user post a path back to it. 
You can set it to any  size you desire (with a max length of ?150) and it generates a list-of-lists it hold the layout.  You are supposed to
solve the maze then post the path you took to see your results.
Full Description can be found here -> https://noopschallenge.com/challenges/mazebot


### My Solution
Why would I want to spend time solving a maze when I could just make my computer do it for me?  I decided that I would create a program to
accept the maze as input and solve it for me.  Additionally, I thought it would be cool to include an animation of the maze being solved
so I used Python's Arcade library to show a little ghost sprite traverse his way about the maze from start to finish.

#### My Algorithm
Given enough time, solving a maze is quite simple when you have a bird's eye view of it.  It immediately becomes obvious which directions will lead you towards the exit and what will put you at a dead end.  But, imagine that you are thrown into a dark maze with a dinmly lit flashlight that is only capable of showing the space directly in front of you and the only thing you know is the coordiantes of the exit.  This is how the player, Walter, sees the problem in my program. Now, if you were Walter, think about how you would go about finding the exit. Would you continuously choose a direction at random (North, East, South, or West) and walk that way until you reached the exit? Of course not! This is where the algorithmic approach comes in.  Walter took a class on Data Structures and Algorithms so you better believe he is willing to spend an unneccesary amount of time creating the perfect solution to this problem.  Walter decided to use a greedy algorithm for this (turns out, he actually unknowingly used the A* Search approach).  A greedy approach was perfect for this since Walter knew the ultiamte goal but could only think one step at a time so it would only make sense to move in the direction that brought the player closest to the exit.  Right as he though the distance formula would be left in the past, Walter caclulated how far each adjacnet space to him was from the exit.  From here, he chose the most immediate optimal (greedy approach) spot to go to.  Oh, and Walter is capable of remebering all the steps he has taken so he never will end up getting stuck in an infinite loop.  This worked well, until Walter stumbled across a dead end.  Now what?  He obviously has to backtrack, but to what point? Well, if you think about it intuivtely, it would only make sense for Walter to backtrack to a spot that had he had to make a decison at. Walter refers to these spots as checkpoints.  There were a few different ways he could have went about deciding which checkpoint to return to, but Walter is lazy and decided that he would always return to the most recent checkpoint when he hits a dead end. Onc returned to the checkpoint, Walter would choose the next-most optimal decision as he doesn't want to run into the same dead end twice! Now what if all the paths leading from that checkpoint all lead to dead ends?  Walter would then make his way to the checkpoint before that one.  Walter follows this plan until he finally makes his way to the end of the maze! While this may not always result in the quickest path, Walter is very much proud of his efficient maze-traversing skills.

#### Pseusdocode

