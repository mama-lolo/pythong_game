import pygame


def main():
    # Data structures
    player = Player(0, 0, 0)
    # Setup
    pygame.init()
    print(player)


class Player():
    def __init__(self, pos_x, pos_y, velocity=0.0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity = velocity

    def __str__(self):
        output = "{ "
        output += "x:"+str(self.pos_x)+" || "
        output += "y:"+str(self.pos_y)+" || "
        output += "velocity:"+str(self.velocity)+" || "
        output += "}"
        return output


if __name__ == "__main__":
    main()
