import arcade
import os


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starting Template"


class Visualization(arcade.Window):

    def __init__(self, layout, dimensions, path):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Will hold Sprites
        self.player_list = None
        self.wall_list = None
        self.gates_list = None

        # Sprites
        self.player_sprite = None
        self.start_gate = None
        self.end_gate = None

        # Maze layout
        self.layout = layout
        self.dimensions = dimensions

        # Player's path to success
        self.path = path

        # Size of each block in the grid system
        self.y_change = SCREEN_HEIGHT / (self.dimensions + 1)
        self.x_change = SCREEN_WIDTH / (self.dimensions + 1)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Create your sprites and sprite lists here
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gates_list = arcade.SpriteList()

        # Initialize maze into lists of sprites
        self.create_grid()

        # Initialize player and set it on the start gate
        self.player_sprite = arcade.Sprite(filename='images/player.png')
        self.player_sprite.center_x = self.start_gate.center_x
        self.player_sprite.center_y = self.start_gate.center_y
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.wall_list.draw()
        self.gates_list.draw()
        self.player_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        #time.sleep(.2)
        if self.path:
            self.move_player()

    def create_grid(self):
        """ Creates a list to hold all x, y coordinates for the walls """
        # TODO: Fix coordinates
        y = SCREEN_HEIGHT
        for row in self.layout:
            x = 0
            for value in row:

                # Place a wall
                if value == 'X':
                    wall = arcade.Sprite('images/wall.png', scale=1)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

                # Place the start gate
                if value == 'A':
                    self.start_gate = arcade.Sprite('images/startGate.png')
                    self.start_gate.center_x = x
                    self.start_gate.center_y = y
                    self.gates_list.append(self.start_gate)

                # Place the end gate
                if value == 'B':
                    self.end_gate = arcade.Sprite('images/startGate.png')
                    self.end_gate.center_x = x
                    self.end_gate.center_y = y
                    self.gates_list.append(self.end_gate)

                x += self.x_change
            y -= self.y_change

    def move_player(self):
        """ Moves the player according to the directions"""
        direction = self.path.pop(0)

        # Move player north
        if direction == 'N':
            self.player_sprite.center_y += self.y_change

        # Move player east
        elif direction == 'E':
            self.player_sprite.center_x += self.x_change

        # Move player south
        elif direction == 'S':
            self.player_sprite.center_y -= self.y_change

        # Move player west
        elif direction == 'W':
            self.player_sprite.center_x -= self.x_change

    @staticmethod
    def run():
        arcade.run()


