import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.costumes = {
            "still":  pygame.image.load("stephstanding.png").convert_alpha(),
            "running":  pygame.image.load("stephrunning.png").convert_alpha(),
            "runningup":  pygame.image.load("stephrunningdribblingup.png").convert_alpha(),
            "runningdown":  pygame.image.load("stephrunningdribblingdown.png").convert_alpha(),
            "stillup":  pygame.image.load("stephdribblingup.png").convert_alpha(),
            "stilldown":  pygame.image.load("stephdribblingdown.png").convert_alpha()
        }

        self.speed = 0.8

        self.x = float(x)
        self.y = float(y)

        self.facing = True  #true = right, false = left
        self.image = self.costumes["stillup"]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.animateTimer = [0,0]
        self.animateSpeed = [0.1, 0]
        self.frame = 0

    def dribbleStill(self, dt):
        self.animateTimer[0] += dt
        
        if self.animateTimer[0] >= self.animateSpeed[0]:
            self.animateTimer[0] -= self.animateSpeed[0]
            if self.image == self.costumes["stillup"]:
                self.image = self.costumes["stilldown"]
            else:
                self.image = self.costumes["stillup"]

    def dribbleRunning(self, dt):
            self.animateTimer[0] += dt
            
            if self.animateTimer[0] >= self.animateSpeed[0]:
                self.animateTimer[0] -= self.animateSpeed[0]
                if self.image == self.costumes["stillup"]:
                    self.image = self.costumes["runningup"]
                elif self.image == self.costumes["runningup"]:
                    self.image = self.costumes["runningdown"]
                else:
                    self.image = self.costumes["stillup"]
    
    def running(self, dt):
        self.animateTimer[0] += dt
            
        if self.animateTimer[0] >= self.animateSpeed[0]:
            self.animateTimer[0] -= self.animateSpeed[0]
            if self.image == self.costumes["running"]:
                self.image = self.costumes["still"]
            else:
                self.image = self.costumes["running"]

    def still(self, dt):
        self.image = self.costumes["still"]

    def move(self, direction):
        if direction == "right":
            self.x += self.speed
        if direction == "left":
            self.x -= self.speed
            
    def update(self, dt):
        self.rect.x = self.x
        self.dribbleRunning(dt)
        self.move("right")

        


