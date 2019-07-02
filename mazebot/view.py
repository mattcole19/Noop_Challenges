import arcade

class Screen:
    screen_width = 700
    screen_height = 700
    screen_dimensions = (screen_width, screen_height)

    def __init__(self, maze_layout, maze_dimensions):
        arcade.open_window(width=self.screen_width, height=self.screen_height, window_title='Maze Solver')
        arcade.set_background_color(color=arcade.color.WHITE)
        arcade.start_render()
        self.layout = maze_layout
        self.x_change = self.screen_width / (maze_dimensions + 1)
        self.y_change = self.screen_height / (maze_dimensions + 1)

    def create_grid(self):
        """ Creates the grid for the maze """
        for row in self.layout:
            print(row)
        y = self.screen_height
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
                # Place the end gate
                if value == 'B':
                    arcade.draw_xywh_rectangle_filled(bottom_left_x=x, bottom_left_y=y - self.y_change,
                                                      width=self.x_change,
                                                      height=self.y_change, color=arcade.color.BLUE)
                x += self.x_change
            y -= self.y_change

        arcade.finish_render()
        arcade.run()

    def update_screen(self):
        """ Renders the new screen """
        pass


