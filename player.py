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

        self.costumesReflected = {
            "still":  pygame.transform.flip(pygame.image.load("stephstanding.png").convert_alpha(), True, False),
            "running":   pygame.transform.flip(pygame.image.load("stephrunning.png").convert_alpha(), True, False),
            "runningup":   pygame.transform.flip(pygame.image.load("stephrunningdribblingup.png").convert_alpha(), True, False),
            "runningdown":   pygame.transform.flip(pygame.image.load("stephrunningdribblingdown.png").convert_alpha(), True, False),
            "stillup":   pygame.transform.flip(pygame.image.load("stephdribblingup.png").convert_alpha(), True, False),
            "stilldown":   pygame.transform.flip(pygame.image.load("stephdribblingdown.png").convert_alpha(), True, False)
        }

        self.speed = 0.8

        self.x = float(x)
        self.y = float(y)

        self.suit = self.costumes

        self.key = ""

        self.facing = "right"
        self.image = self.costumes["stillup"]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.animateTimer = [0,0]
        self.animateSpeed = [0.1, 2]
        self.frame = 0

    def dribbleStill(self, dt):
        self.animateTimer[0] += dt
        
        if self.animateTimer[0] >= self.animateSpeed[0]:
            self.animateTimer[0] -= self.animateSpeed[0]
            if self.image == self.suit["stillup"]:
                self.image = self.suit["stilldown"]
            else:
                self.image = self.suit["stillup"]

    def dribbleRunning(self, dt):
            self.animateTimer[0] += dt
            
            if self.animateTimer[0] >= self.animateSpeed[0]:
                self.animateTimer[0] -= self.animateSpeed[0]
                if self.image == self.suit["stillup"]:
                    self.image = self.suit["runningup"]
                elif self.image == self.suit["runningup"]:
                    self.image = self.suit["runningdown"]
                else:
                    self.image = self.suit["stillup"]
    
    def running(self, dt):
        self.animateTimer[0] += dt
            
        if self.animateTimer[0] >= self.animateSpeed[0]:
            self.animateTimer[0] -= self.animateSpeed[0]
            if self.image == self.suit["running"]:
                self.image = self.suit["still"]
            else:
                self.image = self.suit["running"]

    def still(self, dt):
        self.image = self.suit["still"]

    def move(self, direction, direction2 = ""):
        if direction == "right":
            self.x += self.speed
        if direction == "left":
            self.x -= self.speed
        if direction == "up":
            self.x += self.speed
        if direction == "down":
            self.x -= self.speed

    def direction(self, facing):
        if facing == "right":
            self.suit = self.costumes
        else:
            self.suit = self.costumesReflected

    def control(self):
        if self.key == "up":
            self.direction("left")
            #self.move("left")
            self.direction("right")
            #self.move("right")
        if self.key == "down":
            self.move(self.facing)
        if self.key == "left":
            pass
        if self.key == "right":
            pass


    def update(self, dt):
        self.rect.x = self.x
        self.dribbleRunning(dt)
        self.animateTimer[1] += dt
                    
        if self.animateTimer[1] >= self.animateSpeed[1]:
            self.animateTimer[1] = 0
            

        


