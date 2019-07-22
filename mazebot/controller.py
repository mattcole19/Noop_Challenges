import requests
import json
from tkinter import *
from copy import deepcopy
from collections import namedtuple
from mazebot.simpler_GUI import UserInterface
from mazebot.model import Maze
root = Tk()  # FOR SOME REASON THIS HAS TO BE ABOVE IMPORTING VISUALIZATION (CRASHES OTHERWISE)
from mazebot.view import Visualization


Position = namedtuple('Position', ['x', 'y'])


def run():

    # User interface
    ui = UserInterface(root)
    root.mainloop()
    print(ui.min_value)

    # Request data from API
    max_size = ui.max_value
    min_size = ui.min_value
    geturl = f'https://api.noopschallenge.com/mazebot/random?minSize={str(min_size)}&maxSize={str(max_size)}'
    data = requests.get(url=geturl).json()

    # Stores data for the maze
    layout = data['map']
    layout_copy = deepcopy(layout)
    dimensions = len(layout[0]) - 1
    start = data['startingPosition']
    end = data['endingPosition']

    # Start and End positions of the maze as a namedtuple
    maze_start = Position(x=start[0], y=start[1])
    maze_end = Position(x=end[0], y=end[1])

    # Maze Instance to solve the maze
    maze = Maze(layout=layout, start=maze_start, end=maze_end, dimensions=dimensions)

    # Solves maze and gets the "ideal" path
    success = False
    while not success:
        if maze.player_position == maze_end:
            success = True
        else:
            maze.check_possible_movements()

    # TODO: Possibly remove/change this
    # Obtains the path and formats it as a string
    print()
    path = maze.get_path()
    string_path = ""
    for direction in path:
        string_path += direction
    print(f'Path taken: {path}')
    answer = {
        'directions': string_path
    }

    # POSTS the answer to obtain the result
    post_url = 'https://api.noopschallenge.com' + data['mazePath']
    result = requests.post(url=post_url, data=json.dumps(answer))

    # Result...
    print(dimensions)
    print(result.content)



    # Screen Instance to show the animation
    visualization = Visualization(layout=layout_copy, dimensions=dimensions, path=path)
    visualization.setup()
    visualization.run()
    #screen.on_draw()


    # Creates the grid

    # Moves the player on the screen

if __name__ == '__main__':
    run()