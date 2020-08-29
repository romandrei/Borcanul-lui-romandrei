import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Insect")

ceas = pygame.time.Clock()

insectapng = pygame.image.load("Img/insecta.png")
crucepng = pygame.image.load("Img/cruce.png")

cronom = 0
limita = 30
foc = False
scor = 0
scorPrc = 0
reinc = False
pornit = True

font = pygame.font.SysFont("arial", 16)

def txt():
    text = font.render("Gloante:" + str(crc.gloante), True, ((0, 255, 0)))
    textRect = text.get_rect()
    textRect.center = (70, 770)
    text2 = font.render("Scor:" + str(scor), True, ((0, 255, 0)))
    text2Rect = text.get_rect()
    text2Rect.center = (70, 740)
    frstr.blit(text, textRect)
    frstr.blit(text2, text2Rect)

class cruce(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(crucepng, (52, 68))
        self.rect = self.image.get_rect()
        self.gloante = 6
    def update(self):
        if pornit:
            pozMouse = pygame.mouse.get_pos()
            self.rect.center = pozMouse
        if reinc:
            self.kill()

class insecta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(insectapng, (78, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(878, 978, 1)
        self.rect.y = random.randrange(0, 800 - 60, 1)
        self.vit = 4
    def update(self):
        global foc, scor, reinc, pornit
        if pornit:
            self.rect.x -= self.vit
            self.atingere = pygame.sprite.collide_rect(self, crc)
            if self.atingere and click[0] == 1 and foc:
                crc.gloante += 1
                scor += 1
                self.rect.x = random.randrange(878, 978, 1)
                self.rect.y = random.randrange(0, 800 - 60, 1)
        if self.rect.x < 0 - 78:
            reinc = True

toate = pygame.sprite.Group()
insecte = pygame.sprite.Group()

for i in range(5):
    insct = insecta()
    toate.add(insct)
    insecte.add(insct)

crc = cruce()
toate.add(crc)

rulare = True
while rulare:
    ceas.tick(120)
    frstr.fill((185, 122, 87))
    click = pygame.mouse.get_pressed()
    taste = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or taste[pygame.K_ESCAPE]:
            rulare = False
        elif taste[pygame.K_F4]:
            frstr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif taste[pygame.K_F3]:
            frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
        elif taste[pygame.K_p]:
            pornit = True
        elif taste[pygame.K_o]:
            pornit = False
            cronom = 0
        elif cronom >= limita and crc.gloante > 0 and not reinc:
            foc = True
        else:
            foc = False
        if click[0] == 1 and cronom >= limita and crc.gloante > 0 and not reinc and pornit:
            crc.gloante -= 1
            cronom = 0
    if pornit:
        cronom += 1
    toate.update()
    toate.draw(frstr)
    txt()
    pygame.display.flip()

pygame.quit()
