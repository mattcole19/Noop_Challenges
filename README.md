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
#####  Layman's terms
How did I approach the problem?
This problem came to be quite challenging since I really had to delve in deep to think about how I solve mazes.  This became quite interesting to me.  Given enough time, solving a maze is quite simple when you have a bird's eye view of it.  It immediately becomes obvious which directions will lead you towards the exit.  But, imagine that you are thrown into a dark maze with a flashlight that is only capable of showing the space directionly in front of you and the only thing you know is the coordiantes of the exit.  This is how my player sees the problem in my program. Now, how would YOU go about finding the exit? Would you continuously choose a direction (North, East, South, or West) at random and walk that way until you reached the exit? Of course not! This is where the algorithm comes in.  I decided to use a greedy algorithm for this (turns out, I actually unknowingly used the A* Search approach).  A greedy approach was perfect for this since the player knew the ultiamte goal but could only think one step at a time so it would only make sense to move in the direction that brought the player closest to the exit.  Essentially, my player would move in the direction that it deemed optimal at each point.  Alogn with this, the player (I will refer to him as Walter from now on) remembers all the steps he has taken.  This worked well, until Walter stumbled across a dead end.  Now what?  He obviously has to backtrack, but to what point? Well, it would only make sense for Walter to backtrack to a spot that had he had to make a decison at. I will refer to these spots as checkpoints.  There were a few different ways I could have went about implementing this, but I decided that upon hitting a dead end, Walter would revert back to the most recent checkpoint.  Walter would then choose the next-most optimal decision as he doesn't want to run into the same dead end twice! Now what if all the paths leading from that checkpoint all lead to dead ends?  Walter would then make his way to the checkpoint before that one.  Walter follows this plan until he finally makes his way to the end of the maze! While this may not always result in the quickest path, Walter is very much proud of his efficient maze-traversing skills.

##### Pseusdocode

