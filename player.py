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

        self.facing = "right"
        self.pointing = "right"
        self.moving = True

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

    def still(self):
        self.image = self.suit["still"]

    def move(self):
        if self.facing == "right":
            self.x += self.speed
        if self.facing == "left":
            self.x -= self.speed
        if self.facing == "up":
            self.y += self.speed
        if self.facing == "down":
            self.y -= self.speed

    def direction(self, facing=None):
        if facing is not None:
            self.facing = facing

        if facing == "right":
            self.suit = self.costumes
        elif facing == "left":
            self.suit = self.costumesReflected

    def control(self):
        if self.pointing == "left":
            self.direction("left")
            self.moving = True
        if self.pointing == "right":
            self.direction("right")
            self.moving = True
        if self.pointing == "up":
            self.direction("up")
            self.moving = True
        if self.pointing == "down":
            self.direction("down")
            self.moving = True
                
        if self.pointing == None:
            self.facing = None
            self.moving = False
        self.move()

    def animation(self, dt):
        if self.moving == True:
            self.running(dt)
        else:
            self.still()
    def update(self, dt):
        self.rect.x = self.x
        self.animateTimer[1] += dt
        self.control()
        self.animation(dt)
        print(self.direction)
                    
        if self.animateTimer[1] >= self.animateSpeed[1]:
            self.animateTimer[1] = 0
            

        


