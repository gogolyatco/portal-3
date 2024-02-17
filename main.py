from pygame import*
win_width = 700
win_height = 500
window = display.set_mod((win_width, win_height))
display.set_caption("Maze")
backround = transform.scale(image.load("room.portal.jpg")
                            (win_width, win_height))
game = True
clock = time.Clock()
FPS = 120
mixer.init()
mixer.music.load("portal_s 2_01. Science is Fun.mp3")
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rest = self.image.get_rest()
        self.speed = player_speed
        self.rest.x = player_x
        self.rest.y = player_y
    def reset(self):
        window.blit(self.image, (self.rest.x, self.rest.y))
player = GameSprite('Chell.png', 5, win_height - 80, 4)
monster = GameSprite("turret.png", win_width - 80, 280, 3)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        window.blit(backround, (0, 0))
        player.reset()
        monster.reset()
        display.update()
        clock.tick(FPS)