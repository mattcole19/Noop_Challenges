"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import os


dirname = os.path.dirname(__file__)
filename = dirname + '/images/blue_ghost.png'

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starting Template"


class Visualization(arcade.Window):

    def __init__(self, layout, dimensions):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Will hold player Sprite
        self.player_list = None

        # Player sprite
        self.player_sprite = None
        self.player_position = None

        # Maze layout
        self.layout = layout
        self.dimensions = dimensions

        # Size of each block in the grid system
        self.y_change = SCREEN_HEIGHT / (self.dimensions + 1)
        self.x_change = SCREEN_WIDTH / (self.dimensions + 1)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Create your sprites and sprite lists here
        self.player_list = arcade.SpriteList()

        # Player sprite
        self.player_sprite = arcade.Sprite(filename)

        # Initialize maze
        self.create_grid()

        self.player_sprite.center_x = self.player_position[0]
        self.player_sprite.center_y = self.player_position[1]
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.create_grid()
        self.player_list.draw()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def create_grid(self):
        """ Creates the grid for the maze """
        y = SCREEN_HEIGHT
        for row in self.layout:
            x = 0
            for value in row:

                # Place a wall
                if value == 'X':
                    arcade.draw_xywh_rectangle_filled(bottom_left_x=x, bottom_left_y=y - self.y_change,
                                                      width=self.x_change,
                                                      height=self.y_change, color=arcade.color.BLACK)
                # Place the player
                if value == 'A':
                    arcade.draw_xywh_rectangle_filled(bottom_left_x=x, bottom_left_y=y - self.y_change,
                                                      width=self.x_change,
                                                      height=self.y_change, color=arcade.color.GREEN)
                    if self.player_position is None:
                        self.player_position = [x + .5*self.x_change, y - .5*self.y_change]


                # Place the end gate
                if value == 'B':
                    arcade.draw_xywh_rectangle_filled(bottom_left_x=x, bottom_left_y=y - self.y_change,
                                                      width=self.x_change,
                                                      height=self.y_change, color=arcade.color.BLUE)
                x += self.x_change
            y -= self.y_change

    @staticmethod
    def run():
        arcade.run()


