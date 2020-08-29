import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Mush")
ceas = pygame.time.Clock()

ompng = pygame.image.load("Img/om.png")
ciup1png = pygame.image.load("Img/ciuperca1.png")
ciup2png = pygame.image.load("Img/ciuperca2.png")
ciup3png = pygame.image.load("Img/ciuperca3.png")

generare = False

x = 0
y = 0

class jucator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ompng, (82, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vit = 2
        self.cronom = 0
        self.oprire = random.randrange(600, 2400)
    def update(self):
        global generare
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN] and self.rect.y < 800 - 90:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - 82:
            self.rect.x += self.vit
        self.cronom += 1
        if self.cronom == self.oprire:
            generare = True
            self.cronom = 0
            self.oprire = random.randrange(600, 2400)
            self.kill()
            
            

class ciuperca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.skin = random.randrange(1, 4)
        self.diferenta = random.randrange(-40, 40, 1)

        if self.skin == 1:
            self.image = pygame.transform.scale(ciup1png, (57 + self.diferenta, 59 + self.diferenta))
        elif self.skin == 2:
            self.image = pygame.transform.scale(ciup2png, (57 + self.diferenta, 59 + self.diferenta))
        else:
            self.image = pygame.transform.scale(ciup3png, (57 + self.diferenta, 59 + self.diferenta))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

om = jucator()
toate = pygame.sprite.Group()
toate.add(om)

rulare = True
while rulare:
    ceas.tick(120)
    frstr.fill((100, 100, 100))
    taste = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or taste[pygame.K_ESCAPE]:
            rulare = False
        elif generare:
            ciup = ciuperca()
            toate.add(ciup)
            om = jucator()
            toate.add(om)
            generare = False
        elif taste[pygame.K_F4]:
            frstr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif taste[pygame.K_F3]:
            frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

    x = om.rect.x
    y = om.rect.y

    toate.update()
    toate.draw(frstr)
    pygame.display.flip()
    
pygame.quit()
        
