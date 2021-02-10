import pygame

def game():
    current = True
    arena = Arena()
    player = Player()
    while current:
        pygame.display.update()
        pygame.time.delay(6)
        arena.Render()

        for event in pygame.event.get():  # Controla os eventos
            keys = pygame.key.get_pressed()

            # Keydown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = True
                if event.key ==  pygame.K_a:
                    player.PunchLetf(arena)
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = True
                if event.key == pygame.K_SPACE:
                    player.x = 1000

            # Keyup
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = False
                if event.key == pygame.K_SPACE:
                    player.x = 1000

            current = quit(event)  # Controla a saída do jogo

        if player.left_pressed:
            player.MoveLeft(arena)
        elif player.right_pressed:
            player.MoveRight(arena)
        else:
            player.MoveParado(arena)

        pygame.display.update()
    pygame.quit()

class Arena():
    def __init__(self):
        self.map = pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Arenas\ArenaBills.png').convert()
        self.size = (1280, 480)

    def Render(self):
        win.blit(self.map, (0,0))

class Player():
    def __init__(self):
        self.animations = [pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\GokuPos0.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\GokuPos1.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\GokuPos2.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\GokuPos3.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run1.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run2.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run3.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run4.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run5.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run6.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run7.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run8.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run Left\Walk Left 1.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run Left\Walk Left 2.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run Left\Walk Left 3.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run Left\Walk Left 4.png'),pygame.image.load(r'C:\Users\joaop\PycharmProjects\Dragon Ball\Images\Goku Sayajin\Run Left\Walk Left 5.png')]
        self.counter = 0
        self.life = 1000
        self.x = 1000
        self.y = 300
        self.left_pressed = False
        self.right_pressed = False

    def MoveParado(self, arena):
        self.Render(0,3, arena)

    def MoveLeft(self, arena):
        clock = pygame.time.Clock()
        clock.tick(27)
        for a in range(12, 17):
            for i in range(0, 26):
                pygame.time.wait(1)
                self.x -= 0.888
                arena.Render()
                win.blit(self.animations[a], (self.x, self.y-20))
                pygame.display.update()

    def MoveRight(self, arena):
        clock = pygame.time.Clock()
        clock.tick(27)
        for a in range(16, 11, -1):
            pygame.time.wait(50)
            for i in range(0, 26):
                self.x += 0.888
                arena.Render()
                win.blit(self.animations[a], (self.x-10, self.y-20))
                pygame.display.update()

    def PunchLetf(self, arena):
        clock = pygame.time.Clock()
        clock.tick(27)
        for a in range(4, 12):
            pygame.time.wait(10)
            for i in range(0, 26):
                self.x -= 0.666
                arena.Render()
                win.blit(self.animations[a], (self.x, self.y))
                pygame.display.update()


    def Render(self, min, max, arena):
        for a in range(min,max+1):
            clock = pygame.time.Clock()
            clock.tick(20)
            pygame.time.wait(25)
            arena.Render()
            win.blit(self.animations[a], (self.x, self.y))
            pygame.display.update()



def quit(event):
    if event.type == pygame.QUIT:
        return False
    else:
        return True

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1280, 480))
    pygame.display.set_caption("Dragon Ball Fight")
    game()


#keys = pygame.key.get_pressed()
    #            if(player.Check()):
#                player.MoveLetf(arena)

# for event in pygame.event.get():  # Controla os eventos
#     keys = pygame.key.get_pressed()
#     if (event.type == pygame.KEYDOWN):
#         if (keys[pygame.K_LEFT]):
#             pygame.event.pump()
#             pygame.event.Event(pygame.KEYDOWN, button=1)
#             player.MoveLetf(arena)
#
#     if event.key == pygame.K_RIGHT:
#         print("Right")
#
#     if event.key == pygame.K_LEFT and event.type == pygame.KEYUP:
#         print("Solta Left")
#         player.Render(0, 3, arena)