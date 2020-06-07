import pygame

def control_player(player, keys):
    if keys[pygame.K_UP]:
        player.velocity[1] -= 0.15
    if keys[pygame.K_DOWN]:
        player.velocity[1] += 0.15
    if keys[pygame.K_RIGHT]:
        player.velocity[0] += 0.15
    if keys[pygame.K_LEFT]:
        player.velocity[0] -= 0.15
    
def main():
    # Data structures
    player = Player(25.0, 25.0, [1.0,1.0])
    # Setup
    pygame.init()

    # Initialise screen
    screen = pygame.display.set_mode((400, 450))
    pygame.display.set_caption('Python Game')

    # Fill background
    screen.fill((0,0,0))

    """
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    """


    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.draw.circle(screen,(230,0,0),player.pos(), 20)
        player.move()
        keys = pygame.key.get_pressed()
        control_player(player, keys)
        pygame.time.wait(20)
        pygame.display.update()
        pygame.display.flip()
        screen.fill((0,0,0))


    print(player)


class Player():
    def __init__(self, pos_x, pos_y, velocity=[0.0,0.0]):
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
    def move(self):
        self.pos_x += self.velocity[0]
        self.pos_y += self.velocity[1]
    def pos(self):
        return (int(self.pos_x), int(self.pos_y))


if __name__ == "__main__":
    main()
