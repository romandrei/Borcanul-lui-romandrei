import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Body")

ceas = pygame.time.Clock()

cutitpng = pygame.image.load("Img/cutit.png")
corppng = pygame.image.load("Img/corp.png")
marime = 0
marimeActuala = marime
scor = 0
esec = False
pornit = True

font = pygame.font.SysFont("arial", 16)
def txt():
    text = font.render("Scor:" + str(scor), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (30, 30)
    frstr.blit(text, textRect)

class cutit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(cutitpng, (53, 74))
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 53
        self.rect.y = 800 - 64
        self.x = self.rect.x
        self.y = self.rect.y
        self.vit = 2
    def update(self):
        global marime, marimeActuala, pornit
        self.taste = pygame.key.get_pressed()
        if pornit:
            if self.taste[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.vit
                self.x -= self.vit
            if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - 53 - marime:
                self.rect.x += self.vit
                self.x += self.vit
            if marime != marimeActuala:
                self.image = pygame.transform.scale(cutitpng, (53 + marime, 74 + marime))
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y - marime
                marimeActuala = marime
        if esec:
            self.kill()

class corp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(corppng, (100, 110))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 100)
        self.rect.y = random.randrange(-110, -330, -1)
        self.vit = 6
    def update(self):
        global marime, scor, esec, pornit
        if pornit:
            self.rect.y += self.vit
            self.atingere = pygame.sprite.spritecollideany(self, jucatori, False)
        if self.rect.y > 800 + 110:
            self.rect.x = random.randrange(0, 800 - 100)
            self.rect.y = random.randrange(-110, -330, -1)
            esec = True
        if self.atingere:
            marime += 5
            scor += 1
            self.rect.x = random.randrange(0, 800 - 100)
            self.rect.y = random.randrange(-110, -330, -1)

toate = pygame.sprite.Group()
jucatori = pygame.sprite.Group()
ctt = cutit()
crp = corp()
toate.add(ctt)
jucatori.add(ctt)
toate.add(crp)
rulare = True
while rulare:
    ceas.tick(120)
    frstr.fill((239, 228, 176))
    taste = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or taste[pygame.K_ESCAPE]:
            rulare = False
        elif taste[pygame.K_F4]:
            frstr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif taste[pygame.K_F3]:
            frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
        elif taste[pygame.K_o]:
            pornit = False
        elif taste[pygame.K_p]:
            pornit = True

    toate.update()
    toate.draw(frstr)
    txt()
    pygame.display.flip()

pygame.quit()
